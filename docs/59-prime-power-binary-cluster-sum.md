# The binary-cluster separation factor

CMR71 localizes the logarithmic first-separation loss to triples whose closest
p-adic column pair lies in one layer. The local reciprocal parameter at the
pair's separation node supplies one additional independent factor. Exact
clustering counts then remove the factor `p` from the logarithmic term.

Continue with the corrected balanced saturated bank for

\[
N=p^k,
\qquad p\equiv1\pmod4,
\qquad h=(p-1)/2.
\]

Write

\[
\tau(0)=0,
\qquad
\tau(x)=x^{-1}\quad(x\ne0),
\]

so every local map is

\[
F_{b,c}(x)=b+c\tau(x)\pmod p.
\]

## 1. The closest-pair separation digit

Fix a nontransverse binary cluster with

\[
r=\min_{i<j}v_p(x_i-x_j)
<
s=\max_{i<j}v_p(x_i-x_j).
\]

Its unique closest pair has valuation `s` and uses one layer. Its two columns
share a prefix modulo `p^s` and have distinct depth-`s` child digits
`xi_1,xi_2`. Necessarily `s>=1`, so the separation node is nonroot.

### Theorem CMR73 — PROVED

For a fixed nontransverse binary-cluster triple,

\[
\Pr(\Delta\equiv0\pmod N)
\le
\frac1h\,p^{-(k-s-1)}.
\]

The same bound holds for real collinearity.

### Proof

After dividing the determinant coefficients by their common minimum power of
`p`, the unit coefficients are exactly those of the closest pair and are
opposites modulo `p`. At depth `s`, their common node contributes

\[
C+u\bigl(F_{b,c}(\xi_1)-F_{b,c}(\xi_2)\bigr)
\equiv0\pmod p,
\]

where `u` is a unit. The shift cancels and

\[
F_{b,c}(\xi_1)-F_{b,c}(\xi_2)
=
c\bigl(\tau(\xi_1)-\tau(\xi_2)\bigr).
\]

Since completed inversion is a permutation, the final factor is nonzero. At
most one of the `h` nonsquare values of `c` works, giving `1/h`. At every depth
above `s`, CMR68 supplies one independent factor `1/p`. ∎

## 2. Exact p-adic clustering populations

### Equilateral clusters

If all three pair valuations equal `s`, the columns share one prefix modulo
`p^s` and occupy three distinct children at depth `s`. Put

\[
L=p^{k-s-1}.
\]

The exact number of unordered column triples is

\[
E_s
=
p^s\binom p3L^3
=
\binom p3\frac{N^3}{p^{2s+3}}.
\]

Only the two monochromatic layer assignments are nontransverse. CMR68 gives
combined expected mass

\[
\begin{aligned}
2\sum_{s=0}^{k-1}E_sp^{-(k-s-1)}
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

Every unique-closest-pair triple is obtained from one such pair and a third
column, so there are fewer than `P_sN` column triples. Four layer assignments
make the closest pair monochromatic. CMR73 therefore gives expected mass at
most

\[
4P_sN\frac1h p^{-(k-s-1)}
=
4N^2
\]

at each of the at most `k-1` binary valuation levels.

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
4(k-1)N^2+
\frac{p+3}{3}N^2.
\]

The same bounds hold for determinant-zero-modulo-`N` triples with three distinct
columns. Consequently the bank contains a saturated state with

\[
T_k=O(N^2\log_pN)
\]

and an absolute logarithmic coefficient.

### Proof

CMR70--CMR71 bound all layer-transverse triples by less than

\[
\frac{4p}{3(p-1)}N^2.
\]

The equilateral nontransverse clusters contribute less than
`(p-2)N^2/3`. Binary nontransverse clusters contribute at most `4N^2` at
each of at most `k-1` levels. Adding the terms proves the first inequality.
Since `4/(p-1)<=1`, the simpler second bound follows.

All arguments impose successive determinant congruences, so the calculation also
bounds modular determinant-zero triples with three distinct columns. ∎

The remaining logarithm comes from binary same-layer stars: one close pair at
scale `s` and a third point outside that pair's prefix block. Equilateral and
layer-transverse patterns have only quadratic total mass.

The exact clustering formulas are checked in
[`scripts/verify_prime_power_binary_clusters.py`](../scripts/verify_prime_power_binary_clusters.py).
