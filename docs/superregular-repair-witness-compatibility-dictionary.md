# SRR2 repair-witness compatibility dictionary

## Contract

Fix selected burden-repair incidences `R` and live candidate/witness-source tokens `S`. Each record retains candidate, witness atom, conditioned threshold, physical source, tensor cylinder and epoch fields. The deterministic predicate `Compat(r,s)` is evaluated from that complete address, and the stored dictionary `E` must equal the compatible-pair set.

The preceding witness-conservation block supplies an injective one-use debit map `d:R->S` with live tokens.

## SRR2ex--SRR2fb

1. Complete candidate, witness, conditioning and source addresses determine compatibility without hidden state.
2. The stored graph is exact iff `E={(r,s):Compat(r,s)}`.
3. Exactness and `Compat(r,d(r))` make the conserved debit map an explicit matching supplying every selected burden incidence.
4. The least discrepancy is a canonical missing true edge or spurious false edge; omitted witness fields, stale conditioning epochs and relabelled addresses are exact reset witnesses.
5. Every witness retains the candidate, threshold, tensor-cylinder, witness-atom and physical-source fields; hidden capacity or changed conditioning is not payment.

## Deterministic audit

`python scripts/verify_srr_repair_witness_compatibility_dictionary.py`

The audit checks 2,800 systems, 21,142 selected burden incidences, 29,660 witness-source tokens and 238,273 pairs. It finds 1,263 exact dictionaries and 1,537 first failures: 282 missing true edges, 301 spurious false edges, 326 omitted fields, 317 stale epochs and 311 relabelled addresses.

## Scope

This does not construct the tensor-reference witness dictionary, prove SRR2 or SRR4, or prove the no-three-in-line conjecture. Remaining work is verifying concrete conditioned compatibility or discharging the returned exact witness.
