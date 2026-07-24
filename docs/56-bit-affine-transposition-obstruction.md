# Bit-affine obstruction for the recursive transposition class

PX65 identifies the all-transposition relative class as the canonical output of
every successful rectangle template.  PX66 rules out the ordinary affine group
on `Z/8Z` for the first unresolved recursive case.  This chapter enlarges that
map family to a genuinely non-affine structured group on eight symbols.

Identify the eight fine labels with the vectors of `F_2^3`.  Let

\[
G_{\rm bit}
=
F_2^3\rtimes S_3,
\]

where the translation subgroup acts by bitwise XOR and `S_3` permutes the three
binary coordinates.  Thus

\[
|G_{\rm bit}|=8\cdot6=48.
\]

Many elements of `G_bit` are nonlinear when the labels are viewed in the
ordinary order `0,1,...,7`; hence this family is not contained in the failed
ordinary affine group from PX66.

Fix the all-transposition representative

\[
H=(1,0,3,2,5,4,7,6).
\]

For every orientation and every

\[
(T,Q)\in G_{\rm bit}^2,
\]

use the row-pattern normal form of PX65--PX66.  The exact selector search absorbs
all `8!` choices of `P` while considering every spanning degree-two state.

## Theorem PX71 -- PROVED FINITE

No bit-affine column geometry for the side-eight all-transposition relative
class contains a no-three spanning degree-two state, even when `P` is arbitrary.

The complete deterministic search data are:

| Orientation | `(T,Q)` pairs | Search nodes | Maximum nodes in one geometry |
|---|---:|---:|---:|
| `cc` | 2,304 | 29,420,820 | 134,675 |
| `cf` | 2,304 | 32,968,556 | 158,842 |
| `fc` | 2,304 | 69,724,372 | 851,765 |
| `ff` | 2,304 | 104,925,268 | 614,254 |

### Proof

The group generator exhausts every XOR translation followed by every
permutation of the three binary coordinates, producing exactly 48 distinct
permutations.  For each ordered pair `(T,Q)` and orientation, run the exact
row-pattern backtracker from PX66.

The first coarse row block has fixed abstract patterns.  In the second coarse
row block, choosing an unused pattern for each scalar row is exactly the choice
of an arbitrary `P`.  Each row then chooses two of its four host cells.  The
search tracks scalar column degrees and rejects a branch exactly when a new
cell completes an integer-determinant zero with two previously selected cells.
Every one of the 9,216 geometries is exhausted before 32 cells are selected.
\(\square\)

## Consequence

The failed ordinary affine family was not merely missing XOR-type nonlinear
maps.  Any successful `8 -> 16` full-selector recurrence for the transposition
class must leave both of the following controlled groups:

1. the 32-element affine group of the ring `Z/8Z`;
2. the 48-element bit-affine group `F_2^3 semidirect S_3`.

The complete vector-affine group `AGL(3,2)` has order 1,344 and remains too large
for a direct square census with the current exact solver.  Deterministic broad
sampling in that group and in the full symmetric group has not produced a
witness, but those samples are not obstruction theorems and are therefore not
recorded as proved results.

Together with PX67--PX70, this shifts the general route away from successively
larger small map groups and toward a direction-aware matching or sparse-repair
theorem.

## Verification

Run

```bash
python scripts/verify_product_bit_affine_transposition_eight.py
```

The harness compiles the exact C++ solver and checks every orientation total and
maximum node count.