# Sparse typed occurrence-slot assignment Hall core

This block converts localized pair/completion collisions into a complete finite typed use-to-neutral-slot assignment problem. It is conditional on complete sign, boundary-profile, move, source and legality dictionaries.

## SAS5ly: typed unit assignment network

Let `U` be the localized typed pair/completion use claims and `S` the faithful boundary-neutral source/move occurrence slots. Join `u` to `s` exactly when the complete pair or completion type, sign, boundary profile, move, neutral source and legality fields permit that debit. The unit network `source -> U -> S -> sink` has integral maximum flow equal to the largest injective one-use realization.

## SAS5lz: exact typed Hall criterion

All pair/completion uses have injective one-use neutral lineage if and only if the maximum matching has size `|U|`, equivalently `|N(X)| >= |X|` for every typed use set `X`. A complete matching debits each neutral slot once and excludes duplicate consumption and non-injective move reuse.

## SAS5ma: canonical typed maximum-deficit core

If the maximum matching size is `nu<|U|`, put `delta=|U|-nu`. Among all subsets with `|X|-|N(X)|=delta`, choose minimum cardinality and then the lexicographically least complete boundary-neutral address. The returned `X_*` preserves pair/completion type and all sign, profile and move fields; every proper subset has deficit below `delta`.

## SAS5mb: saturation and essentiality

A maximum matching on `X_*` saturates every slot in `N(X_*)`, leaves exactly `delta` typed uses unmatched and preserves every neutral-source and move address. Removing any retained pair or completion use lowers the maximum core deficit by at least one.

## SAS5mc: physical interface and resets

Thus each localized typed collision is resolved by an injective assignment or returns one exact pair/completion Hall core. Remaining work is proving Hall from concrete neutral execution, pair graphs and completion moves, adding named physical capacities, or excluding/paying the core. Omitted types, signs, profiles, moves or legality fields, hidden capacity, splitting, relabelling or reuse reset the theorem.

This theorem does not prove SAS6 or the no-three-in-line conjecture.