# Side-ten opposite-pair fine-row ninth prefix

This chapter records the exact side-ten opposite-pair double-coset searches for pair indices `3200` through `3599` in the two remaining fine-row orientations. It is a finite obstruction, not a recursive closure theorem.

## PX1133 — `fc` obstruction on indices 3200 through 3599

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 3200 | 5,716,774 | 319,997 |
| 3300 | 3,825,283 | 421,080 |
| 3400 | 3,384,865 | 213,636 |
| 3500 | 3,657,273 | 149,780 |
| Total | 16,584,195 | 421,080 |

## PX1134 — `ff` obstruction on indices 3200 through 3599

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 3200 | 1,989,681 | 110,191 |
| 3300 | 2,251,035 | 194,878 |
| 3400 | 1,749,589 | 213,367 |
| 3500 | 1,620,334 | 85,076 |
| Total | 7,610,639 | 213,367 |

GitHub Actions run `30326638624` completed all eight interval jobs.

## PX1135 — cumulative fine-row boundary

The exact fine-row obstruction now covers pair indices `0` through `3599` in both orientations:

- `fc`: 3,600 geometries, `108,097,044` nodes, maximum `1,387,828`;
- `ff`: 3,600 geometries, `72,006,698` nodes, maximum `909,040`.

No constructive witness appears in these 7,200 fine-row geometries. The next bounded prefix begins at pair index `3600`.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_3200_3599.py
```
