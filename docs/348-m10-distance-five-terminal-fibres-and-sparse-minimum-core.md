# Exact `m=10` distance-five terminal fibres and sparse minimum core

`docs/346` proves that every one of the `115,586,396` parity-clean signed states
at `m=10` reaches validity within five clean macro moves, with `535,072` states
at the maximum distance.  This chapter classifies that terminal layer and
computes the sharp shortest-path collateral barrier for its smallest atomic
core.

No asymptotic clean-macro horizon theorem is claimed.

## 1. The terminal layer is a union of complete clean fibres

For a parity-satisfiable Hamilton cycle `rho`, write `Omega(rho)` for its affine
clean orientation fibre and `c(rho)` for the number of parity components, so

```text
|Omega(rho)|=2^c(rho).
```

### Theorem PP3bqp -- VERIFIED FINITELY / COMPLETE-FIBRE TERMINAL LAYER

The `m=10` distance-five layer consists of the complete clean fibres over
exactly `1,260` Hamilton cycles.  In particular, if one clean orientation over
one of these cycles has distance five, then every clean orientation over that
cycle has distance five.

The supporting-cycle component distribution is

| parity components `c` | supporting cycles | states contributed |
|---:|---:|---:|
| 4 | 6 | 96 |
| 5 | 26 | 832 |
| 6 | 86 | 5,504 |
| 7 | 202 | 25,856 |
| 8 | 340 | 87,040 |
| 9 | 388 | 198,656 |
| 10 | 212 | 217,088 |
| **total** | **1,260** | **535,072** |

Every supporting parity graph has cyclomatic rank zero.  Thus none of the
rank-one clean parity fibres that first appear at `m=10` lies in the maximum
macro-distance layer.

#### Verification

The root-cube reverse search records the exact first-reached bitset at each
macro distance.  For every cycle meeting layer five, the checker compares that
bitset with the complete `2^c` root cube.  All `1,260` comparisons are equal.
The displayed state counts sum to the complete `535,072`-state terminal layer.
∎

This is the first finite indication that the extremal macro horizon may be a
cycle-coordinate obstruction rather than an orientation-coordinate
obstruction.

## 2. Complete terminal atomic census

For one clean signed state, let

```text
H = number of three-owner flaw supports,
Z = number of atomic collinear triples,
tau_H = minimum number of owners meeting every flaw support.
```

### Theorem PP3bqq -- VERIFIED FINITELY / TERMINAL GEOMETRY CENSUS

Across all `535,072` distance-five states:

```text
2 <= H <= 47,
8 <= Z <= 188,
1 <= tau_H <= 6.
```

The exact owner-cover distribution is

| `tau_H` | states |
|---:|---:|
| 1 | 168 |
| 2 | 21,640 |
| 3 | 256,256 |
| 4 | 240,504 |
| 5 | 16,376 |
| 6 | 128 |

The parity-component distribution over signed states is

| components | states |
|---:|---:|
| 4 | 96 |
| 5 | 832 |
| 6 | 5,504 |
| 7 | 25,856 |
| 8 | 87,040 |
| 9 | 198,656 |
| 10 | 217,088 |

The complete support-count and atomic-count histograms are stored in

```text
experiments/m10-distance-five-terminal-classification-audit.json
```

and are hard-coded into the executable regression checker.  Global sign
complementation preserves the terminal layer and partitions it into exactly
`267,536` complement pairs.

#### Verification

For every root assignment in the exact layer-five bitsets, the checker
reconstructs the signed owner assignments and all `C(10,3)=120` three-owner
atomic predicates.  It counts exact atomic multiplicity rather than merely
support presence, solves the owner-cover problem by exhaustive owner masks, and
compares every histogram with the stored ledger. ∎

## 3. The sixteen-state sparse minimum core

Exactly sixteen distance-five states attain the joint minimum

```text
H=2,
Z=8.
```

They form eight global-sign-complement pairs.  In every pair, the two flaw
supports share one owner and hence have owner-cover number one.

### Theorem PP3bqr -- VERIFIED FINITELY / COMPLETE MINIMUM-CORE BANK

