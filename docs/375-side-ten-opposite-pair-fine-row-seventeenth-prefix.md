# Side-ten opposite-pair fine-row seventeenth prefix

This chapter records the exact side-ten opposite-pair double-coset searches for pair indices `6400` through `6799` in the two remaining fine-row orientations. It is a finite obstruction, not a recursive closure theorem.

## PX1222 — `fc` obstruction on indices 6400 through 6799

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 6400 | 1,307,940 | 50,519 |
| 6500 | 1,849,486 | 73,456 |
| 6600 | 1,991,015 | 89,440 |
| 6700 | 2,663,691 | 80,905 |
| Total | 7,812,132 | 89,440 |

## PX1223 — `ff` obstruction on indices 6400 through 6799

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 6400 | 2,081,486 | 99,345 |
| 6500 | 2,784,407 | 161,219 |
| 6600 | 4,660,688 | 566,774 |
| 6700 | 5,073,185 | 330,134 |
| Total | 14,599,766 | 566,774 |

GitHub Actions run `30747166514` produced the first exact matrix. Run `30747345046` independently replayed the deterministic expected outputs before promotion.

## PX1224 — cumulative fine-row boundary

The exact fine-row obstruction now covers pair indices `0` through `6799` in both orientations:

- `fc`: 6,800 geometries, `232,466,543` nodes, maximum `1,877,339`;
- `ff`: 6,800 geometries, `150,194,835` nodes, maximum `909,040`.

No constructive witness appears in these 13,600 fine-row geometries. The next bounded prefix begins at pair index `6800`.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_6400_6799.py
```
