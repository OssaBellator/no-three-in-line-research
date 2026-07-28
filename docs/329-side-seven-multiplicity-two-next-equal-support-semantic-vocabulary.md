# Next equal-support semantic vocabulary

PX1030--PX1032 deduplicate the dominant repeated support class `6975`. This chapter performs semantic deletion and actual-assignment deduplication for the next five paired-equal support classes among the first 64 clean top orders of multiplicity-two case zero, orientation three.

This is a finite certificate-compression result, not a complete top-family classification.

## PX1054 — exact semantic deletion census

The measured syntactic support classes and reference indices are:

- `7487`: `8,10,11,62`;
- `11039`: `33,39,49,55`;
- `11071`: `3,32,36,37`;
- `11551`: `41,52,58`;
- `11583`: `5,38,40`.

Across all 18 references, both selectors minimize to the same semantic mask. The exact semantic-mask reference counts are:

| Semantic mask | References | Size |
|---:|---:|---:|
| `7432` | 1 | 5 |
| `7448` | 3 | 6 |
| `8984` | 1 | 5 |
| `9496` | 1 | 5 |
| `11032` | 7 | 6 |
| `11544` | 5 | 6 |

Thus fifteen references yield six-column pair cores and three yield five-column pair cores. No selector-union penalty occurs.

## PX1055 — actual assignment vocabulary

Deduplicating both mask and retained values reduces the 18 reference cores to exactly 16 partial assignments:

- one key on mask `7432`;
- one key on mask `7448`;
- one key on mask `8984`;
- one key on mask `9496`;
- seven keys on mask `11032`;
- five keys on mask `11544`.

The three references with mask `7448` share one actual key. The `11032` and `11544` references have distinct retained values and therefore remain separate vocabulary entries.

## PX1056 — union coverage

The extension-set sizes sum to `55`. After exact clean-top deduplication, the 16-key vocabulary covers `47` distinct clean top orders, leaving `8` repeated extension occurrences.

This improves the cumulative measured semantic vocabulary over the two studied support groups to:

- 30 reference cores;
- 21 distinct partial-assignment keys;
- 61 distinct covered clean top orders before cross-group union is recomputed.

The final number is an upper bound on the cross-group union because overlap between the two vocabulary groups has not yet been removed.

## PX1057 — exact bottom verification

Both selector covers are replayed on every measured extension against all `5,040` bottom permutations. The complete census uses `554,400` exact bottom checks and has ordered transcript digest

`1088196697277134895`.

GitHub Actions run `30319175851` completed the exact measurement.

## Consequence

Mask-shape compression alone is insufficient to predict actual-key compression. The `7448` class has strong value reuse, while `11032` and `11544` currently do not. The next proof-object target is a joint vocabulary census across all measured support groups, followed by semantic deletion for the unequal-support and singleton classes.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_next_equal.py
```
