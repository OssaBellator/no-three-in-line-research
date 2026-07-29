# Status and honesty ledger

**Last updated:** 29 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open. This repository does **not** contain a complete proof.

The authoritative theorem ledger reaches **CMR2751**. CMR2390 onward is recorded in
`proofs/composite-modulus-theorem-index-live-continuation-8.md`.

Every final checker, finite theorem checker, fixture, runtime manifest and branch-wide regression permanently
reports or preserves:

```text
all_n_proved_by_checker = 0
```

## Current exact finite endpoint

The branch contains synchronized documentary work banks through all 43 atomic targets:

| Target | Exact finite surface | Mathematical status |
|---|---|---|
| T01 | literal source statements, hashes and sealed source artifacts | genuine source statements remain unproved/unpopulated |
| T02 | cases, clauses, axes, exclusions and global-parent applications | genuine recurrence exhaustiveness remains open |
| T03 | open/populated/proved slot and candidate payloads | actual complete population remains absent |
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
| T19 | T02/T18-derived parent-to-final-row coverage with T04 clause ancestry | genuine global-family exhaustiveness remains open |
| T20 | exact 232 zero-selector chamber dispositions with typed host/row support | every zero-selector chamber proof remains open until supplied and reviewed |
| T21 | exact 20 hard-core chambers, one exchange functional, sharp cardinality threshold and exact two-point `Q4` classification | genuine recurrence signatures, labelled semantics and all 20 chamber arguments remain open |
| T22 | exact T01 dependency census and base-case premise bundle | the complete base-domain theorem remains open |
| T23 | exact T02/T19 dependency census and recurrence premise bundle | the nonbase recurrence-exhaustiveness implication remains open |
| T24 | exact T05/T07 dependency census and invariant premise bundle | invariant preservation remains open |
| T25 | exact T03/T06 dependency census and selection premise bundle | operation admissibility and intended minimization remain open |
| T26 | exact T08/T09/T10 dependency census and resource premise bundle | physical resource and credit semantics remain open |
| T27 | exact T11/T12 dependency census and contraction premise bundle | genuine contraction remains open |
| T28 | exact T13--T18 dependency census and cross-block premise bundle | validity of the assembled quotient remains open |
| T29 | exact T20/T21 dependency census and exceptional premise bundle | all 252 chamber theorems remain open |
| T30 | exact T11/T16/T18 dependency census and termination premise bundle | genuine branch termination remains open |
| T31 | exact T12/T16/T18--T21 dependency census and translation bundle | translation to `D(n)=2n` remains open |
| T32 | exact non-root obligation-to-target census and typed artifact-bank aggregation | genuine obligation proofs remain open with their lower mathematics |
| T33 | exact stable obligation-artifact support DAG surface | acyclicity metadata does not prove semantic sufficiency |
| T34 | exact aggregation of all ten T22--T31 premise artifacts and bundles | every final premise remains mathematically open |
| T35 | exact base-domain assertion, premise support and typed handoff bundle | the base handoff argument remains open |
| T36 | exact recurrence/selection assertion support and typed handoff bundle | the exhaustive nonbase handoff remains open |
| T37 | exact invariant/resource assertion support and typed handoff bundle | invariant preservation remains open |
| T38 | exact contraction/cross-block/termination assertion support | termination of every genuine recurrence branch remains open |
| T39 | exact exceptional assertion support and typed handoff bundle | all 252 chamber proofs and the exceptional implication remain open |
| T40 | exact objective-translation assertion support and typed handoff bundle | the quotient-to-objective translation remains open |
| T41 | exact six-assertion review census and final-handoff gate binding | ordinary mathematical review remains open |
| T42 | exact seven-gate dossier and blocker audit binding | a ready dossier would still not prove the root theorem |
| T43 | stable root cores, exact three-artifact bank and noncircular dual binding | the reviewed implication to `D(n)=2n` remains open |

## Canonical execution and validation

```text
python scripts/check_prime_power_canonical_frontier_roots.py --self-test
python scripts/check_prime_power_all_open_target_fixture.py --self-test
python scripts/test_prime_power_current_frontier_regression.py
python scripts/check_prime_power_hard_core_exchange_normal_form.py
python scripts/check_prime_power_hard_core_exchange_realisability.py
python scripts/check_prime_power_hard_core_two_point_classification.py
python -B -S -s scripts/check_prime_power_reproducible_runtime_manifest.py --self-test \
  --manifest artifacts/current-frontier-runtime.json
python scripts/run_prime_power_current_frontier_regression.py
python scripts/check_prime_power_final_support_handoff_frontiers_v2.py certificate.json
```

Canonical target roots remain:

```text
T19 <- T02, T18
T20 <- T05, T18, T19
T21 <- T05, T18, T19
```

## T21 hard-core exchange normal form

The eleven positive-minimum side-four hosts have exactly two response-family types:

