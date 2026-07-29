# Geometric-cleaning occurrence-slot assignment Hall core

This block converts localized cause collisions into one finite use-to-slot assignment problem. It is conditional on complete cause-use, donor/remedy/height-slot and geometric compatibility dictionaries.

## GC2kz: unit assignment network

Let `U` be the localized cause-use claims and `S` the faithful donor/remedy/height occurrence slots. Join `u` to `s` exactly when the complete physical source, donor, remedy, height, cause and conditioning fields permit that use to debit that slot. The unit-capacity network `source -> U -> S -> sink` has integral maximum flow equal to the largest injective one-use cleaning realization.

## GC2la: exact Hall criterion

All cause uses admit faithful injective lineage if and only if the maximum matching has size `|U|`, equivalently `|N(X)| >= |X|` for every `X subseteq U`. A complete matching debits every donor/remedy/height slot at most once and excludes duplicate cleaning consumption and non-injective slot reuse.

## GC2lb: canonical maximum-deficit core

If the maximum matching size is `nu<|U|`, put `delta=|U|-nu`. Among all subsets with `|X|-|N(X)|=delta`, choose minimum cardinality and then the lexicographically least complete cleaning address. The returned `X_*` is canonical and every proper subset has deficit strictly below `delta`.

## GC2lc: saturation and essentiality

A maximum matching on `X_*` saturates every slot in `N(X_*)`, leaves exactly `delta` cause uses unmatched and preserves all donor, remedy, height, source and cause fields. Removing any retained cause use lowers the maximum core deficit by at least one.

## GC2ld: geometric interface and resets

Each localized cause collision is therefore resolved by an injective realization or returns one exact finite cleaning Hall core. Remaining work is proving Hall from concrete donor/remedy/height incidence and capacities, adding named deposits, or excluding/paying the returned cause core. Omitted causes or slots, suppressed geometry or conditioning, hidden issuance, splitting, relabelling, untagged feedback or reuse reset the theorem.

This theorem does not prove GC5 or the no-three-in-line conjecture.