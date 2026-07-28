# Side-ten opposite-pair fine-row tenth prefix

This chapter records the exact side-ten opposite-pair double-coset searches for pair indices `3600` through `3999` in the two remaining fine-row orientations. It is a finite obstruction, not a recursive closure theorem.

## PX1136 — `fc` obstruction on indices 3600 through 3999

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 3600 | 2,528,158 | 146,051 |
| 3700 | 4,284,334 | 256,437 |
| 3800 | 2,912,136 | 111,426 |
| 3900 | 2,572,161 | 149,592 |
| Total | 12,296,789 | 256,437 |

## PX1137 — `ff` obstruction on indices 3600 through 3999

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 3600 | 3,456,168 | 616,766 |
| 3700 | 3,044,983 | 280,226 |
| 3800 | 1,943,360 | 124,984 |
| 3900 | 1,685,357 | 89,347 |
| Total | 10,129,868 | 616,766 |

GitHub Actions run `30327332584` completed all eight interval jobs.

## PX1138 — cumulative fine-row boundary

The exact fine-row obstruction now covers pair indices `0` through `3999` in both orientations:

- `fc`: 4,000 geometries, `120,393,833` nodes, maximum `1,387,828`;
- `ff`: 4,000 geometries, `82,136,566` nodes, maximum `909,040`.

No constructive witness appears in these 8,000 fine-row geometries. The next bounded prefix begins at pair index `4000`.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_3600_3999.py
```
