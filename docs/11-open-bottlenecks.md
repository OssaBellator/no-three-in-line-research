# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. Through **CMR2771**, this branch contains exact documentary
interfaces for all 43 atomic targets, canonical T19--T21 ancestry through T43, corrected runtime manifests, one
explicit side-four hard-core exchange functional, exact two-point and collinear geometry, and an arbitrary-
background pivot-line energy identity with sharp cardinality extremes.

Every final checker, finite theorem checker, fixture and validation runner permanently reports or preserves:

```text
all_n_proved_by_checker = 0
```

The branch still lacks genuine source proofs, an exhaustive recurrence theorem, the complete populated
construction, arbitrary-`n` geometry, semantic row proofs, the global-family theorem, all 252 chamber arguments,
all premise implications, all handoff arguments, final mathematical review and the root implication to
`D(n)=2n`.

A locator, digest, affine halfspace, finite witness, classification, energy identity, successful import, manifest
or workflow artifact is not evidence that the underlying all-`n` theorem is true.

## 2. Canonical execution and validation

Run:

```text
python scripts/test_prime_power_current_frontier_regression.py
python scripts/check_prime_power_hard_core_exchange_normal_form.py
python scripts/check_prime_power_hard_core_exchange_realisability.py
python scripts/check_prime_power_hard_core_two_point_classification.py
python scripts/check_prime_power_hard_core_collinear_backgrounds.py
python scripts/check_prime_power_hard_core_pivot_line_energy.py
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
The branch-wide runner retains the pure validator APIs used by the negative mutation suite and executes all five
hard-core finite theorems. Inspect actual workflow runs and artifacts before claiming CI success.

## 3. T01--T04: source truth, recurrence and actual population

### T01 source statements

Transcribe every cited statement literally, recompute its UTF-8 digest and supply the source-kind-specific proof
artifact. Each statement needs ordinary mathematical review. A sealed literal statement is not a proof.

### T02 recurrence exhaustiveness

Populate and prove every case, clause, finite axis, exclusion and global-parent application. Bind every
application to its exact source case, clause and operation slot. Then prove that the supplied rule bank is the
genuine exhaustive recurrence rather than merely an internally complete manifest.

### T03 slot and candidate population

Enter every literal operation-slot field: points, removals, survivors, fate witnesses, response families,
selectors, vectors, routed credits, loads and transitions. Keep data `populated` rather than `proved` until its
exact mathematical support exists.

### T04 block and interface population

Enter every skeleton-derived recurrent block and return/interface/off-diagonal row with exact T03 ancestry.
Recurrent blocks need local states, recurrent rows, return routes, interface attachments and source-clause
bindings. Interface rows need target, route, transition and source-clause data.

## 4. T05--T10: geometry, policy, state, resources and credits

For T05, prove every responsewise finite delta, threshold and selector theorem, then prove that the finite
geometry bank covers every relevant configuration for arbitrary `n`.

For T06, prove every integer candidate score, reconstruct each complete candidate set, select the least
`(score, slot_id)` pair and prove every T02 application uses the intended winner.

For T07, prove every exact fate, state and transition statement. For T08, prove the application-derived rows form
the genuine simultaneous active-row family. For T09, prove the coordinate-canonical resource bank is physically
exhaustive. For T10, prove every routed-credit assignment has the claimed resource, witness, child-state and
transition meaning.

## 5. T11--T18: contraction, identity, interfaces, rank and rows

Every T11 block must bind the exact selected-row population and provide primitive positive weights, exact
recurrent support, no recurrent exit, strong connectivity and positive margin. T12 must prove every auxiliary
expansion and elimination has the claimed semantic meaning.

T13 needs the actual cross-block identity theorem. T14 needs the external meaning of every scale equation and
component weight. T15 must prove every interface row and final exit genuinely exhaustive. T16 must prove the
supplied rank meaningful and well-founded. T17 predicates must be true on every representative. T18 must prove
every reconstructed row theorem and fixed-offset interpretation.

## 6. T19: genuine global-family exhaustiveness

```text
T02_RULE_EXHAUSTIVENESS + T18_ROW_THEOREMS
    -> T19_GLOBAL_FAMILY
