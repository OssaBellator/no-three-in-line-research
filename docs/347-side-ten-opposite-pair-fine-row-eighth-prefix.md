# Side-ten opposite-pair fine-row eighth prefix

This chapter records the exact side-ten opposite-pair double-coset searches for pair indices `2800` through `3199` in the two remaining fine-row orientations. It is a finite obstruction, not a recursive closure theorem.

## PX1122 — `fc` obstruction on indices 2800 through 3199

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 2800 | 4,794,532 | 497,413 |
| 2900 | 8,750,171 | 823,382 |
| 3000 | 8,192,818 | 1,387,828 |
| 3100 | 12,947,020 | 674,754 |
| Total | 34,684,541 | 1,387,828 |

## PX1123 — `ff` obstruction on indices 2800 through 3199

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 2800 | 4,522,407 | 740,706 |
| 2900 | 4,182,037 | 443,114 |
| 3000 | 2,625,942 | 191,947 |
| 3100 | 2,361,072 | 296,010 |
| Total | 13,691,458 | 740,706 |

GitHub Actions run `30325981315` completed all eight interval jobs.

## PX1124 — cumulative fine-row boundary

The exact fine-row obstruction now covers pair indices `0` through `3199` in both orientations:

- `fc`: 3,200 geometries, `91,512,849` nodes, maximum `1,387,828`;
- `ff`: 3,200 geometries, `64,396,059` nodes, maximum `909,040`.

No constructive witness appears in these 6,400 fine-row geometries. The next bounded prefix begins at pair index `3200`.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_2800_3199.py
```
