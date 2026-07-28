# Global support condensation and critical-descent bounds

The global integer quotient publishes one strict or critical-descending row for every parent.
This chapter reconstructs the complete positive-support graph and extracts its exact SCC and
rank-termination structure.

## Theorem CMR2302 — PROVED

The global support graph has one vertex for every final nonauxiliary state and an edge

\[
\boxed{p\longrightarrow t}
\]

for every positive target multiplicity of the row whose parent is `p`. Each edge retains its
row ID, multiplicity, row classification and endpoint ranks.

## Theorem CMR2303 — PROVED

The checker computes the exact strongly connected components of the support graph and the
canonical condensation DAG. Every component publishes its states, internal edge census,
rank interval, cyclicity and digest.

## Theorem CMR2304 — PROVED

An edge from a critical-descending row satisfies

\[
\boxed{\rho(t)<\rho(p).}
\]

All critical edges are therefore strictly decreasing in a nonnegative integer coordinate.

## Theorem CMR2305 — PROVED

The critical-edge subgraph is acyclic. A canonical topological order is published and any
critical-only directed cycle is rejected.

## Theorem CMR2306 — PROVED

The exact longest critical-edge path is computed by dynamic programming. Its length `d`
satisfies

\[
\boxed{d\le \max_g\rho(g)-\min_g\rho(g).}
\]

Thus the number of consecutive critical-descending transitions is explicitly bounded before
a strict row or terminal state must occur.

## Theorem CMR2307 — PROVED

Every directed cycle in the full support graph contains at least one strict-row edge. Indeed,
a cycle containing only critical edges would contradict CMR2305. Consequently every cyclic
support SCC contains a strict edge.

## Theorem CMR2308 — HONEST TERMINATION BOUNDARY

The graph result proves a finite strict-or-ranked descent property of the supplied quotient.
It does not prove that the rows are the genuine exhaustive recurrence, that multiplicities
have their intended semantics, or that the weight/rank potential controls the original
no-three-in-line construction.

## Corollary CMR2309 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_global_support_condensation.py` reconstructs all support edges,
computes SCCs and the condensation DAG, certifies critical-edge acyclicity, publishes the
exact longest critical path and verifies that every support cycle contains a strict edge.

The checker was syntax-compiled in the publication environment. No genuine complete global
quotient family is yet supplied.
