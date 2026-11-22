# Fit-only retrieval of molecular identity across aliases

Measured 24 molecules, each with two names and two matched prompts. Each full-gallery row below averages the two alias directions, for 48 dependent queries against 24 candidate identities. Top-1 credits share ties equally. The hard foil is another member of the same frozen family when available, otherwise the nearest competing molecular fingerprint.

| Layer | Representation | Name → alias | Alias → name | Top-1 mean | Shuffle mean [central 95%] | Same-endpoint top-1 | Hard foil |
|---|---|---:|---:|---:|---:|---:|---:|
| none | spelling | 75.0% | 70.8% | 72.9% | 4.2% [0.0%, 12.5%] | 72.9% | 84.4% |
| 23 | odor minus name | 16.7% | 25.0% | 20.8% | 4.3% [0.0%, 12.5%] | 20.8% | 79.2% |
| 23 | odor only | 25.0% | 37.5% | 31.2% | 4.2% [0.0%, 12.5%] | 31.2% | 75.0% |
| 23 | printed name only | 25.0% | 33.3% | 29.2% | 4.2% [0.0%, 12.5%] | 29.2% | 68.8% |
| 47 | odor minus name | 20.8% | 29.2% | 25.0% | 4.2% [0.0%, 12.5%] | 25.0% | 75.0% |
| 47 | odor only | 20.8% | 29.2% | 25.0% | 4.2% [0.0%, 10.4%] | 25.0% | 62.5% |
| 47 | printed name only | 16.7% | 20.8% | 18.8% | 4.2% [0.0%, 12.5%] | 18.8% | 70.8% |
| 71 | odor minus name | 29.2% | 25.0% | 27.1% | 4.2% [0.0%, 12.5%] | 27.1% | 75.0% |
| 71 | odor only | 25.0% | 33.3% | 29.2% | 4.2% [0.0%, 12.5%] | 29.2% | 81.2% |
| 71 | printed name only | 29.2% | 25.0% | 27.1% | 4.2% [0.0%, 12.5%] | 27.1% | 68.8% |

Engineering replication and sampling: 1 endpoint fingerprint(s); each identity contributes its two alias directions. A random full-gallery guess has mean top-1 credit 4.2%. 4 molecules have a same-family foil and 20 use molecular-fingerprint fallback. Candidate foils are reused (14 distinct identities).

This measures recognition of the same molecule under different names. Odor-specific input, subjective sensation, and behavioral causality remain separate questions. The observations do not change the predeclared writer, selected layer or gain.

The full tables include midranks, endpoint-restricted denominators, matched-foil provenance, per-query scores, all control contrasts, and coupled-permutation reference probabilities.

Verified 96 completed fit-state receipts across 24 molecules. The registered within-node gallery uses the endpoint fingerprint and recorder source. The primary GPU container was replaced during as-36aefc8b83b3ab691909. The fingerprint is shared across its old and new containers; this restriction cannot control for container-specific differences.

Against permuted identity labels, the upper-tail references for odor-minus-name top-1 recovery at L23, L47 and L71 were 0.000600, 0.000100, 0.000100. These are (1 + exceedances) / 10,001 descriptive permutation probabilities for each individual gallery statistic, without multiplicity correction over layers, views, galleries or controls. They do not test odor specificity.

## Post-hoc paired overlap

| Layer | Both outright | Spelling only | Odor-minus-name only | Both miss | Any tied top | Distinct recovered molecules |
|---|---:|---:|---:|---:|---:|---:|
| 23 | 9 | 26 | 1 | 12 | 0 | 1 |
| 47 | 11 | 24 | 1 | 12 | 0 | 1 |
| 71 | 12 | 23 | 1 | 12 | 0 | 1 |

Post-hoc descriptive overlap; no significance test. A miss has zero first-place credit; tied and outright first are recorded separately.
Across all three layers, contrast recovered 1 distinct directed query/queries from 1 molecule(s) that spelling missed. The recurrence across layers supplies no additional independent rescue. This overlap is not evidence of spelling-independent sensation.
