# Sparse algebraic free-token repair gains

## Status

This note proves SAS5ns--SAS5nv under the rooted neutral cut, complete boundary-neutral witness, and local repair contracts through SAS5nr. It does not construct the sparse repairs, prove SAS6, or prove the no-three-in-line conjecture.

## Setup

Fix a maximum matching `M` in the balanced neutral-key component. Let `U` be a selected support-key family of unmatched pair/completion incidences, `m=|U|`, and `(A,B)` its alternating closure. Let `Z` be the free neutral tokens in that key.

## SAS5ns -- free-neutral missing rectangle -- PROVED

Every neutral token in `B` is matched. If the component deficit is `delta_k>=m` and `|T_k|>=|R_k|`, then

\[
|Z|=|T_k|-|M|=(|T_k|-|R_k|)+\delta_k\ge m.
\]

Since `N(A)=B`, every pair in `U x Z` is a boundary-neutral compatibility nonedge. The balanced sparse branch contains at least `m^2` unmatched-root/free-neutral pairs.

## SAS5nt -- free-neutral predicate concentration -- PROVED

Assign each pair in `U x Z` to its least failed retained sparse predicate among `q` predicates. One predicate labels `F_p` with

\[
\boxed{|F_p|\ge\left\lceil\frac{m|Z|}{q}\right\rceil\ge\left\lceil\frac{m^2}{q}\right\rceil.}
\]

A pair with no named sign, profile, move, legality, boundary, orientation, source, occurrence, repair or lineage failure is an incomplete dictionary witness.

## SAS5nu -- local sparse repair gives augmenting gain -- PROVED UNDER THE EDGE-REPAIR CONTRACT

Let `Q` be endpoint-disjoint in `F_p`. If local row/cell, swap, profile, orientation, legality, boundary, pair/completion, owner or lineage repairs restore all edges in `Q`, preserve every edge of `M`, and commute on distinct witnesses, then `M union Q` is a matching after repair. The neutral-assignment deficit drops by at least `|Q|`.

A repairable star edge gives one-step descent; a common-witness edit restoring `t` endpoint-disjoint overload pairs gives batch descent `t`; and a commuting independent stock gives descent equal to its size.

## SAS5nv -- sparse repair-or-rigidity router -- PROVED UNDER THE REPAIR CONTRACTS

One exact continuation holds: complete neutral assignment; numerical neutral-key shortage; a repairable star edge with one-step descent; a uniformly repairable witness overload with batch descent; a commuting independent stock with full descent; or a rigid sparse repair-contract or lineage failure caused by a missing repair, destruction of a carried edge, noncommutation, or an incomplete dictionary.

Compatibility repair creates no neutral mass and changes no orientation payment.

## Corrected SAS6 frontier

The balanced sparse obstruction now yields matching-deficit descent or one rigid named sparse/lineage repair failure. Remaining work is to construct move/legality/orientation repairs and prove preservation, commutation, and sparse-ledger payment.

## Finite check

`scripts/verify_sas_free_token_repair_gains.py` checks rooted closures, free-neutral rectangles, predicate concentration, and exact simultaneous matching gain.