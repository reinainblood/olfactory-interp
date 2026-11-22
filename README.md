# What the air remembers

**Sunday, November 22, at 2 p.m. Chicago time.** Kimi had completed 869 scientific trials, including all 160 ordinary state captures. The fitting and development sets had 312 of the 336 required odor comparisons, with complete inputs for 19 of 28 compounds. The experiment had yet to deliver its first learned odor cue. [Download the illustrated Sunday report and timestamped evidence (ZIP)](reports/what-the-air-remembers-sunday-interim.zip)

What could already be measured? At layer 71, the difference between activations after an odor instruction and a printed-name instruction retrieved the alternate name in 13 of 48 searches. Matching letter sequences alone retrieved 35. Both measurements use the same 24 fitting compounds. This leaves a concrete question for the intervention. If the question contains neither name, can a cue built from odor judgments recover a decision about the compound? [Sunday evidence record](reports/sunday-interim/evidence-20261122T200005389208Z.json) · [Underlying measurements and controls](reports/fit-aliases/measured-results.md)

Kirsten Ruge’s independent Hive Fidelity research asks whether a hidden cue synthesized from Kimi K3.1 Pro’s own odor-similarity judgments can recover decisions about an unnamed sample and retrieve an arbitrary detail from a recent household episode. The fixed checkpoint is `moonshotai/Kimi-K3.1-Pro` at `d9e99b0792a5e93b78ea9bea62a68167e36ddd9e`. Study execution uses maximum reasoning effort, temperature 1, and natural generation without an application output-token cap.

The [scientific registration](protocol/natural-response-registration.md) defines the revised natural-response endpoint. The [scientific proposal sections](protocol/design.md) contain the original rationale and contrasts. The natural-generation requirements and frozen trial inventory supersede software-only examples or conditional sizing in that earlier document.

- [Frozen inputs and checksums](stimuli/manifest.json) cover 24 fitting, four development and 12 held-out compounds, 20 candidate reference odors and 24 household narratives. The 2,852 planned records include conditional extensions. [Every planned input](stimuli/trials.jsonl) includes the text and exact rendered token IDs.
- [Human-source provenance](stimuli/source/provenance.json) and the [selected human measurements](stimuli/source/selected-human-panel.csv.gz) document the Keller–Vosshall panel reanalysis.
- [Earlier Costco donor-identification audit](phase0/donor-audit/summary.json) and its [individual rows](phase0/donor-audit/donor-ranks.csv) describe a retrospective test using previously captured states. These are separate from the prospective trial results.

The human odor panel was collected by Andreas Keller and Leslie Vosshall. The present study refers to their published [2016 paper](https://doi.org/10.1186/s12868-016-0287-2) and the [Pyrfume archive](https://github.com/pyrfume/pyrfume-data/tree/main/keller_2016). The MIP protocol is credited to K. Ruge and Claude, version 1.0, under CC BY-SA 4.0. Source-specific provenance and terms remain with the supplied materials.

## Pre-exposure observations

The [original activation rows](phase0/donor-audit/native-rows/native-rows.json) make the earlier sentence-identification audit independently reproducible. The four NPZ files contain the relevant donor, dots and patched attention inputs at L28/L71/L92. Use `python phase0/recheck_published_donors.py phase0/donor-audit` from this repository with NumPy installed. Each recovered sentence is one candidate in a finite library.

The [human split-half analysis](analysis/phase0-human/human-reliability.json) measures the stability of the ratings-derived external reference. The [low-dose arithmetic tests](phase0/dose-rounding/summary.json) and [corrected native rounding bound](analysis/phase0-dose/historical-bf16-cap.json) use old Kimi states and CPU arithmetic. The [Monte Carlo sensitivity grid](phase0/design-sensitivity/operating-characteristics.csv) uses synthetic data only. None of these pre-exposure results is a prospective hidden-odor behavioral effect.

[Published subset for the three-layer wording and rounding controls](phase0/frame-inputs/frame-records.json). The frame-specificity and dose-rounding scripts accept the frame-inputs directory directly. The [lexical surrogate analysis](phase0/lexical-surrogate/summary.json) fits on other donors, withholding both candidates for every pair. The [48-record condition-masked historical safety audit](phase0/prior-safety-coding/result.json) includes separate reviews and the underlying historical texts. All these samples predate the prospective experiment and retain their original status.

[Illustrated pre-exposure report](reports/pre-exposure/index.html), with the prospective count explicitly shown as zero in this version. Download the reports/pre-exposure directory to view the interactive chart offline.

The checkpoint and its license are maintained by Moonshot AI. [Official model card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · [Kimi K3.1-Pro License](https://huggingface.co/moonshotai/Kimi-K3.1-Pro/blob/main/LICENSE). This dataset contains study inputs and measurements; it does not redistribute checkpoint weights.

[Signed Phase 0 acknowledgment](phase0/acknowledgment-completed.md) · [measured review record](phase0/completion.json) · [terminal observer result](phase0/live-observer-run/results.json).

## What one coordinate changed

On the vanillin acetate calibration prompt, Kimi chose eugenol after 314 emitted tokens. At the same seed, changing one coordinate at layer 47 by a single BF16 step led to a whiskey lactone choice after 2,146 tokens. The first token disagreement came at output token ten. Clean and zero-write controls matched exactly. All three machines reproduced both trajectories. The second named compound kept its final choice under its one-step edit. These two examples test sensitivity to an arbitrary numerical change. Odor selectivity requires the held-out scientific comparisons. [Paired per-node measurements](analysis/native-qualification/trajectory-sensitivity.json) · [Native parity receipt](analysis/native-qualification/source-parity.json)

The twelve explicit controls each yielded the correct sampled choice and an A−B score favoring that choice at the first natural answer position. The median A+B probability was 0.99999815. [Scientific qualification](analysis/native-qualification/scientific-h0.json) · [Download all 30 native calibration and answer-control records](https://github.com/kirstenruge-ship-it/what-the-air-remembers/releases/tag/native-qualification-v1)

Before the first hidden odor write, we registered a supplementary comparison of the token at which matched reasoning histories diverge. Its unit is the molecule. The original primary endpoint stays fixed. [First-divergence registration](protocol/trajectory-registration.md)

An outcome-blind scheduling amendment assigned ten whole, previously untouched groups to the faster of two parity-qualified recorders. An independent audit verified every earlier assignment and the full input manifest. [Assignment audit](protocol/scheduling/20261122T062628-post-application-audit.json)

## Sunday field note

The first 200 completed scientific trials yielded 100,629 emitted tokens. The field note shows the two measured calibration trajectories, the earlier donor-sentence audit, and the answer-boundary check on the first 100 scientific completions. It records what the study had established by 1:57 a.m. Chicago time on November 22. [Download the illustrated field note and data tables](reports/what-the-air-remembers-first-200.zip) · [Browse its sources](reports/first-200)

## Can another name retrieve the same compound?

Across 24 fitting compounds, the odor-minus-printed-name activation retrieved the correct alternate name in 10, 12, and 13 of 48 reciprocal queries at layers 23, 47, and 71. Random matching averages two. Spelling alone recovered 35. At every layer, the activation contrast recovered one query spelling missed, the same direction from methyl octanoate to methyl caprylate. This secondary analysis measures identity in ordinary named prompts. The causal study tests whether an unnamed odor-quality intervention can steer a decision. [Measured results and controls](reports/fit-aliases/measured-results.md) · [96 native records, exact activations, code and offline field note](https://github.com/kirstenruge-ship-it/what-the-air-remembers/releases/tag/fit-cross-alias-v1)
