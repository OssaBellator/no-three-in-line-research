# RI5 typed repair-collateral compatibility dictionary

## Contract

Fix selected typed owner/charge repair incidences `R` and live physical-source/collateral tokens `S`. Each record retains owner-or-charge type, field element data, host/context, secant or line address, coherence, collateral class and epoch. The deterministic predicate `Compat(r,s)` is evaluated from the complete arithmetic address, and the stored dictionary `E` must contain exactly the compatible pairs.

The preceding collateral-conservation block supplies an injective one-use debit map `d:R->S` with live tokens.

## RI5gm--RI5gq

1. Complete typed arithmetic addresses determine compatibility without hidden state.
2. The dictionary is exact iff `E={(r,s):Compat(r,s)}`.
3. Exactness and `Compat(r,d(r))` turn the conserved debit map into an explicit matching of all selected owner/charge incidences into live collateral tokens.
4. The least dictionary discrepancy is a canonical missing true edge or spurious false edge; omitted fields, stale epochs and relabelled arithmetic addresses are returned as exact reset witnesses.
5. Owner/charge type and every physical, collateral, secant/line, host/context and coherence field persist in the witness. No omitted field or relabelled collateral is treated as supplied capacity.

## Deterministic audit

`python scripts/verify_ri_typed_repair_collateral_compatibility_dictionary.py`

The audit checks 2,600 systems, 19,307 selected incidences, 26,980 collateral tokens and 214,318 pairs. It finds 1,192 exact dictionaries and 1,408 first failures: 274 missing true edges, 309 spurious false edges, 286 omitted fields, 254 stale epochs and 285 relabelled addresses. The selected debit set contains 9,657 owner and 9,650 charge incidences.

## Scope

This does not construct the RI arithmetic dictionary, prove RI6 or prove the no-three-in-line conjecture. The remaining task is to verify concrete owner/charge compatibility or discharge the returned exact witness.
