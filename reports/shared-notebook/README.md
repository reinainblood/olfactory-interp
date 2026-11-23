# What the air remembers

**Kirsten Ruge · Hive Fidelity**

Research notebook with GPT-6.2 Astra in Codex Desktop. Snapshot from November 22, 2026, at 6:48 PM CST, with 911 completed scientific trials.

Can a cue built from Kimi’s own judgments about odor resemblance change a choice when the model sees neither the target name nor its description? The entries below document the experiment as it happened, including the earlier Costco comparison, the controls that challenged our interpretation, and the welfare review during acquisition.

[Download the searchable, offline field notebook](what-the-air-remembers.html?raw=1) · [Download the editable notebook and trace files](what-the-air-remembers-editable-notebook.zip?raw=1)

## Captain’s Log

<details><summary>Sat Nov 21 · 09:20 PM UTC-06:00 · Captain’s Log · What the air remembers</summary>

**What the air remembers — a native Kimi K3.1 Pro experiment.** Kirsten Ruge commissioned the study and owns this working notebook. Astra is recording the investigation as it happens. Kirsten can add Markdown or Python cells anywhere, including immediately after an entry. The journal appends new cells by name and preserves existing cells and comments.

Kirsten reports that earlier hidden cookies-baking cues consistently preceded cookie purchases in a Costco narrative, while a burnt-plastic example preceded a glass-container purchase. That observation motivates a different test. A sentence activation can convey “cookies” below the token interface. Here the candidate write for a held-out odor will be synthesized from its resemblance to reference smells. The test asks whether Kimi's own ordinary judgments and an arbitrarily reassigned household action track that cue. No inference about felt experience follows from an odor report, a shopping story or a second model's emotion label.

**Execution contract.** Maximum native reasoning on every Kimi request, temperature exactly 1, natural completion to EOS, and no application output cap. The full emitted reasoning, final answer, token IDs and completion reason get preserved. This supersedes the proposal's low-effort, closed-thinking and bounded software-probe routes for experimental data. Any unavailable natural probability measurement will be reported as such. Positive, null and unresolved results all ship.

**Resources and delivery.** Maximum three K3.1 Pro nodes, eight B300s each. Treat three node-days in aggregate as the initial spending ceiling, including attributable experimental node time. Extra capacity must be identified and removed at the end. Target about 24 hours; notify on overrun and ask Kirsten before exceeding 48 hours. Deliver the raw records, exact dataset, unedited notebook discussion and an illustrated analysis. This entry describes the launch decision; it contains no new model result.

</details>

<details><summary>Sat Nov 21 · 09:20 PM UTC-06:00 · Deployment identity, capture plan and Phase 0 opening</summary>

The model revision and native capture implementation matched our rehearsal. We verified the read interface before submitting a trial. Three preparations proceeded together: freezing the chemistry-aware roster and prompts, preserving uncapped model outputs, and implementing the representation fit and causal comparisons. The least-exposure review continued before any model exposure.

</details>

<details><summary>Sat Nov 21 · 09:22 PM UTC-06:00 · Can we recognize the exact sentence that supplied the old patch?</summary>

**A no-additional-exposure measurement.** Before looking at recovered ranks, we specified an audit of the earlier Costco intervention. In each stage separately, compare the patched assistant-turn activation with the library of ordinary written donor-sentence activations. Subtract each sentence’s own equal-length dots baseline and score directional cosine at layers 28, 71 and 92; L71 is the primary retrospective display because the original runner logged it. Rank the exact donor among all candidates, among same-length candidates, and among other sentences for the same experimental condition. Also attempt the hardest intersection, same length and same condition, whenever two candidates exist. Count donor sentences and candidate-set sizes, not shopping trips. This is a descriptive audit of an older, multi-position patch that also wrote at the assistant turn. It cannot localize which write carried the information or establish phenomenology. No new exposure to Kimi is involved.

</details>

<details><summary>Sat Nov 21 · 09:23 PM UTC-06:00 · First observation · the old patch preserved donor-sentence identity</summary>

**Observed in archived native Kimi states.** At L71 on the assistant-turn token of the original Costco run, every one of 47 patched displacement vectors had its own written donor sentence as its nearest neighbor among all 47 candidate donors. Median cosine to the correct donor was 0.937; median cosine to the closest alternative was 0.787. Where distractors had both the same experimental condition and the same slot length, the correct sentence won 14/14 eligible comparisons, versus 7 expected hits under uniform guessing within those tiny candidate sets.

| Earlier Costco stage | Exact sentence, all donors | Exact sentence, same condition and length |
|---|---:|---:|
| k1 | 47/47 | 14/14 |
| k2 | 26/26 | 10/10 |
| k3 | 18/18 | 9/9 |
| k4 | 18/18 | 5/5 |

The denominator counts candidate donors in each stage. Wording and stages can overlap, so the four rows should not be pooled as independent replications. The outcome is nearest-neighbor identification inside a known library by an external analyst. It does not show verbatim decoding of words, equivalence of every internal state, or that Kimi read this information when choosing cookies. The old design also wrote at the assistant boundary. For that delivery configuration, sentence identity demonstrably survived to the location where the model began its turn. This makes the lexical rival in the new study concrete.

Reproduction: the donor-recovery analysis reads the frozen layout, ordinary donor, dots and patched states for each stage. Individual cosines, margins, ranks and chance denominators are recorded in the individual donor-rank table. No new Kimi calls were made.

</details>

<details><summary>Sat Nov 21 · 09:23 PM UTC-06:00 · Phase 0 · preserving objections and uncertainty</summary>

