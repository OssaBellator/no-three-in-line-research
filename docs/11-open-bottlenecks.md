# Open bottlenecks and execution roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. Through **CMR2839**, this branch
contains exact documentary interfaces for all 43 atomic targets, ten finite
theorem checkers, corrected runtime validation and one T03-to-T21 population
bridge.

Every final checker, finite theorem checker, bridge, fixture and regression
permanently reports or preserves:

```text
all_n_proved_by_checker = 0
```

A locator, hash, finite census, selector inequality, bridge manifest, runtime
manifest or workflow result is not evidence of the all-`n` theorem.

## 2. Canonical validation

```text
python scripts/check_prime_power_canonical_frontier_roots.py --self-test
python scripts/check_prime_power_all_open_target_fixture.py --self-test
python scripts/test_prime_power_current_frontier_regression.py
python scripts/check_prime_power_canonical_prescription_partition.py
python scripts/check_prime_power_target_trigger_response_partition.py
python scripts/check_prime_power_canonical_target_dispatch.py
python scripts/check_prime_power_masked_host_parent_generation.py
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

The source registry binds literal UTF-8 statement text, hashes and typed
verification artifacts. The genuine work remains to transcribe, verify, prove
or independently check, seal and review every mathematical source statement.
No sealed source record proves its statement true by itself.

## 4. T02: local masked-host dispatch closed, global generation open

### Closed deterministic masked-host rule

For side \(n\), define the labelled two-layer host

\[
H_n=\{0,1\}\times[n]\times[n].
\]

A saturated state is an ordered pair of permutation matchings with no shared
physical cell. For a monotone deleted-edge mask \(D\), define

\[
\mathcal F(n,D)
=
\{S:\ S\text{ is saturated, layer-disjoint and }S\cap D=\varnothing\}.
\]

The checker reconstructs this family exactly and without duplicates. It also
reconstructs the exact realizable triple universe

\[
\mathcal U(n,D)
=
\bigcup_{S\in\mathcal F(n,D)}
\{T\subseteq S:|T|=3,\ T\text{ physically collinear}\}.
\]

Single-edge deletion is now literal mask extension:

\[
\mathcal F(n,D\cup\{f\})
=
\{S\in\mathcal F(n,D):f\notin S\},
\]

with

\[
\mathcal U(n,D\cup\{f\})\subseteq\mathcal U(n,D).
\]

Thus the CMR830 abstract child \(\mathcal F-f\) is exactly the generated child
under mask \(D\cup\{f\}\).

The local dispatch is:

```text
F(n,D) empty
  -> infeasible-mask terminal

F(n,D) nonempty and least state has no realizable triple
  -> clean terminal

F(n,D) nonempty and least state is dirty
  -> least anchor triple
  -> preserving contraction,
     strict improvement,
     or least-new-triple first-missing partition
```

For a canonical new triple \((f_0,f_1,f_2)\), the exact children remain:

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
python scripts/check_prime_power_canonical_target_dispatch.py
python scripts/check_prime_power_masked_host_parent_generation.py
```

They record:

```text
conditional_parent_rule_clause_ready = 1
local_target_response_rule_ready = 1
canonical_target_bank_external_choice_required = 0
local_anchor_dispatch_complete = 1
masked_host_family_generated = 1
triple_universe_generated_from_family = 1
single_edge_mask_extension_exact = 1
child_triple_universe_monotone = 1
local_masked_parent_dispatch_complete = 1
actual_global_parent_rule_complete = 0
```

### Remaining T02 work

The remaining parent-rule problem is global rather than local:

1. prove which side, factor host and labelled coordinate system each genuine
   parent uses;
2. generate every initial and inherited deletion mask from the actual
   construction;
3. prove every owner, routing and closure-envelope transition induces the
   claimed mask, contraction and relabelling;
4. identify every additional non-mask restriction, if one exists;
5. classify every parent/context type and prove the classification exhaustive;
6. define every finite parameter axis and justify every exclusion;
7. assign genuine raw hosts and ordered labels;
8. bind every parent to exactly one admitted clause and slot; and
9. prove that no recurrence alternative is omitted and every branch terminates
   or reaches a successful descent.

The declarative clause enumerator remains exhaustive only relative to supplied
cases and clauses.

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

Keep data `populated` rather than `proved` until its source and T02 ancestry are
established. T04 must assemble exact recurrent blocks, return rows, interface
rows, off-diagonal rows, local states and route attachments.

## 6. T05--T10: geometry, policy and resources

T05 must prove that the masked-host model and finite geometry bank cover every
genuine arbitrary-`n` parent/context, including any contraction or relabelling
not represented by a plain deletion mask.

T06 must prove the candidate score is the intended recurrence policy. T07 must
prove every fate, state and transition record. T08--T10 must prove simultaneous
row completeness, physical resource scope, routed-credit meaning and nonreuse.

## 7. T11--T18: contraction and global quotient

Every T11 recurrent block needs a genuine primitive positive state-weight
vector, exact parent-row coverage, closure, strong connectivity and positive
margin. T12 must prove every auxiliary expansion semantically valid. T13--T18
still require genuine identities, scale meaning, interface exhaustiveness,
well-founded ranks, predicate truth and final row theorems.

## 8. T19: global-family exhaustiveness

The documentary family binds rows to the supplied T02 skeleton. The missing
theorem is that the globally generated context/mask tree and final row bank
exhaust every genuine recurrence alternative for every parent state.

## 9. T20: 232 zero-selector chambers

Every chamber needs genuine host geometry, the selected response,
destroyed-threshold consequences, labelled child vectors, return/interface
terms, recurrent-row semantics and ordinary mathematical review.

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

The remaining sequence is to obtain genuine hard-core slots from the global
T02 rule, populate every survivor background, run the bridge, prove owner-fate,
destroyed-threshold, labelled-vector, routed-credit, return/interface and
recurrent consequences, and review all 20 host-labelled chambers.

## 11. T22--T43

Prove and review all ten T22--T31 premise implications, all six T35--T40
handoff arguments, the T41 mathematical review, the T42 dossier sign-off and
the T43 implication to `D(n)=2n`.

T32--T34 remain documentary aggregation gates.

## 12. Immediate work order

1. Trace every actual prime-power parent/closure context to one labelled host
   and deletion mask, or isolate the exact additional restriction.
2. Prove contraction and relabelling preserve the masked-host semantics.
3. Prove the global context/mask trigger bank exhaustive and terminating.
4. Populate and prove the T01 sources required by those clauses.
5. Generate the genuine T02 registry and enter exact T03/T04 populations.
6. Run the T05--T21 finite engines on those real records.
7. Prove the semantic rows, chambers, premises, handoffs and root theorem.

No finite selector calculation, documentary checker or runtime manifest
substitutes for the missing mathematical proofs.
