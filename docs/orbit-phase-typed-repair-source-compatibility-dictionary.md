# OP4 typed repair-source compatibility dictionary

## Contract

Fix selected typed residual/edit repair incidences `R` and live unit-sensitive source tokens `S`. Each record retains residual-or-edit type, physical source, unit class, valuation vector, holonomy, action-kernel and epoch fields. The deterministic predicate `Compat(r,s)` is evaluated from that complete address, and the stored dictionary `E` must equal the compatible-pair set.

The preceding source-conservation block supplies an injective one-use debit map `d:R->S` with live tokens.

## OP4fn--OP4fr

1. Complete unit, valuation, holonomy and physical-source addresses determine compatibility without hidden state.
2. The stored graph is exact iff `E={(r,s):Compat(r,s)}`.
3. Exactness and `Compat(r,d(r))` turn the conserved debit map into an explicit matching supplying every selected residual/edit incidence.
4. The least discrepancy is a canonical missing true edge or spurious false edge; omitted fields, stale epochs and relabelled unit-sensitive addresses are exact reset witnesses.
5. Residual/edit type and every unit, valuation, holonomy, kernel and source field persist in the witness; unrecorded source creation or field changes are not payment.

## Deterministic audit

`python scripts/verify_op_typed_repair_source_compatibility_dictionary.py`

The audit checks 2,800 systems, 20,919 selected incidences, 29,379 source tokens and 234,018 pairs. It finds 1,245 exact dictionaries and 1,555 first failures: 304 missing true edges, 340 spurious false edges, 312 omitted fields, 299 stale epochs and 300 relabelled addresses. The selected set contains 10,481 residual and 10,438 edit incidences.

## Scope

This does not construct the unit-sensitive source dictionary, prove OP5 or prove the no-three-in-line conjecture. Remaining work is verifying concrete residual/edit compatibility or discharging the returned exact witness.
