# Side-ten opposite-pair fine-row seventh prefix

This chapter records the exact side-ten opposite-pair double-coset searches for pair indices `2400` through `2799` in the two remaining fine-row orientations. It is a finite obstruction, not a recursive closure theorem.

## PX1095 — `fc` obstruction on indices 2400 through 2799

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 2400 | 4,563,766 | 810,889 |
| 2500 | 6,895,140 | 811,641 |
| 2600 | 2,801,776 | 263,333 |
| 2700 | 2,448,213 | 409,736 |
| Total | 16,708,895 | 811,641 |

## PX1096 — `ff` obstruction on indices 2400 through 2799

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 2400 | 2,371,220 | 145,572 |
| 2500 | 1,939,029 | 314,014 |
| 2600 | 2,556,553 | 200,371 |
| 2700 | 1,889,038 | 100,172 |
| Total | 8,755,840 | 314,014 |

GitHub Actions run `30324357836` completed all eight interval jobs.

## PX1097 — cumulative fine-row boundary

The exact fine-row obstruction now covers pair indices `0` through `2799` in both orientations:

- `fc`: 2,800 geometries, `56,828,308` nodes, maximum `955,107`;
- `ff`: 2,800 geometries, `50,704,601` nodes, maximum `909,040`.

No constructive witness appears in these 5,600 fine-row geometries. The next bounded prefix begins at pair index `2800`.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_2400_2799.py
```
