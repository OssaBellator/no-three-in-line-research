# Entering-pair concentration yields majority-layer line absorption

CMR1011--CMR1012 show that the higher-entry-rank robust-surplus branch produces
one entering physical pair `Z` and `t` distinct third cells on its unique nonaxis
line. Thus one bank state contains at least `t+2` selected physical cells on one
line. This chapter polarizes those cells by permutation layer and applies the
heavy-line protected absorption theorem in the majority layer.

Let `Q` be the bank state, let `K` be the nonaxis line supplied by CMR1011, and
let

\[
X=|Q|\cap K,
\qquad
r=|X|\ge t+2.
\]

For `ell\in\{0,1\}`, let `X_ell` be the cells of `X` selected in layer `ell`, and
put `r_ell=|X_ell|`.

## 1. Exact layer split on the loaded line

### Theorem CMR1022 -- PROVED

\[
\boxed{r=r_0+r_1.}
\]

Consequently one layer `ell_*` satisfies

\[
\boxed{
r_{\ell_*}
\ge
\left\lceil\frac r2\right\rceil
\ge
\left\lceil\frac{t+2}{2}\right\rceil.
}
\]

### Proof

Every selected physical cell has exactly one layer label. Partition and average. ∎

## 2. The majority-layer line set is a partial matching

### Theorem CMR1023 -- PROVED

The set `X_{ell_*}` is a compatible partial matching in layer `ell_*`.

### Proof

It is a subset of one permutation matching. Equivalently, a nonaxis line meets
each source row and target column at most once. ∎

Thus the higher-rank branch has produced a one-layer heavy-line profile of size
at least `ceil((t+2)/2)`.

## 3. Few majority-line cells touch the protected core

Let `P` be the current protected partial matching in layer `ell_*` and put
`k=|P|`.

### Theorem CMR1024 -- PROVED

At most `2k` cells of `X_{ell_*}` touch a protected source or target vertex.
Hence the free majority-line set

\[
X_{\ell_*}^{\circ}
=
\{x\in X_{\ell_*}:x\cap V(P)=\varnothing\}
\]

satisfies

\[
\boxed{
|X_{\ell_*}^{\circ}|
\ge
\max\left\{0,
\left\lceil\frac{t+2}{2}\right\rceil-2k
\right\}.
}
\]

### Proof

Apply CMR605 to `X_{ell_*}` and then CMR1022. ∎

## 4. Simultaneous majority-line absorption

### Theorem CMR1025 -- PROVED

The union

\[
P\cup X_{\ell_*}^{\circ}
\]

is a partial matching with a canonical perfect-matching extension. Its exact
`D_n` derangement cylinder avoids every cell of `X_{ell_*}^{\circ}`.

Therefore the protected matching grows by at least

\[
\boxed{
G_K
=
\max\left\{0,
\left\lceil\frac{t+2}{2}\right\rceil-2k
\right\}.
}
\]

### Proof

Apply CMR606 to the majority-layer line set and use CMR1024. ∎

Every absorbed cell is one of the selected cells responsible for the high line
load in `Q`.

## 5. Quantitative robust-surplus growth

Let `H=N_2+N_3` and let `a` be the number of entering physical cells in the
transition. CMR1011 permits

\[
t
\ge
\left\lceil\frac{H}{\binom a2}\right\rceil.
\]

### Corollary CMR1026 -- PROVED

The protected growth satisfies

\[
\boxed{
G_K
\ge
\max\left\{0,
\left\lceil
\frac{
\left\lceil H/\binom a2\right\rceil+2
}{2}
\right\rceil
-2k
\right\}.
}
\]

If the higher-rank half of CMR1007 holds, one may replace `H` by
`ceil((D+g)/2)` in this lower bound.

### Proof

Substitute the CMR1011 lower bound for `t` into CMR1025. ∎

## 6. Failure of growth certifies a large protected core

### Theorem CMR1027 -- PROVED

If `G_K=0`, then

\[
\boxed{
k\ge
\left\lceil
\frac12
\left\lceil\frac{t+2}{2}\right\rceil
\right\rceil.
}
\]

In particular the protected core is linear in the square-root-scale or larger
line occupancy produced by any concentrated entering pair.

### Proof

`G_K=0` gives `ceil((t+2)/2)<=2k`. Rearrange and use integrality. ∎

## 7. Finite total line absorption

Consider a monotone sequence of such executions in one residual layer. Let the
initial protected size be `k_0` and let `G_i` be the number of newly absorbed
majority-line cells at step `i`.

### Theorem CMR1028 -- PROVED

\[
\boxed{
\sum_iG_i\le n-k_0.
}
\]

For every threshold `G_0>=1`, the number of executions with `G_i>=G_0` is at most

\[
\boxed{
\left\lfloor\frac{n-k_0}{G_0}\right\rfloor.
}
\]

### Proof

Every absorbed line cell adds one new edge to the same protected partial
matching, whose size is at most `n`. ∎

## 8. Entering-pair line endpoint

### Corollary CMR1029 -- PROVED

Every higher-rank robust-surplus concentration reaches at least one of:

1. simultaneous majority-layer line absorption with growth `G_K`;
2. a protected core satisfying CMR1027;
3. post-absorption line-atom caps `binom(2k,3)` and `binom(2k,2)` from CMR607;
4. finite protected-capacity expenditure CMR1028;
5. matching-vertex wall, full-token return, factor descent, envelope expansion,
   or strict potential improvement.

Thus the entering-pair branch is no longer only a cubic line-energy certificate:
it has a direct monotone protected execution in one actual permutation layer.

### Proof

Combine CMR1022--CMR1028 with CMR605--CMR610 and CMR1011--CMR1013. ∎

No all-`n` theorem is claimed. Layer load, free-cell bounds, protected growth,
large-core alternatives, and finite absorption arithmetic are checked in
[`scripts/verify_prime_power_entering_pair_line_absorption.py`](../scripts/verify_prime_power_entering_pair_line_absorption.py).
