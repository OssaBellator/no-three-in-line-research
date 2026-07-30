# Status and honesty ledger

**Last updated:** 30 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open. This repository does **not** contain a complete proof.

The authoritative theorem ledger reaches **CMR2839**. Every final checker,
finite theorem checker, population bridge, fixture, runtime manifest and
branch-wide regression permanently reports or preserves:

```text
all_n_proved_by_checker = 0
```

## Current exact finite endpoint

| Target | Exact finite surface | Mathematical status |
|---|---|---|
| T01 | literal source statements, hashes and sealed source artifacts | genuine source statements remain unproved/unpopulated |
| T02 | canonical masked-host family, realizable triple universe, anchor, target and complete local response | global generation of the actual host/mask/context sequence and recurrence exhaustiveness remain open |
| T03 | open/populated/proved slot payloads plus a hard-core population bridge | actual complete population, including survivor backgrounds, remains absent |
| T04 | skeleton-derived recurrent-block and interface assembly | actual complete assembly remains absent |
| T05 | exact finite geometry and selector arithmetic | arbitrary-`n` coverage remains open |
| T06 | exact slot scores, candidate sets and deterministic winners | score theorems and intended policy remain open |
| T07 | exact fate, state and transition subjects and support DAGs | semantic truth remains open |
| T08 | one active row per exact T06 application | genuine simultaneous-row exhaustiveness remains open |
| T09 | literal destroyed resources, overlap graph and scopes | physical resource exhaustiveness remains open |
| T10 | routed-credit subjects, assignments and injectivity | route and child-state semantics remain open |
| T11 | exact row bridges, primitive weights, recurrent closure and margins | genuine recurrent-block semantics remain open |
| T12 | acyclic auxiliary substitution and selected-response stability | expansion truth and target-state meaning remain open |
| T13 | T04-derived states, T07-supported global classes and proof trees | genuine cross-block identity remains open |
| T14 | T11/T13 scale equations, multipliers and component weights | external scale semantics remain open |
| T15 | T04-derived interface rows, final multipliers and exit dispositions | genuine interface exhaustiveness remains open |
| T16 | T15-derived critical edges, rank domains, ranks and graph audit | genuine rank meaning remains open |
| T17 | T13-derived predicates and rank-sensitive binding | predicate truth remains open |
| T18 | T12/T15-derived final rows and exact predicate multisets | row theorems and fixed-offset meaning remain open |
| T19 | T02/T18-derived parent-to-final-row coverage | genuine global-family exhaustiveness remains open |
| T20 | exact 232 zero-selector chamber dispositions | every zero-selector chamber proof remains open |
| T21 | exact hard-core scalar geometry, stability and T03 bridge | genuine recurrence populations, labelled semantics and all 20 chamber arguments remain open |
| T22 | exact base-domain premise bundle | complete base-domain theorem remains open |
| T23 | exact recurrence premise bundle | nonbase recurrence-exhaustiveness implication remains open |
| T24 | exact invariant premise bundle | invariant preservation remains open |
| T25 | exact selection premise bundle | operation admissibility and intended minimization remain open |
| T26 | exact resource premise bundle | physical resource and credit semantics remain open |
| T27 | exact contraction premise bundle | genuine contraction remains open |
| T28 | exact cross-block premise bundle | validity of the assembled quotient remains open |
| T29 | exact exceptional premise bundle | all 252 chamber theorems remain open |
| T30 | exact termination premise bundle | genuine branch termination remains open |
| T31 | exact objective-translation bundle | translation to `D(n)=2n` remains open |
| T32 | typed non-root obligation aggregation | genuine obligation proofs remain open |
| T33 | stable obligation-artifact support DAG | acyclicity metadata does not prove semantic sufficiency |
| T34 | aggregation of all ten final premises | every final premise remains mathematically open |
| T35 | base-domain handoff bundle | base handoff argument remains open |
| T36 | recurrence/selection handoff bundle | exhaustive nonbase handoff remains open |
| T37 | invariant/resource handoff bundle | invariant preservation remains open |
| T38 | contraction/cross-block/termination handoff | termination of every genuine branch remains open |
| T39 | exceptional handoff bundle | all chamber proofs and exceptional implication remain open |
| T40 | objective-translation handoff bundle | quotient-to-objective translation remains open |
| T41 | six-assertion review census | ordinary mathematical review remains open |
| T42 | seven-gate dossier | final dossier sign-off remains open |
| T43 | stable root cores and three-artifact bank | reviewed implication to `D(n)=2n` remains open |

