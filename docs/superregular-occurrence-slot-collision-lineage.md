# Superregular occurrence-slot collision lineage

This note records SRR2ed--SRR2eh. It refines the physical-source-prefix and internal merge--segment--split burden witnesses from SRR2dy--SRR2ec.

## Contract

Fix one conditioned threshold, the complete physical-source/witness-atom/burden network, canonical burden-path pair, maximal common segment and ordered slots. Every slot carries one complete candidate/witness physical occurrence and every use is debited once.

## Theorem

1. Every localized burden-path collision has a canonical least occupied segment slot.
2. Equal occurrence tokens give an exact double consumption of one candidate/witness occurrence.
3. Distinct occurrence tokens assigned to the same slot give a non-injective atom-capacity dictionary, retaining both candidate, threshold and witness addresses.
4. A missing token returns the first absent physical-source, conditioning or witness-lineage record.
5. Hence injective occurrence-to-slot labelling with one-use debits excludes every burden collision. Hidden atom capacity, omitted witnesses, relabelling, slot reuse or changed conditioning is a reset.

## Deterministic audit

Run `python scripts/verify_srr_occurrence_slot_collision_lineage.py`.

No statement here proves SRR2, SRR4 or the no-three-in-line conjecture.