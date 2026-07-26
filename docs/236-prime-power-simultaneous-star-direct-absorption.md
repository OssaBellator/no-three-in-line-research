# Simultaneous common-layer robust stars absorb without a wall loss

CMR1014--CMR1037 used the generic secant-star execution CMR611--CMR616 for the
common-layer rank-one branch. That theorem allows historical arms whose cells do
not occur together, so it needs a matching-vertex wall versus greedy extraction.
The robust-surplus arms of CMR1008--CMR1010 are different: every arm occurs in one
actual bank state `Q`.

After layer polarization, all outside cells of a common-layer subbank lie in one
permutation matching of `Q`. Their complete union is therefore already a partial
matching. No matching-vertex wall or square-root extraction is needed.

Let

\[
\mathcal A_0=\{\{z,a_i,b_i\}:1\le i\le M_0\}
\]

be the common-layer subbank from CMR1015, in layer `ell`. The outside physical
pairs are cell-disjoint and all outside labelled cells belong to layer `ell` of
one saturated state `Q`.

## 1. The complete outside union is one partial matching

### Theorem CMR1054 -- PROVED

The set

\[
W=\{a_i,b_i:1\le i\le M_0\}
\]

has size `2M_0` and is a compatible partial matching in layer `ell`.

### Proof

Cell-disjointness gives `|W|=2M_0`. Every cell of `W` belongs to the same
permutation matching of `Q`, so no two use the same source or target vertex. ∎

Thus the wall branch of CMR611 cannot occur for this simultaneous subbank.

## 2. At most two protected vertices are charged per protected edge

Let `P` be the protected partial matching in layer `ell` and put `k=|P|`.
Call an arm protected-touching when one of its outside cells uses a vertex of
`P`.

### Theorem CMR1055 -- PROVED

At most

\[
\boxed{2k}
\]

arms are protected-touching. Hence at least

\[
\boxed{M_0-2k}
\]

arms are completely disjoint from the protected vertices whenever this quantity
is positive.

### Proof

The complete outside union is a partial matching, so every protected source or
target vertex is incident with at most one outside cell and therefore at most one
arm. There are `2k` protected vertices. ∎

## 3. Direct simultaneous absorption

### Theorem CMR1056 -- PROVED

Let `\mathcal A_0^\circ` be the free arms from CMR1055 and let `W^\circ` be their
outside-cell union. Then

\[
P\cup W^\circ
\]

is a partial matching, and the canonical exact derangement cylinder avoids every
cell of `W^\circ`.

The protected matching grows by at least

\[
\boxed{
G_\star
=
2\max\{0,M_0-2k\}.
}
\]

Every free arm is absent from every state of the new cylinder.

### Proof

CMR1054 gives compatibility and CMR1055 gives vertex-disjointness from `P`.
Apply the canonical forbidden-matching extension CMR571, equivalently CMR613
without the preliminary greedy extraction. Each free arm contributes its two
outside cells. ∎

## 4. Zero growth gives a stronger core bound

### Theorem CMR1057 -- PROVED

If `G_star=0`, then

\[
\boxed{k\ge\frac{M_0}{2}.}
\]

### Proof

Zero growth gives `M_0<=2k`. ∎

This replaces the weaker generic bound involving
`ceil(M_0/(4(ceil(sqrt(M_0))-1)))`.

## 5. Robust-surplus quantitative form

Use the notation of CMR1030:

\[
B=\left\lceil\frac{D+g}{2}\right\rceil,
\qquad
d=\left\lceil\frac{B}{a}\right\rceil,
\qquad
M=\left\lceil\frac{d}{\binom{R-1}{2}}\right\rceil.
\]

If the common-layer branch of CMR1015 occurs, then

\[
M_0\ge\left\lceil\frac M4\right\rceil.
\]

### Corollary CMR1058 -- PROVED

The direct protected growth obeys

\[
\boxed{
G_\star
\ge
2\max\left\{0,
\left\lceil\frac14
\left\lceil
\frac{
\left\lceil\lceil(D+g)/2\rceil/a\right\rceil
}{\binom{R-1}{2}}
\right\rceil
\right\rceil
-2k
\right\}.
}
\]

If the lower bound is zero, the protected core satisfies

\[
\boxed{
k\ge\frac12\left\lceil\frac M4\right\rceil.}
\]

### Proof

Substitute the CMR1030 and CMR1015 lower bounds into CMR1056--CMR1057. ∎

## 6. Finite direct-star capacity

### Theorem CMR1059 -- PROVED

Across a monotone two-layer history, let `G_i` count protected edges added by
direct simultaneous star absorption. Then

\[
\boxed{
\sum_iG_i
\le
2n-k_0^{(0)}-k_0^{(1)}.
}
\]

For every `G_0>=1`, at most

\[
\boxed{
\left\lfloor
\frac{2n-k_0^{(0)}-k_0^{(1)}}{G_0}
\right\rfloor
}
\]

episodes add at least `G_0` protected edges.

### Proof

Apply the common two-layer protected-capacity budget CMR1034--CMR1035. ∎

## 7. Scope of the strengthening

### Theorem CMR1060 -- PROVED

The direct matching conclusion CMR1054 is valid because all outside cells are
simultaneously selected in one permutation layer of `Q`.

For a historical secant-star family whose arms occur in different states, only
cell-disjointness may be known; matching vertices can repeat, and the generic
wall/extraction theorem CMR611 remains necessary.

### Proof

Simultaneous selection in one permutation forbids repeated source or target
vertices. Historical occurrence in different permutations has no such global
constraint. ∎

No historical theorem is strengthened silently.

## 8. Simultaneous-star endpoint

### Corollary CMR1061 -- PROVED

The common-layer branch of one robust-surplus episode reaches exactly one of:

1. direct protected growth `2 max(0,M_0-2k)`;
2. a protected core with `k>=M_0/2`;
3. protected-capacity saturation;
4. large-core minimum product descent CMR1038--CMR1045;
5. restoration, owner/envelope exit, or strict potential improvement.

The matching-vertex wall alternative is absent from this simultaneous branch.
The remaining rank-one difficulty is therefore the cross-layer rooted paid-pair
bank, not common-layer matching overlap.

### Proof

Combine CMR1054--CMR1060 with CMR1014--CMR1021 and CMR1038--CMR1045. ∎

No all-`n` theorem is claimed. Simultaneous compatibility, protected-touch
injection, direct growth, core thresholds, and capacity bounds are checked in
[`scripts/verify_prime_power_simultaneous_star_absorption.py`](../scripts/verify_prime_power_simultaneous_star_absorption.py).
