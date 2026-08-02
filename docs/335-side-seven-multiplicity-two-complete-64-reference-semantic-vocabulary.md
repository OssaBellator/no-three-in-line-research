# Complete 64-reference semantic vocabulary

Earlier chapters semantically minimize the repeated paired-equal support classes of multiplicity-two case zero, orientation three. This chapter processes every one of the first 64 clean top orders, including all unequal-support references, and computes the complete measured master-nogood vocabulary.

This is a finite certificate-compression theorem for one signature and orientation, not a complete multiplicity-two proof by covers.

## PX1076 — complete reference census

All 64 reference top orders are semantically minimized for both selectors. Exactly thirty references give identical selector masks. The other thirty-four require a union of two distinct selector masks.

The exact pair-core size distribution is:

| Pair-core columns | References |
|---:|---:|
| 5 | 4 |
| 6 | 36 |
| 7 | 16 |
| 8 | 7 |
| 9 | 1 |
| Total | 64 |

Thus forty of the 64 reference pairs are certified by at most six fixed top columns.

## PX1077 — complete actual-key vocabulary

Deduplicating pair mask and retained values reduces the 64 reference cores to exactly 49 actual partial assignments. These keys use thirty distinct pair-mask shapes.

The reference-to-key compression is therefore `64 -> 49`.

## PX1078 — exact clean-top union

The extension sets of the 64 keys contain 169 occurrences. Their exact union contains 92 distinct clean top orders, so 77 extension occurrences are duplicates.

The vocabulary certifies 28 additional clean top orders beyond the 64 selected references.

## PX1079 — selector-alignment boundary

All thirty references in the six repeated paired-equal support groups retain equal selector masks after semantic deletion. None of the remaining thirty-four unequal-support references does. Therefore the selector-aligned and selector-union regimes coincide exactly with the syntactic paired-equal/unequal partition on this measured prefix.

This observation is finite and does not assert the same partition for later top orders or other signatures.

## PX1080 — exact bottom verification

For every measured extension, both stored selector covers are replayed against all `5,040` bottom permutations. The complete census uses `1,703,520` exact bottom checks and has ordered transcript digest

`8868513888596877870`.

GitHub Actions run `30321409199` completed the exact measurement.

## Consequence

The first 64 reference orders can be replaced by 49 replayable master keys that jointly certify 92 clean top orders. The next compression target is to enumerate new support classes beyond top index 63, reuse existing keys when possible, and select a minimum or near-minimum set-cover basis for the full clean-top family.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_full64.py
```
