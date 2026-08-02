# Side-ten opposite-pair fine-row sixteenth prefix

This chapter records the exact side-ten opposite-pair double-coset searches for pair indices `6000` through `6399` in the two remaining fine-row orientations. It is a finite obstruction, not a recursive closure theorem.

## PX1215 — `fc` obstruction on indices 6000 through 6399

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 6000 | 469,639 | 17,824 |
| 6100 | 547,596 | 17,172 |
| 6200 | 638,837 | 23,756 |
| 6300 | 747,433 | 21,420 |
| Total | 2,403,505 | 23,756 |

## PX1216 — `ff` obstruction on indices 6000 through 6399

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 6000 | 531,863 | 17,818 |
| 6100 | 561,966 | 23,590 |
| 6200 | 1,489,081 | 76,725 |
| 6300 | 1,387,628 | 46,602 |
| Total | 3,970,538 | 76,725 |

GitHub Actions run `30746691737` produced the first exact matrix. Run `30746882426` independently replayed the deterministic expected outputs before promotion.

## PX1217 — cumulative fine-row boundary

The exact fine-row obstruction now covers pair indices `0` through `6399` in both orientations:

- `fc`: 6,400 geometries, `224,654,411` nodes, maximum `1,877,339`;
- `ff`: 6,400 geometries, `135,595,069` nodes, maximum `909,040`.

No constructive witness appears in these 12,800 fine-row geometries. The next bounded prefix begins at pair index `6400`.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_6000_6399.py
```
