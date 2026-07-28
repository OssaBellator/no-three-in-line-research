# Side-seven relaxed semantic vocabulary through 192 references

This chapter extends the exact semantic certificate census for multiplicity-two case zero, orientation three, from 128 to 192 clean-top references. It is a proof-compression result, not a classification of additional signatures.

## PX1153 — 192-reference vocabulary size

The 192 reference cores reduce to `150` actual partial-assignment keys on `57` mask classes.

The established 128-reference prefix contains `102` keys. References `128` through `191` add `48` genuinely new keys, while `15` of those later references reuse keys already present in the 128-prefix vocabulary.

## PX1154 — selector alignment profile

The two selector masks agree at `60` of the 192 references. The new 64-reference block contributes `20` aligned references.

The pair-mask size distribution over all 192 references is

`5:11, 6:64, 7:45, 8:56, 9:16`.

## PX1155 — cover-size stabilization

Across all 192 references:

- selector zero has 189 seven-triple covers and three twelve-triple covers;
- selector one has 192 seven-triple covers.

Every one of the 64 new references uses a seven-triple cover for both selectors. Thus the three selector-zero twelve-triple anomalies remain confined to the first 128 references in the measured prefix.

## PX1156 — clean-top coverage

The 150 keys have `443` total extension occurrences with an exact union of `204` clean top orders.

Relative to the 128-prefix:

- extension occurrences increase by `127`;
- the covered union increases by `40` clean top orders;
- overlap rises to `239` repeated extension occurrences.

Vocabulary growth therefore continues, but new coverage grows more slowly than raw extension count.

## PX1157 — exact bottom replay

All selector covers are replayed against every extension using `4,465,440` exact bottom checks. The new 64-reference block contributes `1,280,160` checks.

The next compression target is no longer merely more references. It is to compute a compact set-cover basis from the 150 keys and determine how much of the complete clean-top family can be certified by a much smaller master subset.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_full192_relaxed.py
```
