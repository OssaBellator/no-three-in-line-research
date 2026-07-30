# Open bottlenecks and execution roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. Through **CMR2817**, this branch
contains exact documentary interfaces for all 43 atomic targets, eight finite
theorem checkers, corrected runtime validation and one T03-to-T21 population
bridge.

Every final checker, finite theorem checker, bridge, fixture and regression
permanently reports or preserves:

```text
all_n_proved_by_checker = 0
```

A locator, hash, affine inequality, finite census, bridge manifest, runtime
manifest or workflow result is not evidence of the all-`n` theorem.

## 2. Canonical validation

```text
python scripts/check_prime_power_canonical_frontier_roots.py --self-test
python scripts/check_prime_power_all_open_target_fixture.py --self-test
python scripts/test_prime_power_current_frontier_regression.py
python scripts/check_prime_power_canonical_prescription_partition.py
python scripts/check_prime_power_target_trigger_response_partition.py
python scripts/check_prime_power_hard_core_exchange_normal_form.py
python scripts/check_prime_power_hard_core_exchange_realisability.py
python scripts/check_prime_power_hard_core_two_point_classification.py
python scripts/check_prime_power_hard_core_collinear_backgrounds.py
python scripts/check_prime_power_hard_core_pivot_line_energy.py
python scripts/check_prime_power_hard_core_extremal_stability.py
python scripts/check_prime_power_hard_core_population_bridge.py --self-test
python -B -S -s scripts/check_prime_power_reproducible_runtime_manifest.py --self-test \
  --manifest artifacts/current-frontier-runtime.json
python scripts/run_prime_power_current_frontier_regression.py
```

Inspect actual workflow runs and artifacts before claiming CI success.

## 3. T01: source truth

The source registry can bind literal UTF-8 statement text, hashes and typed
verification artifacts. The genuine work is still to:

1. transcribe each mathematical source statement;
2. verify its exact locator and text digest;
3. prove or independently check the statement;
4. supply the source-kind-specific artifact; and
5. review every downstream use.

No sealed source record proves its statement true by itself.

## 4. T02: complete parent rule

### Closed local response rule

Let \(S\) be a supplied anchor, \(\mathcal F\) a supplied equal-cardinality
feasible family and \(\mathcal Q\) a nonempty designated target bank in \(S\).
Define

\[
K(\mathcal Q)=\bigcup_{T\in\mathcal Q}T.
\]

CMR2806--CMR2817 give a complete local response for every alternative
\(R\in\mathcal F\setminus\{S\}\):

```text
A. R preserves every designated target
   -> R contains the complete target core K
   -> exact target-core contraction

B. R destroys a target and Phi(R) < Phi(S)
   -> strict potential improvement

C. R destroys a target and Phi(R) >= Phi(S)
   -> CMR698 gives at least one genuinely new triple
   -> choose the canonical first new triple
   -> apply the duplicate-free first-missing partition
```

For case C, if the canonical new triple is \((f_0,f_1,f_2)\), the exact
children are:

```text
B0: omit f0
B1: contain f0 and omit f1
B2: contain f0,f1 and omit f2
B3: contain f0,f1,f2 and contract the forced triple
```

The executable endpoints are:

```text
python scripts/check_prime_power_canonical_prescription_partition.py
python scripts/check_prime_power_target_trigger_response_partition.py
```

They record:

```text
conditional_parent_rule_clause_ready = 1
local_target_response_rule_ready = 1
exact_candidate_trigger_partition = 1
target_preserving_core_contraction = 1
strict_improvement_action = 1
nonimproving_new_triple_action = 1
actual_global_parent_rule_complete = 0
```

This is a complete local response **relative to supplied data**. It is not the
complete global parent rule.

### Remaining T02 work

The genuine parent-rule frontier is now:

1. generate every feasible parent family \(\mathcal F\) from the actual
   construction;
2. prove the anchor and exact triple universe correct;
3. prove that a nonempty designated target bank exists whenever this local rule
   is invoked;
4. classify every parent/closure situation where no such target bank is
   available;
