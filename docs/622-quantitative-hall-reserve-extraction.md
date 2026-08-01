# Quantitative Hall reserve extraction

`docs/616` proves robust completion in a residual `K_4,4` when the restricted
partner and source forbidden families are partial matchings.  This chapter gives
a quantitative condition that forces such a four-by-four reserve inside a larger
conditional host.

Let `F_1,F_2` be two forbidden bipartite graphs on equal residual resource sets
of size `N`.  Assume every vertex has degree at most `Delta` in each family.

## 1. Collision-graph extraction

### Theorem PP3cwg -- PROVED / FOUR-RESOURCE RESERVE FROM BOUNDED FORBIDDEN DEGREE

Set

```text
b = C(Delta,2),
N_0(Delta) = 4(1+4b).
```

If `N>=N_0(Delta)`, there are four left resources and four right resources such
that each restricted forbidden family is a partial matching.

#### Proof

On the left resources, join two vertices when they share a right neighbour in
`F_1` or `F_2`.  Each right vertex contributes at most `b` collision edges per
family, so the collision graph has at most `2Nb` edges.  The standard bound

```text
alpha(G) >= N^2/(N+2|E(G)|)
```

gives an independent set of size at least

```text
N/(1+4b) >= 4.
```

Choose four independent left resources.  In either forbidden family their right
neighbourhoods are pairwise disjoint, so every right vertex already has restricted
degree at most one.

Now join two right resources when they lie in the same neighbourhood of one of
the four selected left resources in either family.  There are eight such
neighbourhood buckets, each of size at most `Delta`, hence at most `8b` collision
edges.  Again

```text
alpha >= N^2/(N+16b) >= 4
```

under the stated bound.  Four independent right resources therefore give left
and right restricted degree at most one in each family. ∎

## 2. Degree-two numerical threshold

### Theorem PP3cwh -- PROVED / TWENTY-RESOURCE RESIDUAL THRESHOLD

For `Delta=2`, twenty residual resources per side suffice.  If two decoder
choices have already consumed one left and one right resource each, a host with
twenty-two available resources per side meets the stated reserve count.

#### Proof

`C(2,2)=1`, so `N_0(2)=4(1+4)=20`. ∎

## 3. Robust conditional completion

### Theorem PP3cwi -- PROVED / QUANTITATIVE SIX-RESOURCE HALL PIPELINE

Under `PP3cwg`, the extracted `K_4,4` minus the two restricted partial matchings
retains at least two perfect matchings and survives deletion of one additional
allowed cell.

#### Proof

Apply the complete two-matching exclusion audit of `docs/616` to the extracted
reserve. ∎

## Consequence

The Hall obligation is now numerical: it is enough to prove a residual pool
lower bound and a uniform forbidden-degree bound.  The PP3 asymptotic host has
not yet supplied those two estimates, so this remains a conditional source
bridge rather than a promoted Hall row.
