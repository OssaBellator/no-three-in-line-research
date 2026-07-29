# AC5 repair-source compatibility dictionary

## Contract

Fix a finite ordered set `R` of selected repair incidences and a finite ordered set `S` of live occurrence-faithful source tokens. Every incidence and token carries its complete physical source, certificate, defect, epoch and repair-class address. A deterministic predicate `Compat(r,s)` is evaluated from those retained fields, and the stored dictionary `E` is required to contain exactly the compatible pairs.

The preceding source-conservation block supplies an injective one-use debit map `d:R->S` and verifies that every debited token is live at its debit time.

## AC5fk--AC5fo

1. The complete retained addresses determine `Compat(r,s)` without hidden state.
2. The dictionary is exact precisely when `E={(r,s):Compat(r,s)}`.
3. If the dictionary is exact and every selected debit satisfies `Compat(r,d(r))`, then `d` is an explicit matching of all selected repair incidences into live source tokens. In particular every deficit-sized transversal is physically supplied without reuse.
4. If the dictionary is not exact, the least pair in the fixed product order is a canonical missing-true-edge or spurious-false-edge witness. If a required field is absent, evaluated in a stale epoch or relabelled, the least such record is returned instead.
5. All witnesses retain the full physical/source/certificate/defect and repair-class address. Omitted compatibility, hidden fields or unrecorded relabelling reset the argument rather than being treated as payment.

## Deterministic audit

`python scripts/verify_ac_repair_source_compatibility_dictionary.py`

The audit checks 2,600 systems, 19,356 selected incidences, 27,227 source tokens and 216,740 incidence-token pairs. It finds 1,227 exact dictionaries and classifies 1,373 first failures as 305 missing true edges, 235 spurious false edges, 278 omitted fields, 249 stale epochs and 306 relabelled addresses.

## Scope

This is a finite contract theorem. It does not construct the geometric AC5 source dictionary, prove AC5 or prove the no-three-in-line conjecture. The remaining task is to verify the concrete physical compatibility predicate or discharge the returned exact dictionary witness.
