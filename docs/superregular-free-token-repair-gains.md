# Superregular free-token repair gains

## Status

This note proves SRR2gc--SRR2gf under the rooted conditioned cut, complete physical witness, and local repair contracts through SRR2gb. It does not construct the conditioned repairs, prove SRR4, or prove the no-three-in-line conjecture.

## Setup

Fix a maximum matching `M` in the balanced conditioned-key component. Let `U` be a selected support-key family of unmatched candidate incidences, `m=|U|`, and `(A,B)` its alternating closure. Let `Z` be the free witness tokens in that key.

## SRR2gc -- free-witness missing rectangle -- PROVED

Every witness token in `B` is matched. If the component deficit is `delta_k>=m` and `|T_k|>=|R_k|`, then

\[
|Z|=|T_k|-|M|=(|T_k|-|R_k|)+\delta_k\ge m.
\]

Since `N(A)=B`, every pair in `U x Z` is a conditioned compatibility nonedge. The balanced resampling branch contains at least `m^2` unmatched-candidate/free-witness pairs.

## SRR2gd -- free-witness predicate concentration -- PROVED

Assign each pair in `U x Z` to its least failed retained conditioned predicate among `q` predicates. One predicate labels `F_p` with

\[
\boxed{|F_p|\ge\left\lceil\frac{m|Z|}{q}\right\rceil\ge\left\lceil\frac{m^2}{q}\right\rceil.}
\]

A pair with no named threshold, burden, source, endpoint, blocker, cycle, occurrence or repair failure is an incomplete dictionary witness.

## SRR2ge -- local conditioned repair gives augmenting gain -- PROVED UNDER THE EDGE-REPAIR CONTRACT

Let `Q` be endpoint-disjoint in `F_p`. If local source, endpoint, blocker, cycle, threshold, burden or conditioning repairs restore all edges in `Q`, preserve every edge of `M`, and commute on distinct witnesses, then `M union Q` is a matching after repair. The witness-assignment deficit drops by at least `|Q|`.

Thus a repairable star edge gives one-step descent; a common physical-witness repair restoring `t` endpoint-disjoint overload pairs gives batch descent `t`; and a commuting independent stock gives descent equal to its size.

## SRR2gf -- conditioned repair-or-rigidity router -- PROVED UNDER THE REPAIR CONTRACTS

One exact continuation holds: complete witness assignment; numerical conditioned-key shortage; a repairable star edge with one-step descent; a uniformly repairable witness overload with batch descent; a commuting independent stock with full descent; or a rigid conditioned repair-contract failure caused by a missing repair, destruction of a carried edge, noncommutation, or an incomplete dictionary.

Compatibility repair creates no witness mass and does not itself pay endpoint burden.

## Corrected SRR frontier

The balanced conditioned obstruction now yields matching-deficit descent or one rigid named repair failure. Remaining work is to construct cycle/threshold/burden repairs and prove preservation, commutation, and burden payment.

## Finite check

`scripts/verify_srr_free_token_repair_gains.py` checks rooted closures, free-witness rectangles, predicate concentration, and exact simultaneous matching gain.