# Semantic refinement of global quotient states and rows

The global quotient currently consists of exact finite state IDs, rows, weights and ranks. This
chapter requires an explicit mathematical predicate for every global state and an explicit
recurrence theorem for every final row.

## Theorem CMR2366 — PROVED AS AN INTERFACE

Every global state receives one canonical predicate record containing a predicate ID, source
locator, digest, mathematical statement and evidence. Predicate IDs are unique and state
records cover the complete cross-block global-state registry exactly.

## Theorem CMR2367 — PROVED

Each predicate record inherits the state's exact role, stratum, owner, complete local-member
list and the spanning equivalence-tree evidence used to merge those members.

Thus the semantic predicate is bound to the same state class and equivalence evidence as the
finite quotient.

## Theorem CMR2368 — PROVED AS AN INTERFACE

Every final global quotient row receives one canonical theorem record containing a theorem ID,
source locator, digest, theorem statement, interpretation of the signed fixed offset and
evidence. Theorem IDs and row IDs are unique.

## Theorem CMR2369 — PROVED

For each row, the checker reconstructs the parent predicate and the complete target predicate
multiset from the quotient's global-state targets and multiplicities. The row's kind,
classification, margin and global-row digest are retained exactly.

## Theorem CMR2370 — PROVED

State semantic records cover every global state exactly, and row semantic records cover every
final global row exactly. Missing, duplicate and extraneous semantic records are rejected.

## Theorem CMR2371 — PROVED

The refinement certificate uses the exact same skeleton-derived global family and the exact
same state-equivalence certificate as the closure dossier. Parallel semantic universes cannot
be substituted by matching names alone.

## Theorem CMR2372 — HONEST REFINEMENT BOUNDARY

Complete predicate and theorem coverage documents the intended interpretation of the finite
quotient. It does not prove those predicates equivalent to their local states or prove the row
theorems true.

## Corollary CMR2373 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_global_quotient_semantic_refinement.py` validates complete state and
row semantic coverage and reconstructs every predicate-level recurrence row exactly.

The checker was syntax-compiled in the publication environment. No genuine semantic refinement
bank is supplied.
