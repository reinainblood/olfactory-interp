"""Verify the air-raw-v1 release or restore its scientific and H0 records offline."""

import argparse
import hashlib
import json
import os
import re
import stat
import sys
import tarfile
import tempfile
from contextlib import ExitStack
from pathlib import Path

GROUPS = {
    "scientific": Path("raw"),
    "qual-primary": Path("qualification/primary"),
    "qual-b": Path("qualification/b"),
    "qual-c": Path("qualification/c"),
}
CATALOG = "study-raw-index.json"
CHUNK = 1 << 20


def require(condition, message):
    if not condition:
        raise ValueError(message)


def components(name):
    """The producing packer uses portable, relative POSIX identifiers."""
    require(isinstance(name, str), "Expected a relative filename")
    parts = name.split("/")
    for part in parts:
        require(
            re.fullmatch(r"[A-Za-z0-9_.-]+", part) and part not in {".", ".."},
            f"Invalid path component in {name!r}",
        )
    return parts


def basename(name):
    require(len(components(name)) == 1, f"Expected one filename: {name!r}")
    return name


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Repeated JSON key {key!r}")
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_bytes(), object_pairs_hook=unique_keys)


def digest_stream(stream, output=None):
    sha = hashlib.sha256()
    for block in iter(lambda: stream.read(CHUNK), b""):
        sha.update(block)
        if output is not None:
            output.write(block)
    return sha.hexdigest()


def digest_file(path):
    require(
        path.is_file() and not path.is_symlink(), f"Expected a regular file: {path}"
    )
    with path.open("rb") as source:
        return digest_stream(source)


def checksum(value):
    require(
        isinstance(value, str) and re.fullmatch("[a-f0-9]{64}", value),
        "Invalid SHA-256",
    )
    return value


def checked_directory(path):
    path.mkdir(exist_ok=True)
    require(
        stat.S_ISDIR(path.lstat().st_mode),
        f"Refusing a linked or non-directory path: {path}",
    )


def output_path(root, relative):
    *folders, leaf = components(relative)
    directory = root
    for name in folders:
        directory = directory / name
        checked_directory(directory)
    return directory / leaf


def accept_member(source, expected, target=None):
    """Hash every input. Atomically add verified files without replacing existing entries."""
    if target is None or os.path.lexists(target):
        require(digest_stream(source) == expected, "Input file checksum mismatch")
        if target is not None:
            require(
                digest_file(target) == expected, f"Existing output differs: {target}"
            )
        return

    with ExitStack() as cleanup:
        with tempfile.NamedTemporaryFile(
            prefix=".air-restore-", dir=target.parent, delete=False
        ) as tmp:
            stage = Path(tmp.name)
            cleanup.callback(stage.unlink, missing_ok=True)
            require(
                digest_stream(source, tmp) == expected,
                f"Input checksum mismatch: {target.name}",
            )
        try:
            os.link(stage, target)
        except FileExistsError:
            require(
                digest_file(target) == expected, f"Concurrent output differs: {target}"
            )


def locate_asset(folder, name, entry):
    basename(name)
    relative = components(entry["relative"])
    require(relative[-1] == name, f"Asset basename mismatch: {name}")
    flat = folder / name
    # GitHub Release downloads are flat. A local assembly retains the relative components.
    source = flat if os.path.lexists(flat) else folder.joinpath(*relative)
    require(
        source.resolve().is_relative_to(folder),
        f"Asset resolves outside its folder: {name}",
    )
    require(
        source.is_file() and not source.is_symlink(), f"Missing or linked asset: {name}"
    )
    require(
        source.stat().st_size == entry["bytes"], f"Asset byte count differs: {name}"
    )
    require(
        digest_file(source) == checksum(entry["sha256"]),
        f"Asset SHA-256 differs: {name}",
    )
    return source


