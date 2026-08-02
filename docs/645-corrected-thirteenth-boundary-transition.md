# Corrected thirteenth boundary transition

`docs/639` advances the radius-64 corrected path to twelve blocks and records
that no raw thirteenth block survives.  This chapter exhausts the thirteenth
conflict spectrum and advances the corrected path by one further block.

## 1. Exact thirteenth conflict spectrum

### Theorem PP3cyx — PROVED / COMPLETE RADIUS-64 THIRTEENTH CENSUS

For the corrected twelve-block state, the 1,032 typed thirteenth attempts have
minimum line-conflict transversal histogram

```text
3:3, 4:8, 5:25, 6:84, 7:163, 8:240,
9:15, 10:37, 11:123, 12:135, 13:135, 14:64.
```

The three minimum-three and eight minimum-four attempts contain ninety-three
minimum cores in total.

#### Proof

`scripts/check_boundary_thirteenth_spectrum.cpp` reconstructs the ninety-six-
point state, forms every old-old-new and old-new-new collinear triple, and solves
the minimum hitting-set problem exactly for every block type and offset in
`[-64,64]`.  The displayed histogram sums to 1,032. ∎

## 2. Complete correction census for the best cores

### Theorem PP3cyy — PROVED / ALL NINETY-THREE CORES CORRECT

Every minimum core in the eleven attempts of transversal number at most four
admits a row-and-column-preserving legal refill with total deletion size at most
seven.  The exact minimum-budget distribution is

```text
4:19, 5:45, 6:26, 7:3.
```

#### Proof

`scripts/check_boundary_thirteenth_corrections.cpp` enumerates all ninety-three
cores, every enlargement through budget seven, and every exact row-column refill,
with retained-pair and final determinant checks.  Every core succeeds. ∎

## 3. A corrected thirteen-block state

### Theorem PP3cyz — PROVED / FOUR-POINT THIRTEENTH TRANSITION

Choose block `P0` at offset `56`.  One minimum-four core has correction

```text
delete:
(18,75), (40,193), (50,316), (51,315)

add:
(18,316), (40,315), (50,193), (51,75).
```

The corrected state has 104 distinct points, no collinear triple, and thirteen
blocks.  None of the 1,032 raw fourteenth attempts in radius `64` is legal.

#### Proof

The row and column multisets agree exactly.  The wrapper
`scripts/check_boundary_thirteenth_transition.py` reconstructs the state,
verifies all determinants, and tests every raw fourteenth attempt. ∎

## Consequence

The canonical corrected path now reaches thirteen blocks.  This remains a
bounded radius-64 path: no corrected fourteenth transition, recurrence theorem,
or periodic corrected-state component is known.
