# SAS5 typed repair-neutral compatibility dictionary

## Contract

Fix selected typed pair/completion repair incidences `R` and live boundary-neutral source/move tokens `S`. Each record retains pair-or-completion type, sign, boundary profile, neutral move, legality class, physical source and epoch. The deterministic predicate `Compat(r,s)` is evaluated from that complete address, and the stored dictionary `E` must equal the compatible-pair set.

The preceding neutral-conservation block supplies an injective one-use debit map `d:R->S` with live tokens.

## SAS5mn--SAS5mr

1. Complete sign, profile, legality, move and physical-source addresses determine compatibility without hidden state.
2. The stored graph is exact iff `E={(r,s):Compat(r,s)}`.
3. Exactness and `Compat(r,d(r))` turn the conserved debit map into an explicit matching supplying every selected pair/completion incidence.
4. The least discrepancy is a canonical missing true edge or spurious false edge; omitted legality fields, stale epochs and relabelled boundary-neutral addresses are exact reset witnesses.
5. Pair/completion type and every sign, profile, move, legality and source field persist in the witness; nonneutral or unrecorded capacity is not payment.

## Deterministic audit

`python scripts/verify_sas_typed_repair_neutral_compatibility_dictionary.py`

The audit checks 2,700 systems, 20,340 selected incidences, 28,272 neutral tokens and 226,822 pairs. It finds 1,245 exact dictionaries and 1,455 first failures: 306 missing true edges, 255 spurious false edges, 313 omitted fields, 299 stale epochs and 282 relabelled addresses. The selected set contains 10,112 pair and 10,228 completion incidences.

## Scope

This does not construct the boundary-neutral dictionary, prove SAS6 or prove the no-three-in-line conjecture. Remaining work is verifying concrete pair/completion compatibility or discharging the returned exact witness under sign, boundary and legality constraints.
