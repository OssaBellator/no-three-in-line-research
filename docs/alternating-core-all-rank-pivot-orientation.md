# Canonical pivot orientation for all created-cell ranks

**Branch:** `research/alternating-core-chain`

AC3fa--AC3fo classify failed-bank collateral by the number of cells absent from a fixed parent configuration. AC3fs--AC3fv then construct a union-safe paid decoder for rank-one pivot buckets. The local decoder proof does not use rank one: it uses only a current pivot cell common to every paid certificate in the bucket. A canonical orientation therefore reduces every realized rank-two or rank-three certificate to the same pivot interface without discarding its secant, channel, closure, blocker or arithmetic labels.

## Created certificates and orientation

Fix a parent two-layer union `M` and one realized legal descendant union `S`. Let `C_new(S;M)` be a weighted family of distinct current collinear triples `T` satisfying

$$
T\subseteq S,
\qquad
T\setminus M\ne\varnothing.
$$

Fix a total order on physical cells. Define

$$
N(T)=T\setminus M,
$$

$$
\boxed{p(T)=\min N(T).}
$$

For a current cell `z`, put

$$
\mathcal P_z
=
\{T\in\mathcal C_{\rm new}(S;M):p(T)=z\},
$$

$$
W_z=\sum_{T\in\mathcal P_z}w(T).
$$

All source-rank, current/new-word, line, channel, closure, blocker, product-law and overload decorations of `T` remain attached after orientation.

## AC3gg -- exact all-rank pivot partition -- PROVED

The nonempty pivot buckets partition the created current certificate family:

$$
\boxed{
\mathcal C_{\rm new}(S;M)
=
\mathop{\dot\bigcup}_{z}\mathcal P_z.
}
$$

Hence

$$
\boxed{
\sum_zW_z
=
w(\mathcal C_{\rm new}(S;M)).
}
$$

The partition causes no loss and applies simultaneously to created-cell ranks one, two and three.

### Proof

Every created triple has a nonempty set `N(T)` and therefore one least new cell. It belongs to exactly the bucket indexed by that cell. QED.

## AC3gh -- union-safe decoder for every oriented rank -- PROVED

For every pivot `z` with `W_z>0`, the AC3fs union-safe rectangle decoder removes `z` from the full two-layer union and destroys every certificate in `P_z`.

This holds whether a paid certificate has one, two or three cells outside the parent union.

### Proof

The AC3fs construction uses the permutation layer containing `z`, one same-layer partner, and the exact zero/singleton/full blocker repair which never restores `z`. A current triple guarantees grid size at least three, so the required partner and outside column exist. Every certificate in `P_z` contains `z`; once `z` is absent from the final union, every such certificate is destroyed. No step uses the cardinality of `T\setminus M`. QED.

## AC3gi -- paid all-rank pivot bank or explicit overload -- PROVED

Let

$$
W_{\rm new}=\sum_zW_z.
$$

Build the complete AC3v envelope for each pivot decoder, including every local state, auxiliary blocker cell, replacement, protected scope, full arithmetic decoration and the private bucket `P_z`.

For every `K>=1`, one of the following holds.

1. One pivot decoder has closed-neighbourhood paid load greater than `K W_z`; AC3fr returns one exact role-labelled cell, row, column, cross-triple or protected witness.
2. An independent executable pivot family has private certified payment
   $$
   \boxed{D\ge W_{\rm new}/K.}
   $$
   Every product state is legal and destroys every represented certificate.

### Proof

AC3gg gives disjoint private paid buckets. AC3gh gives a nonempty legal local decoder for every bucket. AC3v makes independent complete envelopes jointly legal and AC3w makes the payment additive. Apply AC2c. QED.

## AC3gj -- recursive all-rank product comparison -- PROVED

Choose independently from the finite local repair menu of every decoder in an executable all-rank pivot family. Relative to the realized state `S`, let `N'_r` be the exact expected weight of newly created union triples of new-cell rank `r=1,2,3`.

Then

$$
\boxed{
\mathbb E[\text{destroyed certified payment}]=D,
}
$$

$$
\boxed{
\mathbb E[\text{created collateral}]
=N'_1+N'_2+N'_3.
}
$$

If

$$
D>N'_1+N'_2+N'_3,
$$

one product state improves. If no product state improves, one created-cell rank has expected weight at least

$$
\boxed{
D/3
\ge
W_{\rm new}/(3K).
}
$$

Every pivot decoder consumes the AC3fv capacity-one ticket of its full row-column rectangle and exact decorations.

### Proof

AC3gh destroys every private bucket in every local state. AC3gg and AC3v give exact destroyed-payment additivity. AC3fa partitions every genuinely new collateral triple by rank. Failure of strict improvement makes the three nonnegative expected rank terms sum to at least `D`; pigeonhole gives `D/3`. The ticket is AC3fv. QED.

## Consequence for the current frontier

The separate local-existence problems for

- rank-one current-pair contexts,
- rank-two current-centred secants,
- rank-three all-new quadratic, closure or crossed-blocker tuples

are unified. After a realizing state is fixed, all three ranks orient without loss to privately paid pivot buckets and admit the same union-safe rectangle transition.

This does **not** prove termination. A failed pivot product may return another created rank, and the same arithmetic or geometric decorations can recur across successive parent configurations. The remaining frontier is now:

1. same-role AC2d overload termination;
2. a finite reuse bound or monotone signature for repeated pivot rectangles and retained arithmetic labels;
3. affine-chain termination;
4. assembly of the total AC4 oracle and AC5 reverse-scale audit.

## Finite check

`scripts/verify_ac_all_rank_pivot_orientation.py` enumerates every nonempty current/new word on abstract triples, all disjoint normalized two-permutation states on grids three through six, all-rank pivot assignments, union-safe repairs, exact bucket partitions, weighted payment identities and the `1/(3K)` failed-bank scale.
