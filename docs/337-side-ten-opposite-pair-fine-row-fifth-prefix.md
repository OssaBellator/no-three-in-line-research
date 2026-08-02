# Side-ten opposite-pair fine-row fifth prefix

This chapter records the exact side-ten opposite-pair double-coset searches for pair indices `1600` through `1999` in the two remaining fine-row orientations. It is a finite obstruction, not a recursive closure theorem.

## PX1085 — `fc` obstruction on indices 1600 through 1999

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 1600 | 1,983,296 | 135,219 |
| 1700 | 2,926,390 | 118,965 |
| 1800 | 1,094,675 | 32,800 |
| 1900 | 1,056,998 | 30,605 |
| Total | 7,061,359 | 135,219 |

## PX1086 — `ff` obstruction on indices 1600 through 1999

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 1600 | 1,728,800 | 72,527 |
| 1700 | 1,680,046 | 66,093 |
| 1800 | 667,922 | 22,250 |
| 1900 | 714,352 | 27,231 |
| Total | 4,791,120 | 72,527 |

GitHub Actions run `30321624738` completed all eight interval jobs.

## PX1087 — cumulative fine-row boundary

The exact fine-row obstruction now covers pair indices `0` through `1999` in both orientations:

- `fc`: 2,000 geometries, `22,001,684` nodes, maximum `170,613`;
- `ff`: 2,000 geometries, `31,399,506` nodes, maximum `909,040`.

No constructive witness appears in these 4,000 fine-row geometries. The next bounded prefix begins at pair index `2000`.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_1600_1999.py
```
