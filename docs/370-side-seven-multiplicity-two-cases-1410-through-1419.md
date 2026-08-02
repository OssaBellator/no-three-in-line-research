# Multiplicity-two cases 1410 through 1419

This chapter records the selector-aware exact classification of side-seven support-twenty multiplicity-two cases `1410` through `1419`.

## PX1204 — exact selector classification

The ten signatures contain 20 selectors. Every selector is infeasible in all four radix orientations. No constructive selector occurs in this tranche.

GitHub Actions run `30746062602` produced the first exact matrix. Run `30746389101` independently replayed the deterministic expected outputs before promotion.

## PX1205 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 174,452 | 842,077 |
| Interleaved | 321,392 | 1,353,776 |
| Total | 495,844 | 2,195,853 |

## PX1206 — rejection-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 482,999 |
| 1 | 866,412 |
| 2 | 465,679 |
| 3 | 833,084 |
| Total | 2,648,174 |

The exact per-case digests are:

| Case | Digest |
|---:|---:|
| 1410 | `17584218828418708989` |
| 1411 | `2957650116471118414` |
| 1412 | `2222917410722152829` |
| 1413 | `4273257825716142296` |
| 1414 | `14893605509215099704` |
| 1415 | `5331428447541144751` |
| 1416 | `493467968458165697` |
| 1417 | `17855131710443158887` |
| 1418 | `14861941076081487932` |
| 1419 | `11557078296270044135` |

## PX1207 — revised support-twenty boundary

The exact cache now contains:

- `40,439` certified-infeasible selectors;
- two constructive selectors;
- `31,419` unclassified selectors;
- `3,293,788,263` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `2,420` multiplicity-two signatures containing `4,840` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1420`. The classified multiplicity-two prefix uses `527,333,019` certified rejection-CSP nodes.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_cases1410_1419.py
```
