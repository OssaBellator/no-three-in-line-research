# Multiplicity-two cases 1390 through 1399

This chapter records the selector-aware exact classification of side-seven support-twenty multiplicity-two cases `1390` through `1399`.

## PX1187 — exact selector classification

The ten signatures contain 20 selectors. Every selector is infeasible in all four radix orientations. No new constructive selector occurs in this tranche.

GitHub Actions run `30728198789` completed all ten compact case jobs and the full matrix was independently rerun before promotion.

## PX1188 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 631,906 | 2,855,780 |
| Interleaved | 585,598 | 2,663,000 |
| Total | 1,217,504 | 5,518,780 |

## PX1189 — rejection-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 1,702,433 |
| 1 | 1,605,246 |
| 2 | 1,749,053 |
| 3 | 1,632,278 |
| Total | 6,689,010 |

The exact per-case digests are:

| Case | Digest |
|---:|---:|
| 1390 | `4594628904029995916` |
| 1391 | `5822347682282802730` |
| 1392 | `3809179463797773456` |
| 1393 | `15167240076065072039` |
| 1394 | `9838461318309294600` |
| 1395 | `6505911925465808203` |
| 1396 | `13009508480959642895` |
| 1397 | `2640712232549379923` |
| 1398 | `7580872602665828403` |
| 1399 | `7784300008166380410` |

## PX1190 — revised support-twenty boundary

The exact cache now contains:

- `40,399` certified-infeasible selectors;
- two constructive selectors;
- `31,459` unclassified selectors;
- `3,285,616,695` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `2,440` multiplicity-two signatures containing `4,880` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1400`. The classified multiplicity-two prefix uses `519,161,451` certified rejection-CSP nodes.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_cases1390_1399.py
```
