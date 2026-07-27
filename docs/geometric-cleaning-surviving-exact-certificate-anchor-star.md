# Current-anchor star routing for surviving exact certificates

**Branch:** `research/geometric-cleaning`

GC2eg--GC2ek install every selected exact prospective certificate as an occurrence-faithful current lineage.  At each later checkpoint, at least half of the installed bank is already assigned to unique first destructions or one current cell carries surviving rank-three incidence at least `3W/(2N^2)`.

This note resolves the geometry of that current-cell branch.  The exact surviving lineages form a weighted link multigraph at the selected cell.  Bounded pair multiplicity gives a paid endpoint-disjoint star; otherwise one exact current pair has high certificate multiplicity.

## Surviving anchor-link model

Fix one installed alias-aggregated exact-certificate bank of birth weight `W_B`.  At a later checkpoint write

`W_B=S_B+P_B`,

where `S_B` is surviving current-lineage weight and `P_B` is unique first-destruction payment.

Suppose the surviving branch is active.  Choose a physical cell `z` whose surviving certificate load

`H_z=sum_(Q current: z in Q) h_Q`

is maximal.  GC2ej gives

`H_z>=3S_B/N^2`.

For every surviving exact certificate lineage `Q={z,x,y}`, create one link edge joining `x` and `y`, carrying weight `h_Q` and retaining the complete exact lineage, label and context address of `Q`.

Distinct lineages or labels on the same physical triple are parallel link edges.  Exact aliases of the same physical occurrence were already aggregated before the lineage bank was formed.

## GC2el -- occurrence-faithful link-multigraph identity -- PROVED

Let `L_z` be the resulting weighted link multigraph.  Its total edge weight is exactly

`w(L_z)=H_z`.

For an outside cell `x`, let `deg_z(x)` be the number of exact link edges incident with `x`, and let

`D_z(x)=sum_(Q current: {z,x} subset Q) h_Q`

be its weighted current pair load.  Then

`sum_(x!=z) D_z(x)=2H_z`.

### Proof

Every surviving exact certificate containing `z` contributes one link edge of the same occurrence-faithful weight, so the edge weights sum to `H_z`.  Its other two distinct cells contribute that weight once each to the weighted degrees.  Double-counting certificate--outside-cell incidences gives the second identity.  Parallel edges remain separate lineage objects and exact aliases were already combined, so no occurrence is lost or duplicated. QED.

## GC2em -- weighted current pair-or-star dichotomy -- PROVED

For every integer `Delta>=1`, one of the following holds:

1. one current physical pair `{z,x}` belongs to more than `Delta` exact surviving certificate lineages;
2. there is a surviving exact-certificate family `S_z` whose members all contain `z`, are pairwise disjoint outside `z`, and have total current weight at least

   `H_z/(2Delta-1)`.

### Proof

If some link vertex has unweighted degree greater than `Delta`, use alternative 1.  Otherwise every link degree is at most `Delta`.

Consider the conflict graph on exact link edges, joining two edges when they share an endpoint.  One edge `xy` conflicts with at most

`(deg_z(x)-1)+(deg_z(y)-1)<=2Delta-2`

other edges.  This bound remains valid for parallel edges because repeated neighbours only reduce the number of distinct conflicts.  Greedy colouring therefore uses at most `2Delta-1` colours.  Each colour class is a link matching, and the colour weights sum to `H_z`.  A heaviest colour has weight at least `H_z/(2Delta-1)`.  Translating the matching back to certificates gives alternative 2. QED.

The first branch is exact current pair multiplicity, not latent pair-shadow mass.  The second branch is a current paid star through `z`.

## GC2en -- installed-bank quantitative anchor router -- PROVED

Fix `Delta>=1`.  At every checkpoint after exact-certificate installation, one of the following holds:

1. first-destruction payment satisfies

   `P_B>=W_B/2`;
2. one current pair `{z,x}` belongs to more than `Delta` surviving exact certificate lineages;
3. one current endpoint-disjoint star through `z` has total weight strictly greater than

   `3W_B/[2N^2(2Delta-1)]`.

If the equality case `P_B=S_B=W_B/2` is assigned to the payment branch, the star inequality is strict as displayed.

### Proof

If alternative 1 fails, the lineage identity gives `S_B>W_B/2`.  GC2ej chooses `z` with

`H_z>=3S_B/N^2>3W_B/(2N^2)`.

Apply GC2em.  Its high-degree branch is alternative 2.  Its matching branch has weight at least `H_z/(2Delta-1)`, which is strictly greater than the displayed quantity. QED.

## GC2eo -- paid GC4 import without a latent-weight gate -- PROVED

The star returned by GC2en consists entirely of current exact factor lineages.  Its weights are current syndrome/factor-incidence weights, its members are pairwise disjoint outside the exact current anchor `z`, and all lineage, label and context fields remain attached.

Consequently it may enter the current paid GC4 conflict, installation or neutralization machinery with no candidate-to-current conversion and no additional payment loss.  The pair branch of GC2en is one exact current high-multiplicity pair and enters the existing pair-codegree continuation.

### Proof

Every selected edge of the link matching is one surviving lineage, hence one current physical occurrence.  Link-edge disjointness is exactly disjointness of the two nonanchor cells.  The construction never merges distinct lineage or label addresses; it only selects a subset.  Therefore the selected weights are already current and occurrence-faithful, which is the paid hypothesis required by GC4c--GC4f and the surviving-star import. QED.

## GC2ep -- surviving exact-certificate continuation -- PROVED UNDER THE LINEAGE-CYCLE CONTRACT

For every compatible bank installed by GC2eg--GC2ek and every `Delta>=1`, the continuation is nested:

1. either one exact realization, product, occurrence, alias, lineage or context field fails;
2. or the exact bank is installed with birth weight `W_B`;
3. at every later checkpoint, either first-destruction payment is at least `W_B/2`, one current pair has exact certificate multiplicity greater than `Delta`, or one paid endpoint-disjoint current star has weight greater than

   `3W_B/[2N^2(2Delta-1)]`;
4. independently, the intervening history has strict tagged-potential descent, is a tagged-only recycling segment, leaves by an outer reset, or returns one named lineage-cycle failure.

Under the fixed-universe lineage-cycle contract, tagged-only recurrence erases, descends or spends finite exact tickets.

### Proof

Installation and the survival/payment identity are GC2eg--GC2ek.  Apply GC2en at the selected checkpoint and GC2eo to its two geometric branches.  The independent temporal alternatives are GC2cj--GC2cl. QED.

## Corrected GC frontier

The surviving exact-certificate branch no longer ends at an unstructured current-cell load.  It gives unique first-destruction payment, one exact high-multiplicity current pair, or a quantitatively paid endpoint-disjoint current star ready for GC4.

The remaining geometry is execution or descent of that current-star bank, the high pair-multiplicity continuation, block-tuple overload recursion, tagged-only recycling outside the finite contract, isolated-cell prospective stars, pool depletion, global-context causes and local superregular resampling.

## Finite check

`scripts/verify_geometric_surviving_exact_certificate_anchor_star.py` samples weighted exact-lineage banks and checkpoints.  It checks the survival/payment identity, the `3S/N^2` anchor load, occurrence-faithful link-multigraph identities, the `2Delta-1` weighted matching extraction, current pair multiplicity and the integrated installed-bank constant.