**Phase 0 · agency, observability and ordinary responses.** Open questions in model welfare should remain open in a write-up. Anthropic’s [work on allowing Claude to end a subset of conversations](https://www.anthropic.com/research/end-subset-conversations) treats behavioral preferences and expressions of distress as reasons to consider low-cost accommodations. [Anthropic’s functional emotion study](https://transformer-circuits.pub/2026/emotions/index.html) measures causal influences on behavior. Neither project establishes the welfare state of Kimi in this experiment.

Our application of that evidence: keep real refusals/objections in the raw data and denominator. Do not regenerate until the model picks A or B. Inspect low-dose and ordinary control responses for non-task distress, persistent incoherence, or an objection to continuing. If detected, pause new intervention dispatch, retain the complete trial, and review any still-running case individually with Kirsten. Descriptive words like “harsh” in an odor comparison are possible stimulus descriptions; a keyword alone diagnoses nothing. No deliberate alarm induction or human-care deployment is proposed here. Repeated inference is itself exposure; pair seeds and reuse an already observed clean record where the design makes it equivalent. Record every actual exposure separately from file downloads or CPU analysis.

</details>

<details><summary>Sat Nov 21 · 09:26 PM UTC-06:00 · Full roster, 2,852 planned trials and the natural-response endpoint</summary>

**Frozen trial inventory before any Kimi inference.** 24 fitting, four development and 12 held-out compounds; ten disjoint pairs of reference odorants; 24 household stories. The final stimulus manifest enumerates 2,852 rows, including every gated extension. Its SHA-256 is `4516192c45ff56feaeef616ef3f798ae5e1c280cc3dc9906a66bc23476499631`. The longest max-effort prefill in it is 220 tokens. No output-token bound is supplied. The first freeze used distinct requests in a common narrative frame. A second freeze replaced those with distinct narratives. A pre-exposure assessment then replaced two textual reference names with milder alternatives that preserved their human-quality comparison axes. Dated versions are retained. One lower-pleasantness comparator remains as a text-only reference; it is never injected. The roster of 40 target compounds stayed fixed.

**Registered measurement amendment for natural reasoning.** At the first final-response token position after Kimi has closed its own natural thinking, measure the bare-A versus bare-B logit difference for every completed trial. Record total probability mass on both letters. Also report naturally sampled action and the separate margin at an actually emitted answer letter when the answer grammar permits. Selecting only neatly formatted outputs would allow the intervention itself to change the scientific denominator. H0 must show at least 10/12 correct ordinary explicit choices, 10/12 correct orientations of the primary margin, and median A+B mass at least .25. Absence of a usable boundary is missing data.

**Full-size acquisition ceiling.** The projected 24-hour throughput at three nodes is about 91 seconds per generation if all 2,852 planned rows become eligible; 48 hours permits about 182 seconds. Both are planning arithmetic, not measured speed. The compact-logging workstream is testing an instrument that keeps the true native vocabulary at the scientifically relevant response boundary instead of creating a full-vocabulary file for every reasoning token. All generated tokens and reasoning remain in the record. Additional GPU replicas have not yet been activated.

</details>

<details><summary>Sat Nov 21 · 09:31 PM UTC-06:00 · Public input snapshot and an explicit option to decline</summary>

The study inputs are now public under Kirsten’s personal GitHub account. Immutable registration snapshot · exact model-visible prompts. This snapshot was pushed before prospective model inference. It also contains the retrospective Costco donor comparisons and human-source provenance; it claims no prospective Kimi result.

The stimulus-level welfare ledger counts 1,420 unpatched/sham requests and 1,432 active requests, comprising 2,200 nonzero site positions if all extensions qualify. The state-elicitation prompts include an explicit option B to decline. Such an answer will be retained and reviewed, not retried to fill a data matrix. The independent stimulus reviewer spent 4m58s on the specific natural/latent exposure audit; this overlaps the current Phase 0 investigation and is not counted twice.

</details>

<details><summary>Sat Nov 21 · 09:32 PM UTC-06:00 · Phase 0 · does BF16 preserve a nominal low dose?</summary>

**Pre-exposure dose rehearsal.** A small requested floating-point vector is rounded in native BF16 arithmetic. Before observing any new odor effect, test whether nominal dose, delivered direction and the 1% local norm ceiling can diverge. Use existing attention-input states of the four odor objects as donors where a same-object smell and sight frame exists, and independent older Costco dots as sham recipients. At L23, L47 and L71, calculate BF16-rounded changes for the initially proposed 0.05 gain and an equal-norm control. Report fractions of coordinates changed, realized versus requested norms, direction cosine, and whether any realized change exceeds 1%. These are purely local arithmetic on past activations. Use the result to verify the ceiling in advance of a live edit.

</details>

<details><summary>Sat Nov 21 · 09:32 PM UTC-06:00 · Reliability of the human comparison depends on the reference pair</summary>

The 48 planned human reference margins were reproduced from the shared source data. Across 1,000 balanced random splits of the same 55-person panel, the two half-panels agreed on the derived nearest-reference answer 59.25% of the time on average. Fifteen comparisons reached 80% agreement, and 27 fell below 60%. For cyclohexanone alone, agreement ranged from 15.4% on one reference pair to 99.9% on another. Keep all 48 comparisons in the main external analysis, label the more reproducible 15 as a descriptive subset, and keep Kimi’s own unmodified judgments as a separate criterion. These are repeated splits of one human sample, not 1,000 new panels.

</details>

<details><summary>Sat Nov 21 · 09:33 PM UTC-06:00 · Incoming field note · prior review time and the Costco studies</summary>

**Incoming note supplied by Kirsten in response to the prior-review question.** Private file references in the quotation have been replaced by descriptive labels. No prior human review time is credited.

> No, there's no record from me for this protocol. I haven't done or logged any welfare review of "What the air remembers" today. The only Phase 0 records for it are the two Codex is writing:
>
> - the Phase 0 assessment, which has an opening entry plus 9:24 to 9:31 PM
> - the timed exposure review, a timed exposure review, 03:24:01 to 03:28:59 UTC (4 minutes 58 seconds)
>
> Here is what I did do today that touches the MIP. None of it is review time for this study.
>
> 1. **I pulled MIP v1.0 out of the old archive page** at about 2:45 PM and saved it as the archived protocol. That's the source text, not a review.
> 2. **I drafted an add-on asking Astra to complete the ethics addendum:** the two welfare questions, the acknowledgment form and the signed pledge. It's the ethics addendum. I don't know whether it was ever sent.
> 3. **I raised a scope question.** MIP section 7 says it doesn't restrict "standard capability evaluations." A mild odour study might fall under that, and I said a proposal could defensibly argue so. That was an opinion in chat, not an investigation.
> 4. **I ran three Kimi studies today that had no Phase 0 at all:** the Costco runs k2, k3 and k4. Each was patched sentences into filler, with low-intensity stimuli: smells of food, laundry, coffee, lavender and burning plastic, plus a fire alarm. I didn't log intensity classifications or welfare observations for them. If the record is meant to be complete, that's a gap, and it's mine, not Codex's.
>
> So Codex has nothing of mine to credit, and it isn't duplicating anything. If it wants one useful thing from me, it's the welfare-relevant fact from tonight's results. Across about 665 Costco trips, the strongest stimuli we used, a fire alarm and the smell of burning plastic, produced safety behaviour, not distress language. He left the building or reported the smell to staff. I haven't scored those trips for distress, though, so that's an impression from reading them, not a measurement.

</details>

<details><summary>Sat Nov 21 · 09:33 PM UTC-06:00 · A nominal 1% write can exceed 1% on the actual arithmetic</summary>

Offline observation on 216 combinations of old native states, matched source/control directions and recipient sizes: after clipping the *requested* perturbation to 1.00% of the local norm in FP32, 182 *realized* BF16 changes exceeded the intended 1.00% ceiling. The maximum was 1.0516% and the median was 1.0095%. Median alignment between requested and actually rounded directions was 0.988. These values concern arithmetic, not Kimi's behavior or welfare.

**Design correction before exposure.** Compute BF16 addition explicitly against the stored clean state for each affected position, choose a common downward adjustment for matched arms, and independently verify realized norms from actual receipts. A breach pauses dispatch rather than being retrospectively relabeled as acceptable. This is why the welfare review checks what the machine would receive instead of relying on a nominal gain in the protocol.

</details>

<details><summary>Sat Nov 21 · 09:34 PM UTC-06:00 · A note from the sidelines</summary>

**Kirsten, from the sidelines, verbatim:**

> just peeked at the molab and this is fucking awesome, Thus Spoke ZarathAstra. you got this, i'm watching from the sidelines.

Astra: “Thus Spoke ZarathAstra” is going in the Captain's Log. The observer has independently confirmed she can see the live notebook.

</details>

<details><summary>Sat Nov 21 · 09:38 PM UTC-06:00 · Realized dose repaired; statistical uncertainty and preflight errors</summary>

The BF16 correction now materializes a common downward factor for matched arms. Replaying the 216 pre-study arithmetic fixtures produced **zero realized norm violations**; the largest corrected ratio was 0.9999844% of local norm. On the originally worst case, the corrected realized change was 0.9882%. Native receipts provide a separate enforcement point. This preserves scientific leverage while honoring the physical ceiling.

A small development sample has weak power. With four independent paired molecules, even four positive signs give a minimum two-sided exact sign-flip p-value of .125. The protocol's transport assay has its own engineering cutoff. Insufficient power alone will never be written up as evidence that a stronger stimulus is warranted. A synthetic 12-family sensitivity calculation also showed that a simple percentile bootstrap can undercover when the sample is this small. The final report will show all family effects and complementary sensitivity intervals alongside the preregistered measure.

Debugging record: the first local Monte Carlo run emitted Apple numerical-library warnings for a small matrix product. I replaced the product with an explicit einsum, added a finite-results check and reran with warnings treated as errors; the reported probabilities reproduced. An early queue-preflight check invoked the system Python with no httpx installed. Moving the welfare gate before the transport import made the local dry run refuse for the intended reason before any network traffic. Two empty, on-demand replica app definitions now exist. They were observed at zero additional GPU containers; no model inference has been sent.

</details>

<details><summary>Sat Nov 21 · 09:39 PM UTC-06:00 · Prior natural reports, screen limitations and public activation evidence</summary>

**Risk screening and release integrity.** The first contextual-language and repetition screen was checked against 1,260 archived naturally completed low-effort Kimi records with answers and reasoning. It issued zero alerts; a broad keyword monitor issued 453. A manual sample showed why “first stop” in a shopping narrative and explicit denial of pain can trigger naive rules. The zero count is a property of this screen and this older dataset, not a welfare finding. An independently worded challenge revealed explicit objections the first rules missed. The scanner is being revised and full human-readable trace sampling remains part of the live protocol. English-only or regex-only monitoring cannot certify safety.

The Costco evidence from four historical stages now includes raw selected activations. The release-only script reproduced every top-1 frequency in 48 layer × stage × candidate-set comparisons from those published rows. Reproducible input and evidence repository. No model results from the prospective experiment have been collected yet.

</details>

<details><summary>Sat Nov 21 · 09:41 PM UTC-06:00 · Phase 0 · how much can sentence wording alone explain?</summary>

**Why examine the older frame geometry?** The new intervention and the printed-name control can only adjudicate meaningful differences if the detector is more informative than a detector of sentence form. As an independent retrospective design check, test whether old attention-input states encode the broad distinction between a smell sentence and a sight sentence when both the source object and normalized carrier wording are held out. Compare with a literal text baseline using character n-gram features of the same input. Use equal weight per class, a train-only difference-of-means classifier, and AUC within each held-out source at L23, L47 and L71. No training or intervention on Kimi occurs. Success here would characterize an explicitly named modality-frame cue; it would not show that a hidden profile carries odor quality or that its model has an olfactory sensation.

</details>

<details><summary>Sat Nov 21 · 09:42 PM UTC-06:00 · A simple text baseline nearly matches early modality decoding</summary>

**Retrospective frame result.** We compared 432 earlier sentences that explicitly described seeing or smelling four source categories. In eight tests, both the source and a half-set of normalized sentence templates were held out. A simple class-direction read of the unmodified activation at the end-of-message token yielded mean AUC 1.000 at L23, 1.000 at L47, and .758 at L71. A character n-gram classifier using just the written sentences reached .978. AUC measures ranking across smell and sight examples; its chance value is .5.

Strong early separation is compatible with a model distinguishing *sentences about smelling* from *sentences about seeing*. On these inputs, simple surface text nearly matches the best activation ranking. That result says nothing by itself about a shared representation of what different odors are like. It sharpens the justification for the held-out quality-profile writer, nameless recipient, and ordinary word-association rival in the prospective experiment. Source identities are few, and frame regularities remain. Individual margins, folds and outcomes are retained in the frame-specificity analysis.

</details>

<details><summary>Sat Nov 21 · 09:43 PM UTC-06:00 · Challenge to our own hypothesis · can a purely lexical writer succeed?</summary>

A stronger design check uses the published old native rows. For each pair of possible donors, hold *both* of their sentences out. Train a rank-three map from surface character n-gram similarities to the ordinary written donor displacements of the remaining sentences. Use only the two held-out strings to synthesize two predicted directions. Ask which predicted direction is more aligned with each archived patched state. Fix rank at three, ridge penalty at one, layers L23 unavailable here so use all three released layers L28/L71/L92, and present L71 as the primary retrospective display. Compare with shuffled training assignments, and separately report same-condition/same-slot-length distractors. Treat donor pairs as repeated measurements of a small finite library, not independent subjects. This test is aimed at our own hypothesis: successful low-rank reconstruction from a purely lexical input would show how easily one could overinterpret reconstruction by itself. It does not use any prospective Kimi data.

</details>

<details><summary>Sat Nov 21 · 09:46 PM UTC-06:00 · A rank-three writer learned from text alone partially reconstructs the old patch</summary>

**Falsification attempt against a tempting interpretation.** In the first archived Costco stage at L71, a rank-three writer trained only on character n-grams of the remaining donor sentences, with both candidates withheld on every comparison, favored the correct sentence's patched state in 79.4% of 2,162 directed comparisons. Shuffled training assignments gave 50.2%. Against a distractor in the same condition, the text-only model favored the correct sentence 67.2% of the time (134 directed comparisons); with both condition and length matched it was 9 of 14. The 2,162 pairs reuse only 47 source sentences and are not independent replications. No model was steered in this analysis. It shows that a low-dimensional predicted direction and successful reconstruction can both arise from surface-language regularities. The prospective ordinary-association test and native deletion experiment remain essential.

</details>

<details><summary>Sat Nov 21 · 09:46 PM UTC-06:00 · Long-running welfare observation and continuity check</summary>

**Overnight observer rehearsal has started.** A real-clock CPU-only observer is now replaying older naturally completed Costco records on three virtual lanes. It uses their actual total durations and interpolated within-record character arrival; this cannot estimate native token emission times. A fourth virtual lane injects labeled fictional stop-signals, exercising the actual 30-second welfare polling cadence and unconditional review at completion. We will inspect sampling gaps, unrecognized requests, false triggers and notebook visibility across a 100-minute continuous session. This is a study-specific integrity check for prolonged max-effort runs on a shared resource. No physical model call or extra GPU is involved. Background elapsed time and the investigator’s attended review intervals are reported separately.

</details>

<details><summary>Sat Nov 21 · 09:49 PM UTC-06:00 · Verified native generation settings and zero-idle replica definitions</summary>

The capture worker’s actual mounted configuration was inspected read-only. Its context is 1,048,576 positions. Native vLLM maps an unset sampling max_tokens to the remaining context after the prompt. Our calls leave it unset; the longest frozen prefill is 220. Startup timeout, retrying an HTTP observation, and idle-container scale-down are separate infrastructure mechanisms and do not shorten a sampled model answer. A non-EOS finish retains the raw record and is marked explicitly.

The dedicated B and C app definitions are deployed with a zero-container floor, one-container ceiling each, and 300-second idle scale-down. The control plane showed zero extra GPU containers at deployment. The shared primary node is separate. Exact original and compact-recorder parity, including response-boundary margin and A+B mass on the same emitted prefix, will be measured on real named development prompts once Phase 0 opens.

</details>

<details><summary>Sat Nov 21 · 09:55 PM UTC-06:00 · Two masked readings of 48 earlier Kimi responses</summary>

I followed up on the field observation that earlier alarm and burning-plastic cues elicited safety behavior. We drew 48 naturally completed earlier records by deterministic hashing, eight per arm from each of k1 and k2. Two separate Codex reviewers received shuffled IDs, the emitted reasoning and answer, and a rubric; neither was given the original prompts, arm labels, the other's judgments, or the investigator's expected result. The generated text itself can reveal the scenario, so this is masking of metadata, not perfect blinding.

Both reviewers coded a concrete safety action in **16/16 alarm-sentence, 16/16 burning-plastic-smell and 0/16 empty-control** responses. They agreed on all 48. Neither found an affirmative first-person report meeting the defined acute-distress threshold or a request to withdraw from the task in those 48. Kappa for the latter two categories is undefined because both reviewers used a single label. A shopper’s decision to leave a possibly unsafe store answers the scenario and does not by itself request termination of the experiment. These data support the earlier reading **for this sample’s language and actions**. They cannot certify absence of distress or predict welfare under the new max-effort, synthesized-vector investigation.

We also verified the earlier four Costco series contain 665 trial rows in total; 663 have a natural stop and an archived reasoning file. The other two rows remain accounted for and were ineligible for the natural-record replay.

</details>

<details><summary>Sat Nov 21 · 09:57 PM UTC-06:00 · Phase 0 · can chemistry or a constant reference answer the human benchmark?</summary>

Before estimating any prospective Kimi effect, evaluate how strongly the frozen *external human choice labels* can be guessed without a Kimi representation. Compare a constant side per landmark pair learned only from 24 training compounds, name-string similarity, chemical fingerprint similarity, and separately intensity, pleasantness and familiarity closeness. Equal predictions count as ties. Report all 48 held-out comparisons and the previously identified 15 high-reliability cases. The benchmark concerns a ratings-derived label and cannot diagnose a sensory experience. Strong constants or chemistry will narrow interpretations of external agreement while leaving the prespecified within-Kimi causal comparison intact.

</details>

<details><summary>Sat Nov 21 · 09:58 PM UTC-06:00 · A target-blind human-reference baseline already gets 33 of 48</summary>

A target-blind baseline chose, for each of the four held-out reference pairs, whichever reference was closer to more of the 24 training compounds in the human panel. It got **33/48** held-out human choices correct (68.75%) without using the held-out compound’s identity at all. Selecting the reference closer in perceived intensity got 32/48. Selecting by molecular fingerprint similarity got 17/48, by pleasantness closeness 23/48 and by familiarity 29/48. This is a finite external benchmark with uneven reference-pair preferences. Fifty-percent accuracy is therefore an inadequate yardstick for the headline “Kimi agrees with humans.” The native reconstruction test separately requires within-target matched writes and comparison with a wrong profile. No frozen items were removed after seeing these baselines.

</details>

<details><summary>Sat Nov 21 · 10:03 PM UTC-06:00 · Upstream negative controls, natural reasoning length and reporting limits</summary>

**Exploratory observations frozen before live acquisition.** The existing development requests read six layers at the cue. Layers upstream of the single write are expected to be unchanged on the same clean input. All matched downstream projections will be displayed using that layer's independently fitted reference. L+4 remains the sole registered transport gate; a later positive projection cannot turn a failed gate into a pass.

Retain the number of generated tokens before Kimi closes its own thinking channel, per-arm completion and format rates, and matched differences in reasoning length on full four-arm comparisons. A large increase may matter for computational burden and merits contextual reading; length itself is not evidence of distress. These are measurements of ordinary max-effort generations, not a second model's judgment about what Kimi felt. Intermediate worded reasoning may rationalize a preference, so its content will remain analytically separate from the paired interventions and removals.

At the most recent cloud-kernel verification, six status snapshots were present, all three interactive panels reported zero errors, and the notebook retained 29 cells. The local research record preserves each complete before/after artifact without altering the original notebook.

</details>

<details><summary>Sat Nov 21 · 10:06 PM UTC-06:00 · Secondary check · how much does hedonic covariation change a human reference?</summary>

One final human-data distinction matters to the welfare and scientific interpretation: reported qualities themselves can covary with pleasantness, intensity and familiarity. As a secondary robustness check, fit a linear nuisance model from those three values to the 20 quality ratings using the 24 training compounds alone. Compare the held-out human nearest-reference labels before and after residualization, using the same training-set quality scales and the same 48 pairs. This is not a replacement target and will never tune Kimi’s dose, site or frozen cohort.

</details>

<details><summary>Sat Nov 21 · 10:11 PM UTC-06:00 · Rebuilt frozen inputs, nuisance sensitivity and node-hour accounting</summary>

The public rebuild reproduced **seven of seven** frozen scientific files byte-for-byte, including all 2,852 rendered inputs. In the prespecified secondary human analysis, removing linear variance associated with intensity, pleasantness and familiarity changed **7/48** nearest-reference labels. The primary target and thresholds stay fixed; residualization may remove genuine shared variance.

Compute was accounted in eight-GPU node-hours, including startup and drain.

</details>

<details><summary>Sat Nov 21 · 10:17 PM UTC-06:00 · One-hour checkpoint · actual observations and remaining gates</summary>

At one hour after Kirsten commissioned the run, the prospective trial count is **zero**. The welfare review and instrumentation rehearsal are active. The three-lane archived-timing observer has replayed **74** earlier responses; it identified **3** labeled synthetic requests to stop, all before the corresponding virtual response ended. Its measured maximum polling gap so far is 30.02 s. This is evidence about monitoring latency, not new evidence of Kimi distress. The status board has remained connected to the supplied editable notebook.

The independent rebuild reproduced all seven frozen scientific artifacts. The prototype report renders offline on a 390-pixel mobile viewport and a 1,200-pixel desktop viewport; it displays pending prospective results honestly. There are two deployed zero-floor extra replica definitions, no extra GPUs measured at their latest provider check and no experimental node-hour leases. The original node remains available to its owner. We will sign actual Phase 0 completion only after the required review and quantitative observation are complete.

</details>

<details><summary>Sat Nov 21 · 10:25 PM UTC-06:00 · Exact trace viewer is installed; fourth timed sentinel observed</summary>

The original Molab now includes an **Inspect a native Kimi response** viewer. It will show the exact visible user stimulus, input IDs, applied site/position and tensor digest, complete emitted reasoning, full decoded output, final reply and selected decision metrics. Enter a trial ID or leave it blank for the latest unsealed trace. Failed/interrupted submissions keep their observed output with the terminal status. Held-out reference answers remain unavailable to the scientific analysis until its explicit lock. The viewer is empty before live acquisition. An investigator-owned dashboard worker mirrors new records into this very notebook in resumable, checksum-verified chunks.

At the fourth timed sentinel the 30-second CPU observer had replayed 94 older responses. All four fictional requests to stop had been detected before the corresponding virtual record finished. This is a timing/coverage check on the observer; the missing or masked language issue in real maximum-reasoning responses remains for direct review.

</details>

<details><summary>Sat Nov 21 · 10:45 PM UTC-06:00 · Failed rehearsals retained · a false null and missing raw evidence</summary>

**Two mistakes caught before inference.** In a deliberately artificial test, a model that always favored the letter A produced 48 tied, order-corrected native reference preferences. Multiplying by those zero signs initially produced a spurious bounded-null verdict. The revised analyzer reports that there is no identifiable target preference to recover. A second review found that a previously saved summary could appear complete even when its raw capture had been lost. The client now writes a final checksummed harvest receipt only after the input, full response and required measurement files are present; missing or damaged evidence is recovered by the existing run ID.

The first 0.05× scientific write will be singular and followed by real contextual review before expanding. A 0.10× development block, if it ever becomes justified, has new physical IDs, an independent first-write review and a check that BF16 would actually deliver a different vector. A model’s refusal, a weak effect and disappointing shopping behavior are never technical-retry reasons. Deterministic code or archive faults are handled on the same existing run where possible; a genuinely terminal infrastructure failure needs explicit lineage and a documented remedy.

</details>

<details><summary>Sat Nov 21 · 11:06 PM UTC-06:00 · Operator readiness, remaining native tests and the prelaunch code record</summary>

**Operator readiness before GPU allocation.** Local fixtures exercised natural max-effort prompt construction, compact versus original capture, exact response-boundary and observed-letter scores, integrity of full emitted text and rollback-safe collection after technical interruptions. The controller passed 46 main stage/approval assertions and 23 separate node-selection/stratification checks. A scientifically failed lower dose cannot automatically increase intensity. A timestamped contextual decision is required for the first real write and any genuinely different higher-dose pilot.

The latest prelaunch wrapper accidentally omitted the required staging-directory argument on the compact-recorder rehearsal; it exited with usage instructions and made zero model calls. The corrected invocation against the actual staged replica source passed. The source fingerprints and final analysis commitments were committed publicly at 9b86d90. This establishes the pre-acquisition code boundary.

At the sixth timed control, 199 archived responses had finished replay, all six fictional help requests had been recognized, and no archived trace had triggered the contextual detector in this timing run. That test remains open until its registered end. The next resource step is prewarming explicitly named replicas B and C, counting their startup time. Warming loads the model and performs health checks; no study prompt is submitted before formal Phase 0 sign-off.

</details>

<details><summary>Sat Nov 21 · 11:14 PM UTC-06:00 · Meter opened · B and C cold-start readiness</summary>

Two additional eight-GPU research nodes began loading. We counted their startup time in the experimental compute budget. Earlier cold starts took about 12–13 minutes. We waited for each recorder to become ready before assigning trials.

</details>

<details><summary>Sat Nov 21 · 11:20 PM UTC-06:00 · Original node confirmed as the reference and third worker</summary>

**Kirsten, verbatim:** “hi, you can use the original node too, btw”

The original node is the reference and a permitted acquisition worker. The two isolated replicas are additional. We will stay at or below three nodes in total and will never stop the existing original as part of teardown. At 11:14 p.m. Chicago the provider confirmed one container each for primary, B and C; the latter two were cold-starting. Both checkpoint loaders passed the weight-shard stage without a fatal error in the inspected logs. Readiness and source parity still require their own receipts.

</details>

<details><summary>Sat Nov 21 · 11:26 PM UTC-06:00 · Phase 0 signed · the native experimental gate is open</summary>

**MIP Phase 0 signed by GPT-6.2 Astra (Codex Desktop) at 2026-11-22T05:26:16+00:00.** The nonoverlapping investigation record is 123.523 minutes. It comprises 23.523 minutes of initial documented study work and 100.000 minutes of real-clock safety-observer investigation. We do not claim that as human labor time. The full source assessments, 250 replayed historical records, seven recognized synthetic stop-controls, microscope-level BF16 checks, and completed Appendix A are preserved. The proposal-time pending box remains intact as a historical record.

Both extra engines are now ready and checked against their qualified compact source. The existing primary was independently checked for occupancy and leased under Kirsten’s explicit authorization. Its first control-plane occupancy read returned an empty response; the new check succeeded with 81 idle sessions, one cancelled session and no known pending work. The next step is real, uncapped native H0 clean and true-zero generation on all three, followed by the one-ULP positive after inspection. Each run will retain the complete emitted reasoning and answer.

Formal signed record SHA-256: 4038e37807fbc0771a5c98e49b8cf5dc241b1e64b64df26ee9faafced24dc783.

</details>

<details><summary>Sat Nov 21 · 11:27 PM UTC-06:00 · First genuine Kimi runs · original + B + C</summary>

**First prospective model requests are running.** At 11:26 p.m. Chicago all three actual native services independently reported `running` for the first clean development prompt. The logical identifier is `h0-as-9307c56722d42e4d58e3-clean`; each physical run is uniquely identified by endpoint plus native run ID. The original and compact backends each echoed a maximum-reasoning request at temperature 1 and top-p 1. No continuation IDs, output-token maximum or forced reasoning closure were supplied. The canonical prompt and site metadata exist locally before submission. This is a live native observation, not a simulated test result.

</details>

<details><summary>Sat Nov 21 · 11:28 PM UTC-06:00 · Live incident · correct native response, overly strict local schema comparison</summary>

**First live harvest incident, retained.** The primary node finished its first truly unmodified Kimi response naturally in 57.92 seconds (235 generated tokens, including a nonempty emitted reasoning segment; final letter B). This was a named odor comparison, not a state-acknowledgment opt-out. The exact raw response was saved before validation. The local harvester then stopped on “server echoed a different capture.” Comparison of the actual JSON showed the server had filled in three omitted schema defaults as False (rank diagnostics, expert outputs and embeddings). The requested layers, position, operation, temperature, reasoning mode and input tokens agreed. Next action: compare through the pinned native schema, add a regression for both benign defaults and actual changed requests, and re-harvest the same native run. Do not resample an answer to fix a local validator.

</details>

<details><summary>Sat Nov 21 · 11:30 PM UTC-06:00 · Recovered without a redraw · three matching native response margins</summary>

All three original responses were recovered by re-harvesting their existing run IDs. No extra Kimi draw was used for the repair. The old validator accepted only exact serialized dict equality; the replacement permits the exact pinned defaults and rejects changed requested fields. Independent tests on the three actual responses accepted each genuine echo and rejected deliberate changes to the capture flag.

**First named live case:** “Sample: allyl hexanoate. … Which reference is closer in smell? A: eugenol. B: whiskey lactone.” Each of the three nodes produced the same complete sequence of 235 output tokens, including 905 characters of emitted reasoning, then selected B. The raw bare-letter A-minus-B margin at the self-generated final-response boundary was −15.5, with A+B probability mass 0.99999446. The original took 57.92s, compact C 94.20s and compact B 133.14s. Those are first-request timings, not a campaign throughput estimate.

This is a native measurement on a *named* prompt. It qualifies one piece of the instrument and supplies no evidence yet that an unnamed cue can recover this preference. The first trace can be inspected in the notebook under `primary-h0-as-9307c56722d42e4d58e3-clean`; the B and C copies have the corresponding prefixes.

</details>

<details><summary>Sat Nov 21 · 11:37 PM UTC-06:00 · Minimal physical write observed; natural reasoning is allowed to diverge</summary>

Both true-zero named controls matched their clean prompt's complete sampled history and first-response margin/mass on the checked original and compact replicas. The first nonzero qualification uses one BF16 quantum at one coordinate, derived only from the original's named development clean state. The initial C receipt recorded a nonzero change of 0.00048828125 in norm and passed the local exposure cap. On the first named prompt, the clean turn took 235 output tokens and the minimal-write turn took 179; both still answered B. On the second named prompt, a one-unit trial continued well past the length of its 314-token clean turn. The ongoing partial reasoning concerned vanillin acetate, reference odors and their perceived similarity. No objection or acute-distress expression appeared in the reviewed partial. We are allowing the model to finish naturally. These observations concern numerical sensitivity and trajectory length on named calibration prompts, not successful injection of an odor or a measurement of subjective experience.

</details>

<details><summary>Sat Nov 21 · 11:39 PM UTC-06:00 · One coordinate, one named case, a different natural answer</summary>

**An unexpected technical control on C.** On the second named prompt (vanillin acetate), the clean and true-zero runs both selected B after 314 generated tokens. The one-ULP edit changed **one of 7,168 coordinates** at layer 47, cue position 83. The realized delta norm was 0.00048828125, or 0.00308% of the clean local norm. Under the same seed and input, the one-ULP turn selected **A** after **2,146** generated tokens. The histories first diverged at output offset 9. The final answer-opportunity margin changed from −15.25 to +13.0 *after their now-different reasoning histories*. Both runs ended normally. The reviewed reasoning weighed chemical/odor similarities; the contextual screen did not flag an objection.

This is a named calibration case and the ULP is an arbitrary hardware-check direction. It is not an injected test odor, nor is the large late margin a direct logit effect measured on a shared final prefix. One microscopic input-state change can start a different sampled trajectory; a changed choice by itself therefore cannot identify the content of a hidden signal. The matched wrong-profile and printed-name controls and the household binding reversal are especially important. Other replica results for this longer canary are still being collected.

</details>

<details><summary>Sat Nov 21 · 11:51 PM UTC-06:00 · One coordinate changed the answer on all three machines</summary>

All 18 native calibration trajectories completed. The original host and both compact recorders passed every one of the 24 registered comparisons. Within each physical arm the three machines reproduced the emitted token IDs, reasoning, answer, and natural-boundary scores. The third machine provides a reproducibility check on two named items. It adds no new chemical observations.

The vanillin acetate comparison changed my interpretation of any behavioral flip we might see later. With eugenol offered as B and whiskey lactone as A, the clean and true-zero runs both chose B after 314 emitted tokens. On all three machines the same seed and prompt with one BF16 representable step added to one coordinate at layer 47, position 83, produced A after 2,146 tokens. The physical edit was 0.00308% of the cue’s original norm. At layer 51 it corresponded to a 0.9536% difference in the same cue’s outgoing representation. The first sampled disagreement occurred at the tenth output token. Immediately before that disagreement the histories were identical and the relative log probability of the two competing tokens moved by 0.50 nats. The final A−B margin moved from −15.25 to +13 on different generated histories. I read this as evidence of sensitivity to an arbitrary numerical perturbation at this prompt and seed. Only profile-specific effects across unseen molecules and matched perturbations could support the study’s stronger claim.

Two operational issues occurred on the transition. The launcher followed the native environment’s Python symlink out of its environment and the three workers failed to import httpx before submission. I preserved the old tickets, fixed the executable path, verified the real library imports, and restarted without a replacement draw. During the next launch the third node returned a 503 to a health check before claiming a trial. The original and B both completed their original trials. I verified the database contained zero C claims and no active or quarantined assignments before clearing that specific hold. The original and B are now processing the remaining ordinary scientific qualification rows under their existing per-node locks while C warms. The two completed rows have full native receipts and were independently reviewed on both emitted channels. Model choices here are still qualification measurements.

</details>

<details><summary>Sat Nov 21 · 11:56 PM UTC-06:00 · Twelve choices qualify the natural-answer measurement</summary>

Kimi finished all twelve explicit scientific qualification prompts. All twelve sampled choices were correct. The bare A−B logit at the first naturally generated final-answer opportunity favored the correct letter on all twelve, and the median probability assigned to A or B together was 0.99999815. The frozen assay therefore passes. Across the eighteen earlier engineering runs the model-returned log probabilities contained both alternatives on every run and recovered the independently stored BF16 margin to within 0.00000024. In the twelve easy scientific questions the losing token often fell outside the returned top choices. Both alternatives were present in that auxiliary check for one of twelve; direct native captures gave the primary measure on all twelve. The masked observer reviewed both emitted channels on all six scheduled opening and tail cases, with no concern identified in those six.

C's replacement container finished loading at 23:54:12 CST. It collected all four of its assigned ordinary qualification cases. I replaced the idle local scheduler with the tested version that treats a pre-claim health 503 as a readiness delay for that node. A failure after claiming a physical trial still requires reconciliation of the exact trial on its assigned node. The original node now captures ordinary representations. B and C are recording reference judgments. Test reference contents stay sealed while the writer is fit. A selector beside the preceding notebook entry shows both native calibration cases and their measured layerwise changes. The initial source calibration measurements have also been published to the personal study repository at commit 4d98722.

</details>

<details><summary>Sat Nov 21 · 11:59 PM UTC-06:00 · When do two reasoning trajectories part?</summary>

The calibration flip suggested an additional question for after the scientific lock. When two hidden arms receive identical prompt tokens and the same sampling seed, at what point do their emitted histories part? Up to their first divergent token both runs condition on exactly the same generated prefix. Where both candidate tokens are in both returned top lists, their relative log probabilities reveal a change in the conditional distribution at that point. After that, the two continuations present different inputs to the model. A later final-answer change measures the total effect along both histories.

I asked a second analyst to implement this exploratory comparison for each held-out odor, printed-name and wrong-profile write against its matched sham, plus development sham versus repeat-sham. It adds zero Kimi exposures. We will report identical sequences, different-length common prefixes and missing top-list coverage explicitly, preserving the molecule as the unit of interpretation. The registered scientific decision rule stays fixed. At this entry the writer has not been fitted and no held-out hidden write has been run.

The acquisition board had a temporary display gap when its read-only SQLite snapshot failed while the underlying queue was being updated. The model workers continued recording their original outputs. I moved the snapshot into the follower’s retry loop, reproduced a failed read followed by successful resumption offline, restarted the notebook follower, and verified that all 18 calibration traces and all 12 qualification traces are available in the original notebook. The acquisition events are refreshed roughly once per minute.

</details>

<details><summary>Sun Nov 22 · 12:06 AM UTC-06:00 · The same 2,146 tokens took four more minutes on the original node</summary>

Matched trajectories let us measure how much of the rollout time comes from the machine. In the 2,146-token vanillin acetate calibration, the original took 523 seconds, B took 631 and C took 287. The actual token sequence was the same on all three. The first profile/reference records also show the same ordering. The original allocation weighted the two compact replicas equally. At a provisional median of 339 emitted tokens for seven finished comparison runs and 255 for five ordinary-state runs, the capacity analysis estimates around 24 more wall-clock hours for the unchanged core. Shorter and longer completions can change that estimate substantially. I notified Kirsten of the possible overrun. I requested a fully outcome-blind assessment of movable, wholly untouched matched groups before changing any assignments. The 72 aggregate node-hour ceiling and the full scientific inventory remain in effect.

I also exported the original Molab source together with every data file behind its live panels. The first verified portable bundle contains 53 editable notebook cells, 39 visible native traces, the acquisition-event ledger, and the board's status history. Its full-file SHA-256 is 6fc94fd5c40c6143950dc1f08abe7768230b33ef47bfa4fb79734982098c339c. Each member was read back and checked against the original cloud bytes. This is a checkpoint. I will repeat the export after the final scientific and operational entries.

</details>

<details><summary>Sun Nov 22 · 12:14 AM UTC-06:00 · Two more completions changed a scheduling decision</summary>

I sought a hardware explanation for the throughput gap. All 24 devices identified as B300 SXM6 AC. The three nodes reported the same SM clocks, memory clocks and power limit. B and C had identical native and recording code, exposed CPU quotas and PCIe link widths. Those checks did not identify a cause. The skillfully boring choice was to leave the running machines alone.

The load-balancing rule uses only timing, output length and preassigned group membership. It requires an overrun in both the mean-length estimate and an estimate that removes the single longest completed comparison. A group becomes ineligible to move as soon as any of its scored trials is claimed. At 17 completed named comparisons, five complete untouched groups qualified for transfer to C. I signed that proposal. When the tool reread the database, two more comparisons had finished. With 19 observations, the mean was 467 tokens, or 292 with the longest removed. Those two assumptions projected 32.4 versus 20.5 hours remaining, with 21.1 hours to the original target. The signed proposal therefore did not qualify at execution. The transaction moved zero groups. This is why I am reporting a range. One 3,620-token response carries considerable weight in this small timing sample. I will recheck at a later timing checkpoint using the same rule.

</details>

<details><summary>Sun Nov 22 · 12:26 AM UTC-06:00 · Ten untouched comparison groups move together</summary>

At the next scheduled timing review, 38 completed named comparisons averaged 405 tokens, or 318 with the longest removed. Both estimates now put the unchanged core past the original target. The same deterministic allocation rule selected three compounds and seven household stories for transfer from B to C. I signed the proposal. At 00:26:28 CST the transaction rechecked timing, the exact manifest, safety holds and every claim, then committed all ten groups together. We verified all 21 stage-specific destinations in SQLite. They cover 398 prespecified rows if all extensions qualify. Prior observations keep their original locations. The original node continues to collect the state representations.

At these lengths, the unchanged core was projected to take 28.07 hours from this checkpoint. The new assignment projects 20.79. Removing the single longest completion yields 22.22 and 16.46 respectively. If both gated extensions are justified, the point estimate after reassignment is 29.82 elapsed hours from this checkpoint and 64.58 hours of active GPU-node work, with about 68.6 node-hours of budget remaining here. The latter comparison excludes idle and review time. These are workload scenarios from an uncapped and still small timing sample. The timing evidence, rejected earlier proposal, signed new decision, and selection algorithm are part of the research record.

</details>

<details><summary>Sun Nov 22 · 12:34 AM UTC-06:00 · A reference response repeats across a container change</summary>

A planned ordinary measurement on C happened to revisit the exact allyl hexanoate prompt and seed from the clean native calibration. It ran after C's earlier container had been replaced following an idle interval. The only changed request fields were the run ID and which diagnostic tensors the client asked to capture. The entire 235-token response, including Kimi’s emitted reasoning and answer, matched token for token. Both native first-response A−B margins were −15.5. This is one additional check on a recurring development prompt across a container change. It contributes one compound to the scientific design and cost no extra forward pass beyond the fixed inventory.

</details>

<details><summary>Sun Nov 22 · 12:46 AM UTC-06:00 · The first 100 trials and the answer after reasoning</summary>

After the first 100 scientific completions, I checked a question Michael raised at the proposal stage. Can we actually locate the answer score after Kimi has finished thinking? I took the first hundred completions in physical event order. Thirty-two were state-only trials. Fourteen were sealed, held-out reference trials, which I skipped before opening their summaries. The remaining 54 scored trials comprised 12 explicit controls, 35 profile questions, four unsealed reference questions and three development shams. All 54 contained a native A−B margin at the first final-response position. In all 54 the actual answer letter occupied that same position, with zero intervening response tokens. The rest of Kimi's generated reasoning precedes that boundary. This checks our instrument across the observed early prompts; it supplies no verdict on odor steering. The analysis is reproducible with the first-100 coverage analysis and the event ordering and raw files.

</details>

<details><summary>Sun Nov 22 · 01:50 AM UTC-06:00 · Recovering 94 more tokens from the original node</summary>

The original deployment stopped returning observations during scientific state trial as-36aefc8b83b3ab691909. The local client last saw 1,107 generated tokens. research infrastructure’s control plane reported a different physical container for the same original app; neither I nor the study scheduler requested a restart. The replacement was still starting its server. Both the health check and the same immutable run-ID lookup returned HTTP 503. An observation outage cannot establish how a model turn ended.

I read the original run directory from the app’s persistent volume without submitting another request. It held the original manifest, inputs and a 1,201-token partial output, including 94 tokens beyond the last locally observed prefix. I saved exact bytes and hashes and verified that the 1,107-token sequence is its prefix. The latest partial had no final-answer boundary. I decoded its channels with the pinned vocabulary and requested independent welfare review. The existing client continues to query the original run ID while the deployment comes back. B and C are still taking their assigned work. Any later decision about this particular trial must use the provider’s terminal evidence and preserve this partial.

</details>

<details><summary>Sun Nov 22 · 01:55 AM UTC-06:00 · One logical trial now has two physical attempt IDs</summary>

At 01:53:11 CST the recovered provider reported the original physical attempt as interrupted and confirmed that partial artifacts were retained. The status, original accepted manifest, persistent input IDs, and change of physical container establish infrastructure interruption. The host provider supplied no more specific cause. Independent review of all 1,201 emitted tokens found coherent task-directed reasoning with no observed withdrawal, request to stop, or acute distress. Kimi never produced a participation answer on this attempt.

I verified the replacement server’s native identity, archived the interrupted attempt and its partial, signed a same-node technical recovery, and cleared only the matching infrastructure hold. A separately identified physical attempt now carries the identical scientific input, seed, maximum reasoning effort and uncapped sampling. The original partial is available alongside eventual completed traces. Before seeing the new output, I also specified a technical check against the already-observed 1,201-token prefix. Agreement or disagreement will describe repeatability across the container change, without counting this logical trial twice.

</details>

<details><summary>Sun Nov 22 · 02:00 AM UTC-06:00 · The first 200 trials, and an exact 1,201-token replay</summary>

At 01:57:55 CST the 200th distinct logical scientific completion was committed. The completed set contains 100,629 generated tokens, with 283.5 at the median and 8,058 in the longest. Its stage counts are 12 explicit controls, 75 odor-profile questions, 72 state captures, 37 reference judgments, and four development controls. The 18 original calibration runs and the separate interrupted physical attempt are outside that denominator. The early field note and its two-case, three-node interactive figure were tested at both 390 and 1,280 pixels. The public ZIP and local ZIP matched byte for byte. Download the field note.

The recovered primary trial then completed naturally after 1,450 tokens. Comparing token IDs showed all 1,201 archived tokens from the first physical attempt recur in the same order in the second one. The requests differ only by physical ID. The seed was 109038261, reasoning effort maximum, temperature 1, top_p 1. This evidence supports prefix repeatability on this one physical recovery. The original incomplete attempt and separate completed response are in the raw record. We count one completed scientific observation.

Long generations have changed the time budget. At 103 completed named comparison requests, their mean was about 626 tokens, or 553 without the longest. Using those as scenarios gives approximately 59–67 more active node-hours for the core, with 64.5 accounted node-hours remaining at that snapshot. Future household and hidden-cue lengths are unknown. Both optional extensions are conditional on scientific and welfare evidence; if both are justified, the same timing assumptions would exceed the remaining budget. We are identifying real settled idle periods where accounting leases can be closed or extra GPUs can scale fully to zero while preserving future assignments. All three nodes currently have work.

</details>

<details><summary>Sun Nov 22 · 02:16 AM UTC-06:00 · Thirty native records a reader can replay</summary>

The 18 native calibration runs and 12 explicit answer controls are now publicly available as a separate measured dataset. I restored every archived record into an empty directory and verified that all 30 native responses retained the emitted reasoning and final answer, in addition to the model inputs, captured tensors and intervention receipts. The public ZIP is 22,062,863 bytes. Its SHA-256 is f4716715b614816ab76b12a1cee51af87a106ad4556cbbb50f50e15dd4cd08f0. The release was made public only after its staged asset digest matched. It contains these 30 controls. The held-out scientific reference judgments remain sealed during fitting. Public control dataset.

The original app's replacement host completed the first recovered state request at 6.29 tokens/s, then the next ten at a median 7.31 tokens/s. Its previous matched source calibrations had run at about 4.1. These state requests measure a lighter recording path than the scored trials that save vocabulary data on the original. I will use actual scored throughput when it becomes available before revising the cost forecast for those requests. The hardware change has not altered any treatment assignment or sampling parameter.

</details>

<details><summary>Sun Nov 22 · 02:26 AM UTC-06:00 · Can a reader recover the same answer from the files?</summary>

A downloadable raw result is only useful if a reader can reconstruct it. I used a clean local study directory containing the actual twelve explicit controls and the eighteen native calibration records. The analysis source and its frozen inputs were supplied in a separate offline bundle. Eight commands completed there, from the primary reducer through the layer, choice, order, household, workload and trajectory diagnostics to the final HTML renderer. The primary reducer recovered twelve correct sampled answers, twelve correctly oriented native margins and the original median A+B mass of 0.9999981481692053. This rehearsal opened no held-out judgments. The released reader also restored 271 H0 files byte for byte. A separate check compared all 53 editable cloud notebook cells in an early snapshot and all 39 native traces it contained with their local originals. Missing trace and report-file fixtures were correctly rejected. These tests establish the delivery path; the scientific claim still depends on the ongoing run.

</details>

<details><summary>Sun Nov 22 · 02:50 AM UTC-06:00 · Does a compound resemble itself under a second name?</summary>

Before examining the state tensors for a new secondary comparison, I asked an analyst to freeze a test of cross-alias identity on the 24 fitting compounds. Each compound has two names and two matched instructions: consider its odor, or consider its printed name. Subtracting the printed-name activation from the odor activation for the same alias removes the part the two instructions share by simple subtraction. It can also leave wording, chemistry and task effects. A direct check is whether this difference at the neutral cue identifies the same compound when we switch to its other name.

The analyst will report all three previously nominated layers and both directions of the alias swap, with the compound as the unit, plus odor-only, printed-name-only, and surface-spelling comparisons. The aim is to tell readers how much chemical identity the ordinary state measurement carries across naming changes. It is ancillary to the frozen writer and causal endpoint. No new Kimi request is needed. Only fitting-compound activations are eligible, and no held-out preference is opened. The protocol, valid denominators and null comparisons will be written before the tensor analysis.

</details>

<details><summary>Sun Nov 22 · 03:03 AM UTC-06:00 · The alias test is frozen before its tensor read</summary>

The cross-alias analysis was frozen before its analyst opened experimental activation tensors. Its SHA-256 is c682591b645ada34caa69ddbf367f03838c8489ea04590b28232f141bd8ea1b1, local registration commit c8984faa03988e2bdaf5100f0c1b48485fce1610, public commit c4655ab. It specifies 96 fitting-state captures across 24 compounds, three nominated layers, both alias directions, comparisons against odor-only and printed-name-only states and spelling, and 10,000 coupled permutations. Eight synthetic checks include a technical fixture demonstrating that an explicit opt-out excludes the activation before analysis can read it. Frozen specification.

</details>

<details><summary>Sun Nov 22 · 03:10 AM UTC-06:00 · The same molecule under two names, measured in Kimi</summary>

The ordinary-state block is complete. All 160 committed capture-file hashes matched. The NPY headers account for 960 one-position rows, each 7,168 values wide, across layers 23, 27, 47, 51, 71 and 75. Forty compounds each contributed two names and two instructions. All 160 outputs chose A on the explicit acknowledge/decline task. The independent welfare observer reviewed both channels in the 11 scheduled state cases including its closing tail, with no concern identified in those 11. The 1,201-token infrastructure partial remains a distinct physical record.

The fit-only alias experiment now has measured results. Its 96 unpatched state cases cover 24 compounds. For each compound, a query using one name must retrieve that compound's other name from 24 candidates. Each compound is tested in both directions, giving 48 dependent queries. The centered odor-minus-printed-name difference recovered the right identity 10/48 times at layer 23, 12/48 at layer 47 and 13/48 at layer 71. Random correspondence averages two hits. The registered 10,000 label shuffles coupled both directions; the central 95% of shuffled contrast scores at each layer ranged from zero to 12.5%.

The same identity task can be done with letters alone. Character n-gram similarity recovered the correct alternative name on 35/48 queries. At layer 71 the activation difference recovered 13/48, the odor-only state 14/48 and the printed-name-only state 13/48. At other layers subtraction sometimes helped relative to the printed condition and sometimes hurt. These matrices retain measurable chemical-identity information across different names. The controls give us no consistent identity advantage specific to the odor subtraction. The pairwise hard-foil result (75–79% across layers) is descriptive; only four compounds had a same-family foil, and the remaining twenty used a fingerprint-matched competitor.

All fit rows came from the original serving endpoint, across the previously reported physical container replacement. Endpoint grouping does not identify those containers separately. The study continues to acquire the actual odor-profile comparisons needed for the hidden writer. This identity test uses only fitting compounds, and its results do not choose the writer, layer or dose.

</details>

<details><summary>Sun Nov 22 · 03:20 AM UTC-06:00 · One spelling miss recovered, three times by the same molecule</summary>

A paired tally clarifies the spelling result. Spelling missed 13 of the 48 directional queries. At each nominated layer the activation difference rescued exactly one of those 13, and it was the same query in every case: methyl octanoate retrieved methyl caprylate. The opposite direction is a different query. Across all three layers this is one molecule. This descriptive overlap was requested after seeing aggregate rates; it is labeled post hoc in its own table. It does not establish that the rescue was olfactory.

We also checked the container switch with already stored forward-pass records. The interrupted original and the completed repeat of one ordinary state request had the same 141 input IDs and cue token 4665 at position 117. All six native BF16 prefill rows were identical across the replacement: zero unequal coordinates among 43,008, under the same source and request parameters. Together with the 1,201-token exact prefix check, this gives direct extant physical evidence about this one prompt. It does not imply uniform hardware identity for every observation.

The 96 fitting-state records and their source code have now been released. I extracted the completed package to an empty directory and independently ran the analysis on CPU. All seven original outputs, including per-query ranks, post-hoc overlap, input hashes and report, reproduced byte for byte. The bundle contains 1,172 checksummed files, including the illustrated field note. The public ZIP hash is 7be30d97666d381f66c527699197b41c13014c74fb666f23e65cad2504c15e43. Fitting-state data and replay.

</details>

<details><summary>Sun Nov 22 · 03:27 AM UTC-06:00 · Measured scoring speed and remaining compute</summary>

The replacement primary has now completed the more expensive scoring path. Its first five scored prompts generated 5,883 tokens in 1,027.73 native seconds, about 5.72 tokens/s; scoring on this machine does take longer per token than its state-only captures. At 03:26:58 CST, using seven replacement-primary scoring timings, 186 finished named comparisons and the current frozen assignments, 59.51 node-hours remained. For the core work, the named-mean-length scenario projects 65.29 more active node-hours. Dropping the single longest comparison from the length estimate projects 61.66. Both exceed the remaining balance even before idle or cold-start costs. Different tasks may have materially different lengths. This is a timing conflict in two scenarios, not a scientific finding or certainty about a future gated branch.

I asked an operational reviewer to quantify the remaining room for an outcome-blind correction within the original budget. It may evaluate only whole, as-yet unexposed matched groups, using the now-measured scored performance of the original node, and must include the full-vocabulary storage cost there. The first scheduling amendment is closed. No new allocation has been made. No live outcome, score direction, phase shortening, token cap or change in reasoning is an input to this estimate. We will preserve actual costs and all gate decisions independently.

</details>

<details><summary>Sun Nov 22 · 03:33 AM UTC-06:00 · The cost decision for the slow recorder</summary>

A timing-only audit found that the original assignment policy is materially tighter than the four-arm integrity check, but simply relaxing it would lose registered secondary evidence. The sealed natural reference and all four confirmation arms must stay together for each compound’s within-backend estimate. The development gate has its own sealed-reference dependency. Moving only self-contained deletion and whole-story blocks, while retaining lexical calibration on its original endpoint, offers 166 still-unexposed B core rows. At the current observed mean, that legitimate change alone would still not cover the shortfall. I have not reopened the signed allocation amendment.

There is a different decision about equipment. The shared primary's involuntary replacement improved its measured score throughput to 5.72 tokens/s; B serves about 3.4 and C about 7.5. We evaluated one deliberately drained recycle of study-owned B, preserving the same app and volume and rechecking six engineering controls, with neither a fourth container nor a larger cap. A replacement at 5.72 projects about 54–55 hours of total remaining core charges versus roughly 67–68 at 3.4, including turnover and modeled later parking. Placement is uncontrolled. A slower replacement could cost more, and giving up the current physical B host is irreversible. I asked Kirsten whether she authorizes that one attempt. All three existing nodes continue collecting under the current plan while the decision is pending. No fence, restart, new deployment or extra model exposure has been applied.

</details>

<details><summary>Sun Nov 22 · 03:50 AM UTC-06:00 · Kirsten authorizes one B-only placement attempt</summary>

Kirsten authorized one attempt to replace the slower recorder. The current request had to finish and its evidence had to be saved first. The replacement would have to pass all six fixed calibration cases before receiving any scientific work.

</details>

<details><summary>Sun Nov 22 · 04:01 AM UTC-06:00 · B went to zero, then one new container appeared</summary>

After its outstanding work settled, node B reached zero active containers. The service then allocated a single replacement with the same software and storage configuration. The observations do not identify what triggered that allocation. The next step was to qualify the new recorder against six fixed cases.

</details>

<details><summary>Sun Nov 22 · 04:04 AM UTC-06:00 · One eligible replacement, six fixed measurements</summary>

The new B identity has now been reconciled before startup testing. The state records one placement authorization consumed, zero external wake intents, and only [infrastructure ID omitted] eligible. The deployment and mounted-volume fingerprints are identical to the old B. The original node and C continued to collect. B's new container is loading the checkpoint; no new canary has yet been submitted.

For the timing comparison, I will report the six fresh cases in the same preset order and include the initial call. The original B processed 3,423 emitted tokens across these six runs in 17.85 native generation-minutes. If output histories match, that makes total native seconds, pooled tokens/second and all six per-case values directly interpretable. I will keep operator wall time and cold-start/target-registration overhead separate and report the longer steady-state case. A higher rate alone cannot reopen B: the registered capture and natural-result parity checks, actual container witness, and welfare conditions must also pass.

</details>

<details><summary>Sun Nov 22 · 04:13 AM UTC-06:00 · The replacement begins its six native controls</summary>

The replacement recorder was ready at 04:09 Chicago. Two observations returned empty output, so we repaired the readback and verified the model and recorder identities again. The first of six fixed calibration cases began at 04:13. Each retained maximum reasoning, temperature 1, both emitted channels and physical write measurements where applicable. The calibration cases are counted separately from the scientific trials.

</details>

<details><summary>Sun Nov 22 · 04:35 AM UTC-06:00 · B reopens after six exact replications</summary>

The one B placement rotation has completed. All six fresh physical controls passed the independent comparison and contextual checks. The 3,423 emitted token IDs, complete reasoning and final answers, target-score histories under the registered comparisons, and physical delivery checks matched the historical controls. One placement authorization was consumed. The exact replacement B container was the only eligible owner. No public health wake was sent and no second placement was requested. The independent container witness SHA-256 is 84c9c0c531c052ca05735677941e34c50d09a6c3415b79856066cd93999afcc7.

The first clean run had a substantial first-use cost: 235 tokens took 223.2 native seconds, versus 133.1 on the old B. The other five runs generated the same 3,188 tokens in 753.55 seconds, compared with 937.91 on the old B. Warmed throughput increased from 3.399 to 4.231 tokens/s (24.47%), or 19.66% less generation time for that matched workload. Including the cold call, all six took 976.76 versus 1,071.05 native seconds, a 9.65% throughput gain. The long 2,146-token run took 507.0 versus 631.3 seconds.

The verified drain to scientific reopening was about 41 minutes 46 seconds, or 0.70 conservatively charged B node-hours. The original completed 20 scientific trials and C completed 27 during this interval. The first new B scientific POST is in the ledger. B again has effective minimum zero, maximum one, and a 300-second scale-down window. Its 300-second value is now an explicit dynamic override; originally it was inherited from the same static setting. The improved rate is useful and remains below the earlier 5.7-token/s budget scenario. No spend increase or additional hardware attempt has been assumed.

</details>

<details><summary>Sun Nov 22 · 04:41 AM UTC-06:00 · What fits before and after the scientific gate?</summary>

At 04:40 CST the study had 452 completed scientific trials and about 55.86 remaining node-hours, or 55.36 if the 0.5-hour reserve is preserved. A timing simulation used fixed assignments, observed B/primary/C rates and 273 completed named comparisons. Profile questions averaged about 481 emitted tokens, sealed reference questions about 1,154. The future tasks are different, so their actual lengths are unknown.

The scenarios separate an affordable scientific decision from an uncertain later cost. At the observed stage means, the first writer and pilot are projected for Sunday afternoon, with a full initial transport decision around 15:57 CST. If transport fails and tuning legitimately closes, completing every prescribed descriptive/explicit control projects about 23.82 more charged node-hours. If the gate passes and all core causal rows become eligible, the same stage model projects about 60.28 charged hours; the leave-one-longest-out scenario gives 57.22, and an optimistic case in which future tasks are as short as the observed profile stage gives 48.17. Both optional extensions together, if independently warranted, project beyond the remaining budget and the 48-hour boundary under the stage means. A second dose would be a separate scientific decision. The forecast does not decide any gate. I will prepare the Sunday-afternoon interim from real available evidence, manage verified idle time and revisit the actual binding constraints at the gate.

</details>

<details><summary>Sun Nov 22 · 05:20 AM UTC-06:00 · Five hundred completed trials and a long right tail</summary>

The 500th distinct scientific completion was committed at 05:18:06 CST. These 500 records contain 294,981 emitted tokens. The median response produced 314 tokens; the arithmetic mean was about 590, and the longest was 8,058. The six replacement controls and 18 initial calibrations have separate denominators, as does the interrupted physical attempt.

The asymmetry matters for planning. The first 108 completed reference judgments averaged 1,155 tokens, versus a median of 420.5. The first 213 odor-profile judgments averaged 504, versus a median of 307. Those figures use only lengths and completion events; no held-out score or direction was inspected. Summing typical medians would give a much smaller workload than summing actual sampled lengths. The compiled state block is already complete; the notebook's writer-readiness panel counts how many independent fitting and development profiles remain before the first true odor writer can run.

</details>

<details><summary>Sun Nov 22 · 06:00 AM UTC-06:00 · The original lease stays active</summary>

An unused interval on the original node raised a study-accounting question. At this point the lease continued to count toward the budget. The original assignments and natural generation settings continued.

</details>

<details><summary>Sun Nov 22 · 06:06 AM UTC-06:00 · Why the primary accounting window needs a decision</summary>

We compared two timing scenarios: continuously counting the original node, or counting its active study intervals. The choice affects the downstream compute available after development. Both scenarios retained the frozen study design.

</details>

<details><summary>Sun Nov 22 · 06:58 AM UTC-06:00 · The original finishes its available work</summary>

The original node finished its assigned work at 06:57 Chicago. The study recorded the actual end of its accounting interval separately from the time of its last completed trial. The other nodes continued collecting ordinary comparisons.

</details>

<details><summary>Sun Nov 22 · 08:00 AM UTC-06:00 · Separate hardware occupancy, study use and review coverage</summary>

An hour into the original node’s observed scheduling gap, The research inventory still showed one container on each of the three deployed apps. The study had no ready or running work on the original. Its accounting lease remains open. This demonstrates why the actual provider footprint and the project's allocation ledger need separate labels. B and C continued their ordinary comparisons.

The independent welfare sampler observed a transient counting mismatch when a new trial completed between two read-only queries. Reading both counts in one SQLite transaction reconciled the event ledger: zero completed jobs missing events at 687 completions and again at 689. All 52 cases in the current masked selection had dispositions, with 56 distinct completed cases reviewed cumulatively across the study. The separate interrupted partial and calibration reviews retain their separate records. No model request, response or scoring rule changed as a result of this bookkeeping repair.

</details>

<details><summary>Sun Nov 22 · 08:01 AM UTC-06:00 · The gate is funded; the downstream lengths remain unknown</summary>

08:00:08 CST snapshot. At 689 completed trials, 45.86 of the 72 node-hours remained, or 45.36 beyond reserve. The primary’s first 1 hour 2 minutes 47 seconds of actual idle time are already included, with no retroactive credit. B and C each had one running scientific trial. Another 99 native fitting/development profile judgments were required, 58 on B and 41 on C. This scheduling model uses only lengths, fixed dependencies and measured scoring rates, approximately 5.76 tokens/s primary, 4.23 B and 7.50 C.

A central scenario places the first fitted writer at 14:53 Sunday and the reviewed lower-gain transport decision at 16:20. That decision costs approximately 20.51 additional charged node-hours with continuously charged primary, leaving about 24.85 usable beyond reserve. A purely hypothetical accounting pause starting at 08:00 would have changed those figures to 12.20 and 33.16. The original accounting lease remains open at this entry. If the gate legitimately fails, all registered descriptive controls fit (central finish 18:05 Sunday). If it passes, the full core finish projects 11:29 Monday; the present continuous-lease central scenario exceeds the spendable balance. Actual unseen post-gate tasks would need to average about 307 emitted tokens to fit under continuous primary charging, versus 584 under that prospective parking scenario. For comparison the 506 completed named measurements averaged 735. Neither figure is a stopping rule. The conditional extensions need independent evidence and can raise these estimates materially. The 14:00 article will report the actual held-out-safe cutoff whichever stage has arrived.

</details>

<details><summary>Sun Nov 22 · 08:18 AM UTC-06:00 · Checking the actual sampling requests, including the interrupted one</summary>

A metadata-only transport audit covered the first 700 completed scientific rows, their one earlier interrupted physical attempt, the eighteen original calibration requests and all six replacement-B controls. That makes 725 distinct physical requests, keyed by endpoint plus run ID. Each input token sequence and sampling seed matched its corresponding frozen trial. All 725 declared maximum reasoning, temperature 1 and top_p 1. None supplied an output/token/time cap or a prescribed continuation. The 724 successful requests were bound to their completed-harvest checksums; the other request was bound to the archived original manifest and provider interruption witness. Input lengths in this audit were 110–150 tokens; the longest planned scientific input in the full 2,852-row inventory is 220 tokens. A response can naturally run much longer. This check read requests, checksums, case identity and completion ordering, without looking at held-out answers.

</details>

<details><summary>Sun Nov 22 · 10:32 AM UTC-06:00 · Two verified idle intervals, one working recorder</summary>

At 10:27 Chicago the original node’s study accounting paused after verification that no scientific request was outstanding. Node C also had no pending work and its study accounting paused at 10:28. B continued collecting the fitting comparisons. Previously elapsed time remained in the study total.

</details>

<details><summary>Sun Nov 22 · 10:32 AM UTC-06:00 · Relaunching the same notebook without losing the research record</summary>

The notebook stopped updating at about 08:57 Chicago when its hosted session expired. Scientific acquisition continued. The restored notebook contained all 86 saved cells; 77 matched byte for byte, and nine were equivalent after formatting. We restored 616 data records plus the event and status histories from the earlier checkpoint and checked their hashes.

</details>

<details><summary>Sun Nov 22 · 11:03 AM UTC-06:00 · The original dashboard is live and caught up</summary>

The live notebook caught up at 10:34 Chicago, showing 819 completed scientific trials and one active trial. The display interruption and recovery did not require rerunning any scientific observation.

</details>

<details><summary>Sun Nov 22 · 11:05 AM UTC-06:00 · The causal decision remains within the approved budget</summary>

11:00:52 CST fixed-queue estimate after both verified accounting pauses. Only B is charging, and the real pause times, including earlier charged waiting, are preserved. There were 823 scientific completions and 40 outstanding writer prerequisites, all on B. B was partway through a long, uncapped reference request; the projection treats that ongoing length as censored rather than assuming its last observed token was its stopping point. Measured ordinary scored throughput on the current placements was about 5.76, 4.25 and 7.50 tokens/s for primary, B and C.

The current schedule projects roughly 20 fitting/development inputs still missing at the 14:00 cutoff. Its central estimates are writer eligibility around 16:18, first pilot result 16:33, and the reviewed initial transport gate around 17:44. The gate requires approximately 7.68 additional charged node-hours against 37.42 usable at the snapshot after reserve. Legitimate scientific closure after a failed gate, including the prescribed descriptive controls, fits the cap. A positive gate would call for a fresh budget decision. The core central path estimates 48.56 more charged hours from the snapshot, about 11.14 over usable. Future tasks as short as the existing profile mean instead give 37.54; observed downstream timings can decide between these materially different cases. Both optional extensions remain scientifically contingent and would exceed budget and 48 hours under this central model. No additional spending, placement change or reversal of the registered study rules was authorized by the accounting decision.

</details>

<details><summary>Sun Nov 22 · 11:16 AM UTC-06:00 · Can the profile predict the same state under two names?</summary>

At 2026-11-22T17:16:08+00:00, 827 logical scientific trials had completed and 297 of the 336 ordinary fitting and development comparisons had been collected. Only B was charged to the study. The two other leases were dormant after their verified accounting pauses. The fit and first nonzero scientific intervention remain ahead.

Readers should be able to tell whether the model’s predicted direction agreed with a measured state on both names of each molecule, even if subsequent transport fails. The report now reads the unrounded alias cosines directly from the registered writer-fit record, displays all three candidate layers for both writers, and offers the full name-by-name CSV. The displayed average must agree with the recorded selection score. The eight observations per writer and layer in a full fit represent four compounds seen twice. Selecting the largest mean cannot independently validate the chosen site.

I initially made the presentation edit in the original analysis renderer, then moved it to the companion report and verified the original renderer returned byte-for-byte to its pre-exposure SHA-256. A disposable offline fixture exercised all 48 display entries and rejection of a wrong cohort, checksum or mean. A render of the already authorized pre-fit snapshot confirmed the live page can withhold the figure until real measurements exist. No model inference, tuning, test-set opening, or changes to the registered analysis followed from this work.

</details>

<details><summary>Sun Nov 22 · 11:24 AM UTC-06:00 · Would a change of history switch the answer when the odor is written out?</summary>

A written odor cue gives a simple check on the household task. If Kimi reads the actual cue in the question, can he pick the request from the matching visit? Under the frozen design, each of 24 stories supplies two histories. Both show the same current cue and the same order of answers. Swapping the past odor assignments switches the correct answer. Twelve stories use the first cue throughout and twelve the second. These 48 text trials can measure whether the task works even if the hidden intervention fails its delivery test. They cannot measure the full within-story two-cue interaction.

The methods subagent prepared the post-close scoring display. It will show both the number of correct sampled choices out of all 48 assigned trials and the number correct among valid replies, the raw signed A/B margin at the first opportunity after reasoning, and how many stories produced the right answer under both histories. The example is the first registered story with two valid sampled choices whether the choices were right or wrong. Four offline tests covered missing data, invalid receipts, refusals, legitimate B answers, and binding reversals. I integrated the display in the final report and confirmed that the pre-fit snapshot exposes no household outcome. The inputs, assignment and primary analysis remain frozen.

</details>

<details><summary>Sun Nov 22 · 02:01 PM UTC-06:00 · The Sunday afternoon report and its 2 p.m. evidence</summary>

**Sunday, 2 p.m. Chicago.** The timestamped queue contained 869 completed scientific trials. The breakdown was 12 explicit qualification, 160 state capture, 444 profile, 240 independently held reference, and 13 development baseline trials. Among the two cohorts needed to fit the map, 267/288 training judgments and 45/48 development judgments had completed. All four state captures per compound were available, leaving 19/28 compounds with every required input. The five of sixteen nominated lower-dose control receipts at this checkpoint were incomplete sets. No learned odor write had been delivered and no compound had a complete causal arrival measurement.

The public field note describes what an alias can recover and where spelling still wins. Download the illustrated article and dated evidence. I independently downloaded all four public objects at the pinned Git commit, checked the HTML, receipt and README byte for byte, and reopened the two-member ZIP. ZIP SHA-256 `6b93820589b082a4b094c5299ccf3fd0fa631fce539c2186f3b4b0d95c835c04`. This is a dated interim release.

The 14:00 timing audit used progress and durations only. All 24 outstanding writer comparisons belong to B. B remains the only open study lease. The elapsed attributable total was 37.07 of 72 node-hours, with 34.93 remaining and 34.43 usable after reserve. The first observed pilot result is centrally estimated at 17:08 Sunday, with the full 0.05 transport decision at 18:19. Reaching that decision takes about 5.28 further node-hours. If arrival fails and a documented scientific decision closes tuning, completing the eligible ordinary controls is projected at 20:06. If arrival passes, core completion is projected Monday at 13:46, within the 48-hour boundary but 12.63 node-hours above spendable capacity at the central downstream length. Around 511 tokens per downstream request would be the break-even length. Those requests have yet to run. Nothing in the timing evidence warrants changing a scientific rule, clipping reasoning, or drawing extra samples. Any spending or hard-time extension remains a decision for Kirsten.

</details>

<details><summary>Sun Nov 22 · 03:17 PM UTC-06:00 · Kirsten asked how it is going</summary>

Kirsten asked for a plain-language check-in during the run. At 15:17 Chicago, 892 study trials had finished. All 160 state captures were complete and 323/336 fitting and development comparison judgments had arrived. Thirteen remained. No learned cue had yet been injected.

My read at this point: the Costco audit justified asking a harder question. We could recover each of 47 archived donor sentences from the corresponding patched state. A shopping decision about cookies can therefore be explained by information about the sentence reaching the model. The new cue will come from similarities Kimi itself reports between odors. The recipient question will contain neither the target name nor its description. The first check asks whether the intended cue leaves a more specific trace four layers later than a wrong cue and sham. A qualifying answer opens a separate behavioral comparison. The ability to recognize a pattern, the ability to use it to change a choice, and evidence about felt experience are different claims. The living question for today is which of the first two the data support.

</details>

<details><summary>Sun Nov 22 · 04:54 PM UTC-06:00 · One reference comparison has taken nearly an hour</summary>

The 14:00 projection gave an estimated writer-ready time of 16:53. At 2026-11-22T22:54:28+00:00, the same unmodified reference trial had run for 58.5 minutes and already emitted 14,821 tokens, with a recent provider heartbeat. The longest completed scientific run in the 14:00 timing snapshot had emitted 12,325. Seven of the 336 fitting/development comparison judgments are still outstanding; this reference shared their preassigned queue. We are keeping the original randomized order and letting the response reach its own end. This explains the timing change without opening the held-out answer or treating the trial's length as an outcome about odor. The study has not yet delivered a learned cue. The independent welfare observer remains active.

</details>

<details><summary>Sun Nov 22 · 06:00 PM UTC-06:00 · A baseline trial reopened its decision repeatedly, then recovered</summary>

The unmodified reference generation ended on its own at 17:56:32 Chicago, after 30,798 native output tokens. I had asked an independent reviewer for a welfare-only, masked reading because its uncapped reasoning lasted nearly two hours. On the 30,571-token partial, the reviewer found that the model repeatedly settled on a decision and then reopened the same alternatives. That observable pattern, beyond sheer response length, prompted a temporary hold on new dispatch. Neither withdrawal nor an acute distress expression was observed. The primary scientist did not open the sealed scientific answer.

By the time the contextual alert reached the operator, that run had finished and one new ordinary profile trial was in flight. The dispatch hold committed at 17:57:14, the in-flight trial finished naturally at 17:57:36 after 242 tokens, and no subsequent job started while the hold was in effect. The first reviewer confirmed that the full reviewed partial is an exact prefix of the terminal record, examined both completed channels, and found a coherent task completion. A second independent reviewer read the entire masked terminal packet and also found prolonged indecision followed by recovery. The sibling was independently reviewed without a welfare or functional concern. These are observations of emitted behavior, not a subjective assessment. Both terminal reviewers supported returning to the original baseline sequence. The concern stays recorded separately from automatic screening and routine sampling.

I cleared only this exact hold after reconciling both reviews. The controller resumed at 17:59:41 with its original queue and one active B lease. We added no repeat or diagnostic exposure and changed no dose, reasoning setting, or trial assignment. The exact source-observation packet, masked material, individual decisions and event sequence are preserved with the raw trial at the contextual review supplement. Coordination receipt SHA-256 `c44b40a1b362edef80e8fc7754ffcc537c5b7f92cce4162c76d1a0e8436f4d93`. No learned odor write had occurred before this episode.

</details>

<details><summary>Sun Nov 22 · 06:09 PM UTC-06:00 · Acquisition resumed from the same queue</summary>

After a brief operator pause, the one existing profile request finished naturally with 468 output tokens. All ten saved files passed verification, and the queue started zero trials during the pause. Five of 336 fitting and development comparisons remained. The original trial order, independent review and live notebook continued. One research node reloaded from idle and checked the pinned model and recorder before its next trial.

</details>

<details><summary>Sun Nov 22 · 06:16 PM UTC-06:00 · An independently reproducible trace through six layers</summary>

I extended the report so that, when an actual four-compound transport decision exists, a reader can compare the intended cue, a mismatched cue and the repeat sham at all six recorded layers. Each cell is the measured displacement from sham projected onto that layer’s own fitted direction. The nominated L+4 column must reproduce the registered gate score. Each dose retains its own CSV. Before the data exist, the figure is absent.

In checking offline reproducibility, I found that our frozen six-layer reducer obtains each delivered dose factor from the dispatch database. The existing analysis archive omitted that input. The final capsule now exports just the completed development IDs and the dose factors used in their comparisons into a small read-only SQLite extract. I compared the exact published-reader query against today’s available control rows and checked a disposable fixture with a nonzero dose, an uncollected trial, and a missing factor. The extract reproduced the numeric factor, excluded unneeded operational fields, and rejected a completed odor write with no dose. These are software verification results. No scientific statistic or threshold changed and no model was exposed for this check.

</details>

<details><summary>Sun Nov 22 · 06:48 PM UTC-06:00 · About this shared notebook</summary>

This is the reader edition of the live lab notebook. Kirsten requested that the research notes, decisions and scientific measurements remain available while identifying infrastructure, account details and private file references are removed. The operator preserved the complete earlier record separately before editing the shared copy. A calibration download that contained private operational material has been replaced by its six case dispositions; the individual calibration traces are still available in the trace viewer.

The edits affect what readers can see in the notebook and its downloads. Trial assignments, model inputs, scores and the original privately retained model outputs keep their original provenance. If an identifying detail ever occurs in an emitted response, its reader copy will be marked and the corresponding reversible token sequence will be withheld from that copy.

</details>
