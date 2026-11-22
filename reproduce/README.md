# Verify and read the study data

The raw release has four groups. The scientific trials restore under `raw/`. The node-qualification trials, called H0, restore under `qualification/primary/`, `qualification/b/`, and `qualification/c/`. Each group's input manifest identifies what was planned. Its coverage index identifies the trials for which physical evidence was retained and whether a complete harvest receipt exists. Use the terminal eligibility table in the analysis materials to distinguish a planned, withheld, failed, or unobserved trial.

## Verify a release and restore it offline

From the repository root, use Python 3.9 or newer. The reader uses the standard library. Download the assets of one release into a single folder. Keep the release tag and GitHub's SHA-256 for the top-level `study-raw-index.json` with your analysis. For example, a reader with GitHub CLI can run the following after setting `TAG` to the chosen release tag.

```sh
gh release download "$TAG" --repo kirstenruge-ship-it/what-the-air-remembers --dir assets
CATALOG_SHA=$(gh release view "$TAG" --repo kirstenruge-ship-it/what-the-air-remembers \
  --json assets --jq '.assets[] | select(.name == "study-raw-index.json") | .digest')
python3 reproduce/data_release.py restore assets restored --catalog-sha256 "$CATALOG_SHA"
```

`restore` verifies every catalogued asset, including report, notebook and analysis supplements, every compressed raw part, and every member in each raw tar archive. It checks the input manifests and reconciles indexed coverage to the actual per-trial files and completion markers. It creates the four raw trees plus a `release/` folder holding the original catalog, group indexes and physical trial manifests. The supplemental ZIPs remain in `assets/`. The analysis supplement provides its own instructions for use alongside the restored data.

Use a new or empty output directory on a filesystem that supports hard links. A retry against the same catalog can reuse verified identical files. An interruption can leave verified individual files in place. A conflicting file, symlink, unsafe archive path or failed checksum stops the restore. For a read-only check of the assets, run:

```sh
python3 reproduce/data_release.py verify assets --catalog-sha256 "$CATALOG_SHA"
```

The optional digest pins the exact catalog to a separately obtained release record. Without that argument, the reader prints the catalog's SHA-256 and checks the files against the supplied catalog. A local assembly with nested asset folders also works. The summary distinguishes `interim` from `terminal` bundles.

## Follow one physical model run

The following example uses the public H0 engineering case `h0-as-9307c56722d42e4d58e3-one_ulp` on the primary recorder. This particular intervention changed one BF16 coordinate at layer 47. It provides a small example with a completed natural response, two layers of captured activations and before/after write tensors. H0 measures numerical and recorder behavior. Scientific estimates come from the separate scientific groups and registered comparisons.

Run the examples from the directory containing `restored/`. This first example prints the original question, exact input and output token IDs, model-emitted reasoning and final response. These are separate fields in the raw native response.

```python
import json
from pathlib import Path

root = Path("restored")
trial = "h0-as-9307c56722d42e4d58e3-one_ulp"
node = root / "qualification" / "primary"
record = node / trial
manifest = root / "release" / "qual-primary-physical-trial-inputs.jsonl"
with manifest.open() as stream:
    case = next(row for row in map(json.loads, stream) if row["trial_id"] == trial)
request = json.loads((record / "request.json").read_text())
response = json.loads((record / "response.json").read_text())
summary = json.loads((record / "summary.json").read_text())

assert request["input_ids"] == case["input_ids"] == response["input_ids"]
print(case["user"])
print("Input IDs", response["input_ids"])
print("Emitted IDs", response["output_ids"])
print("Reasoning", response["message"]["reasoning_content"])
print("Answer", response["message"]["content"])
print("Termination", response["finish_reason"])
```

The example has 127 input tokens, 179 emitted tokens and a final answer of B. The source of the prompt wording is the physical trial manifest. The native request retains the actual patch and sampling settings, including seed and reasoning effort. The native response also contains `text`, the emitted sequence with channel delimiters. A recorded partial can have shorter or missing channels. Its partial status and observation timestamp should accompany any quotation.

With NumPy installed, the same example reproduces the choice margin from the original captured numbers, shows the pre/post vectors and checks the requested vector against its content-addressed reference.

