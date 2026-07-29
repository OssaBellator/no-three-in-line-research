# Geometric-cleaning free-token repair gains

## Status

This note proves GC2mt--GC2mw under the rooted donor-cut, complete geometric witness, and local repair contracts through GC2ms. It does not construct the geometric repairs, prove GC5, or prove the no-three-in-line conjecture.

## Setup

Fix a maximum matching `M` in the balanced geometric-key component. Let `U` be a support-key family of unmatched remedy incidences, `m=|U|`, and `(A,B)` its alternating closure. Let `Z` be the free donor tokens in the same chart/height key.

## GC2mt -- free-donor missing rectangle -- PROVED

Every donor in `B` is matched. If the component deficit is `delta_k>=m` and `|T_k|>=|R_k|`, then

\[
|Z|=|T_k|-|M|=(|T_k|-|R_k|)+\delta_k\ge m.
\]

Since `N(A)=B`, every pair in `U x Z` is a geometric compatibility nonedge. The balanced cleaning branch therefore contains at least `m^2` unmatched-remedy/free-donor pairs.

## GC2mu -- free-donor predicate concentration -- PROVED

Assign each pair in `U x Z` to its least failed retained geometric predicate among `q` predicates. One predicate labels `F_p` with

\[
\boxed{|F_p|\ge\left\lceil\frac{m|Z|}{q}\right\rceil\ge\left\lceil\frac{m^2}{q}\right\rceil.}
\]

A pair with no named chart, height, protected-event, donor, remedy, certificate or boundary failure is an incomplete dictionary witness.

## GC2mv -- local cleaning repair gives augmenting gain -- PROVED UNDER THE EDGE-REPAIR CONTRACT

Let `Q` be endpoint-disjoint in `F_p`. If local moved-cell, protected-event, chart, donor, remedy, height or boundary repairs restore all edges in `Q`, preserve the current matching, and commute on distinct witnesses, then `M union Q` is a matching after repair. The donor-assignment deficit drops by at least `|Q|`.

Thus one repaired star edge gives one-step descent; one common-witness edit restoring `t` endpoint-disjoint pairs gives batch descent `t`; and one commuting independent stock gives descent equal to its size.

## GC2mw -- cleaning repair-or-rigidity router -- PROVED UNDER THE REPAIR CONTRACTS

One exact continuation holds: complete donor assignment; numerical donor-key shortage; a repairable star edge with one-step deficit descent; a uniformly repairable witness overload with batch descent; a commuting independent stock with full descent; or a rigid geometric repair-contract failure caused by missing repairs, destruction of carried edges, noncommutation, or an incomplete dictionary.

Repairing compatibility creates no donor mass and does not change the protected-height ledger; physical costs remain separately charged.

## Corrected GC5 frontier

The balanced cleaning obstruction now yields matching-deficit descent or a rigid named geometric repair failure. Remaining work is to construct chart/protected-event repairs and prove preservation, commutation, and geometric payment.

## Finite check

`scripts/verify_gc_free_token_repair_gains.py` checks rooted closures, free-donor rectangles, predicate concentration, and exact simultaneous matching gain.