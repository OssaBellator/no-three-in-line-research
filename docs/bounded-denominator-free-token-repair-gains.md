# Bounded-denominator free-token repair gains

## Status

This note proves BDA5hv--BDA5hy under the rooted restoration-cut, complete predicate-witness, and local repair contracts through BDA5hu. It does not construct the rational-gain repairs, prove BDA6, or prove the no-three-in-line conjecture.

## Setup

Fix a maximum matching `M` in the balanced restoration-key component. Let `U` be a selected support-key family of unmatched repair incidences, `m=|U|`, and `(A,B)` its alternating closure. Let `Z` be the unmatched potential tokens in the same key.

## BDA5hv -- free-potential missing rectangle -- PROVED

Every token in `B` is matched. If the component deficit is `delta_k>=m` and `|T_k|>=|R_k|`, then

\[
|Z|=|T_k|-|M|=(|T_k|-|R_k|)+\delta_k\ge m.
\]

Since `N(A)=B`, every pair in `U x Z` is a repair-potential compatibility nonedge. Thus the balanced branch has at least `m^2` unmatched-incidence/free-potential pairs.

## BDA5hw -- free-potential predicate concentration -- PROVED

Assign each pair in `U x Z` to its least failed retained restoration predicate among `q` predicates. One predicate labels an edge set `F_p` with

\[
\boxed{|F_p|\ge\left\lceil\frac{m|Z|}{q}\right\rceil\ge\left\lceil\frac{m^2}{q}\right\rceil.}
\]

A pair with no named failure is an incomplete rational-gain dictionary witness.

## BDA5hx -- local restoration repair gives augmenting gain -- PROVED UNDER THE EDGE-REPAIR CONTRACT

Let `Q` be endpoint-disjoint in `F_p`. If the selected gate, source, gain, damping, line, owner, arithmetic or boundary repairs restore all edges in `Q`, preserve every edge of `M`, and commute on distinct witnesses, then `M union Q` is a matching in the repaired graph. The restoration matching deficit drops by at least `|Q|`.

Consequently any locally repairable star edge gives one-step descent; a single witness-local repair restoring `t` endpoint-disjoint overload edges gives descent at least `t`; and a commuting independent stock gives descent equal to its size.

## BDA5hy -- restoration repair-or-rigidity router -- PROVED UNDER THE REPAIR CONTRACTS

One exact continuation holds:

1. the potential assignment is complete;
2. one restoration key has a direct numerical potential shortage;
3. one failed-predicate star has a repairable edge and the deficit drops by one;
4. one overloaded witness has a uniform local repair and the deficit drops by its endpoint-disjoint multiplicity;
5. one independent stock has commuting repairs and the deficit drops by its stock size;
6. one named predicate/witness lacks a local repair, a repair destroys a carried edge, selected repairs fail to commute, or the dictionary is incomplete.

Matching repair creates no gain or potential mass; physical costs remain in the occurrence-faithful restoration ledger.

## Corrected BDA6 frontier

The balanced restoration obstruction now yields matching-deficit descent or one rigid named rational-gain repair failure. Remaining work is to construct the actual repairs and prove preservation, commutation, and payment.

## Finite check

`scripts/verify_bda_free_token_repair_gains.py` checks rooted closures, free-potential rectangles, predicate concentration, and exact simultaneous matching gain.