# Protected trades from discrete tomography

## 1. Difference operators

For \(w\in\mathbb Z^2\), let \(T_w\) translate a finitely supported function and define

\[
\Delta_w=I-T_w.
\]

If \(w\) is parallel to direction \(d\), then \(\Delta_wf\) has zero sum on every line parallel to \(d\).

Therefore

\[
\prod_{d\in\mathcal D}\Delta_{w_d}f,
\qquad w_d\parallel d,
\]

has zero line sums in every protected direction.

## 2. Protected rectangle completion

For an ordinary alternating rectangle

\[
g^\square=-\mathbf1_{(x,y)}-\mathbf1_{(u,v)}+
\mathbf1_{(x,v)}+
\mathbf1_{(u,y)},
\]

define

\[
G=\prod_{d\in\mathcal D}\Delta_{w_d}g^\square.
\]

### Theorem T1 — PROVED

\(G\) has zero row sums, zero column sums, and zero line sums in every direction in \(\mathcal D\).

This is a formal signed trade.

## 3. Binary separation

Choose scaled direction vectors \(w_i=s_id_i\) so that all subset sums have distinct first coordinates and distinct second coordinates. If the original rectangle displacement avoids the finite subset-difference sets, the translated rectangles are row- and column-disjoint.

### Theorem T2 — PROVED

Under this separation condition:

- all coefficients of \(G\) are \(\pm1\);
- positive and negative supports are disjoint partial permutations;
- each support has \(2^{|\mathcal D|+1}\) cells;
- the supports have identical row, column, and protected-direction line sums.

The bank of formally nondegenerate partners has size \(n-O_{\mathcal D}(1)\) for an interior target.

### Limitation

The negative support of the completed trade need not already be selected. Formal abundance does not imply executable absorber abundance.

## 4. Colour-cube states

Include rows and columns among the protected directions. Choose separated scaled vectors \(w_1,\ldots,w_s\), a prime \(k\), and colour

\[
z_\alpha=\sum_i\alpha_iw_i,
\qquad
c(\alpha)=\sum_i\lambda_i\alpha_i\pmod k.
\]

### Theorem T3 — PROVED

Each protected line in direction \(d_j\) through the cube contains exactly one point of every colour. Hence every colour class is a partial permutation and all colour classes have identical protected line sums.

Unions of any two colour classes are local saturated states with two points on every occupied protected line.

### Remaining installation problem

The colour cube gives exact local states, but a global saturated configuration containing a positive density of these gadgets must still be constructed. The subgroup absorber pathway solves this installation problem for certain arithmetic moduli.
