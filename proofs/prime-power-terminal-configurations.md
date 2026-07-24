# Exact companion-offset terminal configurations

The terminal block obstruction CMR23 concerns the unrestricted uniform
permutation measure. It can be removed for several prime bases by fixing an
exact local two-layer state.

Let \(p\) be an odd prime, \(k\ge2\), and

\[
a=p^{k-1}.
\]

For permutations \(P,Q\) of \(\{0,\ldots,p-1\}\), define

\[
S_{p,k}(P,Q)
=
\{(ja,aP(j)):0\le j<p\}
\cup
\{(ja,1+aQ(j)):0\le j<p\}.
\]

The first row set is the terminal completed-reciprocal row block, and the
second is its companion row block.

## Theorem CMR24 — PROVED BY EXHAUSTIVE FINITE CHECK

For every

\[
p\in\{3,5,7,11,13,17,19,23,29,31\}
\]

and every \(k\ge2\), the permutations in the following table make
\(S_{p,k}(P,Q)\) an executable two-layer terminal state with one cell from
each layer in every terminal column, each prescribed row block used exactly
once, and no real collinear triple.

| \(p\) | \(P(0),\ldots,P(p-1)\) | \(Q(0),\ldots,Q(p-1)\) |
|---:|---|---|
| 3 | `1,0,2` | `0,2,1` |
| 5 | `1,4,0,3,2` | `2,3,1,0,4` |
| 7 | `4,5,3,0,1,6,2` | `2,1,5,6,0,3,4` |
| 11 | `8,6,3,9,7,0,2,10,4,1,5` | `2,9,3,7,0,6,1,10,5,8,4` |
| 13 | `6,2,1,4,9,3,0,11,8,7,12,10,5` | `1,10,12,7,4,3,9,5,2,8,11,0,6` |
| 17 | `12,8,13,16,2,15,6,3,7,0,9,5,10,14,4,11,1` | `12,14,7,3,15,11,6,10,0,1,4,5,16,8,9,2,13` |
| 19 | `5,7,12,18,1,17,6,13,8,14,9,3,16,4,15,0,2,10,11` | `7,11,18,10,1,14,17,6,3,2,5,16,13,15,8,0,12,9,4` |
| 23 | `7,19,10,2,4,16,22,12,15,3,13,21,18,6,8,1,5,0,17,11,9,14,20` | `4,12,15,22,2,0,8,6,18,1,5,3,17,21,19,9,14,11,20,10,16,7,13` |
| 29 | `26,12,2,16,10,18,25,7,14,19,22,8,5,0,4,23,21,9,11,17,27,15,24,28,3,6,20,1,13` | `16,24,14,12,4,19,20,22,25,15,8,7,21,28,0,13,6,2,23,10,1,17,5,9,18,26,11,3,27` |
| 31 | `21,26,1,13,8,15,7,0,28,9,18,22,2,19,17,6,25,30,14,5,27,29,24,16,10,20,11,23,3,12,4` | `4,14,25,10,28,8,19,23,13,1,20,12,11,24,18,27,0,7,29,2,26,16,9,5,22,17,3,21,15,30,6` |

### Why checking \(k=2\) is sufficient

Represent a selected point as

\[
(ax,ay+arepsilon),
\qquad arepsilon\in\{0,1\}.
\]

For any triple, its exact determinant has the form

\[
\Delta_a=a(aD+E),
\]

where \(D\) is the determinant of the integer pairs \((x,y)\), while

\[
E=(x_2-x_1)(\varepsilon_3-\varepsilon_1)
 -(x_3-x_1)(\varepsilon_2-\varepsilon_1).
\]

Because the layer indicators are binary, either \(E=0\) or \(E\) is the
difference of two column indices in one layer. Hence

\[
|E|\le p-1.
\]

The verifier checks \(\Delta_p\neq0\) for every triple. If \(D=0\), this implies
\(E\neq0\), so the determinant is nonzero for every `a`. If \(D\neq0\) and
\(a=p^{k-1}\ge p^2\), then

\[
|aD|\ge p^2>p-1\ge|E|,
\]

so \(aD+E\neq0\). Thus the check at \(k=2\) proves all \(k\ge2\).

Each layer bijects the terminal columns to its prescribed `p`-point row block,
and the two row blocks are disjoint modulo `a`. The state is therefore
compatible with the global two-layer saturation constraints. It is not, by
itself, a row-saturated subgrid.

## Consequence

For the listed prime bases, the terminal block may be fixed to a no-three
state rather than sampled uniformly. The remaining all-stratum bank then
moves every nonterminal block in both layers, and its certificate mass contains
no terminal-internal triples.

This is finite prime-base coverage, not an all-primes theorem. A scalable
terminal construction or a spread distribution supported on terminal
no-three states remains open.

The exact check is implemented in
[`scripts/verify_prime_power_terminal_configurations.py`](../scripts/verify_prime_power_terminal_configurations.py).
