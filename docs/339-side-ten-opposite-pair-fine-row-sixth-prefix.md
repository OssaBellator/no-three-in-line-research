# Side-ten opposite-pair fine-row sixth prefix

This chapter records the exact side-ten opposite-pair double-coset searches for pair indices `2000` through `2399` in the two remaining fine-row orientations. It is a finite obstruction, not a recursive closure theorem.

## PX1092 — `fc` obstruction on indices 2000 through 2399

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 2000 | 2,159,382 | 109,513 |
| 2100 | 2,052,531 | 98,292 |
| 2200 | 5,243,099 | 521,147 |
| 2300 | 8,662,717 | 955,107 |
| Total | 18,117,729 | 955,107 |

## PX1093 — `ff` obstruction on indices 2000 through 2399

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 2000 | 1,835,243 | 226,247 |
| 2100 | 2,304,264 | 153,011 |
| 2200 | 3,124,937 | 873,267 |
| 2300 | 3,284,811 | 270,865 |
| Total | 10,549,255 | 873,267 |

GitHub Actions run `30323383298` completed all eight interval jobs.

## PX1094 — cumulative fine-row boundary

The exact fine-row obstruction now covers pair indices `0` through `2399` in both orientations:

- `fc`: 2,400 geometries, `40,119,413` nodes, maximum `955,107`;
- `ff`: 2,400 geometries, `41,948,761` nodes, maximum `909,040`.

No constructive witness appears in these 4,800 fine-row geometries. The next bounded prefix begins at pair index `2400`.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_2000_2399.py
```
