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

A cell `(x,y)` is **admissible** when `y` is not `F(x)` and it does not lie on
a real line through two points of `S_F`. Any second layer in a no-three
completion must use only admissible cells. Exact enumeration gives `390`
admissible cells, with between `3` and `13` in every column. Their bipartite
graph has perfect matchings, so ordinary Hall feasibility is not the
obstruction.

For a real line `L` containing exactly one point of `S_F`, a valid second layer
may use at most one admissible cell on `L`.

## Integer covering certificate

The verifier stores nonnegative integer weights:

- one weight `r_x` for selected grid columns;
- one weight `c_y` for selected grid rows;
- one weight `w_L` for each of `122` listed one-fixed-point lines.

With scale

\[
D=500,
\]

they satisfy:

1. every admissible cell `(x,y)` has coverage
   \[
   r_x+c_y+\sum_{L\ni(x,y)}w_L\ge501>D;
   \]
2. the total capacity cost is
   \[
   \sum_xr_x+\sum_yc_y+\sum_Lw_L=31718<64D=32000.
   \]

### Theorem CMR55 — PROVED BY EXACT FINITE CERTIFICATE

There is no permutation `G` of `[64]` such that

\[
S_F\cup\{(x,G(x)):0\le x<64\}
\]

contains no real collinear triple.

In fact, no second permutation can simultaneously avoid triples containing two
fixed points and triples containing one fixed point and two second-layer
points.

### Proof

Assume such a second permutation exists. Its `64` cells are admissible. Summing
the cell-coverage inequality over them gives a lower bound of `64D`.

Every grid column and row is used once, and every listed one-fixed-point line
is used at most once. Hence the same sum is at most the total capacity cost
`31718`, contradicting `64D=32000`. ∎

This is an exact integer Farkas certificate, not a failed bounded search. No
assumption is made about triples lying entirely in the proposed second layer.
The digital branch must replace the CMR12 first layer or search jointly for two
layers.

The checker is
[`scripts/verify_digital_64_completion_obstruction.py`](../scripts/verify_digital_64_completion_obstruction.py).