def verify_group(group, description, assets, catalog, destination):
    index_name = description["index"]
    manifest_name = f"{group}-physical-trial-inputs.jsonl"
    require(index_name == f"{group}-raw-index.json", f"Unexpected {group} index name")
    info = read_json(assets[index_name])
    require(
        info["format"] == "air-raw-v1" and info["compression"] == "gzip tar",
        "Unknown group format",
    )
    require(
        info["manifest_sha256"] == catalog[manifest_name]["sha256"],
        f"{group} input hash mismatch",
    )
    with assets[manifest_name].open("rb") as stream:
        inputs = {}
        for line in stream:
            entry = json.loads(line, object_pairs_hook=unique_keys)
            name = basename(entry["trial_id"])
            require(
                name not in inputs and name != "_target_vectors",
                f"Duplicate or reserved trial: {name}",
            )
            inputs[name] = entry
    require(len(inputs) == description["planned"], f"{group} input count mismatch")
    expected_trials = {}
    for row in info["coverage"]:
        name = row["trial_id"]
        require(
            name in inputs and name not in expected_trials,
            f"Invalid coverage for {name}",
        )
        require(
            all(inputs[name].get(k) == v for k, v in row.items() if k != "status"),
            f"Coverage disagrees with manifest for {name}",
        )
        require(
            row["status"] in {"complete", "failure_or_needs_review"},
            f"Unknown status: {name}",
        )
        expected_trials[name] = row["status"]
    require(
        len(expected_trials) == description["coverage"],
        f"{group} coverage count mismatch",
    )

    if destination is not None:
        for name in (index_name, manifest_name):
            with assets[name].open("rb") as source:
                accept_member(
                    source,
                    catalog[name]["sha256"],
                    output_path(destination, "release/" + name),
                )

    seen = {}
    found_trials = set()
    complete = set()
    part_names = set()
    for part in info["parts"]:
        name = basename(part["file"])
        require(
            name not in part_names
            and name.startswith(f"air-{group}-")
            and name.endswith(".tar.gz"),
            f"Unexpected or duplicate part: {name}",
        )
        part_names.add(name)
        require(
            part["bytes"] == catalog[name]["bytes"]
            and part["sha256"] == catalog[name]["sha256"],
            f"Catalog and group index disagree for {name}",
        )
        files = part["files"]
        in_part = set()
        with tarfile.open(assets[name], "r|gz") as tar:
            for member in tar:
                parts = components(member.name)
                require(
                    member.type in (tarfile.REGTYPE, tarfile.AREGTYPE)
                    and not member.sparse
                    and len(parts) >= 2,
                    f"Unexpected tar entry: {member.name}",
                )
                require(
                    member.name in files and member.name not in in_part,
                    f"Unexpected or duplicate member: {member.name}",
                )
                expected = checksum(files[member.name])
                require(
                    seen.get(member.name, expected) == expected,
                    f"Conflicting repeated member: {member.name}",
                )
                if parts[0] == "_target_vectors":
                    require(
                        len(parts) == 2
                        and re.fullmatch(r"[a-f0-9]{64}\.npy", parts[1]),
                        f"Unexpected vector path: {member.name}",
                    )
                else:
                    require(
                        parts[0] in expected_trials, f"Undeclared trial: {member.name}"
                    )
                    found_trials.add(parts[0])
                    if parts[1:] == ["harvest-complete.json"]:
                        complete.add(parts[0])
                target = (
                    output_path(destination, (GROUPS[group] / member.name).as_posix())
                    if destination
                    else None
                )
                with tar.extractfile(member) as data:
                    accept_member(data, expected, target)
                in_part.add(member.name)
                seen[member.name] = expected
        require(in_part == set(files), f"Indexed member missing in {name}")
    require(
        found_trials == set(expected_trials),
        f"Coverage lists missing raw trial(s) in {group}",
    )
    require(
        complete
        == {t for t, status in expected_trials.items() if status == "complete"},
        f"Harvest markers disagree with coverage in {group}",
    )
    require(
        part_names
        == {
            n for n in assets if n.startswith(f"air-{group}-") and n.endswith(".tar.gz")
        },
        f"Orphan or missing {group} part",
    )
    return {
        "planned": len(inputs),
        "covered": len(found_trials),
        "complete": len(complete),
        "parts": len(part_names),
        "unique_files": len(seen),
    }


def process(folder, destination=None, expected_catalog=None):
    folder = folder.resolve(strict=True)
    catalog_path = folder / CATALOG
    fingerprint = digest_file(catalog_path)
    if expected_catalog is not None:
        require(
            checksum(expected_catalog.removeprefix("sha256:")) == fingerprint,
            "The root catalog differs from the supplied SHA-256",
        )
    catalog = read_json(catalog_path)
    require(catalog["status"] in {"interim", "terminal"}, "Unknown release status")
    require(
        set(catalog["groups"]) == set(GROUPS),
        "Release is missing or has unexpected study groups",
    )
    checksum(catalog["frozen_base_input_sha256"])
    entries = catalog["assets"]
    require(
        CATALOG not in entries, "The root catalog cannot declare itself as an asset"
    )
    assets = {n: locate_asset(folder, n, entry) for n, entry in entries.items()}

    if destination is not None:
        destination = destination.absolute()
        destination.parent.mkdir(parents=True, exist_ok=True)
        checked_directory(destination)
        root_marker = destination / "release" / CATALOG
        if any(destination.iterdir()):
            metadata = destination / "release"
            require(not metadata.is_symlink(), "Linked destination release directory")
            if root_marker.exists():
                require(
                    digest_file(root_marker) == fingerprint,
                    "Existing destination belongs to a different catalog",
                )
            else:
                # Recognize a crash before the very first catalog hard link was installed.
                initializing = (
                    set(destination.iterdir()) == {metadata}
                    and metadata.is_dir()
                    and all(
                        f.name.startswith(".air-restore-")
                        and f.is_file()
                        and not f.is_symlink()
                        for f in metadata.iterdir()
                    )
                )
                require(
                    initializing,
                    "Choose an empty destination or resume a restore of this exact catalog",
                )
        with catalog_path.open("rb") as stream:
            accept_member(
                stream, fingerprint, output_path(destination, "release/" + CATALOG)
            )

    groups = {
        g: verify_group(g, catalog["groups"][g], assets, entries, destination)
        for g in GROUPS
    }
    return {
        "release_status": catalog["status"],
        "catalog_sha256": fingerprint,
        "assets_verified": len(assets),
        "groups": groups,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("verify", "restore"):
        cmd = subparsers.add_parser(name)
        cmd.add_argument(
            "assets",
            type=Path,
            help="Downloaded release assets or the local assembly folder",
        )
        if name == "restore":
            cmd.add_argument(
                "destination",
                type=Path,
                help="New/empty directory, or a matching previous restore",
            )
        cmd.add_argument(
            "--catalog-sha256",
            help="Expected study-raw-index.json digest from the release host",
        )
    args = parser.parse_args()
    try:
        result = process(
            args.assets, getattr(args, "destination", None), args.catalog_sha256
        )
    except (
        ValueError,
        OSError,
        KeyError,
        TypeError,
        tarfile.TarError,
        EOFError,
    ) as exc:
        parser.exit(1, f"Release verification failed: {exc}\n")
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