```

For every T02 parent application, prove that the exact nonempty T18 row bank exhausts every genuine recurrence
alternative and has the intended T04 source-clause interpretation.

## 7. T20: 232 zero-selector chambers

Every zero-selector chamber needs its genuine T05 host geometry and a chamber-specific proof that the selected
zero-rank-three response has the claimed destroyed-threshold, labelled-child, return, interface and recurrent-row
semantics. Typed dispositions and affine inequalities do not establish those meanings.

All 232 mathematical arguments remain open.

## 8. T21: exact scalar evaluation for arbitrary backgrounds

The eleven positive-minimum side-four hosts have response families

```text
9 hosts: Q1=(3,0,1,2), Q4=(3,2,1,0)
2 hosts: Q4 only
```

For every two-response host,

\[
\Delta=d_{32}-d_{12}+3h_{x-y-1}+h_{3x+y-3}+h_{x+3y-9}-5h_{x+y-3}-3,
\]

with exact deterministic selection

```text
Q1 iff Delta <= 0
Q4 iff Delta > 0
```

and integer threshold

\[
Q_4\iff
d_{32}+3h_{x-y-1}+h_{3x+y-3}+h_{x+3y-9}
\ge d_{12}+5h_{x+y-3}+4.
\]

The twenty scalar chambers therefore use one nontrivial functional: nine weak `Q1` halfspaces, nine strict `Q4`
halfspaces and two singleton-response full spaces.

### Sharp realisability and two-point classification

No background of at most one legal point selects `Q4`; two points suffice. For exactly two points, strict `Q4`
occurs precisely in the double-`K_-` family with `Delta=5`, or in the mixed `K_-`/`K_30` or `K_-`/`K_03` family
with a joining line avoiding the two negative pivots, where `Delta=1`. Negative-pivot alignment is the exact
`Delta=0` boundary.

### Collinear compression

For a finite legal background `B` collinear on a line `L`,

\[
\Delta(B)=\beta(L)\binom{|B|}{2}+\sum_{x\in B}\omega(x)-3.
\]

This gives the sharp supporting-line thresholds `2`, `3`, `3` and `4` for `K_-`, `K_30`, `K_03` and a clean
positive-pivot pencil, while pure negative and neutral pencils never select `Q4`.

### Arbitrary-background pivot-line energy

For each positive or negative response pivot, partition `B` by the line through that pivot. Let `E_+(B)` and
`E_-(B)` be the total within-pencil pair counts over the two positive and two negative pivots, and let `W(B)` be
the signed occupancy weight on the four relevant lines. Then

\[
\boxed{\Delta(B)=E_+(B)-E_-(B)+W(B)-3.}
\]

Equivalently,

\[
\boxed{Q_4\iff E_+(B)+W(B)\ge E_-(B)+4.}
\]

Insertion of a legal point `x` has the exact marginal

\[
\Delta(B\cup\{x\})-\Delta(B)=\omega(x)+\sum_{y\in B}\chi(x,y).
\]

For every `m=|B|`,

\[
\boxed{-(m+1)(m+3)\le\Delta(B)\le(m-1)(m+3).}
\]

The upper equality is exactly concentration on `K_-`, and the lower equality exactly concentration on `K_+`,
apart from the empty background where both formulas give `-3`. Thus strict `Q4` is scalar-feasible at size `m`
exactly when `m>=2`.

The next T21 work is now sharply separated from scalar evaluation:

1. populate every genuine survivor background produced by the actual recurrence;
2. prove that point set and its T03/T04 ancestry are mathematically correct;
3. compute its four pivot-pencil energies and four relevant-line occupancies;
4. prove destroyed-threshold and labelled child-vector consequences separately in the `Q1` and `Q4` regimes;
5. retain return, interface and recurrent-row terms;
6. review all twenty host-labelled semantic arguments.

Keep fixed-response correction `17`, rollback distance `12` and uniform correction `44` distinct. The two
singleton `Q4` hosts remain irreducible on their current raw allowed-edge sets.

## 9. T22--T31: ten final premise implications

Each premise reconstructs its exact T01--T21 dependency-target census and requires one reviewed implication with
explicit arbitrary-`n` scope. Stable premise and target artifact cores prevent circular outward hashes. The
dependency interfaces exist; all ten mathematical implications remain open.

## 10. T32--T43: typed aggregation, handoff and root implication

T32--T34 aggregate genuine typed obligation and premise artifacts. T35--T40 require six ordinary induction
handoff arguments. T41 requires final mathematical review. T42 requires dossier sign-off. T43 requires the
reviewed implication from the global quotient and handoff to `D(n)=2n`.

The finite hard-core theorems, canonical-root audit, all-open fixture, negative tests and runtime manifests prove
only their stated finite or software claims.

## 11. Immediate execution order

1. Prove and seal high-use T01 source statements.
2. Close every T02 case, clause, exclusion and global-parent record; prove recurrence exhaustiveness.
3. Enter actual T03/T04 data.
4. Prove T05 arbitrary-`n` coverage and every T06--T18 theorem.
5. Prove genuine T19 global-family exhaustiveness.
6. Prove all 232 T20 zero-selector chamber arguments.
7. Populate genuine T21 backgrounds and prove all 20 semantic arguments; scalar evaluation is now available for any supplied background.
8. Supply and review all ten T22--T31 premise implications.
9. Prove all six T35--T40 handoff assertions.
10. Complete T41 review and T42 dossier sign-off.
11. Prove the T43 implication to `D(n)=2n`.

No finite selector theorem, documentary checker or runtime manifest substitutes for the missing mathematical
proofs.
