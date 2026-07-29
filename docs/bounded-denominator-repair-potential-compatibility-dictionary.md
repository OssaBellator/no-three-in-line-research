# BDA5 repair-potential compatibility dictionary

## Contract

Fix selected restoration-repair incidences `R` and live primitive-potential tokens `S`. Every record retains the complete physical source, numerator weight, rational gain, damping factor, restoration class and epoch. The deterministic arithmetic predicate `Compat(r,s)` is evaluated from those fields, and the stored dictionary `E` must equal the set of compatible pairs.

The preceding potential-conservation block supplies an injective one-use debit map `d:R->S` and verifies that each debited token is live.

## BDA5gv--BDA5gz

1. Complete arithmetic addresses determine compatibility without hidden state.
2. The stored graph is exact iff `E={(r,s):Compat(r,s)}`.
3. Exactness plus `Compat(r,d(r))` for every selected debit makes `d` an explicit restoration-to-potential matching, so a deficit-sized transversal is supplied without double spending.
4. The least product-order discrepancy is a canonical missing true edge or spurious false edge. Missing gain/damping data, stale epochs and relabelled arithmetic addresses are returned as exact reset witnesses.
5. Every witness retains source, gain, damping, primitive-potential and restoration fields; omitted fields or unrecorded arithmetic changes cannot be counted as payment.

## Deterministic audit

`python scripts/verify_bda_repair_potential_compatibility_dictionary.py`

The audit checks 2,700 systems, 20,182 selected restoration incidences, 28,377 potential tokens and 226,285 pairs. It finds 1,245 exact dictionaries and 1,455 first failures: 296 missing true edges, 292 spurious false edges, 251 omitted fields, 308 stale epochs and 308 relabelled addresses.

## Scope

This does not construct the rational-gain dictionary, prove BDA6 or prove the no-three-in-line conjecture. The remaining work is verifying the concrete arithmetic compatibility predicate or discharging the returned exact witness.
