# Rational-inverse typed occurrence-slot assignment Hall core

This block converts localized owner/charge collisions into a complete finite typed use-to-slot assignment problem. It is conditional on complete physical-source, collateral, owner, charge and arithmetic compatibility data.

## RI5fs: typed unit assignment network

Let `U` be the localized typed owner/charge use claims and `S` the faithful physical-source/collateral occurrence slots. Join `u` to `s` exactly when all retained owner or charge type, terminal, host, secant, coherence, source, collateral and perturbation fields permit that debit. The unit network `source -> U -> S -> sink` has integral maximum flow equal to the largest injective one-use realization.

## RI5ft: exact typed Hall criterion

Every typed use has faithful injective lineage if and only if the maximum matching has size `|U|`, equivalently `|N(X)| >= |X|` for every typed use set `X`. A complete matching debits each physical/collateral slot once and excludes duplicate consumption and non-injective collateral reuse.

## RI5fu: canonical typed maximum-deficit core

If the maximum matching size is `nu<|U|`, set `delta=|U|-nu`. Among all subsets with `|X|-|N(X)|=delta`, choose minimum cardinality and then the lexicographically least complete typed arithmetic address. The returned `X_*` preserves owner/charge type and every retained field; every proper subset has deficit below `delta`.

## RI5fv: saturation and essentiality

A maximum matching on `X_*` saturates every slot in `N(X_*)`, leaves exactly `delta` typed uses unmatched and preserves all physical-source and collateral addresses. Removing any retained owner or charge use lowers the maximum core deficit by at least one.

## RI5fw: arithmetic interface and resets

Thus each localized typed collision is resolved by an injective assignment or returns one exact owner/charge Hall core. Remaining work is proving the Hall inequalities from concrete arithmetic compatibility and collateral stocks, adding named deposits, or excluding/paying the returned core. Omitted types or fields, changed terminal arithmetic, hidden collateral, splitting, relabelling or independent reuse reset the theorem.

This theorem does not prove RI6 or the no-three-in-line conjecture.