## Canonical execution and validation

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
python scripts/check_prime_power_final_support_handoff_frontiers_v2.py certificate.json
```

Every runtime artifact contains a literal `manifest_sha256` seal. A manifest
records validation execution and is not a proof certificate.

## Canonical masked-host T02 dispatch

For side \(n\), the labelled host is

\[
H_n=\{0,1\}\times[n]\times[n].
\]

A state is an ordered pair of permutation matchings whose physical cells are
disjoint. For a canonical deleted-edge mask \(D\), the checker generates

\[
\mathcal F(n,D)
=
\{S:\ S\text{ is saturated, layer-disjoint and }S\cap D=\varnothing\}.
\]

It then generates the exact realizable collinear-triple universe

\[
\mathcal U(n,D)
=
\bigcup_{S\in\mathcal F(n,D)}
\{T\subseteq S:|T|=3,\ T\text{ collinear}\}.
\]

For every undeleted edge \(f\),

\[
\mathcal F(n,D\cup\{f\})
=
\{S\in\mathcal F(n,D):f\notin S\},
\]

and

\[
\mathcal U(n,D\cup\{f\})\subseteq\mathcal U(n,D).
\]

The local dispatch is now canonical from \((n,D)\):

```text
F(n,D) empty
  -> infeasible-mask terminal

F(n,D) nonempty and least anchor is triple-free
  -> clean-anchor terminal

F(n,D) nonempty and least anchor is dirty
  -> least anchor triple
  -> target contraction, strict improvement,
     or least-new-triple first-missing partition
```

The T02 theorem contracts record:

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

Their contract digests are:

```text
dca487a954f03f5aaebf09394ab427ef5b338f0e107adf6581146d84863ce39c
c7239521fb73e0347783e76ebfde83d96e968712376745542b5a93888312c0ef
634318242ece5cab549b9394ba33e116d7c1b01b4c74d5a02e276004fe1e8444
0cdc1914c11c79e1c9f3274f025263597c8eec5a7ed9c7e60d8cc24d66f817e7
```

The local rule still does not prove that the actual prime-power construction
generates every required host, deletion mask, factor, owner, routing or
closure-envelope context, nor that every contraction and relabelling is
captured by this masked-host model.

## T21 scalar and population boundary

For the nine two-response hard-core hosts,

\[
\Delta(B)=E_+(B)-E_-(B)+W(B)-3,
\]

with `Q1` selected for \(\Delta\le0\) and `Q4` selected for \(\Delta>0\).
The remaining two hosts admit only `Q4`.

For \(m=|B|\),

\[
-(m+1)(m+3)\le\Delta(B)\le(m-1)(m+3),
\]

with exact support-line stability gaps away from the two extremal lines.

The T03 bridge validates any supplied hard-core survivor background and exact
selector data, but it records:

```text
actual_t03_population_supplied_by_bridge = 0
t21_semantic_chambers_proved = 0
```

## Corrected runtime and regression audit

GitHub Actions is configured for Python 3.10 and 3.12 to run:

- the negative validator suite;
- ten finite theorem checkers;
- the T03/T21 population-bridge self-test;
- the strict runtime-manifest audit; and
- the complete current-frontier regression.

The branch-wide runner retains `validate_endpoint_text`,
`validate_document_markers` and `run_self_test` for the negative suite.
Configuration is not evidence that a workflow passed.

## Genuine current frontiers

```text
T01 prove and populate genuine source statements
T02 prove global host/mask/context generation and complete recurrence exhaustiveness
T03--T04 populate every real slot, block and interface
T05 prove arbitrary-n geometry coverage
T06--T18 prove semantic, score, resource, rank, predicate and row theorems
T19 prove genuine global-family exhaustiveness
T20 prove all 232 zero-selector chambers
T21 populate genuine hard-core slots and prove all 20 semantic arguments
T22--T31 prove all ten final premise implications
T35--T40 prove all six ordinary handoff arguments
T41 complete ordinary final review
T42 complete dossier sign-off
T43 prove the reviewed root implication to D(n)=2n
```

T32--T34 are documentary aggregation gates and become effective only when
their lower proof banks are genuinely complete.

## Bottom line

There is no complete proof. Through **CMR2839**, the branch contains a complete
local masked-host dispatcher relative to a side length and deletion mask, six
exact hard-core scalar theorems, a T03/T21 population bridge, and synchronized
documentary interfaces through all 43 targets. Global generation of the actual
prime-power context/mask sequence, real population, recurrence exhaustiveness
and all global semantic implications remain open.
