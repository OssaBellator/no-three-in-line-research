# Layer-transverse recursive certificates and codegree localization

CMR68 uses only digit levels above the closest pair of columns. In the corrected
balanced recursive bank of CMR67, many layer patterns expose a unit-coefficient
row digit at every depth. Nonroot depths contribute exact factors `1/p`; the
saturated root law contributes `1/(p-1)`.

Throughout this chapter,

\[
N=p^k,
\qquad
p\equiv1\pmod4,
\]

and the bank uses the saturated common-parameter root law from CMR67, followed
by independent uniform maps from `B_p` at every nonroot layer-prefix node.

Fix three distinct columns `x_1,x_2,x_3` with layer labels
`ell_1,ell_2,ell_3`. Put

\[
r=\min_{i<j}v_p(x_i-x_j),
\qquad
s=\max_{i<j}v_p(x_i-x_j).
\]

If `s>r`, the ultrametric property gives one unique closest pair, namely the
pair with valuation `s`.

Call the selected triple **layer-transverse** when either

1. `s=r` and the three layer labels are not all equal; or
2. `s>r` and the two points in the unique closest pair use different layers.

## 1. Full-depth anti-concentration

### Theorem CMR70 — PROVED

Every fixed layer-transverse triple satisfies

\[
\Pr(\Delta\equiv0\pmod N)
\le
\frac1{(p-1)p^{k-1}}
=
\frac{p}{p-1}\frac1N.
\]

The same bound therefore holds for real collinearity.

### Proof

Use the determinant coefficients

\[
\kappa_1=x_3-x_2,
\qquad
\kappa_2=x_1-x_3,
\qquad
\kappa_3=x_2-x_1,
\]

and divide them by their common minimum power `p^r`. The indices whose reduced
coefficients are units are determined by the p-adic clustering pattern.

If `s=r`, all three reduced coefficients are units. Since the layer labels are
not all equal, one layer occurs exactly once. That point's node key is unique at
every depth.

If `s>r`, the unit coefficients are exactly those attached to the two endpoints
of the unique closest pair. Their layers are different. At every depth, the
endpoint whose layer differs from the third point has a node key distinct from
both other keys.

At each nonroot depth `n=1,...,k-1`, expose every output except the chosen unique
unit-coefficient digit. The next determinant congruence fixes at most one value,
and CMR67 makes that digit exactly uniform on `F_p`. These levels contribute
`p^{-(k-1)}`.

At the root, the other layer is queried at two distinct columns. Its two outputs
determine its shift and the common nonsquare parameter. The singleton layer's
shift remains uniform among the `p-1` values distinct from the other shift.
Thus the required singleton row has conditional atom at most `1/(p-1)`.
Multiplying the root and nonroot factors proves the theorem. ∎

## 2. The logarithmic syndrome is layer-aligned

For one unordered column triple, the number of nontransverse layer assignments
is at most four:

- if `s=r`, only the two monochromatic assignments are nontransverse;
- if `s>r`, the closest pair must use one common layer, giving four assignments
  after the third layer is chosen.

### Corollary CMR71 — PROVED

The expected number of layer-transverse real triples is less than

\[
\frac{8p}{(p-1)N}\binom N3
<
\frac{4p}{3(p-1)}N^2.
\]

The expected number of nontransverse triples is at most

\[
2pkN^2.
\]

Consequently

\[
\mathbb E T_k
<
2pkN^2+rac{4p}{3(p-1)}N^2.
\]

### Proof

The first estimate uses CMR70 and at most eight layer assignments for every
column triple.

For the nontransverse part, group column triples by

\[
s=\max_{i<j}v_p(x_i-x_j).
\]

As in CMR69, the number in one group is less than `N^3/(2p^s)`. There are at
most four nontransverse layer assignments, and CMR68 gives probability at most

\[
p^{-(k-s-1)}.
\]

Thus every `s` contributes at most `2pN^2`. Sum the `k` valuation levels. ∎

The theorem identifies the source of the logarithmic loss: same-layer closest
pairs, not generic mixed-layer triples.

## 3. Pair-codegree stratification

Fix two selected positions in distinct columns and put

\[
u=v_p(x_1-x_2).
\]

Let `D(x_1,ell_1;x_2,ell_2)` be the expected number of selected third points
that complete this pair to a real triple.

### Theorem CMR72 — PROVED

For a same-layer pair,

\[
D(x_1,\ell;x_2,\ell)
\le
2p^{u+1}+4p(k-u-1).
\]

For a cross-layer pair,

\[
D(x_1,0;x_2,1)
\le
\frac{2p}{p-1}
+
\frac{2p^{1-u}}{(p-1)^2}
+
2p(k-u-1).
\]

The same cross-layer bound holds with the layers reversed.

### Proof

For a third column `x_3`, let

\[
t=\max_{i<j}v_p(x_i-x_j).
\]

There are fewer than `N` choices with `t=u`. For each `t>u`, the third column
must be congruent modulo `p^t` to one of the fixed endpoints, so there are at
most

\[
\frac{2N}{p^t}
\]

choices.

For a same-layer pair, use CMR68 for both choices of the third layer. This gives

\[
\begin{aligned}
D
&\le
2N p^{-(k-u-1)}
+2\sum_{t=u+1}^{k-1}
\frac{2N}{p^t}p^{-(k-t-1)}\\
&=
2p^{u+1}+4p(k-u-1).
\end{aligned}
\]

Now suppose the fixed pair uses different layers. Every third point with `t=u`
is layer-transverse, so CMR70 gives contribution at most

\[
2N\frac{p}{(p-1)N}=\frac{2p}{p-1}.
\]

For `t>u`, one of the two third-layer choices is layer-transverse while the other
is nontransverse. Hence

\[
\begin{aligned}
D
&\le
\frac{2p}{p-1}
+
\sum_{t=u+1}^{k-1}
\frac{2N}{p^t}
\left(
\frac{p}{(p-1)N}
+p^{-(k-t-1)}
\right)\\
&\le
\frac{2p}{p-1}
+
\frac{2p^{1-u}}{(p-1)^2}
+
2p(k-u-1).
\end{aligned}
\]

This proves both bounds. ∎

The high-codegree term `p^(u+1)` occurs only for same-layer pairs with a long
common p-adic column prefix. At valuation `u`, there are fewer than

\[
\frac{N^2}{p^u}
\]

such pairs across both layers. Thus the exceptional pair mass is organized in
an explicit multiscale Carleson family.

The structural cases are checked in
[`scripts/verify_prime_power_layer_transverse.py`](../scripts/verify_prime_power_layer_transverse.py).
