# Alternating-core occurrence-slot assignment Hall core

This block converts the occurrence-slot trichotomy into one complete finite assignment problem. It is conditional on a complete dictionary of localized defect-use claims, faithful physical/source/certificate slots and exact compatibility.

## AC5eq: unit assignment network

Let `U` be the finite set of localized defect-use claims and `S` the finite set of faithful occurrence slots. Join `u in U` to `s in S` exactly when the complete physical, issued-source, certificate, segment and defect fields permit that use to debit that slot. The network

`source -> U -> S -> sink`

has unit capacities on every source/use and slot/sink arc. Its integral maximum flow is an injective one-use occurrence realization.

## AC5er: exact Hall criterion

All localized uses admit injective one-use lineage if and only if the maximum matching has size `|U|`, equivalently

`|N(X)| >= |X|`

for every `X subseteq U`. A complete matching debits each retained physical slot at most once and therefore excludes duplicate consumption and non-injective slot reuse.

## AC5es: canonical maximum-deficit core

If the maximum matching has size `nu < |U|`, put `delta=|U|-nu`. Among all use sets maximizing `|X|-|N(X)|=delta`, choose first minimum cardinality and then lexicographically least complete address. This gives a canonical core `X_*` with

`|X_*|-|N(X_*)|=delta`.

Every proper subset of `X_*` has deficit strictly below `delta`.

## AC5et: exact core saturation and essentiality

A maximum matching on `X_*` saturates every slot in `N(X_*)`, leaves exactly `delta` core uses unmatched and preserves every physical/source/certificate/defect address. Removing any retained use lowers the maximum core deficit by at least one, so every use in the returned core is essential to the full shortage.

## AC5eu: physical interface and resets

Thus each localized collision is resolved by an injective assignment or returns one finite exact Hall core of defect uses versus faithful physical slots. The remaining physical obligation is to prove the Hall inequalities from the concrete restricted-menu incidence geometry, add named exogenous slots, or exclude/pay the returned core. Omitted uses or slots, suppressed compatibility fields, relabelling, splitting, hidden issuance, changed physical meaning or slot reuse reset the theorem.

This theorem does not prove AC5, AC6 or the no-three-in-line conjecture.