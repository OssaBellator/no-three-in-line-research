# Side-ten opposite-pair fine-row third prefix

PX1044--PX1049 obstruct pair indices `0` through `799` in both fine-row orientations. This chapter closes pair indices `800` through `1199`.

The result is a partial exact obstruction, not a complete double-coset theorem.

## PX1066 — `fc` pair indices 800 through 1199

| Pair interval | Nodes | Maximum per geometry |
|---:|---:|---:|
| `800`–`899` | 613,918 | 30,404 |
| `900`–`999` | 595,801 | 41,699 |
| `1000`–`1099` | 1,175,010 | 102,050 |
| `1100`–`1199` | 1,432,463 | 68,768 |
| Total | 3,817,192 | 102,050 |

No geometry contains a no-three degree-two state.

## PX1067 — `ff` pair indices 800 through 1199

| Pair interval | Nodes | Maximum per geometry |
|---:|---:|---:|
| `800`–`899` | 1,479,138 | 168,049 |
| `900`–`999` | 1,729,715 | 142,919 |
| `1000`–`1099` | 2,107,202 | 111,917 |
| `1100`–`1199` | 3,407,259 | 396,937 |
| Total | 8,723,314 | 396,937 |

No geometry contains a no-three degree-two state. The increased node counts are exact search-cost observations only.

GitHub Actions run `30319547816` completed all eight interval jobs.

## PX1068 — revised fine-row frontier

Combining all three prefixes, pair indices `0` through `1199` are infeasible in each fine-row orientation:

- `fc`: 1,200 geometries, 7,893,920 nodes, maximum 102,050;
- `ff`: 1,200 geometries, 11,382,390 nodes, maximum 396,937.

The unsearched portion of the opposite-pair double coset is pair indices `1200` through `7999` in each fine orientation. The complete `cc` and `cf` obstructions remain unchanged.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_800_1199.py
```
