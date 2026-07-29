# Sparse typed occurrence-slot collision lineage

This note records SAS5lt--SAS5lx. It refines the typed neutral-source-prefix and internal merge--segment--split witnesses from SAS5lo--SAS5ls.

## Contract

Fix the complete neutral-source/move/pair-completion network, canonical typed path pair, maximal common segment and ordered slots. Every occupied slot carries one complete physical neutral occurrence including pair/completion type, sign, boundary profile and move address, and each use is debited once.

## Theorem

1. Every localized pair/completion collision has a canonical least occupied segment slot.
2. Equal occurrence tokens give an exact double consumption of one boundary-neutral occurrence.
3. Distinct tokens assigned to the same slot give a non-injective neutral-move dictionary, retaining both typed terminal and boundary addresses.
4. A missing token returns the first absent neutral-source, move, sign or legality-lineage record.
5. Thus injective occurrence-to-slot labelling with one-use debits excludes every typed collision. Hidden move creation, suppressed legality fields, relabelling, slot reuse or changed boundary state is a reset.

## Deterministic audit

Run `python scripts/verify_sas_typed_occurrence_slot_collision_lineage.py`.

No statement here proves SAS6 or the no-three-in-line conjecture.