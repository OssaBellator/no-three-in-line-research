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

### Verification

For each row of the table, the verifier checks:

1. both lists are permutations of \([N]\);
2. \(p_N(x)\ne q_N(x)\) for every column \(x\);
3. every row and column occurs exactly twice in the union;
4. for all \(\binom{2N}{3}\) triples of selected points, the integer determinant

   \[
   (x_2-x_1)(y_3-y_1)-(x_3-x_1)(y_2-y_1)
   \]

   is nonzero.

The check is implemented in
[`scripts/verify_composite_modulus.py`](../scripts/verify_composite_modulus.py)
and uses exact integer arithmetic only.

These constructions complete five finite composite cases of CM6. They do not
supply a scalable construction or an admissible modulus class.
