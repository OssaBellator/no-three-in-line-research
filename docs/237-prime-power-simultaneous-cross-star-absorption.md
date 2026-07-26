# Simultaneous cross-layer robust stars absorb one endpoint side directly

CMR1018--CMR1021 route each cross-layer arm through a rooted paid-pair cylinder
and an explicit opposite-layer response. As in the common-layer branch, the
simultaneous robust episode supplies more structure than a historical arm
family.

All centre-layer partners occur together in one permutation matching, and all
opposite-layer endpoints occur together in the other. One entire endpoint side
can therefore be absorbed into its layer's protected matching. Keeping the other
permutation fixed, rematch the absorbed layer while forbidding both the protected
extension and the fixed opposite matching. The forbidden board has maximum
degree two, so the degree-two Hall theorem gives a saturated disjoint response.

Let the cross-layer arm bank be

\[
\mathcal A_\times
=
\{\{z,s_i,t_i\}:1\le i\le M\},
\]

where `z,s_i` lie in the centre layer `c` and `t_i` lies in the opposite layer
`o`. The outside pairs are cell-disjoint and all arms occur in one state `Q`.

## 1. Both endpoint families are partial matchings

### Theorem CMR1062 -- PROVED

The sets

\[
S=\{s_i:1\le i\le M\},
\qquad
T=\{t_i:1\le i\le M\}
\]

have size `M`. The set `\{z\}\cup S` is a partial matching in layer `c`, and `T`
is a partial matching in layer `o`.

### Proof

Cell-disjointness gives distinct physical cells. The centre and all `s_i` occur
in one permutation matching of `Q`; all `t_i` occur in the other. ∎

## 2. Free endpoint counts in both layers

Let the protected matching sizes in the two layers be `k_c,k_o`. Let
`S^circ,T^circ` be the endpoint cells avoiding the protected vertices of their
own layers.

### Theorem CMR1063 -- PROVED

\[
\boxed{|S^\circ|\ge\max\{0,M-2k_c\},}
\qquad
\boxed{|T^\circ|\ge\max\{0,M-2k_o\}.}
\]

### Proof

Each endpoint family is a partial matching. At most one endpoint cell meets any
one protected source or target vertex, and each protected matching has twice its
edge count in vertices. ∎

## 3. Degree-two joint rematching after one-side absorption

Fix one endpoint side, say `T^circ` in layer `o`. Extend the union of the protected
matching of layer `o` and `T^circ` to one perfect forbidden matching `F_o`. Keep
the centre-layer permutation `Q_c` fixed.

### Theorem CMR1064 -- PROVED

If the layer side is at least four, there is a perfect matching `Q_o'` satisfying

\[
Q_o'\cap F_o=\varnothing,
\qquad
Q_o'\cap Q_c=\varnothing.
\]

Therefore `Q_c\cup Q_o'` is a saturated disjoint two-layer state which avoids
every cell of `T^circ` and destroys every arm whose opposite endpoint lies in
`T^circ`.

The symmetric statement holds after absorbing `S^circ` and keeping `Q_o` fixed.

### Proof

The forbidden board for the rematched layer is the union of two perfect
matchings, `F_o` and `Q_c`, and therefore has maximum row and column degree at
most two. Apply the degree-two Hall theorem CMR128. Since `T^circ\subseteq F_o`,
all absorbed endpoints are absent. ∎

No sequential-rematching assumption is used: one layer remains fixed throughout
the construction.

## 4. Choose the better endpoint side

### Theorem CMR1065 -- PROVED

One of the two endpoint-side executions destroys at least

\[
\boxed{
G_\times
=
\max\{0,M-2\min(k_c,k_o)\}
}
\]

cross-layer arms and adds that many edges to the corresponding protected
matching.

### Proof

The two free-side lower bounds are `max(0,M-2k_c)` and
`max(0,M-2k_o)`. Choose their maximum and apply CMR1064. ∎

The protected growth is one edge per destroyed cross-layer arm.

## 5. Zero growth forces both protected cores large

### Theorem CMR1066 -- PROVED

If neither endpoint side has positive guaranteed growth, then

\[
\boxed{k_c\ge M/2,
\qquad
k_o\ge M/2.}
\]

### Proof

Zero free-side lower bounds give `M<=2k_c` and `M<=2k_o`. ∎

Thus the no-growth branch gives simultaneous large cores in both layers.

## 6. Current-host execution has the complete transition alternatives

The construction CMR1064 uses the inherited full parent board. In a restricted
current host, some selected rematching edges may need to be added.

### Theorem CMR1067 -- PROVED

Executing the chosen one-side response in the current host reaches at least one
of:

1. a directly available degree-two Hall rematching;
2. exact rollback of a same-value added batch;
3. contraction of an added minimum-core edge;
4. a lost minimum edge and forward ancestry;
5. owner/factor/envelope exit;
6. strict potential improvement.

### Proof

Apply the complete host-transition normalization CMR926--CMR957 to the full-parent
Hall response. ∎

Restoration-only activity is not a separate endpoint.

## 7. Finite cross-star protected capacity

Let `G_i` be the number of protected edges added by cross-star one-side
absorptions across a monotone history.

### Theorem CMR1068 -- PROVED

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

Every absorbed endpoint adds one protected edge in one layer. Apply the common
two-layer capacity CMR1034. ∎

## 8. Simultaneous cross-star endpoint

### Corollary CMR1069 -- PROVED

The cross-layer rank-one branch of one robust-surplus episode reaches at least
one of:

1. direct destruction of `G_cross=max(0,M-2 min(k_c,k_o))` arms and equal protected
   growth;
2. large protected cores `k_c,k_o>=M/2` in both layers;
3. degree-two Hall rematching, rollback, added-edge contraction, loss ancestry,
   structural exit, or strict potential improvement;
4. finite two-layer protected-capacity expenditure;
5. large-core minimum product descent CMR1038--CMR1045.

Thus the simultaneous cross-layer bank is no longer an unresolved family of
independent rooted cylinders. Its only non-growth branch is simultaneous
large-core structure or a paid host transition.

### Proof

Combine CMR1062--CMR1068 with CMR1018--CMR1021 and CMR1038--CMR1045. ∎

No all-`n` theorem is claimed. Endpoint matching compatibility, protected-touch
bounds, degree-two Hall rematching, growth/core alternatives, and capacity
arithmetic are checked in
[`scripts/verify_prime_power_simultaneous_cross_star_absorption.py`](../scripts/verify_prime_power_simultaneous_cross_star_absorption.py).
