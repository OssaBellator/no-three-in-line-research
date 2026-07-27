# Exact p=41 support-thirteen signed branch-and-bound

This diagnostic closes support thirteen for the audited `p=41` swapped
quarter-turn near-state. It distinguishes two exact modes.

- `target` forbids every changed source from retaining its old target. This is
  the derangement-only subspace used in the cycle-first and permanent chapters.
- `signed` excludes only the exact old signed assignment. It also permits a
  source to retain its old target while taking the opposite canonical
  orientation. This is the full canonical signed-support problem.

The complete 1,024-shard audit gives

```text
mode target
supports              75,140
search nodes       16,503,767
Hall failures       1,412,973
initial empty               7
repair found               no

mode signed
supports              75,140
search nodes       21,604,931
Hall failures       1,851,407
initial empty               5
repair found               no
```

Every shard contains the owner-feasible supports whose lexicographic ordinal is
congruent to the shard index modulo 1,024. The shard support totals sum to

```text
C(20,13)-C(17,13)=75,140.
```

The search constructs all `108190` maximal nonaxis lines and all `780`
canonical orbit options. At each node it recomputes the currently legal signed
options, applies an exact Hall perfect-matching test, and branches on the
smallest domain among both unassigned sources and unused targets. Duplicate
orbit blocks and all joint line-capacity violations are rejected incrementally.

Compile and run the all-support checker with

```bash
g++ -O3 -std=c++17 -fopenmp \
  scripts/check_p41_support13_signed_branch_bound.cpp \
  -o /tmp/check_p41_support13_signed

/tmp/check_p41_support13_signed \
  experiments/p41-swapped-quarter-turn-near-example.json signed 8

/tmp/check_p41_support13_signed \
  experiments/p41-swapped-quarter-turn-near-example.json target 8
```

The exact machine-readable ledger is
`experiments/p41-support13-signed-branch-bound-results.json`.

Together with the earlier exhaustive supports one through twelve, the signed
run proves that this near-state has canonical pair-orbit repair radius at least
fourteen. It does not decide support fourteen and does not produce a `p=41`
seed.