One representative of each complement pair is listed below.  The second
orientation is obtained by XOR with `1023`.

| orientation | Hamilton successor array `rho` | two flaw supports |
|---:|---|---|
| 478 | `(3,2,8,9,7,1,4,0,6,5)` | `(1,3,9)`, `(4,8,9)` |
| 293 | `(3,4,9,1,5,7,2,8,6,0)` | `(2,4,8)`, `(3,5,8)` |
| 382 | `(3,7,9,1,5,6,8,4,2,0)` | `(1,2,4)`, `(2,5,7)` |
| 209 | `(7,2,6,9,1,3,8,4,5,0)` | `(4,7,8)`, `(6,7,9)` |
| 42 | `(7,5,1,0,6,9,8,4,2,3)` | `(2,5,9)`, `(5,6,7)` |
| 311 | `(9,3,6,0,1,4,8,5,7,2)` | `(1,6,7)`, `(5,6,9)` |
| 25 | `(9,3,8,0,7,4,5,1,6,2)` | `(4,6,9)`, `(5,7,9)` |
| 402 | `(9,4,1,5,7,8,2,0,6,3)` | `(0,4,8)`, `(1,4,5)` |

Each support contributes exactly four atomic triples.  No distance-five state
has one flaw support or fewer than eight atomic triples.

#### Verification

The checker filters the complete terminal ledger at `H=2,Z=8`, verifies global
complement closure, canonicalizes by successor array and smaller orientation,
and compares the resulting eight representatives and support masks with the
hard-coded bank. ∎

## 4. Sharp shortest-path collateral barrier

For a shortest five-step clean-macro path

```text
x_0,x_1,...,x_5
```

from one minimum-core state to validity, define

```text
peak_H=max_i H(x_i),
peak_Z=max_i Z(x_i).
```

### Theorem PP3bqs -- VERIFIED FINITELY / SHARP JOINT BARRIER

The minimum attainable joint peaks over shortest paths have distribution

```text
(peak_H,peak_Z)=(2,8):  4 states,
(peak_H,peak_Z)=(3,12): 12 states.
```

The support and atomic minima are attained simultaneously.  Therefore:

1. two complement pairs admit a shortest path that never exceeds their initial
   two supports and eight atomic triples;
2. the other six complement pairs necessarily create at least one additional
   flaw support and four additional atomic triples;
3. those same bounds are sufficient—no minimum-core state needs a larger
   shortest-path excursion.

#### Verification

The checker stores the exact root-cube distance layers `0,...,5`.  It then runs
a Pareto recursion only on the shortest-path backward cone of the eight
representatives.  For a state at distance `d`, every legal owner-intersecting
rotation into a cycle of minimum distance `d-1` is considered, and the target
orientation is freely regenerated inside that target fibre.  Nondominated
`(peak_H,peak_Z)` pairs are propagated backward.  The recursion evaluates
`15,936` clean cycles and compares the final joint distribution with the
hard-coded ledger. ∎

Compile and run the complete classifier with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_m10_distance_five_terminal_classification.cpp \
  -o /tmp/check_m10_distance_five_terminal_classification

OMP_NUM_THREADS=8 \
  /tmp/check_m10_distance_five_terminal_classification
```

## 5. Revised clean-macro horizon frontier

The maximum-distance layer now has three useful structural features.

1. **Cycle-level extremality.**  It is a union of complete affine fibres, so
   orientation variation is not responsible for the fifth step.
2. **Forest localization.**  Positive parity cyclomatic rank is absent from the
   terminal layer.
3. **Sparse embedded core.**  The smallest obstruction has only two supports,
   and its necessary shortest-path excursion is bounded by one extra support
   and four extra atomic triples.

The remaining horizon problem is to characterize the `1,260` extremal Hamilton
cycles by a cycle-coordinate invariant and explain why one additional pair
vertex raises the audited maximum from `3` to `4` to `5`.  The minimum-core bank
also supplies the first `m=10` test cases for a structural bounded-collateral
word extending `docs/339`.

The next theorem identifier after this chapter is `PP3bqt`.
