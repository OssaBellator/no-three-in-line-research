# Corrected twelfth boundary transition

`docs/633` extends the radius-64 corrected boundary path through eleven blocks.
This chapter performs the complete twelfth-step minimum-transversal census,
checks every smallest core through correction budget seven, and records one
canonical corrected twelfth state.

## 1. Exact twelfth conflict spectrum

### Theorem PP3cyf — PROVED / COMPLETE RADIUS-64 CENSUS

For the canonical corrected eleven-block state, the 1,032 typed twelfth-block
attempts have exact minimum line-conflict transversal histogram

```text
3:1, 4:4, 5:8, 6:101, 7:173, 8:239,
9:8, 10:25, 11:75, 12:146, 13:158, 14:94.
```

The five attempts of minimum size at most four are

```text
P1 at 63, P1 at 64, P2 at 64, P3 at 61, P3 at 64.
```

Their minimum-core counts are respectively `15,1,9,9,27`, for sixty-one cores
total.

#### Proof

`scripts/check_boundary_twelfth_spectrum.cpp` reconstructs the exact corrected
eleven-block point set, forms every old-old-new and old-new-new collinear triple,
and solves the resulting hitting-set problems by an exact branch-and-bound
kernel. The histogram sums to 1,032. ∎

## 2. Complete low-core correction search

### Theorem PP3cyg — PROVED / ALL FIVE LOW-CORE ATTEMPTS CORRECT

Every one of the five attempts with minimum transversal at most four admits a
row-and-column-preserving legal refill with total deletion size at most seven.
The minimum budgets found in lexicographic attempt order are

```text
6, 6, 5, 5, 5.
```

#### Proof

`scripts/check_boundary_twelfth_corrections.cpp` enumerates all sixty-one minimum
cores. For each core it enlarges the deletion set through budget seven and
searches every exact row/column multiset refill while pruning retained-pair,
retained-addition, and all-addition collinearities. Every attempt has a certified
success. ∎

## 3. Canonical twelfth transition

### Theorem PP3cyh — PROVED / FIVE-POINT TWELFTH CORRECTION

The canonical minimum-budget choice is `P2` at offset `64`. Delete

```text
(2,1), (14,48), (32,98), (46,257), (47,258)
```

and add

```text
(2,257), (14,258), (32,98), (46,1), (47,48).
```

The resulting set has ninety-six points, preserves every row and column degree,
and is no-three-in-line. All 1,032 raw thirteenth-block attempts in radius 64
fail.

#### Proof

`scripts/check_boundary_twelfth_transition.py` compiles both C++ kernels,
verifies the displayed correction, reconstructs the corrected twelve-block
state, checks all triples by exact determinants, and audits every raw thirteenth
attempt. ∎

## Consequence

The corrected radius-64 path now reaches twelve blocks. This is still a bounded,
nonperiodic path; a corrected thirteenth transition, a recurrence, or a scalable
state invariant remains missing.
