# Charging quotient excess energy

CMR82--CMR84 decompose the quotient secant energy used in the prefix repair.
This chapter removes the universal endpoint baseline from the actual rank-one
candidate count and charges the two remaining excess energies.

Let

\[
N=p^k,
\qquad 1\le s<k,
\qquad m=p^s,
\qquad t=N/m,
\]

and retain the notation of CMR75--CMR84. In particular,

\[
\mathcal J_s(S)
=
2|E_s^{\rm dist}|+\mathcal M_s(S)+\mathcal C_s(S),
\]

and

\[
|E_s^{\rm coll}|=N(t-1).
\]

## 1. The endpoint baseline is absent from rank-one collateral

For a selected full secant pair `e={P,Q}`, let `n_s(e)` be the number of
quotient rectangles met by its reduced primitive line, as in CMR82. A prefix
block is eligible for a rank-one certificate only when both `P` and `Q` lie
outside the moved block.

### Theorem CMR85 — PROVED

At every scale,

\[
\sum_{a,\ell}\frac{T_1(A_{s,a,\ell})}{t}
\le
\mathcal M_s(S)+\mathcal C_s(S)-|E_s^{\rm coll}|.
\]

### Proof

Fix `e` and sum its possible rank-one candidate cells over all layer-prefix
blocks.

Suppose first that the endpoint projections are distinct. Each projected
endpoint belongs to one successful quotient rectangle. That complete block is
ineligible because it contains one endpoint of `e`. Hence the two endpoint
rectangles responsible for the baseline `2` in

\[
n_s(e)=2+q_s(e)
\]

are omitted altogether. Every other successful rectangle contributes at most
`t` exact grid cells on the real line. After division by `t`, the contribution
of `e` is at most `q_s(e)`.

Now suppose that `e` is a collision pair. Both endpoints lie in one common
same-layer prefix block. That block is ineligible, so at most `n_s(e)-1`
successful rectangles remain. Their normalized contribution is at most
`n_s(e)-1`.

Summing the two pair classes gives

\[
\sum_{e\in E_s^{\rm dist}}q_s(e)
+
\sum_{e\in E_s^{\rm coll}}(n_s(e)-1),
\]

which is the claimed expression. A vertical cross-layer pair is distinct at
scale `s`, has `q_s(e)=0`, and therefore contributes nothing. ∎

Thus the deliberately coarse endpoint term in CMR82 never enters the actual
prefix-bank rank-one collateral.

## 2. Distinct-projection energy is charged to modular quotient triples

Let

\[
Z_s(\bar S_s)
\]

be the number of unordered triples of three distinct selected quotient points
whose integer determinant is zero modulo `m`.

### Theorem CMR86 — PROVED

\[
\mathcal M_s(S)
\le
3t^2 Z_s(\bar S_s).
\]

### Proof

A contribution to `M_s` consists of a distinct full secant pair `e` and a third
selected quotient point on its reduced primitive line. The two projected
endpoints and the third point are distinct, and their determinant is zero modulo
`m`.

Fix one unordered modular triple. It has three choices for the quotient endpoint
pair. Each quotient point has exactly `t` selected full lifts in its
layer-prefix fibre, so a fixed quotient pair has at most `t^2` full secant lifts.
Every contribution to `M_s` is obtained in this way. Hence the multiplicity of
one modular quotient triple is at most `3t^2`. ∎

The inherited primitive line signature can only reduce this multiplicity.

## 3. Collision excess is always quadratic

### Theorem CMR87 — PROVED

For every saturated recursive state,

\[
0\le
\mathcal C_s(S)-|E_s^{\rm coll}|
<
2N^2.
\]

### Proof

Every collision line contains its collided quotient point, so each summand in
`C_s` is at least one. The quotient state has exactly `2m` points, hence

\[
n_s(e)-1\le2m-1
\]

for every collision pair. Since there are exactly `N(t-1)` collision pairs,

\[
\mathcal C_s(S)-|E_s^{\rm coll}|
\le
(2m-1)N(t-1)
<2mNt=2N^2.
\]

∎

This bound is intentionally geometry-free. Any use of the primitive carry
directions from CMR84 can only improve it.

## 4. Modular syndrome of the balanced recursive quotient

Assume now

\[
p\equiv1\pmod4
\]

and sample the corrected saturated balanced bank of CMR67: a common nonsquare
parameter and distinct shifts at the root, followed by independent balanced
maps at every nonroot node.

CMR68--CMR74 impose successive divisibility of the determinant by powers of
`p`. Their corrected proofs therefore apply to determinant zero modulo the
current modulus as well as to exact real determinant zero.

At quotient modulus `m=p^s`, CMR74 bounds the expected number of modular-zero
triples with three distinct quotient columns by

\[
\left(4(s-1)+\frac{p+3}{3}\right)m^2.
\]

A quotient triple containing a vertical pair is determined by its column and a
third selected point in another column. There are exactly

\[
m(2m-2)=2m(m-1)
\]

such triples, whether or not their determinant vanishes.

### Theorem CMR88 — PROVED

For the corrected balanced recursive quotient,

\[
\mathbb E Z_s(\bar S_s)
<
\left(4s+\frac{p-3}{3}\right)m^2.
\]

Consequently,

\[
\mathbb E\mathcal M_s(S)
<
(12s+p-3)N^2.
\]

### Proof

Apply the modular form of the corrected CMR74 clustering sum to triples with
three distinct columns and add the deterministic vertical-pair population. The
coefficient is

\[
4(s-1)+\frac{p+3}{3}+2
=
4s+\frac{p-3}{3}.
\]

Then use CMR86 and `t^2m^2=N^2`. ∎

## 5. Scale-summed rank-one endpoint

### Corollary CMR89 — PROVED

At one scale in the corrected balanced recursive bank,

\[
\mathbb E
\sum_{a,\ell}\frac{T_1(A_{s,a,\ell})}{t}
<
(12s+p-1)N^2.
\]

Summing all nontrivial quotient scales gives

\[
\mathbb E
\sum_{s=1}^{k-1}
\sum_{a,\ell}\frac{T_1(A_{s,a,\ell})}{t}
<
\left(6k(k-1)+(p-1)(k-1)\right)N^2.
\]

In particular, one saturated state in the corrected balanced recursive bank has
total rank-one prefix collateral

\[
O_p(N^2\log^2 N).
\]

### Proof

Combine CMR85, CMR87, and CMR88. Finally use

\[
\sum_{s=1}^{k-1}12s=6k(k-1)
\]

and average over the recursive product bank. ∎

The quotient-incidence charging target is therefore complete at the
quadratic-polylogarithmic scale. The remaining prefix-repair obstruction is
entirely in the normalized rank-two and rank-three terms from CMR78, or in a
sharper-than-first-moment treatment of the modular quotient syndrome.

The exact finite checks are in
[`scripts/verify_prime_power_quotient_excess.py`](../scripts/verify_prime_power_quotient_excess.py).
