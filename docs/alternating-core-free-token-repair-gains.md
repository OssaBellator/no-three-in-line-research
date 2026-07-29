# Alternating-core free-token repair gains

## Status

This note proves AC5gp--AC5gs under the synchronized rooted-cut, predicate-stock, support-local churn, and local repair contracts through AC5go. It does not construct the physical repairs, prove AC6, or prove the no-three-in-line conjecture.

## Setup

Fix a maximum matching in the synchronized disjoint union of the AC, RI, BDA, GC, OP, SRR and SAS compatibility graphs. A positive synchronized deficit selects one track-support-key component `(s,x,k)` with an unmatched root family `U`, `m=|U|`, and rooted alternating closure `(A,B)`. Let `Z` be the tokens in `(s,k)` that are free in the synchronized matching.

## AC5gp -- typed free-token rectangle -- PROVED

Every token in `B` is matched. In the balanced selected key, if its component deficit is `delta_{s,k}>=m`, then

\[
|Z|=|T_{s,k}|-|M_{s,k}|=(|T_{s,k}|-|R_{s,k}|)+\delta_{s,k}\ge m.
\]

Because `N(A)=B`, every pair in

\[
\boxed{U\times Z}
\]

is a compatibility nonedge inside one track and one key. Hence the selected component has at least `m^2` unmatched-root/free-token pairs. No cross-track or cross-key pair is used.

## AC5gq -- typed free-token predicate concentration -- PROVED

Assign each pair in `U x Z` to its least failed retained predicate on track `s`, whose predicate count is `q_s`. One predicate labels `F_p` with

\[
\boxed{|F_p|\ge\left\lceil\frac{m|Z|}{q_s}\right\rceil\ge\left\lceil\frac{m^2}{q_s}\right\rceil.}
\]

Every edge of `F_p` joins an unmatched incidence to a free token of the same track-key component.

## AC5gr -- synchronized local-repair gain -- PROVED UNDER THE REPAIR CONTRACTS

Let `Q` be endpoint-disjoint in `F_p`. Suppose the selected local repairs restore all edges of `Q`, preserve the current synchronized matching, preserve every other track dictionary, and commute on distinct typed witnesses. Then adjoining `Q` to the matching increases its size by `|Q|`. Therefore the synchronized deficit drops by at least `|Q|`.

This discharges the three concentration branches as follows:

1. a locally repairable star edge gives deficit descent at least one;
2. a single typed witness repair restoring `t` endpoint-disjoint overload pairs gives descent at least `t`;
3. commuting repairs on an endpoint- and witness-disjoint stock `S` give descent at least `|S|`.

A repair that changes another track, deletes a carried matching edge, or does not commute is returned as a typed rigid-repair failure.

## AC5gs -- churn-funded repair-descent ledger -- PROVED UNDER THE MACRO CONTRACT

Let `Delta_j` be the synchronized deficit after repair at macro epoch `j`, let `U_j` be the support-local matching disturbance introduced by the next physical macro edit, and let `g_j` be the number of endpoint-disjoint free-token pairs restored during its repair stage. Then

\[
\boxed{\Delta_j\le \Delta_{j-1}+U_j-g_j.}
\]

Consequently, over epochs `1,...,J`,

\[
\boxed{\sum_{j=1}^J g_j\le \Delta_0+\sum_{j=1}^J U_j.}
\]

For a fixed physical state with `U_j=0`, repeated successful repairs terminate after at most the initial deficit in total repaired pairs. Across changing macro states, every successful repair is charged either to initial deficit or to declared physical churn.

Thus one exact continuation holds: all assignments complete; a numerical track-key shortage; a successful star, batch, or stock repair giving explicit deficit descent; or one rigid support/key/predicate/witness/repair/commutation/source-ledger failure.

## Corrected AC6 frontier

Repair recurrence is now controlled by an integer deficit potential whose increases are funded by physical churn and whose successful repairs give explicit descent. Remaining work is to construct the actual track repairs, prove preservation and commutation, charge their physical costs, and combine the churn-funded descent ledger with pool replenishment and macro-state recurrence.

## Finite check

`scripts/verify_ac_free_token_repair_gains.py` generates seven-track balanced Hall components, checks typed free-token rectangles and simultaneous repair gains, and verifies the cumulative churn-funded deficit inequality.