# The binary-cluster separation factor

CMR71 localizes the logarithmic first-separation loss to triples whose closest
p-adic column pair lies in one layer. The local reciprocal parameter at the
pair's actual separation node supplies one additional independent factor. Exact
p-adic clustering counts then remove the factor `p` from the logarithmic term.

Continue with the corrected balanced saturated bank for

\[
N=p^k,
\qquad
p\equiv1\pmod4,
\qquad
h=(p-1)/2.
\]

Write

\[
\tau(0)=0,
\qquad
\tau(x)=x^{-1}\quad(x\ne0),
\]

so every local map has the form

\[
F_{b,c}(x)=b+c\tau(x)\pmod p.
\]

## 1. The closest-pair separation digit

Fix a nontransverse triple with

\[
r=\min_{i<j}v_p(x_i-x_j)
<
s=\max_{i<j}v_p(x_i-x_j).
\]

Its unique closest pair has valuation `s` and uses one common layer. The two
columns share a prefix modulo `p^s` and have distinct depth-`s` digits
`xi_1,xi_2`. Notice that `s>=1`, so this separation node is never the coupled
root node.

### Theorem CMR73 — PROVED

For a fixed nontransverse binary-cluster triple,

\[
\Pr(\Delta\equiv0\pmod N)
\le
\frac1h\,p^{-(k-s-1)}.
\]

The same bound holds for real collinearity.

### Proof

Divide the determinant coefficients by their common minimum power `p^r`. The
unit coefficients are exactly those attached to the two endpoints of the
closest pair, and modulo `p` they are opposites. The third coefficient is zero
modulo `p`.

At row-digit depth `s`, the closest pair uses one common layer-prefix node but
enters it through the two distinct column digits `xi_1,xi_2`. Conditional on all
lower digits and every other depth-`s` node, the next determinant congruence has
the form

\[
C+u\bigl(F_{b,c}(\xi_1)-F_{b,c}(\xi_2)\bigr)
\equiv0\pmod p,
\]

where `u` is a unit. The shift `b` cancels, while

\[
F_{b,c}(\xi_1)-F_{b,c}(\xi_2)
=
c\bigl(\tau(\xi_1)-\tau(\xi_2)\bigr).
\]

The completed inverse `tau` is a permutation, so the final parenthesis is
nonzero. Therefore at most one nonsquare parameter `c` can satisfy the
congruence. Since `c` is uniform on `h` values, the separation depth costs a
factor `1/h`.

At every depth above `s`, the three column prefixes are distinct. CMR68 supplies
`k-s-1` independent factors of `1/p`. ∎

## 2. Exact p-adic clustering populations

There are two nontransverse column patterns.

### Equilateral clusters

If all three pair valuations equal `s`, the columns share one prefix modulo
`p^s` and occupy three distinct children at depth `s`. Put

\[
L=p^{k-s-1}.
\]

The number of unordered column triples of this type is exactly

\[
E_s
=
p^s\binom p3L^3
=
\binom p3\frac{N^3}{p^{2s+3}}.
\]

Only the two monochromatic layer assignments are nontransverse. CMR68 bounds
each by `p^{-(k-s-1)}`. Hence their total expected contribution over all levels
is less than

\[
\begin{aligned}
2\sum_{s=0}^{k-1}E_s p^{-(k-s-1)}
&=
\frac{2\binom p3}{p^2}N^2
\sum_{s=0}^{k-1}p^{-s}\\
&<
\frac{p-2}{3}N^2.
\end{aligned}
\]

### Binary clusters

For `s>=1`, the number of unordered column pairs with exact valuation `s` is

\[
P_s
=
p^s\binom p2L^2
=
\frac{hN^2}{p^{s+1}}.
\]

Every triple with a unique closest pair of valuation `s` is obtained from one
such pair and a third column, so there are fewer than `P_sN` column triples of
this type. There are four layer assignments in which the closest pair uses one
common layer. CMR73 therefore gives expected mass at most

\[
4P_sN\frac1h p^{-(k-s-1)}
=
4N^2
\]

at every binary valuation level. There are at most `k-1` such levels.

## 3. Sharpened first-separation sum

### Corollary CMR74 — PROVED

The corrected balanced recursive bank satisfies

\[
\mathbb E T_k
<
4(k-1)N^2
+
\left(
\frac{p-2}{3}
+
\frac{4p}{3(p-1)}
\right)N^2.
\]

In particular, for `p>=5`,

\[
\mathbb E T_k
<
4(k-1)N^2+rac{p+3}{3}N^2.
\]

The same bounds hold for the number of determinant-zero-modulo-`N` triples with
three distinct columns.

Consequently the bank contains a saturated state with

\[
T_k=O(N^2\log_pN)
\]

whose logarithmic coefficient is absolute rather than proportional to `p`.

### Proof

CMR70--CMR71 bound all layer-transverse triples by less than

\[
\frac{4p}{3(p-1)}N^2
\]

in expectation. The equilateral nontransverse clusters contribute less than
`(p-2)N^2/3`. The binary nontransverse clusters contribute at most `4N^2` at
each of at most `k-1` valuations. Adding the three terms proves the first bound.
Since `4/(p-1)<=1`, the second follows.

All arguments impose successive determinant congruences, so the same calculation
bounds modular determinant-zero triples with three distinct columns. ∎

The remaining logarithm comes from binary same-layer stars: one close pair at
scale `s`, together with a third point outside that pair's prefix block.
Equilateral clusters and every layer-transverse pattern have only quadratic
total mass.

The exact clustering formulas are checked in
[`scripts/verify_prime_power_binary_clusters.py`](../scripts/verify_prime_power_binary_clusters.py).
