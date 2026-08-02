# Side-ten opposite-pair fine-row thirteenth prefix

This chapter records the exact side-ten opposite-pair double-coset searches for pair indices `4800` through `5199` in the two remaining fine-row orientations. It is a finite obstruction, not a recursive closure theorem.

## PX1191 — `fc` obstruction on indices 4800 through 5199

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 4800 | 3,251,516 | 483,718 |
| 4900 | 2,122,630 | 151,134 |
| 5000 | 2,520,838 | 205,642 |
| 5100 | 4,523,858 | 250,094 |
| Total | 12,418,842 | 483,718 |

## PX1192 — `ff` obstruction on indices 4800 through 5199

All 400 indexed geometries are infeasible.

| First pair | Nodes | Maximum |
|---:|---:|---:|
| 4800 | 2,034,679 | 99,810 |
| 4900 | 1,714,119 | 77,663 |
| 5000 | 3,814,344 | 503,447 |
| 5100 | 4,017,219 | 276,969 |
| Total | 11,580,361 | 503,447 |

GitHub Actions run `30728198799` completed all eight interval jobs and the full matrix was independently rerun before promotion.

## PX1193 — cumulative fine-row boundary

The exact fine-row obstruction now covers pair indices `0` through `5199` in both orientations:

- `fc`: 5,200 geometries, `184,338,885` nodes, maximum `1,877,339`;
- `ff`: 5,200 geometries, `112,022,029` nodes, maximum `909,040`.

No constructive witness appears in these 10,400 fine-row geometries. The next bounded prefix begins at pair index `5200`.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_4800_5199.py
```
