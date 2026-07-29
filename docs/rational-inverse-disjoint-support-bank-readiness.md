# Disjoint-support criterion for physical I6 bank readiness

**Branch:** `research/rational-inverse-expansion`

The bank-ready rank-one, rank-two and rank-three collateral laws are exact once an installed physical I6 block exists. This note gives a direct sufficient criterion for that physical bank.

## RI5bo -- disjoint local-state product criterion -- PROVED

Let `a=1,...,m` index closed physical RI components. For every source component `a`, every target component `b`, and every shift `t in Z/hZ`, suppose there is a legal local replacement state

\[
L(a,b,t)
\]

with physical support contained in a declared region `S_a`. Assume:

1. the regions `S_1,...,S_m` are pairwise disjoint;
2. every `L(a,b,t)` agrees with the fixed exterior state outside `S_a`;
3. every local state satisfies all row, column, layer, host, blocker and protected-cell constraints whose support meets `S_a`;
4. no constraint has support meeting two distinct regions `S_a,S_{a'}` except the target-component bijection condition;
5. choosing distinct target components for distinct sources satisfies that bijection condition.

Then for every permutation `sigma in S_m` and every shift vector `t in (Z/hZ)^m`, the union

\[
\boxed{
L(1,\sigma(1),t_1)\cup\cdots\cup L(m,\sigma(m),t_m)
}
\]

with the fixed exterior is a legal physical state.

### Proof

All constraints internal to one region hold by assumption 3. Pairwise disjoint support and assumption 4 prevent cross-region row, column, layer, host, blocker, protected or geometric conflicts. The only declared cross-region condition is distinct target ownership, which is exactly the permutation condition in assumption 5. Therefore the union is legal. QED.

## RI5bp -- exact physical bank and uniform law -- PROVED

Under RI5bo, the legal states are indexed by

\[
\boxed{S_m\times(\mathbb Z/h\mathbb Z)^m}
\]

and hence the bank contains exactly

\[
\boxed{m!h^m}
\]

states. Uniform sampling from these physical states induces the same I6 law used in RI5bd--RI5bn. In particular, every compatible distinct-coset rank-`r` prescription, `1<=r<=3`, has probability

\[
\boxed{\frac1{(m)_rh^r}}.
\]

### Proof

RI5bo makes every abstract index legal. Distinct indices have different target ownership or a different local shift in at least one disjoint region, so they give distinct physical states. Counting and the cylinder law are then the standard permutation-times-shift count. QED.

## RI5bq -- least failed readiness witness -- PROVED

If the criterion is not certified, the failure has one least exact type:

1. two declared component supports overlap;
2. one local replacement is itself illegal;
3. one constraint meets two component regions;
4. a target-ownership choice is not bijective;
5. the local-state map is not injective in `(b,t)`;
6. one exterior agreement, blocker, protected, owner or occurrence field is missing.

Thus physical bank readiness is reduced to a finite support-separation and local-legality audit rather than a generic lift statement.

## Corrected RI6 frontier

The abstract-to-physical gap is closed for disjoint-support component families satisfying the declared locality contract. Remaining RI6 work is to re-extract such regions, or pay the least overlap/cross-constraint witness; arithmetic owner payment, repeated-coset correlations, blocker repair and replenishable-source recurrence remain.

## Finite check

`scripts/verify_ri_disjoint_support_bank.py` constructs finite disjoint local-state systems, checks all `m!h^m` unions, verifies injectivity and confirms the rank-at-most-three cylinder counts.