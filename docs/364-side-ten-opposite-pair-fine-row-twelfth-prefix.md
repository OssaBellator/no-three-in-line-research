# Side-ten opposite-pair fine-row twelfth prefix

This chapter records the exact side-ten opposite-pair double-coset searches for pair indices `4400` through `4799` in the two remaining fine-row orientations. It is a finite obstruction, not a recursive closure theorem.

## PX1184 — `fc` obstruction on indices 4400 through 4799

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 4400 | 8,355,467 | 1,877,339 |
| 4500 | 13,288,964 | 648,369 |
| 4600 | 6,337,608 | 917,874 |
| 4700 | 5,578,776 | 803,776 |
| Total | 33,560,815 | 1,877,339 |

## PX1185 — `ff` obstruction on indices 4400 through 4799

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 4400 | 2,218,298 | 327,084 |
| 4500 | 2,420,162 | 311,771 |
| 4600 | 2,169,979 | 118,690 |
| 4700 | 2,168,742 | 165,140 |
| Total | 8,977,181 | 327,084 |

GitHub Actions run `30361705367` completed all eight interval jobs.

## PX1186 — cumulative fine-row boundary

The exact fine-row obstruction now covers pair indices `0` through `4799` in both orientations:

- `fc`: 4,800 geometries, `171,920,043` nodes, maximum `1,877,339`;
- `ff`: 4,800 geometries, `100,441,668` nodes, maximum `909,040`.

No constructive witness appears in these 9,600 fine-row geometries. The next bounded prefix begins at pair index `4800`.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_4400_4799.py
```
