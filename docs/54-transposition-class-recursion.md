# Transposition-class recursion and the side-eight affine-column obstruction

PX63 gives an all-side low-syndrome rectangle state. This chapter records a
second structural feature of the rectangle family: whenever a rectangle state
is exact no-three, its output factor belongs to one fixed relative cycle class.
That class is therefore the natural first target for recursive doubling.

The chapter then closes the largest controlled side-eight search currently
available for that class. Affine column labelings do not suffice, even when the
second row-block labeling and the complete degree-two selector are arbitrary.

## 1. Relative type of every rectangle output

Let

\[
Q(p,t,r)=\bigcup_{u\in[n]}
\{X_0(u),X_1(p(u))\}
\times
\{Y_0(t(u)),Y_1(r(u))\}
\]

be any rectangle state from PX43.

### Theorem PX65 -- PROVED

The row-column incidence graph of `Q(p,t,r)` is the disjoint union of `n`
4-cycles. Consequently every decomposition of the state into two permutation
layers has relative permutation of cycle type

\[
\boxed{(2,2,\ldots,2)}
\]

with exactly `n` transpositions.

### Proof

For a fixed index `u`, the state contains all four edges between the two scalar
rows

\[
X_0(u),\qquad X_1(p(u))
\]

and the two scalar columns

\[
Y_0(t(u)),\qquad Y_1(r(u)).
\]

This is one copy of `K_(2,2)`, hence one 4-cycle. Because `p,t,r` are
permutations, different indices use disjoint scalar rows and disjoint scalar
columns. The complete incidence graph is therefore the disjoint union of these
cycles.

A two-edge-colouring of one 4-cycle into perfect matchings alternates around the
cycle. Comparing the two matching layers swaps its two row vertices. Thus each
rectangle contributes one 2-cycle to the relative permutation, and the
components are disjoint. \(\square\)

### Corollary PX65a -- PROVED

A successful rectangle template at base side `n` produces a side-`2n` factor in
the all-transposition relative class. Recursive use of the rectangle pathway
therefore needs only a full-selector closure theorem for this output class, not
a universal theorem for every relative cycle type at side `2n`.

For example, the exact side-four and side-five rectangle templates produce the
relative types `(2,2,2,2)` at side eight and `(2,2,2,2,2)` at side ten.

## 2. Absorbing the row-relative permutation

Use the three-labeling normal form PX61. Fix a relative permutation `H`, a
target labeling `T`, and a second-column relative labeling `Q`. Put

\[
A=T,\qquad B=QT.
\]

The first coarse row block has the `n` fixed abstract row patterns

\[
\{A(u),A(Hu),B(u),B(Hu)\},
\qquad u\in[n].
\]

The second coarse row block has the same `n` patterns. The permutation `P`
only assigns those patterns bijectively to the `n` scalar rows in that block.

Thus an exact selector search may choose `P` inside the row-by-row backtracking:
when a second-block scalar row is exposed, choose one unused abstract pattern
and then choose two of its four incident columns. This covers every
`P in Sym([n])` without enumerating `n!` separate hosts.

## 3. Side-eight all-transposition class

Take

\[
H_{2^4}=(1,0,3,2,5,4,7,6)
\]

and the affine permutation group on `Z/8Z`

\[
A_8=
\{x\mapsto ax+b\pmod8:
 a\in\{1,3,5,7\},\ b\in\mathbb Z/8\mathbb Z\}.
\]

It has order `32`.

For each orientation and every pair

\[
(T,Q)\in A_8^2,
\]

run the exact row-pattern search above, allowing:

- every `P in S_8` through pattern assignment;
- every spanning degree-two selector;
- every real-grid collinearity constraint.

There are only

\[
4\cdot32^2=4096
\]

labeled column geometries, but each search represents all `8!` row labelings.

### Theorem PX66 -- PROVED FINITE

No affine-column geometry for the side-eight all-transposition relative class
contains a no-three spanning degree-two state, even when `P` is arbitrary.

The complete exact search data for the committed deterministic branch order are:

| Orientation | `(T,Q)` pairs | Search nodes | Maximum nodes in one geometry |
|---|---:|---:|---:|
| `cc` | 1,024 | 5,352,870 | 49,571 |
| `cf` | 1,024 | 6,894,433 | 37,471 |
| `fc` | 1,024 | 9,863,816 | 206,093 |
| `ff` | 1,024 | 11,574,689 | 82,500 |

### Proof

For fixed `(T,Q,theta)`, process all sixteen scalar rows. In the first coarse
row block the abstract pattern is fixed. In the second block choose an unused
abstract pattern, which simultaneously chooses the value of `P` on that scalar
row. Then choose two of the four incident columns.

Track scalar column degrees, prune when the remaining rows cannot complete a
column to degree two, and reject a branch exactly when its newly inserted cells
complete an integer-determinant zero with two previously selected cells.
Exhaustion before selecting 32 points proves infeasibility for that geometry.
The 1,024 pairs in each row of the table exhaust `A_8^2`; the pattern assignment
exhausts every `P`. \(\square\)

This result strictly strengthens the direct affine census in which `P` was also
required to be affine. Search-node totals depend on the deterministic branch
order, while infeasibility does not.

## 4. Consequences for a recursive proof

PX65 identifies the all-transposition class as the canonical output of every
rectangle template. PX66 shows that the first unresolved recursive instance,
side eight, cannot be solved by keeping both column labelings affine and hiding
all nonlinearity in `P`.

Therefore a successful `8 -> 16` full-selector recurrence must use at least one
of the following.

1. A genuinely non-affine first-column labeling `T`.
2. A genuinely non-affine relative column labeling `Q`.
3. A larger structured map group with a non-affine double coset.
4. A repair/resampling theorem applied to the universal low-syndrome seed PX63.

PX66 does **not** rule out an arbitrary-map full-selector template for the
all-transposition class. That remains the exact finite recursion target.

## Verification

Run

```bash
python scripts/verify_product_transposition_class_eight.py
```

The harness compiles the exact C++ row-pattern solver and checks all four
orientation totals and maximum search-node counts.
