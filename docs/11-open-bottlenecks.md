# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. Through **CMR2793**, this branch contains exact documentary
interfaces for all 43 atomic targets, six finite side-four hard-core scalar theorems, corrected runtime validation
and an executable T03-to-T21 population bridge.

Every final checker, finite theorem checker, population bridge, fixture and validation runner permanently reports
or preserves:

```text
all_n_proved_by_checker = 0
```

The branch still lacks genuine source proofs, the actual parent rule, an exhaustive recurrence theorem, complete
T03/T04 population, arbitrary-`n` geometry, semantic row proofs, the global-family theorem, all 252 chamber
arguments, all premise implications, all handoff arguments, final review and the root implication to `D(n)=2n`.

A locator, digest, affine halfspace, finite witness, energy identity, stability gap, bridge manifest, runtime
manifest or workflow result is not evidence that the underlying all-`n` theorem is true.

## 2. Canonical execution and validation

Run:

```text
python scripts/test_prime_power_current_frontier_regression.py
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
python scripts/check_prime_power_all_open_target_fixture.py --self-test
python scripts/check_prime_power_canonical_frontier_roots.py --self-test
```

The canonical complete endpoint remains:

```text
python scripts/check_prime_power_final_support_handoff_frontiers_v2.py certificate.json
```

Canonical roots are:

```text
T19 <- T02, T18
T20 <- T05, T18, T19
T21 <- T05, T18, T19
```

The corrected runtime layer uses `-B -S -s`, removes inherited `PYTHON*` variables, scrubs third-party paths,
records source identities and endpoint honesty evidence, and seals one schema-v1 manifest per Python version.
The branch-wide runner executes three structural self-tests, six finite theorem checkers and one frontier-bridge
self-test. Inspect actual workflow runs and artifacts before claiming CI success.

## 3. T01--T04: source truth, parent rule and population

### T01 source statements

Transcribe every cited statement literally, recompute its UTF-8 digest and supply the source-kind-specific proof
artifact. Each statement needs ordinary mathematical review. A sealed literal statement is not a proof.

### T02 actual parent rule and recurrence exhaustiveness

The existing clause enumerator proves only exact expansion relative to supplied parent cases, clauses, finite axes
and exclusions. Its own source states that the actual parent rule is not yet present.

The next genuine work is:

1. state the actual parent rule;
2. prove every parent case and clause exhaustive;
3. prove every finite axis has the intended domain;
4. justify every exclusion;
5. bind every global parent to its exact admitted slot;
6. prove that no genuine recurrence alternative is omitted.

No slot count or internally complete manifest substitutes for this theorem.

### T03 slot and candidate population

Every literal operation-slot payload must contain:

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

The schema reserves these fields but does not manufacture their mathematical values.

For a hard-core expected host, the new bridge additionally requires:

- a literal distinct outside-grid `survivor_background`;
- the exact canonical response family;
- exact positive and negative pivot energies;
- the signed relevant-line weight;
- the exact selector delta and selected response;
- a sealed `side-four-hard-core-exchange-v1` selector record.

Run the bridge on a genuine T03 certificate with:

```text
python scripts/check_prime_power_hard_core_population_bridge.py \
  t03-certificate.json \
  --write artifacts/hard-core-population-bridge.json
```

The current bridge contract honestly records:

```text
actual_parent_rule_present = 0
actual_t03_population_supplied_by_bridge = 0
t21_semantic_chambers_proved = 0
all_n_proved_by_checker = 0
```

A slot may be `populated` before it is `proved`. A scalar-ready bridge record does not prove the underlying point
set genuine or any chamber semantics.

### T04 block and interface population

Enter every skeleton-derived recurrent block and return/interface/off-diagonal row with exact T03 ancestry.
Recurrent blocks need local states, recurrent rows, return routes, interface attachments and source-clause
bindings. Interface rows need targets, routes, transitions and source-clause data.

## 4. T05--T10: geometry, policy, state, resources and credits

For T05, prove every responsewise finite delta, threshold and selector theorem, then prove that the finite geometry
bank covers every relevant configuration for arbitrary `n`.

For T06, prove every integer candidate score, reconstruct each complete candidate set, select the least
`(score, slot_id)` pair and prove every T02 application uses the intended winner.

For T07, prove every exact fate, state and transition statement. For T08, prove the application-derived rows form
the genuine simultaneous active-row family. For T09, prove the coordinate-canonical resource bank is physically
exhaustive. For T10, prove every routed-credit assignment has the claimed resource, witness, child-state and
transition meaning.

## 5. T11--T18: contraction, identity, interfaces, rank and rows

