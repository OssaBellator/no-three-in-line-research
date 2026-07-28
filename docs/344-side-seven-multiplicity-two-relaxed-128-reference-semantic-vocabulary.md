# Relaxed 128-reference semantic vocabulary

The original semantic minimizer assumed that every greedy bottom cover had exactly seven triples. That is true for top indices `0` through `63`, but fails later. This chapter removes only that cardinality assertion; it retains exact greedy covering, semantic deletion, extension enumeration, and bottom-cover replay.

## PX1109 — first cover-size transition

Across top indices `0` through `127`:

- selector 0 has a seven-triple greedy cover at 125 references and a twelve-triple cover at 3 references;
- selector 1 has a seven-triple greedy cover at all 128 references.

All three twelve-triple events occur in the new `64--127` block. This is the exact reason the strict seven-cover extension aborts.

## PX1110 — complete 128-reference vocabulary

The 128 pair cores deduplicate to 102 actual partial-assignment keys on 49 mask shapes. Relative to the first-64 baseline:

- 53 genuinely new keys appear;
- 7 later references reuse a baseline key;
- aligned selector masks increase from 30 to 40, so 10 of the later references remain aligned.

## PX1111 — pair-core size profile

The complete pair-core size distribution is

- size 5: 7 references;
- size 6: 45;
- size 7: 35;
- size 8: 34;
- size 9: 7.

For the new block alone the distribution is `5:3, 6:9, 7:19, 8:27, 9:6`.

## PX1112 — extension union

The 102-key vocabulary has 316 extension occurrences whose exact union contains 164 clean top orders. The new block contributes 147 occurrences and increases the union by 72 orders. Total overlap is 152 occurrences.

## PX1113 — exact replay load

Both selector covers are replayed on every extension using 3,185,280 exact bottom checks, of which 1,481,760 belong to the new block. The ordered digest is `14068988073173727216`.

The result demonstrates continued vocabulary growth rather than saturation: 53 new keys arise from 64 new references, although seven references already reuse the baseline vocabulary.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_full128_relaxed.py
```
