# Rational-inverse typed occurrence-slot collision lineage

This note records RI5fn--RI5fr. It refines the typed physical-source-prefix and internal merge--segment--split witnesses from RI5fi--RI5fm.

## Contract

Fix the complete physical-source/collateral/owner-charge network, canonical typed path pair, maximal common segment and ordered segment slots. Every slot carries one complete arithmetic physical occurrence, including owner/charge type, retained field, source and collateral addresses, and every use is debited once.

## Theorem

1. Every typed owner/charge collision has a canonical least occupied segment slot.
2. Equal occurrence tokens give an exact double consumption of one arithmetic occurrence, with both terminal types retained.
3. Distinct tokens assigned to the same slot give a non-injective collateral-slot dictionary and retain the two conflicting arithmetic addresses.
4. A missing token returns the first absent source, collateral, owner or perturbation-lineage field.
5. Therefore injective occurrence-to-slot labelling with one-use debits forbids every typed collision. Suppressed type fields, changed retained arithmetic, hidden issuance, relabelling or slot reuse is a reset.

## Deterministic audit

Run `python scripts/verify_ri_typed_occurrence_slot_collision_lineage.py`.

No statement here proves RI6 or the no-three-in-line conjecture.