# Layer-transverse recursive certificates and codegree localization

CMR68 uses only the digit levels above the closest pair of columns.  In the
balanced recursive bank of CMR67, many layer patterns expose a unit-coefficient
row digit at every depth, including the depths where the columns still share a
prefix.  Those triples pay the full probability `p^-k=1/N`.

Throughout this chapter,

\[
N=p^k,
\qquad
p\equiv1\pmod4,
\]

and every layer-prefix node uses an independent uniform map from the balanced
family `B_p` of CMR67.

Fix three distinct columns `x_1,x_2,x_3` with layer labels
`ell_1,ell_2,ell_3`.  Put

\[
r=\min_{i<j}v_p(x_i-x_j),
\qquad
s=\max_{i<j}v_p(x_i-x_j).
\]

If `s>r`, the ultrametric property gives one unique **closest pair**, namely the
pair with valuation `s`.

Call the selected triple **layer-transverse** when either

1. `s=r` and the three layer labels are not all equal; or
2. `s>r` and the two points in the unique closest pair use different layers.

## 1. Full-depth anti-concentration

### Theorem CMR70 — PROVED

Every fixed layer-transverse triple satisfies

\[
\Pr(\text{real collinearity})\le p^{-k}=\frac1N.
\]

### Proof

Use the determinant coefficients

\[
\kappa_1=x_3-x_2,
\qquad
\kappa_2=x_1-x_3,
\qquad
\kappa_3=x_2-x_1,
\]

and divide them by their common minimum power `p^r`.  The indices whose reduced
coefficients are units are determined by the p-adic clustering pattern.

If `s=r`, all three reduced coefficients are units.  Since the layer labels are
not all equal, one layer occurs exactly once.  That point's node key is unique
at every digit depth, even while all column prefixes coincide.

If `s>r`, the unit coefficients are exactly those attached to the two endpoints
of the unique closest pair.  Their layers are different.  At every depth, the
endpoint whose layer differs from the third point has a node key distinct from
both other keys.

Thus at each depth `n=0,...,k-1` there is a unit-coefficient row digit supplied
by a node used by no other point in the triple.  Conditional on all lower digits
and every other depth-`n` output, the next determinant congruence prescribes at
most one value of that digit.  CMR67 makes the digit exactly uniform on
`F_p`, and the chosen nodes at different depths are independent.  Multiplying
`k` factors of `1/p` proves the theorem. ∎

## 2. The logarithmic syndrome is layer-aligned

For one unordered column triple, the number of nontransverse layer assignments
is at most four:

- if `s=r`, only the two monochromatic assignments are nontransverse;
- if `s>r`, the closest pair must use one common layer, giving four assignments
  after the third layer is chosen.

### Corollary CMR71 — PROVED

The expected number of layer-transverse real triples is less than

\[
\frac{8}{N}\binom N3
<
\frac43N^2.
\]

The expected number of nontransverse triples is at most

\[
2pkN^2.
\]

Consequently CMR69 may be sharpened to

\[
\mathbb E T_k
<
2pkN^2+\frac43N^2.
\]

### Proof

The first estimate uses CMR70 and at most eight layer assignments for every
column triple.

For the nontransverse part, group column triples by

\[
s=\max_{i<j}v_p(x_i-x_j).
\]

As in CMR69, the number in one group is less than `N^3/(2p^s)`.  There are at
most four nontransverse layer assignments, and CMR68 gives probability at most

\[
p^{-(k-s-1)}.
\]

Thus every `s` contributes at most

\[
4\frac{N^3}{2p^s}p^{-(k-s-1)}
=
2pN^2.
\]

Sum the `k` valuation levels. ∎

The theorem identifies the exact source of the logarithmic loss: same-layer
closest pairs, not generic mixed-layer triples.

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
2+
\frac{2p^{-u}}{p-1}
+2p(k-u-1).
\]

The same cross-layer bound holds with the layers reversed.

### Proof

For a third column `x_3`, let

\[
t=\max_{i<j}v_p(x_i-x_j).
\]

There are fewer than `N` choices with `t=u`.  For each `t>u`, the third column
must be congruent modulo `p^t` to one of the fixed endpoints, so there are at
most

\[
\frac{2N}{p^t}
\]

choices.

For a same-layer pair, use CMR68 for both choices of the third layer.  This gives

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

Now suppose the fixed pair uses different layers.  Every third point with
`t=u` is layer-transverse: either all three pair valuations equal `u`, or the
fixed pair is the unique closest pair and its endpoints use different layers.
The contribution from these columns is therefore at most `2N/N=2`.

For `t>u`, the unique closest pair consists of the third point and one fixed
endpoint.  Of the two possible third-layer choices, one differs from that
endpoint and is layer-transverse, while the other is nontransverse.  Hence

\[
\begin{aligned}
D
&\le
2+
\sum_{t=u+1}^{k-1}
\frac{2N}{p^t}
\left(\frac1N+p^{-(k-t-1)}\right)\\
&\le
2+
2\sum_{t=u+1}^{\infty}p^{-t}
+2p(k-u-1)\\
&=
2+
\frac{2p^{-u}}{p-1}
+2p(k-u-1).
\end{aligned}
\]

This proves both bounds. ∎

The high-codegree term `p^(u+1)` occurs only for same-layer pairs with a long
common p-adic column prefix.  At valuation `u`, there are fewer than

\[
\frac{N^2}{p^u}
\]

such pairs across both layers.  Thus the exceptional pair mass is organized in
an explicit multiscale Carleson family: fewer pairs occur precisely when their
possible codegree is larger.  A repair theorem can therefore target these
same-layer prefix blocks directly, while treating all layer-transverse
certificates by ordinary sparse methods.

The structural cases are checked in
[`scripts/verify_prime_power_layer_transverse.py`](../scripts/verify_prime_power_layer_transverse.py).
