# Alternating-core occurrence-slot collision lineage

This note records AC5el--AC5ep. It refines the canonical source-prefix and internal merge--segment--split witnesses from AC5eg--AC5ek.

## Contract

Fix the complete physical/source/certificate/defect network, the canonical cycle-cancelled path pair, its maximal common segment, and the ordered capacity slots on every segment edge. Every occupied slot carries its complete physical occurrence token and every successful use debits that token exactly once.

## Theorem

1. Every localized collision pair has a canonical least occupied slot: the first common-segment edge, then the least paired capacity index on that edge.
2. If the two defect paths carry the same physical occurrence token at that slot, the witness is an exact double consumption of one occurrence.
3. If they carry distinct physical occurrence tokens at the same slot, the retained slot dictionary is non-injective and the complete physical address has been collapsed.
4. If either token is absent, the occurrence lineage is incomplete and the first missing predecessor/issuance record is returned.
5. Consequently an injective occurrence-to-slot map with one-use debits forbids every cross-side collision. Relabelling, hidden issuance, slot reuse after debit, path suppression, or changed physical meaning is a reset rather than payment.

The statement is local: it does not construct the geometric compatibility graph or prove that its occurrence contract holds.

## Deterministic audit

Run `python scripts/verify_ac_occurrence_slot_collision_lineage.py`.

The audit generates complete finite slot dictionaries and adversarial collision claims, then checks the canonical trichotomy: duplicate occurrence, non-injective slot label, or missing lineage.

No statement here proves AC4, AC5, AC6 or the no-three-in-line conjecture.