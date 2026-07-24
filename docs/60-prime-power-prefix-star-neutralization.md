# P-adic prefix-block neutralization of binary same-layer stars

CMR70--CMR74 isolate the remaining logarithmic recursive syndrome in one
explicit family: a same-layer closest pair at valuation scale `s`, together
with a third point outside the pair's prefix block. This chapter installs an
exact row-column-preserving repair bank on that prefix block.

Let

\[
N=p^k,
\qquad p\ge5
\]

with `p` odd, and let

\[
S=G(f_0)\cup G(f_1)
\]

be any saturated two-permutation state. Thus `f_0,f_1` are permutations of
`[N]` and

\[
f_0(x)\ne f_1(x)
\]

for every column `x`.

For `0<=s<k` and `a` modulo `p^s`, define the column prefix block

\[
C_{s,a}
=
\{x\in[N]:x\equiv a\pmod {p^s}\}.
\]

Its size is

\[
t=|C_{s,a}|=p^{k-s}.
\]

Fix a layer `ell` and put

\[
R_{s,a,\ell}=f_\ell(C_{s,a}),
\qquad
A_{s,a,\ell}=\{(x,f_\ell(x)):x\in C_{s,a}\}.
\]

The row set has size `t` because `f_ell` is a permutation.

## 1. The prefix-block rematching bank

Remove the points of `A_{s,a,ell}` and rematch the columns
`C_{s,a}` perfectly to the same row set `R_{s,a,ell}`. Relabel the columns and
rows by `[t]` so that the original layer matching is the identity.

Two positions are forbidden:

1. the original identity cell, so every selected point actually moves;
2. the cell occupied by the opposite layer, whenever that opposite-layer row
   belongs to `R_{s,a,ell}`.

The second forbidden set is a partial matching. Consequently the union `F` of
the two forbidden sets has degree at most two in every source and target.

### Theorem CMR75 — PROVED

For every prefix block in an odd-prime recursive state with `p>=5`, the allowed
rematching family

\[
\Omega_{s,a,\ell}
=
\{\pi\in S_t:(i,\pi(i))\notin F\text{ for all }i\}
\]

satisfies

\[
|\Omega_{s,a,\ell}|\ge\frac{t!}{128}.
\]

If `Q` is a compatible prescription of `r` allowed block cells and `pi` is
uniform on the family, then

\[
\Pr(Q\subseteq\pi)
\le
\frac{128}{(t)_r}.
\]

Every state produced by the bank:

1. preserves both row and column counts;
2. remains disjoint from the opposite layer;
3. moves every point of `A_{s,a,ell}`;
4. agrees with the original state outside the block.

### Proof

When `t>=7`, apply AN1 directly to the degree-two forbidden set.

The only remaining block size for an odd prime `p>=5` is `t=5`. A finite exact
check over all second forbidden permutations gives at least `12` allowed
matchings. A partial second matching can be extended to a full permutation,
and adding forbidden cells can only decrease the allowed family, so the same
lower bound holds for every partial matching. Since

\[
12>\frac{5!}{128},
\]

the AN1 count and cylinder estimate remain valid.

A rematching uses exactly the old row set, so the changed layer remains a
permutation. Avoiding the opposite-layer cells preserves pointwise disjointness.
Avoiding the identity moves every old block point. ∎

The bank is larger than a one-digit fibre switch: it may permute all
`t=p^(k-s)` rows carried by one complete lower-prefix column block. This is the
correct scale for the binary-star obstruction.

## 2. Exact destruction of the assigned binary stars

Consider a nontransverse binary-cluster triple from CMR73. Its unique closest
column pair has valuation

\[
s=\max_{i<j}v_p(x_i-x_j)
\]

and the two closest points use one common layer `ell`.

### Theorem CMR76 — PROVED

Every such triple is assigned to one unique prefix block
`A_{s,a,ell}`. Every state in the corresponding CMR75 bank destroys that old
triple.

### Proof

The closest columns are congruent modulo `p^s`, so they lie in one unique
`C_{s,a}`. Their difference has valuation exactly `s`, so they occupy distinct
children of that prefix block.

The third column has smaller valuation difference from the closest pair. Hence
it is not congruent to them modulo `p^s` and lies outside `C_{s,a}`.

Both closest-pair points belong to `A_{s,a,ell}`. CMR75 moves every point of
that block, so neither old closest-pair cell remains selected. The original
three-cell certificate is therefore absent in every rematched state. ∎

