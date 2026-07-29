# GC2 cleaning repair-source compatibility dictionary

## Contract

Fix selected cause-repair incidences `R` and live cleaning-source tokens `S`. Each record retains the exact physical source, donor, remedy, height, cause, local geometry and epoch. The deterministic geometric predicate `Compat(r,s)` is evaluated from those fields, and the stored dictionary `E` must equal the compatible-pair set.

The preceding source-conservation block supplies an injective one-use debit map `d:R->S` with each token live at debit time.

## GC2lt--GC2lx

1. Complete donor/remedy/height and physical-source addresses determine compatibility without hidden geometry.
2. The stored graph is exact iff `E={(r,s):Compat(r,s)}`.
3. Exactness and `Compat(r,d(r))` make the debit map an explicit matching supplying every selected cause incidence without reuse.
4. The least discrepancy is a canonical missing true edge or spurious false edge. Omitted geometry, stale epochs and relabelled donor/remedy/height addresses are exact reset witnesses.
5. Every witness retains cause, donor, remedy, height, physical source and local-resampling fields; untagged feedback or hidden compatibility is not payment.

## Deterministic audit

`python scripts/verify_gc_repair_source_compatibility_dictionary.py`

The audit checks 2,600 systems, 19,352 selected cause incidences, 26,989 source tokens and 214,401 pairs. It finds 1,170 exact dictionaries and 1,430 first failures: 312 missing true edges, 272 spurious false edges, 290 omitted fields, 268 stale epochs and 288 relabelled addresses.

## Scope

This does not construct the geometric cleaning dictionary, prove GC5 or prove the no-three-in-line conjecture. Remaining work is verifying concrete donor/remedy/height compatibility or discharging the returned exact witness.
