# Exact obstruction to completing the 64-point digital layer

CMR12 gives a binary digit-linear no-three permutation on the `64` by `64`
grid. This chapter proves that this particular layer cannot be extended to a
saturated `128`-point no-three configuration by any second permutation.

Let `F` be the CMR12 permutation with row masks

```text
25, 8, 2, 11, 52, 28
```

and let

\[
S_F=\{(x,F(x)):0\le x<64\}.
\]

## 1. Candidate cells for a second layer

A cell `(x,y)` is called **admissible** when

1. `y` is not `F(x)`;
2. `(x,y)` does not lie on a real line through two points of `S_F`.

Any second layer in a no-three completion must use only admissible cells. The
exact enumeration contains `390` admissible cells, with between `3` and `13`
in every column. The admissible bipartite graph does have perfect matchings, so
ordinary Hall feasibility is not the obstruction.

For a real line `L` containing exactly one point of `S_F`, a valid second layer
may use at most one admissible cell on `L`; otherwise those two cells and the
fixed point form a mixed triple.

## 2. Integer covering certificate

The verifier stores three finite collections of nonnegative integer weights:

- one weight `r_x` for selected grid column `x`;
- one weight `c_y` for selected grid row `y`;
- one weight `w_L` for each of `122` listed lines containing exactly one fixed
  point.

The scale is

\[
D=500.
\]

The stored weights satisfy two exact properties.

### Cell coverage

For every admissible cell `(x,y)`,

\[
r_x+c_y+\sum_{L\ni(x,y)}w_L\ge501>D.
\]

### Capacity cost

Every second permutation uses at most one cell in each column, at most one in
each row, and at most one on every listed line. The total weighted capacity is

\[
\sum_xr_x+\sum_yc_y+\sum_Lw_L=31718<64D=32000.
\]

### Theorem CMR44 — PROVED BY EXACT FINITE CERTIFICATE

There is no permutation `G` of `[64]` such that

\[
S_F\cup\{(x,G(x)):0\le x<64\}
\]

contains no real collinear triple.

In fact, no second permutation can simultaneously avoid triples containing two
fixed points and triples containing one fixed point and two second-layer
points.

### Proof

Assume that such a second permutation exists. Its `64` selected cells are all
admissible. Summing the cell-coverage inequality over those cells gives

\[
64D
\le
\sum_{(x,y)\text{ selected}}
\left(r_x+c_y+\sum_{L\ni(x,y)}w_L\right).
\]

Because the cells form a permutation, every column and every row is used once.
Because the completion has no mixed triple, every listed one-fixed-point line
is used at most once. Therefore the right side is at most

\[
\sum_xr_x+\sum_yc_y+\sum_Lw_L=31718.
\]

But `64D=32000`, a contradiction. ∎

## 3. Significance

This is stronger than a failed bounded search. The obstruction is an exact
integer Farkas certificate checked using only standard-library arithmetic.
No assumption is made about collinear triples lying entirely in the proposed
second layer.

Thus the digital branch must replace the CMR12 first layer itself, permit a
joint two-layer search from the outset, or move to a nonlinear recursive digit
family. The question “complete the current 64-point layer” is closed
negatively.

The certificate checker is
[`scripts/verify_digital_64_completion_obstruction.py`](../scripts/verify_digital_64_completion_obstruction.py).
