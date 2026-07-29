# Conflict-graph extraction of disjoint physical RI subbanks

**Branch:** `research/rational-inverse-expansion`

RI5bo--RI5bq give a complete physical I6 bank once the component regions are pairwise disjoint and have no cross-region constraints. This note extracts a large bank-ready subfamily when those failures have bounded conflict degree.

## Conflict graph

Let `V` be a family of closed physical RI components. Join distinct components `a,b` by an edge when at least one of the following holds:

1. their declared physical regions overlap;
2. one non-ownership constraint meets both regions;
3. their exterior, blocker, protected, owner or occurrence records are mutually incompatible.

Call the resulting graph `J`. For a vertex set `I`, suppose every local replacement `L(a,b,t)` with `a,b in I` is legal and injective in `(b,t)`.

## RI5br -- independent sets are physical subbanks -- PROVED

Every independent set `I subseteq V` satisfying the local replacement hypotheses supports a legal physical I6 bank on `I`. If `q=|I|`, the bank contains exactly

\[
\boxed{q!h^q}
\]

states, and every compatible distinct-component rank-`r` prescription, `1<=r<=min\{3,q\}`, has probability

\[
\boxed{\frac1{(q)_rh^r}}.
\]

### Proof

Independence removes every declared overlap and cross-region incompatibility. The hypotheses of RI5bo therefore hold after restricting sources and targets to `I`. Apply RI5bp. QED.

## RI5bs -- bounded-degree extraction -- PROVED

If `J` has maximum degree at most `Delta`, then it has an independent set of size at least

\[
\boxed{\left\lceil\frac{|V|}{\Delta+1}\right\rceil}.
\]

Consequently a physical I6 subbank of that many components exists whenever the local replacement hypotheses hold on every nonconflicting pair.

### Proof

Greedily choose one remaining vertex and delete its closed neighbourhood. Each choice deletes at most `Delta+1` vertices. QED.

## RI5bt -- weighted conflict extraction -- PROVED

Give component `a` a nonnegative retained paid weight `w_a`, and write `d(a)` for its conflict degree. Then there is an independent set `I` with

\[
\boxed{
\sum_{a\in I}w_a
\ge
\sum_{a\in V}\frac{w_a}{d(a)+1}.
}
\]

In particular, if `d(a)<=Delta` for all `a`, then

\[
\boxed{w(I)\ge\frac{w(V)}{\Delta+1}}.
\]

### Proof

Choose a uniformly random ordering of `V` and retain every vertex that is earliest in its closed neighbourhood. Two adjacent vertices cannot both be retained, so the retained set is independent. Vertex `a` is retained with probability `1/(d(a)+1)`. Take the expectation of the retained weight and select one ordering attaining at least its expectation. QED.

## RI5bu -- exact conflict overload router -- PROVED

Fix target subbank size `q` and retained weight threshold `W_0`. One of the following holds:

1. an independent set of size at least `q` and weight at least `W_0` gives a physical bank by RI5br;
2. the maximum conflict degree exceeds the proposed `Delta`;
3. the weighted conflict sum `sum_a w_a/(d(a)+1)` is below `W_0`;
4. one least local replacement, injectivity or exterior-field hypothesis fails on an otherwise independent family.

Thus the disjoint-region frontier reduces to bounding an explicit component conflict graph or paying one high-conflict component/neighbourhood.

## Corrected RI6 frontier

Physical bank readiness is now available for any large independent family of the overlap/cross-constraint graph. Remaining work is to bound or pay that graph in the actual RI completion inventory, together with arithmetic owner payment, repeated-coset correlations, blocker repair and replenishable-source recurrence.

## Finite check

`scripts/verify_ri_conflict_graph_subbank.py` exhausts small conflict graphs, verifies the greedy cardinality bound, the weighted Caro--Wei bound and the induced physical bank counts.