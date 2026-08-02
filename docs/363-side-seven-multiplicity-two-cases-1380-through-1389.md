# Multiplicity-two cases 1380 through 1389

This chapter records the selector-aware exact classification of side-seven support-twenty multiplicity-two cases `1380` through `1389`.

## PX1180 — exact selector classification

The ten signatures contain 20 selectors. Every selector is infeasible in all four radix orientations. No new constructive selector occurs in this tranche.

GitHub Actions run `30361705312` completed all ten compact case jobs.

## PX1181 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 354,916 | 3,526,570 |
| Interleaved | 279,144 | 3,166,284 |
| Total | 634,060 | 6,692,854 |

## PX1182 — rejection-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 952,611 |
| 1 | 717,865 |
| 2 | 930,613 |
| 3 | 763,643 |
| Total | 3,364,732 |

The exact per-case digests are:

| Case | Digest |
|---:|---:|
| 1380 | `7319284530954993992` |
| 1381 | `3221066886467667313` |
| 1382 | `18396338264906931230` |
| 1383 | `9146397096454413286` |
| 1384 | `2841601550497478034` |
| 1385 | `3583209879738751821` |
| 1386 | `2908957634065235222` |
| 1387 | `4688154644453038016` |
| 1388 | `8748161535169185449` |
| 1389 | `11172147241996266398` |

## PX1183 — revised support-twenty boundary

The exact cache now contains:

- `40,379` certified-infeasible selectors;
- two constructive selectors;
- `31,479` unclassified selectors;
- `3,278,927,685` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `2,450` multiplicity-two signatures containing `4,900` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1390`. The classified multiplicity-two prefix uses `512,472,441` certified rejection-CSP nodes.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_cases1380_1389.py
```
