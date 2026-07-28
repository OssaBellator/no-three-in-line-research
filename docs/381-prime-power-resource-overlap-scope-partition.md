# Literal resource-overlap scope partition

CMR2198--CMR2205 verify global credit nonreuse relative to supplied resource-scope IDs.
This chapter removes that remaining naming freedom by deriving the minimal scope partition
from complete literal destroyed-triple universes.

## Theorem CMR2222 — PROVED AS AN INTERFACE

For every deterministically selected recurrent row, let

\[
U(r)=\{\text{canonical coordinate triples of all literal destroyed triples in }r\}.
\]

The complete set `U(r)` is reconstructed from the embedded witness-routing certificate,
not from the subset of destroyed triples actually used by the selected response.

## Theorem CMR2223 — PROVED

The row-overlap graph has one vertex for each selected row and an undirected edge

\[
\boxed{r\sim r'\iff U(r)\cap U(r')\ne\varnothing.}
\]

Thus two rows are adjacent exactly when they share at least one literal destroyed resource
by canonical point coordinates.

## Theorem CMR2224 — PROVED

The derived resource scopes are exactly the connected components of the row-overlap graph.
Each component receives a canonical scope ID determined by its complete row-ID set and
complete literal-resource set.

## Theorem CMR2225 — PROVED

Distinct derived components have disjoint resource universes:

\[
\boxed{S\ne S'\Longrightarrow U(S)\cap U(S')=\varnothing.}
\]

This follows from the connected-component construction: any shared resource would create
an overlap edge joining the components.

## Theorem CMR2226 — PROVED

Every selected row's declared resource-scope ID must equal its derived overlap-component
ID. Arbitrary splitting of overlapping rows and arbitrary merging of disjoint components
are both rejected.

## Theorem CMR2227 — PROVED

After the exact scope partition is established, the CMR2198--CMR2205 global resource and
obligation injectivity tests apply to the same selected execution. Consequently nonreuse
is no longer conditional on freely chosen scope names.

## Theorem CMR2228 — HONEST PHYSICAL BOUNDARY

The result proves independence of literal destroyed-triple resources represented by
canonical coordinate triples. It does not by itself prove that the supplied active row
family is the genuine simultaneous recurrence step, or that no additional physical
resource outside the destroyed-triple model couples two components.

## Corollary CMR2229 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_resource_overlap_scope_partition.py` reconstructs every row
resource universe, the exact overlap graph, connected components, canonical scope IDs and
scope agreement, then preserves the embedded simultaneous-credit audit.

The checker was syntax-compiled in the publication environment. A genuine certificate
still requires the actual simultaneous selected-row family.