Thus the bank neutralizes the complete old external star of every closest pair
inside the chosen block, not merely one selected third point.

## 3. Scale-invariant load extraction

Let `B_s` be the number of current real triples whose unique closest pair has
valuation `s` and lies in one common layer. For one layer-prefix block, let
`B_{s,a,ell}` be the number assigned to it by CMR76.

### Theorem CMR77 — PROVED

The binary-star loads partition exactly:

\[
B_s
=
\sum_{\ell=0}^1\sum_{a\bmod p^s}B_{s,a,\ell}.
\]

Consequently some block satisfies

\[
B_{s,a,\ell}
\ge
\frac{B_s}{2p^s}.
\]

Since its size is `t=N/p^s`, this is equivalently

\[
\frac{B_{s,a,\ell}}t
\ge
\frac{B_s}{2N}.
\]

### Proof

CMR76 gives a unique layer and a unique residue block for every binary
same-layer triple. There are exactly `2p^s` layer-prefix blocks. Averaging proves
the first inequality, and division by `t=N/p^s` gives the scale-invariant form.
∎

The last display is the key multiscale feature: the old-star load per movable
endpoint is independent of the valuation scale.

## 4. Exact collateral inequality

Fix one block and abbreviate

\[
A=A_{s,a,\ell},
\qquad
Z=S\setminus A.
\]

Let

\[
D(A)=\Phi(S)-\Phi(Z)
\]

be the number of old real triples touching `A`. In particular,

\[
D(A)\ge B_{s,a,\ell}.
\]

For `r=1,2,3`, let `T_r(A)` be the number of real collinear certificates
consisting of exactly `r` mutually compatible allowed block cells and `3-r`
points of `Z`.

### Theorem CMR78 — PROVED

For a uniformly random state from the prefix-block bank,

\[
\mathbb E\,\Phi(S_\pi)
\le
\Phi(Z)
+
128\left(
\frac{T_1(A)}t
+
\frac{T_2(A)}{t(t-1)}
+
\frac{T_3(A)}{t(t-1)(t-2)}
\right).
\]

Hence the block has a strictly improving state whenever

\[
D(A)
>
128\left(
\frac{T_1(A)}t
+
\frac{T_2(A)}{t(t-1)}
+
\frac{T_3(A)}{t(t-1)(t-2)}
\right).
\]

If no scale-`s` block improves, then

\[
B_s
\le
128\sum_{\ell=0}^1\sum_{a\bmod p^s}
\left(
\frac{T_1(A_{s,a,\ell})}t
+
\frac{T_2(A_{s,a,\ell})}{(t)_2}
+
\frac{T_3(A_{s,a,\ell})}{(t)_3}
\right).
\]

### Proof

A new triple using `r` rematched cells appears only when its compatible
rank-`r` partial matching is contained in the random block matching. CMR75
bounds that probability by `128/(t)_r`. Sum over all certificates.

Every old triple touching `A` disappears because every old block cell moves.
Thus

\[
\Phi(S_\pi)-\Phi(S)
=
-D(A)+\bigl(\Phi(S_\pi)-\Phi(Z)\bigr).
\]

The improvement criterion follows by expectation. If no block improves, use
`B_{s,a,ell}<=D(A)` and sum the resulting inequalities over the exact partition
from CMR77. ∎

## 5. Repair-or-concentration endpoint

CMR75--CMR78 convert the remaining logarithmic syndrome into an executable
multiscale repair dichotomy.

At every valuation scale `s`, either:

1. one prefix-block rematching strictly lowers the real-triple potential; or
2. the normalized collateral sum in CMR78 is at least `B_s/128`.

The first-generation binary stars are removed exactly in every state of the
bank. Failure can therefore no longer be attributed to those stars themselves;
it forces concentration among new certificates meeting a complete prefix
block in one, two, or three compatible cells.

The next quantitative target is to bound the aggregate rank-one term

\[
\sum_{a,\ell}\frac{T_1(A_{s,a,\ell})}{t}
\]

by a paid secant-star or carry-complexity potential. The rank-two and rank-three
terms already carry the natural matching denominators. This is a strictly
smaller target than the original unsummed binary-star problem.

The finite combinatorial checks are in
[`scripts/verify_prime_power_prefix_star_bank.py`](../scripts/verify_prime_power_prefix_star_bank.py).