```python
import hashlib
import numpy as np

with np.load(record / "captures.npz", allow_pickle=False) as capture:
    print({name: capture[name].shape for name in capture.files})
    a, b = summary["choice_ids"]
    scores = capture["first_response_logits"]
    print("A, B, A minus B", float(scores[a]), float(scores[b]), float(scores[a] - scores[b]))
    print("Actual write L2", np.linalg.norm(capture["write_after_p84"] - capture["write_before_p84"]))
target = json.loads((record / "target_input.json").read_text())
vector = np.load(node / target["file_from_raw_root"], allow_pickle=False)
assert hashlib.sha256(np.ascontiguousarray(vector, dtype=np.float32).tobytes()).hexdigest() == target["raw_fp32_sha256"]
```

At the first natural answer position the A/B vocabulary IDs are 32 and 33. The logits in this case are 13.875 and 28.875, so A minus B is −15.0. The one-coordinate edit has an L2 norm of 0.00048828125. Available arrays vary by trial. Use `harvest-complete.json` for the trial's per-file checksums, `provenance.json` for native capture provenance, and `write-diagnostics.json` when a write was measured.

## Follow interrupted and recovered attempts

A group directory has one folder per logical trial. In the H0 example above, `request.json` names the physical run `astra-air-h0-as-9307c56722d42e4d58e3-one_ulp` and there is no retry pointer. A recovered trial also includes `run-lineage.json`. Its `attempt_number`, `physical_run_id` and `prior_physical_run_id` identify the active and preceding attempts. In `recovery/infra-attempt-NNNN/`, `authorization.json` binds the two physical IDs to the logical trial, the original request hash and the terminal-infrastructure decision. `provider-witness.json` and `files/` contain the retained witness and original evidence. Earlier retry pointers can also appear under `files/`. Inspect `partial-history/`, `partial-channels.json`, `failure.json` and `incomplete-outcome.json` when present. Repeated attempts of a logical trial count once in coverage.

```python
for pointer in sorted((root / "raw").glob("*/run-lineage.json")):
    chain = json.loads(pointer.read_text())
    print(pointer.parent.name, chain["attempt_number"], chain["prior_physical_run_id"], chain["physical_run_id"])
    for auth in sorted(pointer.parent.glob("recovery/infra-attempt-*/authorization.json")):
        decision = json.loads(auth.read_text())
        witness = auth.parent / "provider-witness.json"
        assert hashlib.sha256(witness.read_bytes()).hexdigest() == decision["provider_witness_sha256"]
        print(auth.parent.name, decision["verdict"], sorted(decision["original_files"]))
```

## Rebuilding the frozen stimulus manifest


The Kimi study generator is in research/stimuli.py. It imports only the pinned tokenizer utility, marker, scene fixtures and model-revision metadata it needs from astra-rehearsal/prompts.py. The earlier bounded-answer software examples inside that utility are not research model calls. The trial generator makes no model request. It renders with maximum reasoning effort. Every model-facing input and seed is also provided directly in the versioned inputs.

1. Obtain behavior.csv, stimuli.csv, and molecules.csv from the exact Pyrfume Git commit in ../stimuli/source/provenance.json. Verify their SHA-256 values.
2. Uncompress the two PubChem JSON snapshots in this directory. The registered hashes apply to the uncompressed bytes.
3. Obtain encoding_k3.py, tokenization_kimi.py, tokenizer_config.json, and tiktoken.model from the revision of moonshotai/Kimi-K3.1-Pro identified in ../stimuli/manifest.json. The loader verifies the asset hashes.
4. Use Python 3.11 with NumPy, pandas, RDKit, networkx, and tiktoken. Environment versions appear in the manifest. Run the generator with --panel, --pubchem-properties, --pubchem-synonyms, --tokenizer, and --out, pointing to those local resources.
5. Compare trials.jsonl with SHA-256 4516192c45ff56feaeef616ef3f798ae5e1c280cc3dc9906a66bc23476499631. Earlier inputs and explanations for the two pre-inference amendments are in ../stimuli/freeze-history.
