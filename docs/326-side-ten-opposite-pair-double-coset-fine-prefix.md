# Side-ten opposite-pair double-coset fine-row prefix

PX983--PX985 close the complete opposite-pair double coset in coarse-row
orientations `cc` and `cf`, leaving `fc` and `ff`. This chapter records the first
400 exact geometries in each fine-row orientation.

The opposite-pair double coset has 200 column maps and ten affine target maps,
for 8,000 geometries per orientation. The present result covers pair indices
`0` through `399` in each fine orientation. It is a partial obstruction, not a
complete double-coset theorem.

## PX1044 — first 400 `fc` geometries

The four exact 100-geometry intervals are:

| Pair interval | Nodes | Maximum per geometry |
|---:|---:|---:|
| `0`–`99` | 610,634 | 18,321 |
| `100`–`199` | 560,044 | 13,716 |
| `200`–`299` | 510,123 | 16,195 |
| `300`–`399` | 487,926 | 16,500 |
| Total | 2,168,727 | 18,321 |

No geometry contains a no-three degree-two state.

## PX1045 — first 400 `ff` geometries

| Pair interval | Nodes | Maximum per geometry |
|---:|---:|---:|
| `0`–`99` | 298,206 | 12,723 |
| `100`–`199` | 310,324 | 9,718 |
| `200`–`299` | 290,210 | 11,044 |
| `300`–`399` | 263,988 | 14,278 |
| Total | 1,162,728 | 14,278 |

No geometry contains a no-three degree-two state.

GitHub Actions run `30317451777` completed all eight exact interval jobs.

## PX1046 — revised recursion frontier

The first 800 fine-row geometries are now obstructed: 400 in `fc` and 400 in
`ff`. Together with the complete coarse-row obstruction, the smallest non-affine
opposite-pair double coset has the following exact status:

- `cc`: all 8,000 geometries infeasible;
- `cf`: all 8,000 geometries infeasible;
- `fc`: pair indices `0`–`399` infeasible, `400`–`7999` open;
- `ff`: pair indices `0`–`399` infeasible, `400`–`7999` open.

No conclusion is drawn for unsearched fine-row intervals or either larger
800-map transposition double coset.

## Verification

```bash
python scripts/verify_product_transposition_double_coset_opposite_fine_ten_0_399.py
```

The verifier recompiles the exact search, replays all eight intervals, rejects
any `FOUND` output, and asserts every total and maximum.
