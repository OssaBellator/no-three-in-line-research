# Rank-one prefix collateral as quotient secant incidence

CMR78 reduces failure of a prefix-block neutralization to three normalized
collateral terms. This chapter identifies the dominant rank-one term with a
lower-scale modular secant-incidence energy.

Let

\[
N=p^k,
\qquad 0\le s<k,
\qquad m=p^s,
\qquad t=N/m.
\]

Assume the two layers form a recursive p-adic state. Their reductions modulo
`m` are quotient permutations

\[
P_{0,s},P_{1,s}:[m]\to[m].
\]

For a layer `ell`, define the full lifted quotient channel

\[
K_{s,\ell}
=
\{(x,y)\in[N]^2:
 y\equiv P_{\ell,s}(x\bmod m)\pmod m\}.
\]

This is the disjoint union of the `m` prefix rectangles

\[
C_{s,a}\times R_{s,a,\ell}.
\]

Each rectangle has `t` columns and `t` rows.

## 1. One real line inside a quotient rectangle

Let `L` be a real line with primitive integer equation

\[
Ax+By=C.
\]

Define its quotient incidence count in layer `ell` by

\[
I_{s,\ell}(L)
=
\#\{a\in[m]:
Aa+B P_{\ell,s}(a)\equiv C\pmod m\}.
\]

### Theorem CMR79 — PROVED

Every real line satisfies

\[
|L\cap K_{s,\ell}|
\le
 t I_{s,\ell}(L).
\]

### Proof

A point of `K_{s,ell}` lies in one unique quotient rectangle indexed by a
solution `a` of the displayed congruence. If the congruence fails, the line has
no point in that rectangle.

Inside one successful rectangle there are exactly `t` actual columns. A
nonvertical line contains at most one grid point in each column, so it has at
most `t` points there. A vertical line uses at most one of the rectangle's
actual columns and hence also has at most `t` points, one in each permitted row.
Summing over the `I_{s,ell}(L)` successful quotient rectangles proves the
claim. ∎

The estimate is deliberately insensitive to carries inside a successful
rectangle. All lower-scale arithmetic is compressed into the modular incidence
count `I`.

## 2. Aggregate rank-one collateral

For a selected point pair `e={P,Q}` of the current saturated state, write
`L_e` for its real secant line. Define the scale-`s` quotient secant energy

\[
\mathcal J_s(S)
=
\sum_{e\in\binom S2}
\sum_{\ell=0}^1 I_{s,\ell}(L_e).
\]

For a prefix block `A=A_{s,a,ell}`, retain the rank-one certificate count
`T_1(A)` from CMR78.

### Theorem CMR80 — PROVED

At every scale,

\[
\sum_{\ell=0}^1\sum_{a\bmod m}
\frac{T_1(A_{s,a,\ell})}{t}
\le
\mathcal J_s(S).
\]

### Proof

A rank-one certificate consists of one allowed candidate block cell `z` and
one selected pair `e` from the fixed set outside that block, with `z` lying on
`L_e`.

Drop the restrictions that `e` avoid the moved block and that `z` avoid the two
forbidden matchings. This can only increase the count. Summing over all prefix
blocks of one layer then counts at most

\[
\sum_{e\in\binom S2}|L_e\cap K_{s,\ell}|.
\]

Apply CMR79 and divide by `t`. Finally sum the two layers. ∎

Thus the block size disappears exactly. The rank-one matching denominator is
not lost; it converts a full-grid candidate count into a quotient incidence
count.

## 3. Repair-or-quotient-incidence dichotomy

For one scale, define the higher-rank normalized collateral

\[
\mathcal H_s(S)
=
\sum_{a,\ell}
\left(
\frac{T_2(A_{s,a,\ell})}{(t)_2}
+
\frac{T_3(A_{s,a,\ell})}{(t)_3}
\right).
\]

### Corollary CMR81 — PROVED

If no scale-`s` prefix-block state from CMR75 lowers the triple potential, then

\[
B_s
\le
128\bigl(\mathcal J_s(S)+\mathcal H_s(S)\bigr).
\]

In particular, at least one of

\[
\mathcal J_s(S)\ge\frac{B_s}{256}
\]

or

\[
\mathcal H_s(S)\ge\frac{B_s}{256}
\]

must hold.

### Proof

Insert CMR80 into the summed failure inequality of CMR78. If both terms were
smaller than `B_s/256`, their sum would be smaller than `B_s/128`, contradicting
that inequality. ∎

This is the first scale-by-scale neutralization endpoint in which the dominant
rank-one collateral is no longer an unstructured full-grid quantity.

## 4. What the quotient energy counts

For a secant pair `e={P,Q}`, every quotient point counted by
`I_{s,ell}(L_e)` satisfies the reduced line equation modulo `p^s`.
There are two cases.

1. **Distinct pair projection.** If `P` and `Q` remain distinct modulo `p^s`, a
   third distinct quotient point counted by `I` is a modular collinear triple in
   the quotient layer.
2. **Collision projection.** If the pair collapses modulo `p^s`, the incidence
   is a repeated-projection carry star rather than a three-distinct-point
   quotient triple.

Consequently `J_s` splits into a genuine quotient modular-syndrome term and a
collision/carry term. Both are already native objects in the branch's recursive
carry calculus; neither is the original binary real-star population.

The next theorem should charge the distinct-projection part to the quotient
syndrome and the collision part to the displacement/carry cells CMR14--CMR22
and CMR58--CMR66. If that charging is summable, CMR81 converts it into an actual
potential-decreasing prefix repair.

The finite incidence checks are in
[`scripts/verify_prime_power_rank_one_reduction.py`](../scripts/verify_prime_power_rank_one_reduction.py).
