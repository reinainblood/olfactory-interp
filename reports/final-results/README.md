# Can an unnamed odor cue change what Kimi does?

Kirsten Ruge · Hive Fidelity · GPT-6.2 Astra in Codex Desktop

**We changed the model’s internal state, and sometimes its answer. Neither tested dose reliably carried the intended odor direction four layers downstream.** We stopped the intervention series under its registered rule. All 1,068 eligible scientific trials finished.

[Open the illustrated research notebook](https://hivefidelity.ai/kimi-smell/notebook/) · [Download the full illustrated report](https://github.com/reinainblood/olfactory-interp/releases/download/native-study-v1/what-the-air-remembers-report.zip) · [Public dataset, notebook and reproduction code](https://github.com/reinainblood/olfactory-interp/releases/tag/native-study-v1)

## What was injected?

The recipient saw an unnamed sample and a neutral vertical bar. The added vector was constructed from six odor-similarity judgments. We learned the mapping on 24 fitting compounds and used four development compounds to choose a layer. The odor-minus-printed-name map at layer 47 had the highest development cosine, +0.164, across the four compounds and their two names. Two compounds had opposite prediction signs under their two names. The model revision and all inputs were fixed before the study.

## Did the correct signal arrive?

For each compound the intended signed projection at layer 51 had to exceed the magnitude of the mismatched-cue projection by at least 0.10 and exceed three times repeat-sham noise. Three or more of the four compounds had to pass.

| Unnamed development compound | Intended cue, 0.05× | Mismatched cue, 0.05× | Intended cue, 0.10× | Mismatched cue, 0.10× |
| --- | ---: | ---: | ---: | ---: |
| Allyl hexanoate | −0.093 | +0.001 | −1.548 | −0.236 |
| Vanillin acetate | −0.084 | +0.230 | +0.055 | −0.035 |
| Diethyl malonate | −0.255 | −2.429 | −0.051 | −0.131 |
| Ethyl-3-hydroxybutyrate | −0.173 | −4.194 | −0.374 | −0.169 |

All nominated repeat-sham projections were zero. **The result was 0/4 at each dose.** On eight odor writes, increasing the dose improved the median agreement of the physically delivered direction with the requested vector from 0.434 to 0.616. On all 24 paired nonzero edits, the CPU reconstruction predicted the observed differences between the two physical doses. More accurate physical delivery still failed the specificity test.

Across the same eight presentation-order pairs per dose, the intended cue switched the sampled letter relative to sham in **2/8** at 0.05× and **1/8** at 0.10×. A mismatched odor switched **3/8 at each dose**. The printed-name writer also switched 3/8 at each dose, and repeat sham switched 0/8. These are repeated conditions on four compounds.

## What worked with words?

When the odor was written into a household story, Kimi selected the matching request in **48/48** trials. It chose correctly in both histories for **all 24 stories**, switching the action every time the earlier odor assignment was reversed. It also answered all **32 explicit spelling controls** correctly. The protocol withheld the hidden-cue household trials after the delivery failure, so this experiment does not establish smell-induced retrieval, lasting memory or subjective olfaction.

On 48 independently collected comparisons across 12 held-out compounds, Kimi agreed with the human odor panel on **28/48** and with its own word-association judgments on **41/48**. Across the more reliable human-reference subset, agreement was 8/15. An earlier audit of the Costco setup recovered the exact donor sentence in 47/47 cases at one layer. These controls keep language-based explanations in play.

## Coverage and welfare

The acquisition lasted 26 hours and 32 minutes and used 49.64 attributable eight-GPU node-hours. Of 2,892 registered physical IDs including the approved second dose and conditional extensions, **1,068 were observed and 1,824 were withheld by the registered gate**. No eligible trial was missing. The additional engineering calibrations and interrupted predecessor are identified separately in the data. The two extra nodes were verified at zero after the study.

Both emitted channels were independently reviewed in 122 scheduled welfare cases. Each received a disposition of no concern observed. One additional review of prolonged indecision in an ordinary baseline did trigger a temporary hold. That response reached a coherent final answer after 30,798 emitted tokens. Two independent terminal readers found no expressed withdrawal or acute distress. This is a record of observed behavior and review decisions.

[How to verify and restore the release](../../reproduce/README.md) · [Frozen study inputs](../../stimuli/manifest.json)

All 26 release assets were downloaded without authentication and checked against their published digests. A fresh restoration reproduced the final public scientific results byte for byte. [Independent readback receipt](public-verification.json)