5. prove those global trigger classes mutually complete;
6. define every finite parameter axis and justify every exclusion;
7. assign genuine expected raw hosts and ordered state labels;
8. bind every global parent to exactly one admitted clause/slot; and
9. prove that no recurrence alternative is omitted.

The existing declarative clause enumerator is exhaustive only relative to
supplied cases and clauses.

## 5. T03--T04: real population

For every genuine T02 operation slot, enter literal:

```text
points
removals
survivor_background
owner_fate_witnesses
response_family
feasibility_signatures
selector_data
labelled_vectors
routed_credits
row_loads
transitions
```

Keep data `populated` rather than `proved` until its mathematical source and
T02 ancestry are established.

T04 must then assemble the exact recurrent blocks, return rows, interface rows,
off-diagonal rows, local states and route attachments derived from those slots.

## 6. T05--T10: geometry, policy and resources

T05 must prove the finite geometry bank covers every relevant arbitrary-`n`
configuration.

T06 must prove the candidate score is the intended recurrence policy, not only
that a declared minimum was computed correctly.

T07 must prove the external meaning of every fate, state and transition record.

T08--T10 must prove simultaneous row completeness, physical destroyed-resource
scope, routed-credit meaning and global nonreuse.

## 7. T11--T18: contraction and global quotient

Every T11 recurrent block needs one genuine primitive positive state-weight
vector, exact parent-row coverage, closure, strong connectivity and positive
margin.

T12 must prove every auxiliary expansion and elimination semantically valid.

T13--T18 still require genuine cross-block identities, external scale meaning,
complete interface rows, well-founded ranks, predicate truth and final row
theorems.

## 8. T19: global-family exhaustiveness

The documentary family binds rows to the supplied T02 skeleton. The missing
theorem is that the completed skeleton and row bank exhaust every genuine
recurrence alternative for every parent state.

## 9. T20: 232 zero-selector chambers

Every chamber needs:

- genuine T05 host geometry;
- the selected response;
- destroyed-threshold consequences;
- labelled child vectors;
- return and interface terms;
- recurrent-row semantics; and
- ordinary mathematical review.

All 232 arguments remain open.

## 10. T21: hard-core chambers

The scalar selector is exact for every supplied background:

\[
\Delta(B)=E_+(B)-E_-(B)+W(B)-3.
\]

For \(m=|B|\),

\[
-(m+1)(m+3)\le\Delta(B)\le(m-1)(m+3),
\]

with sharp support-line stability.

The population bridge:

```text
python scripts/check_prime_power_hard_core_population_bridge.py \
  t03-certificate.json \
  --write artifacts/hard-core-population-bridge.json
```

validates literal backgrounds, response families and selector data. It does not
supply genuine T03 data or prove chamber semantics.

The remaining T21 sequence is:

1. obtain genuine hard-core slots from the completed T02 rule;
2. populate every survivor background;
3. run the exact bridge;
4. prove owner-fate and destroyed-threshold consequences;
5. prove labelled vectors and routed credits;
6. retain return/interface/recurrent terms; and
7. review all 20 host-labelled chamber arguments.

## 11. T22--T43

Prove and review:

1. all ten T22--T31 premise implications;
2. all six T35--T40 handoff arguments;
3. the T41 mathematical review;
4. the T42 dossier sign-off; and
5. the T43 implication to `D(n)=2n`.

T32--T34 remain documentary aggregation gates.

## 12. Immediate work order

1. Prove global generation of every feasible parent family and the exact target
   bank used by the complete local response theorem.
2. Classify all parent/closure situations outside that target-bank setup and
   prove the global trigger bank exhaustive.
3. Populate and prove the T01 sources required by those clauses.
4. Generate the genuine T02 slot registry and enter exact T03/T04 populations.
5. Run the T05--T21 finite engines on those real records.
6. Prove the semantic rows, chambers, premises, handoffs and root theorem.

No finite selector calculation, documentary checker or runtime manifest
substitutes for the missing mathematical proofs.
