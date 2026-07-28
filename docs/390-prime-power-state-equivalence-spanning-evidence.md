# Spanning evidence for cross-block state equivalence

CMR2254--CMR2261 require complete local-to-global state links and semantic-core agreement.
This chapter adds a finite evidence graph explaining why every shared global class may be
identified transitively.

## Theorem CMR2294 — PROVED AS AN INTERFACE

For every shared global state class, an evidence edge joins two local members and records

\[
(\text{global class},\text{two local references},\text{relation ID},
 \text{source locator},\text{statement digest},\text{evidence}).
\]

The two local endpoints are canonically ordered and must belong to the same supplied global
class.

## Theorem CMR2295 — PROVED

Self-edges, duplicate unordered member pairs, unknown members and cross-class evidence edges
are rejected. Every evidence edge therefore documents one explicit bidirectional equivalence
claim internal to one global class.

## Theorem CMR2296 — PROVED

A singleton global class has no evidence edge. A class with `n>1` members must contain exactly

\[
\boxed{n-1}
\]

evidence edges.

## Theorem CMR2297 — PROVED

The evidence graph of every global class must be connected. Together with the exact `n-1`
edge count, this makes the evidence graph a spanning tree and rejects both missing links and
redundant cycles.

## Theorem CMR2298 — PROVED

The lexicographically first local member is the canonical class root. The checker publishes
the unique evidence-edge path from that root to every member. Hence transitive identification
of every member is explicitly decomposed into supplied pairwise claims.

## Theorem CMR2299 — PROVED

The certificate publishes every class tree, root path, maximum tree size, total root-path
length and all edge, class and source-certificate digests.

## Theorem CMR2300 — HONEST EQUIVALENCE BOUNDARY

A passed tree proves complete documentary support for the supplied equivalence relation. It
does not verify that the cited statements are true or that pairwise mathematical equivalence
is transitive in the intended external state semantics.

## Corollary CMR2301 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_state_equivalence_spanning_evidence.py` validates exact class
membership, canonical pairwise evidence, spanning-tree coverage and root-to-member evidence
paths for every global state class.

The checker was syntax-compiled in the publication environment. No genuine multi-block
state-equivalence evidence bank is yet supplied.
