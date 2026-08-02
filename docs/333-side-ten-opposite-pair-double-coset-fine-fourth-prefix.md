# Side-ten opposite-pair fine-row fourth prefix

PX1044--PX1068 obstruct pair indices `0` through `1199` in both fine-row orientations. This chapter closes pair indices `1200` through `1599`.

The result is a partial exact obstruction, not a complete double-coset theorem.

## PX1069 — `fc` pair indices 1200 through 1599

| Pair interval | Nodes | Maximum per geometry |
|---:|---:|---:|
| `1200`–`1299` | 1,227,566 | 49,897 |
| `1300`–`1399` | 2,062,659 | 170,613 |
| `1400`–`1499` | 1,340,627 | 52,920 |
| `1500`–`1599` | 2,415,553 | 105,685 |
| Total | 7,046,405 | 170,613 |

No geometry contains a no-three degree-two state.

## PX1070 — `ff` pair indices 1200 through 1599

| Pair interval | Nodes | Maximum per geometry |
|---:|---:|---:|
| `1200`–`1299` | 5,682,907 | 909,040 |
| `1300`–`1399` | 4,321,785 | 228,366 |
| `1400`–`1499` | 2,649,324 | 105,192 |
| `1500`–`1599` | 2,571,980 | 116,732 |
| Total | 15,225,996 | 909,040 |

No geometry contains a no-three degree-two state. The large maximum is an exact search-cost observation only.

GitHub Actions run `30320492358` completed all eight interval jobs.

## PX1071 — revised fine-row frontier

Combining all four prefixes, pair indices `0` through `1599` are infeasible in each fine-row orientation:

- `fc`: 1,600 geometries, 14,940,325 nodes, maximum 170,613;
- `ff`: 1,600 geometries, 26,608,386 nodes, maximum 909,040.

The unsearched portion of the opposite-pair double coset is pair indices `1600` through `7999` in each fine orientation. The complete `cc` and `cf` obstructions remain unchanged.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_1200_1599.py
```
