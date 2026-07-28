# Side-ten opposite-pair fine-row second prefix

PX1044--PX1046 obstruct pair indices `0` through `399` in both fine-row orientations. This chapter closes pair indices `400` through `799`.

The result is a partial exact obstruction, not a complete double-coset theorem.

## PX1047 — `fc` pair indices 400 through 799

| Pair interval | Nodes | Maximum per geometry |
|---:|---:|---:|
| `400`–`499` | 457,877 | 9,420 |
| `500`–`599` | 393,513 | 13,421 |
| `600`–`699` | 598,764 | 18,432 |
| `700`–`799` | 457,847 | 23,691 |
| Total | 1,908,001 | 23,691 |

No geometry contains a no-three degree-two state.

## PX1048 — `ff` pair indices 400 through 799

| Pair interval | Nodes | Maximum per geometry |
|---:|---:|---:|
| `400`–`499` | 290,148 | 19,518 |
| `500`–`599` | 249,269 | 14,180 |
| `600`–`699` | 383,909 | 33,547 |
| `700`–`799` | 573,022 | 53,139 |
| Total | 1,496,348 | 53,139 |

No geometry contains a no-three degree-two state.

GitHub Actions run `30318376822` completed all eight interval jobs.

## PX1049 — revised fine-row frontier

Combining both exact prefixes, pair indices `0` through `799` are infeasible in each fine-row orientation:

- `fc`: 800 geometries, 4,076,728 nodes, maximum 23,691;
- `ff`: 800 geometries, 2,659,076 nodes, maximum 53,139.

The unsearched portion of the opposite-pair double coset is pair indices `800` through `7999` in each fine orientation. The complete `cc` and `cf` obstructions remain unchanged.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_400_799.py
```

The verifier recompiles the exact search, replays all eight intervals, rejects any `FOUND` output, and asserts every total and maximum.
