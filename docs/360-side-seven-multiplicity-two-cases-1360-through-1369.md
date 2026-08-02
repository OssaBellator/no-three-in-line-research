# Multiplicity-two cases 1360 through 1369

This chapter records the selector-aware exact classification of side-seven support-twenty multiplicity-two cases `1360` through `1369`. Each selector and orientation was searched independently, with constructive outcomes treated as successful classifications rather than workflow failures.

## PX1169 — exact selector classification

The ten signatures contain 20 selectors. Every selector is infeasible in all four radix orientations. No new constructive selector occurs in this tranche.

GitHub Actions run `30358180474` completed all 80 isolated selector-orientation jobs. Run `30359214265` then reproduced the same classification as ten compact one-process case summaries.

## PX1170 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 569,188 | 2,118,169 |
| Interleaved | 645,362 | 2,243,872 |
| Total | 1,214,550 | 4,362,041 |

## PX1171 — rejection-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 1,585,215 |
| 1 | 1,662,096 |
| 2 | 1,549,148 |
| 3 | 1,811,930 |
| Total | 6,608,389 |

The exact per-case digests are:

| Case | Digest |
|---:|---:|
| 1360 | `13131993118497559949` |
| 1361 | `13006766811822709410` |
| 1362 | `10571013258278950442` |
| 1363 | `16513937281522596800` |
| 1364 | `1439880033829034356` |
| 1365 | `1293143353359751275` |
| 1366 | `13126318732264049288` |
| 1367 | `9591605799865436429` |
| 1368 | `1589417884840706176` |
| 1369 | `306096196577262883` |

## PX1172 — revised support-twenty boundary

The exact cache now contains:

- `40,339` certified-infeasible selectors;
- two constructive selectors;
- `31,519` unclassified selectors;
- `3,272,271,752` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `2,470` multiplicity-two signatures containing `4,940` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1370`. The classified multiplicity-two prefix uses `505,816,508` certified rejection-CSP nodes.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_cases1360_1369.py
```