Every T11 block must bind the exact selected-row population and provide primitive positive weights, exact recurrent
support, no recurrent exit, strong connectivity and positive margin. T12 must prove every auxiliary expansion and
elimination has the claimed semantic meaning.

T13 needs the actual cross-block identity theorem. T14 needs the external meaning of every scale equation and
component weight. T15 must prove every interface row and final exit genuinely exhaustive. T16 must prove the
supplied rank meaningful and well-founded. T17 predicates must be true on every representative. T18 must prove
every reconstructed row theorem and fixed-offset interpretation.

## 6. T19: genuine global-family exhaustiveness

```text
T02_RULE_EXHAUSTIVENESS + T18_ROW_THEOREMS
    -> T19_GLOBAL_FAMILY
```

For every genuine T02 parent application, prove that the exact nonempty T18 row bank exhausts every recurrence
alternative and has the intended T04 source-clause interpretation.

## 7. T20: 232 zero-selector chambers

Every zero-selector chamber needs genuine T05 host geometry and a chamber-specific proof that the selected
zero-rank-three response has the claimed destroyed-threshold, labelled-child, return, interface and recurrent-row
semantics.

All 232 mathematical arguments remain open.

## 8. T21: exact scalar geometry, missing population and semantics

The eleven positive-minimum side-four hosts have response families:

```text
9 hosts: Q1=(3,0,1,2), Q4=(3,2,1,0)
2 hosts: Q4 only
```

For every two-response host and every finite legal background `B`,

\[
\Delta(B)=E_+(B)-E_-(B)+W(B)-3,
\]

with exact selection:

```text
Q1 iff Delta <= 0
Q4 iff Delta > 0
```

The exact all-cardinality bounds are:

\[
-(m+1)(m+3)\le\Delta(B)\le(m-1)(m+3),
\qquad m=|B|.
\]

The upper and lower equality supports are exactly `K_-` and `K_+`. Away from those lines:

\[
B\nsubseteq K_-
\Longrightarrow
\Delta(B)\le(m-1)(m+3)-2m,
\]

\[
B\nsubseteq K_+
\Longrightarrow
\Delta(B)\ge-(m+1)(m+3)+2m+3.
\]

The T03 bridge now makes scalar population consistency executable. For each genuine hard-core slot it will:

1. validate the expected host and literal background;
2. bind the exact response family;
3. recompute the energy identity;
4. verify the selected response;
5. report open, populated, proved and scalar-ready states separately.

The remaining genuine T21 work is:

1. supply the actual parent rule;
2. identify every genuine hard-core expected slot;
3. populate and prove each literal survivor background;
4. run the exact bridge;
5. prove owner-fate and destroyed-threshold consequences;
6. prove labelled child vectors and routed credits;
7. retain return, interface and recurrent-row terms;
8. review all twenty host-labelled semantic arguments.

The two singleton `Q4` hosts remain semantically open even though their scalar response family is fixed.

## 9. T22--T31: ten final premise implications

Each premise reconstructs its exact T01--T21 dependency-target census and requires one reviewed implication with
explicit arbitrary-`n` scope. Stable premise and target artifact cores prevent circular outward hashes. The
dependency interfaces exist; all ten mathematical implications remain open.

## 10. T32--T43: aggregation, handoff and root implication

T32--T34 aggregate genuine typed obligation and premise artifacts. T35--T40 require six ordinary induction
handoff arguments. T41 requires final mathematical review. T42 requires dossier sign-off. T43 requires the
reviewed implication from the global quotient and handoff to `D(n)=2n`.

The finite hard-core theorems, population bridge, canonical-root audit, all-open fixture, negative tests and
runtime manifests prove only their stated finite, interface or software claims.

## 11. Immediate execution order

1. Prove and seal high-use T01 source statements.
2. State and prove the actual T02 parent rule and recurrence exhaustiveness.
3. Enter genuine T03 payloads, beginning with hard-core survivor backgrounds, and run the population bridge.
4. Build the actual T04 block/interface bank.
5. Prove T05 arbitrary-`n` coverage and every T06--T18 theorem.
6. Prove genuine T19 global-family exhaustiveness.
7. Prove all 232 T20 chamber arguments.
8. Prove all 20 T21 semantic arguments after exact scalar projection.
9. Supply and review all ten T22--T31 premise implications.
10. Prove all six T35--T40 handoff assertions.
11. Complete T41 review and T42 dossier sign-off.
12. Prove the T43 implication to `D(n)=2n`.

No finite selector theorem, population bridge, documentary checker or runtime manifest substitutes for the missing
mathematical proofs.
