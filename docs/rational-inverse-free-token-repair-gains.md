# Rational-inverse free-token repair gains

## Status

This note proves RI5hm--RI5hp under the rooted Hall-cut, complete predicate-witness, and local repair contracts through RI5hl. It does not construct the arithmetic repairs, prove RI6, or prove the no-three-in-line conjecture.

## Setup

Fix a maximum matching `M` in the balanced collateral-key branch. Let `U` be the selected support-key unmatched-root family, with `m=|U|`, and let `(A,B)` be its rooted alternating closure. Let

\[
Z=\{t\in T_k:t\text{ is unmatched by }M\}
\]

be the free collateral tokens in the same key. The component deficit is `delta_k=|R_k|-|M|>=m`, and `|T_k|>=|R_k|`.

## RI5hm -- free-collateral missing rectangle -- PROVED

Every token in `B` is matched, so `Z` is disjoint from `B`. Moreover

\[
|Z|=|T_k|-|M|=(|T_k|-|R_k|)+\delta_k\ge m.
\]

Since `N(A)=B`, every pair in

\[
\boxed{U\times Z}
\]

is a compatibility nonedge. Thus the balanced branch contains a missing rectangle of at least `m^2` pairs whose left endpoints are unmatched incidences and whose right endpoints are free collateral tokens.

## RI5hn -- free-token predicate concentration -- PROVED

Assign each pair in `U x Z` to its least failed retained RI predicate among `q` predicates. One predicate labels an edge set `F_p` satisfying

\[
\boxed{|F_p|\ge \left\lceil\frac{m|Z|}{q}\right\rceil\ge\left\lceil\frac{m^2}{q}\right\rceil.}
\]

Every edge of `F_p` joins an unmatched repair incidence to a free collateral token. A pair with no named failed predicate is an incomplete dictionary witness.

## RI5ho -- local repair gives exact augmenting gain -- PROVED UNDER THE EDGE-REPAIR CONTRACT

Let `Q` be any endpoint-disjoint subset of `F_p`. Suppose local repairs restore every compatibility edge in `Q`, preserve all edges of `M`, and commute on the selected physical witnesses. Then

\[
M\cup Q
\]

is a matching in the repaired graph, and therefore the maximum matching size increases by at least `|Q|`; equivalently the collateral deficit drops by at least `|Q|`.

In particular:

1. repairing any one edge of a high-degree root- or token-star drops the deficit by at least one;
2. if one overloaded physical witness labels `t` endpoint-disjoint pairs and one witness-local edit restores all of them, the deficit drops by at least `t`;
3. repairing an endpoint- and witness-disjoint stock `S` from RI5hk drops the deficit by at least `|S|`.

The proof is immediate because every selected root is unmatched by `M`, every selected token is free, and selected pairs have distinct endpoints.

## RI5hp -- repair-or-rigidity router -- PROVED UNDER THE REPAIR CONTRACTS

One exact continuation holds:

1. the collateral assignment is complete;
2. one key has a direct numerical token shortfall;
3. one failed-predicate star has a locally repairable edge and the deficit drops by at least one;
4. one overloaded witness has a uniform local repair restoring `t` endpoint-disjoint edges and the deficit drops by at least `t`;
5. one independent realized stock has commuting local repairs and the deficit drops by at least its stock size;
6. a named predicate or physical witness has no declared local repair, a repair deletes a carried matching edge, two selected repairs do not commute, or the dictionary is incomplete. This is returned as a rigid repair-contract obstruction.

Repairs do not create collateral mass; they only restore compatibility edges whose physical effects must be charged by the existing occurrence-faithful ledger.

## Corrected RI6 frontier

The balanced RI obstruction now either produces an explicit matching-deficit descent or a rigid named predicate/witness repair failure. Remaining work is to construct the physical repairs, prove preservation and commutation, and charge their geometric or arithmetic costs.

## Finite check

`scripts/verify_ri_free_token_repair_gains.py` checks nontrivial rooted closures, free-token counts, the free rectangle, predicate concentration, single-edge star gain, common-witness batch gain, and simultaneous independent-stock gain.