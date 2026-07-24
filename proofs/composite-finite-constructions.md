# Finite composite saturated constructions

This file records explicit finite base cases for the composite-modulus track.
No algebraic pattern is claimed.

For a permutation \(p\) of \(\{0,\ldots,N-1\}\), write

\[
G(p)=\{(x,p(x)):0\le x<N\}.
\]

## Theorem CMF1 — PROVED BY EXHAUSTIVE FINITE CHECK

For each

\[
N\in\{4,6,8,9,10\},
\]

the two permutations in the following table are pointwise disjoint, and
\(G(p_N)\cup G(q_N)\) contains exactly two points in every row and column and
no real collinear triple.

| \(N\) | \(p_N(0),\ldots,p_N(N-1)\) | \(q_N(0),\ldots,q_N(N-1)\) |
|---|---|---|
| 4 | `2, 0, 3, 1` | `0, 2, 1, 3` |
| 6 | `4, 3, 5, 0, 2, 1` | `3, 1, 0, 5, 4, 2` |
| 8 | `3, 6, 7, 1, 0, 5, 2, 4` | `2, 0, 3, 7, 1, 4, 6, 5` |
| 9 | `1, 2, 7, 5, 0, 3, 8, 4, 6` | `6, 0, 8, 3, 7, 5, 1, 2, 4` |
| 10 | `8, 3, 7, 5, 1, 9, 0, 2, 6, 4` | `5, 2, 8, 3, 0, 6, 9, 4, 7, 1` |

These five cases are checked in
[`scripts/verify_composite_modulus.py`](../scripts/verify_composite_modulus.py).

## Theorem CMF2 — PROVED BY EXHAUSTIVE FINITE CHECK

At side length

\[
N=12,
\]

the permutations

```text
p_12 = 0, 2, 6, 5, 10, 11, 1, 8, 4, 3, 9, 7
q_12 = 5, 9, 11, 7, 1, 2, 0, 10, 6, 8, 3, 4
```

are pointwise disjoint, and their two graphs form a saturated no-three
configuration.

The configuration was obtained as a zero-objective integer-feasibility solve
with one binary variable per grid cell, exact degree-two constraints on every
row and column, and an at-most-two constraint on every real grid line
containing at least three cells. The recorded permutations are the complete
certificate; no optimizer is needed for verification.

### Verification

For every recorded construction, the exact checker verifies:

1. both lists are permutations of `[N]`;
2. the two values in every column are distinct;
3. every row and column occurs exactly twice;
4. for all \(\binom{2N}{3}\) triples, the integer determinant
   \[
   (x_2-x_1)(y_3-y_1)-(x_3-x_1)(y_2-y_1)
   \]
   is nonzero.

CMF2 is checked in
[`scripts/verify_composite_finite_extensions.py`](../scripts/verify_composite_finite_extensions.py).

These constructions supply finite CM6 coverage only. They do not give a
scalable construction or an admissible modulus class.
