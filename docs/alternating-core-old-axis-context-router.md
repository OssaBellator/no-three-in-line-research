# Context router for old-axis saturation fans

**Branch:** `research/alternating-core-chain`

AC3hc returns an old-axis saturation fan only after all represented cross-arm pivot cells have already appeared. The target states are alternatives, not simultaneous configurations, so their certificates must not be treated as one executable bank. Their two-cell contexts can still be regularized exactly. This note returns either a pairwise context-disjoint axis-target dispersion family or one fixed current context cell supporting a heavy same-role recurrence fan.

## Old-axis certificate records

Fix one AC3hc old-axis output. Its target states have distinct pivot cells `p_t` on one fixed row or column. In target state `t`, let `F_t` be the selected current certificate family from AC3gx. Every certificate

$$
C=\{p_t,x_C,y_C\}
$$

has one retained created-cell rank, arm label and arithmetic/geometric role. The target buckets are pairwise disjoint as certificate families.

Put

$$
G=\sum_t w(\mathcal F_t).
$$

AC3hc supplies

$$
\boxed{G\ge mW/8.}
$$

For a certificate `C`, define its two-cell context

$$
R_C=\{x_C,y_C\}.
$$

## Context-overlap graph

Join two certificate records when their context pairs intersect. Let

$$
L(C)
=
\sum_{C':R_C\cap R_{C'}\ne\varnothing}w(C')
$$

be the closed-neighbourhood weight. Alternative target states are not combined; the graph is used only for structural extraction.

## AC3hi -- context overload or disjoint axis-target dispersion -- PROVED

For every real `K>=1`, one of the following holds.

1. **Context overload:** some certificate satisfies
   $$
   \boxed{L(C)>K w(C).}
   $$
2. **Context-disjoint dispersion:** there is a certificate subfamily `I` whose context pairs are pairwise disjoint and whose total weight satisfies
   $$
   \boxed{
   w(\mathcal I)\ge G/K\ge mW/(8K).
   }
   $$

The second output is an alternative-state dispersion certificate. It is not claimed to be a simultaneous repair bank.

### Proof

If the overload alternative fails, every closed neighbourhood has weight at most `K` times its centre weight. Greedily select a remaining certificate and delete its closed neighbourhood. Each selected weight pays for at most `K` times itself in deleted weight. The selected contexts are pairwise disjoint, and summing the deletion inequalities gives `w(I)>=G/K`. QED.

## AC3hj -- fixed-context localization of an overload -- PROVED

Suppose `C={p,x,y}` satisfies the overload inequality. For a physical context cell `z`, define

$$
\mu(z)
=
\sum_{C':z\in R_{C'}}w(C').
$$

Then one of the two cells `x,y` satisfies

$$
\boxed{
\mu(z)>\frac K2 w(C).
}
$$

Thus an overload returns one exact current context cell, the fixed axis containing the target pivots, the exact arm/rank/role label and a weighted family of current collinear certificates all containing that context cell.

### Proof

Every member of the closed neighbourhood of `C` contains `x` or `y` in its context. Hence

$$
L(C)\le\mu(x)+\mu(y).
$$

If both loads were at most `Kw(C)/2`, their sum would contradict the overload inequality. QED.

## AC3hk -- fixed pair or many distinct axis pivots -- PROVED

Retain the fixed-context family at cell `z`, and aggregate its weight by the distinct axis pivot cells `p`. Let

$$
\mu_z(p)
$$

be the weight of certificates containing the pair `{z,p}`, and let

$$
M_z=\sum_p\mu_z(p)=\mu(z).
$$

For every threshold `beta>0`, exactly one of the following can be selected.

1. **Heavy fixed pair:** one exact pair `{z,p}` has weight greater than `beta`.
2. **Axis-pivot dispersion:** every pair has weight at most `beta`, and the family uses at least
   $$
   \boxed{
   \left\lceil M_z/\beta\right\rceil
   }
   $$
   distinct pivot cells on the fixed row or column axis.

All certificates in both outputs retain the same current context cell `z` and the same finite arithmetic/geometric role class after one further role pigeonhole if necessary.

### Proof

If no pair exceeds `beta`, at least `ceil(M_z/beta)` nonzero pair classes are required to sum to `M_z`. QED.

## Consequence

An old-axis saturation fan now has one of three exact forms:

- a context-disjoint alternative-target dispersion family of weight at least `mW/(8K)`;
- a heavy fixed current pair `{z,p}`;
- or one fixed current context cell paired with many distinct historical axis pivots.

These are the literal physical inputs required by the pair-core, fixed-centre and carry/BDA/RI routers. The remaining work is arithmetic classification or a genuinely multi-target construction; no arbitrary mixture of alternative-state contexts remains.

## Finite check

`scripts/verify_ac_old_axis_context_router.py` exhausts small weighted two-cell context systems, checks the closed-neighbourhood extraction, the `1/K` disjoint-context bound, fixed-context overload localization and the heavy-pair versus distinct-pivot count.