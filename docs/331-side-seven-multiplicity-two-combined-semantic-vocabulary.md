# Combined semantic vocabulary for thirty references

PX1030--PX1032 and PX1054--PX1057 analyze two disjoint collections of repeated paired-equal support classes for multiplicity-two case zero, orientation three. This chapter recomputes the actual partial-assignment vocabulary and clean-top union across all thirty references simultaneously.

This is a finite certificate-compression result, not a complete classification of the top-order family.

## PX1062 — combined vocabulary

The thirty semantically minimized reference cores deduplicate to exactly twenty-one actual partial assignments. Their mask distribution is:

| Mask | Keys |
|---:|---:|
| `6920` | 1 |
| `6936` | 4 |
| `7432` | 1 |
| `7448` | 1 |
| `8984` | 1 |
| `9496` | 1 |
| `11032` | 7 |
| `11544` | 5 |
| Total | 21 |

Both selectors use the same semantic mask at every reference, so no selector-union penalty occurs.

## PX1063 — exact cross-group union

The thirty extension sets contain ninety-five occurrences in total. Their exact union contains fifty-seven distinct clean top orders, so the combined vocabulary has

`95 - 57 = 38`

repeated extension occurrences.

The two separate measurements had union sizes fourteen and forty-seven. Their sum is sixty-one, so four clean top orders lie in both support-group unions. This is the first exact cross-group overlap measurement.

## PX1064 — measured coverage ratio

The thirty reference cores themselves account for thirty of the fifty-seven covered top orders. The twenty-one stored keys therefore certify twenty-seven additional clean top orders beyond their chosen references.

Relative to the first sixty-four top orders used to select these support classes, the combined vocabulary certifies at least fifty-seven distinct orders. This statement does not claim that the covered set is contained entirely in the first sixty-four enumeration positions, only that the references were selected from that prefix.

## PX1065 — exact bottom verification

Both selector covers are replayed for every extension against all `5,040` bottom permutations. The combined measurement uses `957,600` exact bottom checks and has ordered transcript digest

`14270700727048114206`.

GitHub Actions run `30319666141` completed the exact measurement.

## Consequence

The measured repeated paired-equal support classes already yield a compact twenty-one-key master vocabulary. The next semantic frontier is to process unequal-support and singleton reference classes, then solve a set-cover problem over the complete clean-top order family.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_combined.py
```
