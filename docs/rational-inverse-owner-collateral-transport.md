# Rational inverse: owner-collateral transportation

## Scope

This note records RI5cg--RI5ck. It converts exact symmetric two-lift costs and exact collateral deposits into a finite capacitated transportation problem. It does not prove the arithmetic compatibility or collateral lower bounds for a concrete RI word.

Let `O` be the finite set of retained owner classes and `S` the finite set of collateral-source classes. Owner `o` has symmetric demand `c_o>=0`; source `s` has collateral capacity `d_s>=0`. A compatibility edge `o~s` means that source class `s` may legally pay owner class `o` without changing any retained RI field.

## RI5cg: exact flow formulation

Construct the standard integral network: source-to-owner capacity `c_o`, infinite capacity on compatibility edges, and collateral-source-to-sink capacity `d_s`. The maximum integral flow is the maximum symmetric cost that can be paid without relabelling.

## RI5ch: Hall transportation criterion

All symmetric owner cost is payable if and only if, for every owner subset `X subseteq O`,

`sum_{o in X} c_o <= sum_{s in N(X)} d_s`.

This is the capacitated Hall condition for the retained owner/source compatibility graph.

## RI5ci: exact deficit identity

The unpaid symmetric cost equals

`max_X (sum_{o in X} c_o - sum_{s in N(X)} d_s)_+`.

Thus the transportation failure retains an exact owner subset and its complete compatible collateral neighbourhood.

## RI5cj: canonical deficient owner cut

Fix a deterministic ordering of owner subsets. If payment fails, choose the least subset maximizing the deficit. This cut is a complete finite obstruction address: owner classes, demanded cost, compatible source classes, and available collateral are all retained.

## RI5ck: reset boundary

A payment edge depending on an omitted owner, host, coherence, source-lineage, or arithmetic field is outside the graph and is returned as a compatibility-model reset. It is not counted as paid collateral.

## Remaining frontier

The remaining RI work is to prove the concrete arithmetic owner/source compatibility graph and its source capacities, close blocker-profile interactions, and compare this collateral bank with the other terminal banks. RI6 and the no-three-in-line conjecture are not proved.