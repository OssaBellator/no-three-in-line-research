# Geometric-cleaning occurrence-slot collision lineage

This note records GC2ku--GC2ky. It refines the physical-source-prefix and internal merge--segment--split cleaning witnesses from GC2kp--GC2kt.

## Contract

Fix the complete physical/remedy/height/cause network, canonical cause-path pair, maximal common segment and ordered segment slots. Every slot carries one complete physical cleaning occurrence, including donor, remedy, height and cause fields, and each successful use is debited once.

## Theorem

1. Every localized cause-path collision has a canonical least occupied segment slot.
2. Equal occurrence tokens give an exact double consumption of one physical cleaning occurrence.
3. Distinct occurrence tokens assigned to the same slot give a non-injective remedy/height capacity dictionary, with both geometric addresses retained.
4. A missing token returns the first absent donor, remedy, height-source or predecessor-lineage record.
5. Thus injective occurrence-to-slot labelling with one-use debits excludes every cause-path collision. Untagged feedback, hidden deposits, relabelling, slot reuse or changed cleaning state is a reset.

## Deterministic audit

Run `python scripts/verify_gc_occurrence_slot_collision_lineage.py`.

No statement here proves GC5 or the no-three-in-line conjecture.