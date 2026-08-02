# Exact recurrent global two-point progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

The classical no-three-in-line conjecture remains open. This addendum records two exact advances for first host `s4-75b04c45c1c8eac2` and the resulting physical-data boundary.

## ERL1n — global integer two-point strict reversal classification

For every two-point integer background disjoint from the five-response union, the complete score decomposes as

```text
intrinsic
+ singleton increment at the first point
+ singleton increment at the second point
+ pair-through-response contribution of their line.
```

The exact finite alphabets have

```text
15 singleton vectors
39 pair vectors.
```

Their abstract product contains

```text
43 triples making 3012 uniquely minimal
 0 triples making 3210 uniquely minimal.
```

Exact incidence compatibility reduces these candidates to

```text
14 fixed response-union lines
26 exceptional pairs on those lines
24 candidate pairs through exactly one response-union point
0 generic strict families.
```

The complete global strict-reversal set is exactly

```text
{(-3,5),(5,-3)}
{(-1,3),(5,-3)}
{(-2,6),(4,0)}
{(-2,6),(6,-2)}.
```

Every pair gives

```text
3012=1, 3210=4, 2031=2, 2310=2, 3201=2.
```

There are no other strict original-response reversals anywhere in the integer lattice at background size two. The radius census is two at radius five and two at radius six.

This closes strict reversal classification only. The full two-point score atlas remains open because infinitely many tie signatures still exist.

## ERL1o — side-four projection non-identifiability

The current deterministic first-host row stores

```text
host ID, deletions, intrinsic response energies, dispatch, blocker IDs.
```

It stores no coordinate-labelled background, deletion causes or physical owner/provenance labels.

Two complete lineage candidates therefore share the same projected row:

```text
empty background
  score vector (1,4,0,0,0)
  minimizer face {2031,2310,3201}

background {(-3,5),(5,-3)}
  score vector (1,4,2,2,2)
  minimizer face {3012}.
```

Their complete background-sensitive lineage identifiers differ, but their current side-four projection is identical.

Consequently, no argument using only the existing side-four host/response manifest can physically exclude the strict-reversal signatures. This is an exact projection obstruction, not a claim that the signatures occur in the installed construction.

## Current mandatory input contract

A physical first-host compiler must now provide:

1. every coordinate-labelled background over deletion trace `{02,20}`;
2. physical causes and owners of cells `02` and `20`;
3. owner/fate/collision/line/interface/CRT ancestry;
4. complete scores from the committed 31-coordinate signature;
5. installed legal operations and intermediate states;
6. exact child multiplicities, weights and parent budget.

The four strict signatures may then be excluded, rerouted, paid strictly or retained as recurrent states. Until those fields are populated, neither physical exclusion nor physical realization is proved.

## Executable artifacts

```text
scripts/check_exact_recurrent_first_host_global_integer_two_point_strict_reversal.py
data/exact_recurrent_first_host_global_integer_two_point_strict_reversal.json
docs/exact-recurrent-first-host-global-integer-two-point-strict-reversal.md

scripts/check_exact_recurrent_first_host_side_four_projection_nonidentifiability.py
data/exact_recurrent_first_host_side_four_projection_nonidentifiability.json
docs/exact-recurrent-first-host-side-four-projection-nonidentifiability.md
```

All physical-coverage, legal-operation, recurrent-row, strict-Lyapunov, termination and all-`n` flags remain zero.