```text
9 hosts: Q1=(3,0,1,2) and Q4=(3,2,1,0)
2 hosts: Q4 only
```

For the nine two-response hosts,

\[
\Delta=d_{32}-d_{12}+3h_{x-y-1}+h_{3x+y-3}+h_{x+3y-9}-5h_{x+y-3}-3,
\]

and

```text
Q1 selected iff Delta <= 0
Q4 selected iff Delta > 0
```

or, integrally,

\[
Q_4\text{ selected}
\iff
d_{32}+3h_{x-y-1}+h_{3x+y-3}+h_{x+3y-9}
\ge d_{12}+5h_{x+y-3}+4.
\]

Thus the twenty scalar chambers are nine copies of each halfspace plus two singleton-response full spaces.

## Sharp scalar realisability boundary

For an outside-grid background `B`, pair-count terms vanish when `|B|<=1`. Every pairwise intersection among the
four relevant lines lies inside the forbidden response grid, so one legal background point contributes at most
three positive line units. Therefore

\[
|B|\le1\Longrightarrow\Delta(B)\le0.
\]

The bound is sharp:

```text
empty background: Delta=-3, strict Q1
{(-1,-2)}: Delta=0, tie resolved to Q1
{(-1,-2),(4,3)}: Delta=5, strict Q4
```

Hence the minimum legal background cardinality for strict `Q4` selection is exactly two. Both nontrivial scalar
halfspaces are realizable; feasibility alone cannot discard the `Q4` chamber.

## Exact two-point strict-Q4 classification

For a legal two-point background `B={u,v}`, strict `Q4` selection occurs if and only if one of the following holds:

1. both points lie on `K_-:x-y-1=0`, in which case `Delta=5`;
2. exactly one point lies on `K_-`, the other lies on `K_30:3x+y-3=0` or `K_03:x+3y-9=0`, and their joining line avoids the negative pivots `(3,0)` and `(1,2)`, in which case `Delta=1`.

If the mixed joining line passes through a negative pivot, then `Delta=0` and lexicographic tie-breaking selects
`Q1`. Every other legal two-point background has `Delta<=0`.

The bounded exhaustive census over 3,486 pairs contains:

```text
15 double-K-minus strict-Q4 pairs
22 mixed positive-unit strict-Q4 pairs
2 mixed negative-pivot ties
3447 remaining non-Q4 pairs
```

These are finite scalar facts, not genuine T21 chamber proofs. The actual recurrence signatures,
destroyed-threshold consequences, labelled child vectors, return/interface terms and recurrent semantics remain
unproved.

## Corrected runtime audit

CMR2706--CMR2721 use inherited `PYTHON*` removal, exact seed and bytecode controls, `-B -S -s` startup, path
scrubbing, doubled runtime probes, source identities, AST honesty evidence and a sealed schema-v1 manifest. The
manifest records what runtime validation executed. It is not a proof certificate.

GitHub Actions is configured to run all three hard-core finite theorems and upload one thirty-day runtime-manifest
artifact per Python version. A committed workflow or uploaded artifact is not evidence that the conjecture is
proved.

## Genuine current frontiers

```text
T01--T02 source truth and genuine recurrence exhaustiveness
T03--T04 actual complete population
T05 arbitrary-n geometry coverage
T06--T18 semantic, score, rank, predicate and row theorems
T19 genuine global-family exhaustiveness
T20 all 232 zero-selector chamber theorems
T21 genuine signatures and all 20 semantic arguments, with exact two-point geometry available
T22--T31 all ten final premise implications
T35--T40 all six ordinary handoff arguments
T41 ordinary final review
T42 final dossier sign-off
T43 the reviewed root implication to D(n)=2n
```

T32--T34 are documentary aggregation gates and become effective only when their lower proof banks are genuinely
complete.

## Corrections retained

- A locator, hash, workflow result, fixture, manifest or sealed evidence record does not prove a theorem true.
- Exact recurrence identity does not prove recurrence exhaustiveness.
- Literal T03/T04 data do not prove their intended semantics.
- Finite T05 arithmetic does not prove arbitrary-`n` coverage.
- T06 scores and T07--T18 semantic statements remain external mathematics.
- T19 exact coverage does not prove the global family exhaustive.
- Scalar T21 halfspaces, witnesses and two-point classifications do not supply genuine recurrence signatures or semantics.
- Exact T22--T43 support does not prove any premise, handoff, review, dossier or root theorem.
- Canonical roots, syntax compilation, isolated imports, AST honesty checks, mutation rejection, manifests, CI
  and acyclic graphs are documentary or software metadata.

## Bottom line

There is no complete proof. Through **CMR2751**, the repository has a synchronized finite documentary stack
through all 43 targets, corrected runtime validation, one explicit hard-core exchange functional, the sharp
two-point threshold for strict `Q4`, and a complete geometric classification of every legal two-point background.

The unresolved centre remains the genuine mathematics listed above.
