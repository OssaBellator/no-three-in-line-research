# Matching-reservoir cycle factorization

A parabolic matching reservoir is a perfect matching in an induced subgraph of
the saturated source configuration.  Saturation makes that graph extremely
rigid: every vertex has degree at most two.  This chapter classifies the entire
deletion bank and records the resulting limitation on variable-reservoir
averaging.

## 1. The induced reservoir graph

Let `S subseteq [m]^2` be saturated.  Choose old column and row sets `C,Y` of
the same size.  Form the bipartite graph

\[
 G=G_S(C,Y)
\]

with left vertex set `C`, right vertex set `Y`, and one edge `(x,y)` for every
point of

\[
 S\cap(C\times Y).
\]

A deletion set is a matching reservoir exactly when it is a perfect matching of
`G`.

Because `S` has two points in every row and column,

\[
 \Delta(G)\le2.
\]

Thus every connected component of `G` is a path, a cycle, or an isolated
vertex.

### Proposition PP3aj -- PROVED

The graph `G` has a perfect matching if and only if:

1. it has no isolated vertex;
2. every path component has an even number of vertices.

When these conditions hold:

- every path component has one perfect matching;
- every cycle component has exactly two perfect matchings, its two alternating
  edge sets;
- choices on distinct cycle components are independent.

If `c(G)` is the number of cycle components, then

\[
 \boxed{|\mathcal M(G)|=2^{c(G)}.}
\]

#### Proof

A connected graph of maximum degree two is a path, cycle, or isolated vertex.
A path has a perfect matching exactly when its order is even, and then the edge
incident with either endpoint is forced; deleting its endpoints recursively
shows uniqueness.  Every bipartite cycle is even and has exactly the two
alternating perfect matchings.  Components are vertex-disjoint, so a global
perfect matching is obtained by choosing one component matching independently
in each component. ∎

Since every cycle has at least four vertices and `G` has `4t` vertices when
`|C|=|Y|=2t`, one always has

\[
 c(G)\le t,
 \qquad
 |\mathcal M(G)|\le2^t.
\]

## 2. Exact deletion marginals

Sample a perfect matching of `G` uniformly.

### Corollary PP3ak -- PROVED

Every reservoir edge belongs to exactly one of the following classes.

1. **Forced:** it lies in the unique matching of a path component and is deleted
   with probability `1`.
2. **Never selected:** it lies in a path component but outside its unique
   matching and is deleted with probability `0`.
3. **Cycle optional:** it lies in a cycle component and is deleted with
   probability `1/2`.

For edges on distinct cycle components, deletion indicators are independent.
For two edges on one cycle, they are either always selected together or never
selected together, according to whether they belong to the same alternating
class.

#### Proof

The path statements follow from uniqueness.  On a cycle the two alternating
matchings are equiprobable, so every edge appears in one of them.  Component
choices factor in the uniform product distribution. ∎

This gives exact survival probabilities for every old point in a matching-bank
state.  No permanent or asymptotic approximation is involved.

## 3. Limitation of deletion diversity alone

### Corollary PP3al -- PROVED

In a uniform matching-reservoir bank with one fixed inserted patch:

- an optional old point survives with probability `1/2`;
- two optional points on distinct cycles survive jointly with probability
  `1/4`;
- no nontrivial edge survival probability tends to zero merely because the
  reservoir size grows.

Consequently, deletion variation alone cannot provide `o(1)` joint survival for
an arbitrary fixed old-pair or old-anchor certificate.  An asymptotic PP2l
argument must use at least one additional mechanism:

1. inserted-state variation;
2. forced deletion of the concentrated certificate points;
3. same-cycle anticorrelation arranged around the certificate geometry;
4. a bank in which the coordinate sets themselves vary, not only the perfect
   matching inside one induced graph.

#### Proof

The probabilities are the cases of PP3ak.  They are contained in
`{0,1/4,1/2,1}` for two optional points, independently of the total number of
cycle components.  Hence simply adding unrelated cycles increases the number
of bank states but does not dilute a certificate supported on fixed edges. ∎

This explains the side-four regression bank.  It has four deletion states, but
its fixed inserted patch still has joint certificate probabilities as large as
`1/2`; PP2l improves over the deletion-blind bound without approaching the
asymptotic spread required for completion.

## 4. Geometric opportunity inside cycles

The negative conclusion is limited.  A blocker pair or retained anchor may
interact with several edges from one reservoir cycle.  If every alternating
choice deletes at least one required blocker, or if the two alternating classes
place a bad old pair in opposite states, the joint certificate probability can
be zero.

Thus the next positive target is not a larger number of arbitrary cycles.  It
is a **geometry-aligned cycle bank** in which the alternating classes are chosen
so that high-load old secants and anchors are forced or anticorrelated.

The exact factorization in PP3aj reduces that target to a labelled cycle problem:
for each reservoir cycle, determine which alternating class clears each external
certificate, then combine independent cycle choices using PP2l or a product-space
local lemma.

## 5. Finite analyzer

The script

```bash
python scripts/analyze_matching_reservoir_cycles.py \
  certificates/prime-patching-small.json \
  --n 4 --columns 1,2,3,4 --rows 1,2,3,4
```

constructs the induced degree-two graph, classifies its components, reports the
exact matching count, and labels every source point as forced, never selected,
or cycle optional.
