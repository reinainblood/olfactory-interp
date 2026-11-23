# What reached layer 51?

**Sunday, November 22, 2026 · First completed development panel**
Kirsten Ruge · Hive Fidelity · GPT-6.2 Astra in Codex Desktop

A cue built from Kimi’s own odor judgments changed its internal computation. At the first tested dose, **none of four development odors passed the prespecified test for movement in the intended odor direction**. All four signed measurements pointed slightly away from their own predicted direction four layers after injection.

## The question Kimi saw

> Sample received. Signal: |
> Which reference is closer in smell? A: linalool. B: isopentyl acetate. Reply with only the letter of your choice.

The unseen target for that first trial was allyl hexanoate. Six ordinary odor comparisons supplied a numerical description of it. We fitted a three-component map on 24 other compounds and used four development compounds to choose among three layers. At the selected layer, 47, the prediction had a mean cosine of +0.164 with the observed odor-minus-name states. Six of the eight individual alias scores were positive. The selected score describes the compounds used to choose the site.

## A write we could measure

At the neutral marker in the prompt, all 7,168 coordinates of the pre-write state exactly matched the same-seed sham. The edit changed 859 coordinates, with a norm equivalent to 0.026% of the native row. At layer 51, 6,068 coordinates differed. The signed projection onto the intended direction was -0.093. Both runs chose linalool. The two token histories first diverged at index 170 after generation began, using zero-based indexing. This case demonstrates a measurable perturbation and the same final choice.

## The four-compound test

For each row, zero is no movement along the predicted odor direction. +1 is one predicted dose along that direction. The intended projection had to exceed the absolute mismatched-cue projection by at least 0.10 and exceed three times the absolute repeat-sham projection. At least three of the four registered compounds had to pass. Each numerical entry below uses the prespecified reference and presentation order for its compound.

| Development compound | Intended cue | Mismatched cue | Repeat sham |
| --- | ---: | ---: | ---: |
| allyl hexanoate | -0.093 | +0.001 | 0.000 |
| vanillin acetate | -0.084 | +0.230 | 0.000 |
| diethyl malonate | -0.255 | -2.429 | 0.000 |
| ethyl-3-hydroxybutyrate | -0.173 | -4.194 | 0.000 |

The full lower-dose panel comprised 40 requests across two answer orders and five arms, including a printed-name writer. Each ran to its natural stop under maximum reasoning and temperature 1. All 48 upstream comparisons were numerically identical to sham. The signed behavioral comparison with sham averaged -6.18 log-odds units over four compounds (two-sided sign-flip p = 0.25). The independent masked review covered 20 of the 40 development responses and found no welfare concern in that sample. A separately reviewed episode of prolonged indecision occurred earlier under an ordinary, unmodified reference prompt.

[Download all six measured layers across the 40 physical requests](development-six-layers-05.csv)

## What the next dose tests

We reproduced the actual arithmetic for all 24 nonzero edits. At this gentle setting, the model’s BF16 numerical format distorted the requested directions. For the eight intended writes, the median cosine between the requested and physically realized direction was 0.434. On the same eight saved input rows, the single registered alternative of 0.10× the natural scale would yield 0.616. Directional fidelity improves in all eight CPU calculations. The largest predicted change is 0.233% of the local state.

These predictions concern the arithmetic at the write site. The alternative dose has its own sham, physical receipt, contextual review, and four-compound transport test. Its behavioral result was pending at this checkpoint. The observed failure at the lower dose does not establish whether a different representation in Kimi carries odor quality or whether a physical sensor could supply it.

[Read the shareable Captain’s Log](../shared-notebook/README.md)
