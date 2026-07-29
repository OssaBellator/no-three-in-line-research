# Orbit-phase free-token repair gains

## Status

This note proves OP4gs--OP4gv under the rooted phase-cut, complete unit-sensitive witness, and local repair contracts through OP4gr. It does not construct the phase repairs, prove OP5, or prove the no-three-in-line conjecture.

## Setup

Fix a maximum matching `M` in the balanced quotient-key component. Let `U` be a selected support-key family of unmatched residual/edit incidences, `m=|U|`, and `(A,B)` its alternating closure. Let `Z` be the free typed source tokens in that key.

## OP4gs -- free-source missing rectangle -- PROVED

Every source token in `B` is matched. If the component deficit is `delta_k>=m` and `|T_k|>=|R_k|`, then

\[
|Z|=|T_k|-|M|=(|T_k|-|R_k|)+\delta_k\ge m.
\]

Since `N(A)=B`, every pair in `U x Z` is a unit-sensitive compatibility nonedge. Thus the balanced phase branch contains at least `m^2` unmatched-root/free-source pairs.

## OP4gt -- free-source predicate concentration -- PROVED

Assign each pair in `U x Z` to its least failed retained phase predicate among `q` predicates. One predicate labels `F_p` with

\[
\boxed{|F_p|\ge\left\lceil\frac{m|Z|}{q}\right\rceil\ge\left\lceil\frac{m^2}{q}\right\rceil.}
\]

A pair with no named quotient, residual/edit, unit, valuation, holonomy, owner, carry or boundary failure is an incomplete dictionary witness.

## OP4gu -- local phase repair gives augmenting gain -- PROVED UNDER THE EDGE-REPAIR CONTRACT

Let `Q` be endpoint-disjoint in `F_p`. If local quotient-coordinate, action, owner, unit/valuation, holonomy, carry or boundary repairs restore all edges in `Q`, preserve every edge of `M`, and commute on distinct witnesses, then `M union Q` is a matching in the repaired graph. The source-assignment deficit drops by at least `|Q|`.

A repairable star edge therefore gives one-step descent; a common-witness repair restoring `t` endpoint-disjoint overload pairs gives batch descent `t`; and a commuting independent stock gives descent equal to its size.

## OP4gv -- phase repair-or-rigidity router -- PROVED UNDER THE REPAIR CONTRACTS

One exact continuation holds: complete source assignment; numerical quotient-key shortage; a repairable star edge with one-step descent; a uniformly repairable witness overload with batch descent; a commuting independent stock with full descent; or a rigid phase repair-contract failure caused by a missing repair, destruction of a carried edge, noncommutation, or an incomplete dictionary.

Compatibility repair creates no source mass, residual payment, edit credit, or holonomy credit.

## Corrected OP5 frontier

The balanced phase obstruction now yields matching-deficit descent or one rigid named unit-sensitive repair failure. Remaining work is to construct quotient/action repairs and prove preservation, commutation, and phase-ledger payment.

## Finite check

`scripts/verify_op_free_token_repair_gains.py` checks rooted closures, free-source rectangles, predicate concentration, and exact simultaneous matching gain.