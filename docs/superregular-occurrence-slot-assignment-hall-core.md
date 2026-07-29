# Superregular occurrence-slot assignment Hall core

This block converts localized burden collisions into one finite burden-use to candidate/witness-slot assignment problem. It is conditional on a complete conditioned threshold, candidate, witness-atom and physical-source dictionary.

## SRR2ei: unit assignment network

Let `U` be the localized burden-use claims and `S` the faithful candidate/witness-atom occurrence slots. Join `u` to `s` exactly when the complete threshold, conditioning, candidate, witness atom, physical source and burden fields permit that use to debit that slot. The unit network `source -> U -> S -> sink` has integral maximum flow equal to the largest injective one-use realization.

## SRR2ej: exact Hall criterion

All burden uses have injective one-use lineage if and only if the maximum matching has size `|U|`, equivalently `|N(X)| >= |X|` for every `X subseteq U`. A complete matching debits each candidate/witness slot once and excludes duplicate burden consumption and non-injective atom-capacity reuse.

## SRR2ek: canonical maximum-deficit core

If the maximum matching size is `nu<|U|`, put `delta=|U|-nu`. Among all subsets with `|X|-|N(X)|=delta`, choose minimum cardinality and then the lexicographically least complete conditioned burden address. The returned `X_*` is canonical and every proper subset has deficit below `delta`.

## SRR2el: saturation and essentiality

A maximum matching on `X_*` saturates every slot in `N(X_*)`, leaves exactly `delta` burden uses unmatched and preserves threshold, candidate, witness-atom, conditioning and source fields. Removing any retained burden use lowers the maximum core deficit by at least one.

## SRR2em: geometric interface and resets

Each localized burden collision is therefore resolved by an injective assignment or returns one exact finite burden Hall core. Remaining work is proving Hall from the concrete tensor reference and forward/reverse/conditioning incidence, adding named capacities, or excluding/paying the core. Omitted candidates, witnesses or slots, changed conditioning or threshold, hidden capacity, splitting, relabelling or reuse reset the theorem.

This theorem does not prove SRR2, SRR4 or the no-three-in-line conjecture.