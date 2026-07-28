# Multiplicity-two cases 1370 through 1379

This chapter records the selector-aware exact classification of side-seven support-twenty multiplicity-two cases `1370` through `1379`.

## PX1173 — exact selector classification

The ten signatures contain 20 selectors. Every selector is infeasible in all four radix orientations. No new constructive selector occurs in this tranche.

GitHub Actions run `30360443389` completed all ten compact case jobs.

## PX1174 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 381,782 | 2,616,621 |
| Interleaved | 252,885 | 1,776,684 |
| Total | 634,667 | 4,393,305 |

## PX1175 — rejection-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 993,447 |
| 1 | 636,537 |
| 2 | 988,112 |
| 3 | 673,105 |
| Total | 3,291,201 |

The exact per-case digests are:

| Case | Digest |
|---:|---:|
| 1370 | `1810215207757239972` |
| 1371 | `1771273280478592961` |
| 1372 | `5538187135371104426` |
| 1373 | `6105991396001012831` |
| 1374 | `14917046920312673849` |
| 1375 | `224476763019304889` |
| 1376 | `16287483067216321519` |
| 1377 | `2886759908069204100` |
| 1378 | `17753350937339374626` |
| 1379 | `473366611310269554` |

## PX1176 — revised support-twenty boundary

The exact cache now contains:

- `40,359` certified-infeasible selectors;
- two constructive selectors;
- `31,499` unclassified selectors;
- `3,275,562,953` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `2,460` multiplicity-two signatures containing `4,920` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1380`. The classified multiplicity-two prefix uses `509,107,709` certified rejection-CSP nodes.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_cases1370_1379.py
```
