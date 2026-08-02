# Exact side-seven radius-one coordinate obstruction

PX512--PX514 turn simple alternating-cycle flips into a complete selector move
language and identify exactly `1748` selectors at distance one from the four
certified side-seven centres.  This chapter applies the full coordinate CSP to
that entire layer.

The result is negative: no radius-one selector embeds as a no-three
configuration in any of the four radix orientations.  This is the first exact
selector-changing obstruction beyond the fixed-selector coordinate orbits of
PX504--PX507.

## 1. Incremental dangerous-point masks

For one fixed selector and orientation, the coordinate variables are the three
permutations

\[
A_0,A_1,R\in\operatorname{Sym}([7]),
\]

where `A_0,A_1` order the two abstract column parts and `R` orders the bottom
row part.  There are therefore `21` permutation variables.

At a partial assignment, call a scalar grid point **dangerous** if it lies on a
line through two already completed selected points.  Store the dangerous set as
four 64-bit words over the `196` points of `[14]^2`.

### Lemma PX515 -- PROVED

The dangerous-mask recursion rejects exactly the same partial assignments as
full determinant rescanning.

When one coordinate variable is assigned, at most two selected points become
complete.  A new point is admissible exactly when:

1. it is not in the current dangerous mask; and
2. if two points become complete simultaneously, the second does not lie on a
   line through the first and one previously completed point.

After accepting the new points, update the mask by adjoining every line through
one new point and one earlier completed point, and the line through the two new
points when both appear.

### Proof

Every newly created collinear triple contains at least one newly completed
point.  If it contains exactly one, that point lies on a line through two old
points and is detected by the existing dangerous mask.  If it contains both
new points, its third point is old and is detected by the second test.  No other
triple can become newly complete.  Conversely every rejection is an actual
zero determinant.  Induction on the number of assigned variables proves exact
equivalence. \(\square\)

This changes only the implementation cost; the search tree and variable-order
rule remain exact.

## 2. Sharded radius-one census

The four radius-one layers have sizes

\[
1092,\qquad364,\qquad180,\qquad112.
\]

Each selector is tested in all four radix orientations.  The deterministic
ordered selector sets are split into reproducible contiguous shards.

### Theorem PX516 -- PROVED FINITE

The exact coordinate-CSP node totals are:

| Relative class | Radius-one selectors | CSP nodes | Feasible selectors |
|---|---:|---:|---:|
| `(7)` | 1,092 | 749,452,110 | 0 |
| `(5,2)` | 364 | 237,531,638 | 0 |
| `(4,3)` | 180 | 155,634,538 | 0 |
| `(3,2,2)` | 112 | 59,379,166 | 0 |
| **Total** | **1,748** | **1,201,997,452** | **0** |

Every node uses only permutation-domain tests, bit-mask line updates, and exact
integer collinearity.

### Proof

PX514 supplies the exact neighbour sets.  For each selector and each of the four
orientations, run the PX515 recursion until either a complete assignment is
found or every branch is rejected.  The verifier asserts the node count of each
shard independently.  Summing the shard certificates gives the displayed
class and total counts.  No shard returns a complete assignment. \(\square\)

### Corollary PX517 -- PROVED FINITE

No simple alternating-cycle neighbour of any certified side-seven centre has a
no-three coordinate embedding.

Equivalently, the complete selector-changing radius-one layer is empty of
side-seven product certificates.

## 3. Exact distance boundary

### Corollary PX518 -- PROVED REDUCTION

If a side-seven full-selector template exists in any of the four canonical
relative classes, then its abstract selector has alternating-cycle graph
distance at least two from the corresponding certified centre.

PX512 gives graph diameter at most fourteen, so a breadth-first selector search
remains complete.  The next exact layer is radius two, with coordinate pruning
shared across selectors that have a common radius-one parent.

This is not a proof that universal

\[
2\times7\longrightarrow14
\]

fails.  It proves that neither coordinate reordering nor one selector-cycle
change reaches a certificate from the four current centres.

## 4. Verification

Compile

```bash
g++ -O3 -std=c++17 scripts/verify_product_side_seven_radius_one_csp.cpp \
  -o /tmp/side7_radius1
```

Run every shard:

```bash
for shard in {0..11}; do /tmp/side7_radius1 cycle7 "$shard"; done
for shard in {0..7};  do /tmp/side7_radius1 cycle52 "$shard"; done
for shard in {0..3};  do /tmp/side7_radius1 cycle43 "$shard"; done
/tmp/side7_radius1 cycle322 0
```

The shard sizes and expected node totals are embedded in the verifier.  Every
case independently regenerates the exact radius-one selector set before running
the coordinate CSP.
