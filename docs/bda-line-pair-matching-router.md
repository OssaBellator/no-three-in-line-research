# Pair-matching and context-star routing on heavy BDA lines

**Branch:** `research/bounded-denominator-absorbers`

BDA5by--BDA5cb reduce every off-diagonal overlap to one connector, resonant or radial context line, or to address-disjoint role families. This note gives a quantitative payment router for any weighted family of pair addresses supported on one such line.

Let `L` be a fixed context line. Form a simple weighted graph `G_L` whose vertices are the available context cells on `L` and whose edges are the distinct context-pair addresses of one aggregated record family. Let `w(e)>=0` and

\[
W_L=\sum_{e\in E(G_L)}w(e).
\]

Aliases are aggregated before constructing `G_L`.

## BDA5cc -- bounded-incidence weighted matching -- PROVED

Suppose every context cell belongs to at most `d` positive-weight pair addresses, with `d>=1`. Then `G_L` has a matching `M` satisfying

\[
\boxed{
\sum_{e\in M}w(e)
\ge
\frac{W_L}{2d-1}.
}
\]

### Proof

Process positive-weight edges in nonincreasing weight order. Select the current edge and delete every edge sharing one of its endpoints. A selected edge deletes at most `2d-1` edges including itself, and every deleted edge has weight at most the selected edge. Charging each deleted edge to the selected edge that removed it gives total charged weight at most `(2d-1)w(e)` per selected edge. Summing proves the claim. QED.

## BDA5cd -- high-incidence context-star alternative -- PROVED

For every integer `d>=1`, one of the following holds:

1. one context cell lies in more than `d` positive-weight pair addresses;
2. a vertex-disjoint pair family has total weight at least `W_L/(2d-1)`.

The first branch is an exact context-star obstruction centered at one physical cell on `L`.

### Proof

If the maximum positive-address degree exceeds `d`, use branch 1. Otherwise apply BDA5cc. QED.

## BDA5ce -- capacity-one pair-ticket stock -- PROVED

A matching returned by BDA5cc consists of pairwise context-cell-disjoint addresses. Therefore any physical resource, ticket or protected-cell capacity that is consumed through at least one member of each pair is charged at most once across the matching.

In particular, if each matched pair realizes payment at least `rho w(e)` for some fixed `rho>0`, the total realized payment is at least

\[
\boxed{\frac{\rho W_L}{2d-1}.}
\]

### Proof

Distinct matching edges have disjoint endpoint sets. Hence no context-cell-local capacity can be consumed by two matched addresses. Sum the assumed per-edge payment and use BDA5cc. QED.

## BDA5cf -- complete heavy-line router -- PROVED

Apply the construction separately to every line-supported output from BDA5cb: one-local connector overlap, resonant `CD-A` or `CD-B`, and radial `AB-A` or `AB-B`. For each weighted line family and each chosen incidence threshold `d`, one exact continuation holds:

1. a context-cell star contains more than `d` pair addresses;
2. a vertex-disjoint pair family carries at least a `1/(2d-1)` fraction of the line weight;
3. the line, address aggregation, physical occurrence, owner or context-cell records are not fixed.

Thus a heavy BDA line is no longer merely a concentration locus. It yields either a concentrated one-cell obstruction or a large stock of disjoint pair addresses suitable for independent payment or capacity-one tickets.

## Corrected BDA6 frontier

All off-diagonal geometry and weighted overlap are closed, and every resulting heavy line has a star-versus-disjoint-matching router. Remaining work is to prove a useful context-cell incidence bound or pay the returned high-incidence star, realize owner/payment on the disjoint pair stock, and import higher-rank events.

## Finite check

`scripts/verify_bda_line_pair_matching_router.py` exhausts small weighted line graphs and checks the greedy `W/(2d-1)` matching bound and the star alternative.