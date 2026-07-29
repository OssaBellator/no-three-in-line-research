# Bounded-denominator occurrence-slot assignment Hall core

This block converts localized restoration collisions into one finite primitive-potential use-to-slot assignment problem. It is conditional on complete restoration-use, physical-potential-slot and arithmetic compatibility dictionaries.

## BDA5gb: unit assignment network

Let `U` be the localized restoration-use claims and `S` the faithful primitive-potential occurrence slots. Join `u` to `s` exactly when all retained denominator, primitive weight, gain, damping, predecessor, source and restoration fields permit that use to debit that slot. The unit-capacity network `source -> U -> S -> sink` has integral maximum flow equal to the largest injective one-use realization.

## BDA5gc: exact Hall criterion

All restoration uses are realized injectively if and only if the maximum matching has size `|U|`, equivalently `|N(X)| >= |X|` for every `X subseteq U`. A complete matching debits each primitive-potential slot once and excludes duplicate potential consumption and non-injective arithmetic slot reuse.

## BDA5gd: canonical maximum-deficit core

If the maximum matching size is `nu<|U|`, set `delta=|U|-nu`. Choose, among all subsets with `|X|-|N(X)|=delta`, one of minimum cardinality and then the lexicographically least complete arithmetic address. The resulting `X_*` is canonical and every proper subset has deficit strictly below `delta`.

## BDA5ge: saturation and essentiality

A maximum matching on `X_*` saturates every slot in `N(X_*)`, leaves exactly `delta` restoration uses unmatched and preserves every primitive weight, gain, damping, source and restoration address. Removing any retained use lowers the maximum core deficit by at least one.

## BDA5gf: arithmetic interface and resets

Every localized restoration collision is therefore resolved by an injective assignment or returns one exact finite Hall core. Remaining work is to derive the Hall inequalities from concrete rational gains and physical potential stocks, add named exogenous potential slots, or prove the returned core arithmetically impossible. Omitted uses or slots, changed gains or damping, suppressed predecessor fields, hidden issuance, splitting, relabelling or reuse reset the theorem.

This theorem does not prove BDA6 or the no-three-in-line conjecture.