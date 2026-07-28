# Side-ten opposite-pair fine-row eleventh prefix

This chapter records the exact side-ten opposite-pair double-coset searches for pair indices `4000` through `4399` in the two remaining fine-row orientations. It is a finite obstruction, not a recursive closure theorem.

## PX1177 — `fc` obstruction on indices 4000 through 4399

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 4000 | 3,575,001 | 221,153 |
| 4100 | 3,440,083 | 618,518 |
| 4200 | 5,245,873 | 667,002 |
| 4300 | 5,704,438 | 860,978 |
| Total | 17,965,395 | 860,978 |

## PX1178 — `ff` obstruction on indices 4000 through 4399

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 4000 | 2,341,449 | 235,532 |
| 4100 | 1,595,971 | 99,407 |
| 4200 | 2,603,319 | 276,463 |
| 4300 | 2,787,182 | 390,524 |
| Total | 9,327,921 | 390,524 |

GitHub Actions run `30360563197` completed all eight interval jobs.

## PX1179 — cumulative fine-row boundary

The exact fine-row obstruction now covers pair indices `0` through `4399` in both orientations:

- `fc`: 4,400 geometries, `138,359,228` nodes, maximum `1,387,828`;
- `ff`: 4,400 geometries, `91,464,487` nodes, maximum `909,040`.

No constructive witness appears in these 8,800 fine-row geometries. The next bounded prefix begins at pair index `4400`.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_4000_4399.py
```
