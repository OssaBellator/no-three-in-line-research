# Weighted alternating Hall cores for bounded donor reservoirs

**Branch:** `research/geometric-cleaning`

GC2ge--GC2gi give a canonical maximum matching or Hall-deficient small-reservoir core, while GC2gj--GC2gn retain the exact reservoir subset and its restoration lineage.  This note sharpens the failed-matching output.  The alternating search from all unmatched targets produces one canonical Hall core whose deficiency is exactly the number of unmatched targets and which retains their full weight and blocker labels.

The statement uses capacity-one donors.  Integer donor capacities may be handled by occurrence-faithful cloning; nonintegral or untagged capacities are outside the contract.

## Canonical matching and alternating reachability

Let `G=(T,D;E)` be the exact legal target--donor graph of one bounded reservoir state.  Fix total orders on targets, donors and edges.  Choose the lexicographically least maximum matching `M`.

Let

\[
U=\{t\in T:t\text{ is unmatched by }M\}.
\]

Starting from every vertex of `U`, traverse unmatched edges from targets to donors and matched edges from donors to targets.  Let `X subseteq T` and `Y subseteq D` be the reachable target and donor sets.

## GC2go -- canonical alternating Hall core -- PROVED

If `U` is nonempty, then

\[
\boxed{N_G(X)=Y.}
\]

Every donor in `Y` is matched by `M` to a target in `X`, and every matched target in `X` is matched to a donor in `Y`.

### Proof

Every edge from a reachable target to a donor is either unmatched and is traversed, or is its matching edge.  In the latter case the donor is already reachable from the alternating path that reached the target.  Hence every neighbour of `X` lies in `Y`, while reachability gives `Y subseteq N(X)`.  If a reachable donor were unmatched, an alternating path from `U` to that donor would augment `M`, contradicting maximality.  Therefore every donor in `Y` is matched, and the alternating rule brings its matched target into `X`.  The final assertion follows from the same path structure. QED.

## GC2gp -- exact Hall deficiency -- PROVED

The canonical alternating core satisfies

\[
\boxed{|X|-|Y|=|U|.}
\]

In particular `X` is Hall deficient whenever `U` is nonempty.

### Proof

The matching pairs every donor of `Y` with one distinct target of `X\setminus U` by GC2go.  Conversely every target in `X\setminus U` is reached through its matched donor in `Y`.  Thus `M` gives a bijection between `Y` and `X\setminus U`, so `|Y|=|X|-|U|`. QED.

This is stronger than returning an arbitrary deficient subset: the deficit equals the complete unmatched-target count of the canonical maximum matching.

## GC2gq -- full unmatched weight is retained -- PROVED

Give every target a nonnegative weight `w_t`.  The canonical Hall core contains every unmatched target and therefore retains the exact unmatched weight

\[
\boxed{W_U=\sum_{t\in U}w_t.}
\]

No averaging or donor-count loss occurs before blocker/cause localization.

### Proof

The alternating search starts from all vertices of `U`, so `U subseteq X`.  The displayed weight is attached to those exact physical target occurrences and is unchanged by forming the reachability closure. QED.

## GC2gr -- one exact blocker cause retains weighted shortage -- PROVED

Suppose every unmatched target carries one canonical least shortage cause from a finite dictionary of size `L_cause`: selected donor blocker, target-common line, global context, collision, boundary or omitted-lineage reset.  Then one exact cause class carries unmatched weight at least

\[
\boxed{W_U/L_{\rm cause}.}
\]

The class remains inside the same canonical alternating Hall core `(X,Y)`.

### Proof

The least-cause classes partition `U` and hence partition `W_U`.  Weighted pigeonhole gives the bound.  The core is fixed before the cause split, so the selected class retains its exact Hall witness. QED.

## GC2gs -- weighted small-reservoir Hall router -- PROVED UNDER THE EXACT-DONOR-GRAPH CONTRACT

For every bounded donor reservoir state, one of the following occurs:

1. the canonical maximum matching saturates all targets and supplies a complete donor assignment;
2. it leaves `U` nonempty and returns the canonical alternating Hall core with exact deficit `|U|`;
3. the full unmatched weight `W_U` routes to one exact blocker/cause class with loss at most `L_cause`;
4. occurrence-faithful donor removal or restoration gives current payment, created-collateral descent or a finite restoration ticket through GC2gj--GC2gn;
5. or the donor graph, target set, capacity, blocker label, clean-height, context or lineage interpretation changes, giving an explicit reset.

Thus a failed bounded-reservoir assignment no longer returns only a cardinality shortage.  It returns one exact weighted Hall core together with the physical unmatched targets and their concentrated cause.

### Proof

Choose the canonical maximum matching.  If it is saturating, use the first alternative.  Otherwise apply GC2go--GC2gp, retain the weight by GC2gq and localize its least cause by GC2gr.  Subsequent donor churn uses the exact subset/restoration interface of GC2gj--GC2gn. QED.

## Finite check

`scripts/verify_gc_weighted_alternating_hall_core.py` enumerates small bipartite donor graphs, chooses a canonical maximum matching, constructs the all-unmatched alternating core and verifies `N(X)=Y`, exact deficiency and weighted cause concentration.