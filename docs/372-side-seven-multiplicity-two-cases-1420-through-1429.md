# Multiplicity-two cases 1420 through 1429

This chapter records the selector-aware exact classification of side-seven support-twenty multiplicity-two cases `1420` through `1429`.

## PX1211 — exact selector classification

The ten signatures contain 20 selectors. Every selector is infeasible in all four radix orientations. No constructive selector occurs in this tranche.

GitHub Actions run `30746691734` produced the first exact matrix. Run `30746882426` independently replayed the deterministic expected outputs before promotion.

## PX1212 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 174,260 | 526,067 |
| Interleaved | 213,284 | 627,087 |
| Total | 387,544 | 1,153,154 |

## PX1213 — rejection-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 416,891 |
| 1 | 578,825 |
| 2 | 452,125 |
| 3 | 474,488 |
| Total | 1,922,329 |

The exact per-case digests are:

| Case | Digest |
|---:|---:|
| 1420 | `4183412894217143445` |
| 1421 | `13222211643404472107` |
| 1422 | `7484813740925408592` |
| 1423 | `16594429692102283552` |
| 1424 | `6418617360073411461` |
| 1425 | `769118598104101433` |
| 1426 | `5604718688552064674` |
| 1427 | `12021380072371610692` |
| 1428 | `12006458718341313019` |
| 1429 | `7657698749909335184` |

## PX1214 — revised support-twenty boundary

The exact cache now contains:

- `40,459` certified-infeasible selectors;
- two constructive selectors;
- `31,399` unclassified selectors;
- `3,295,710,592` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `2,410` multiplicity-two signatures containing `4,820` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1430`. The classified multiplicity-two prefix uses `529,255,348` certified rejection-CSP nodes.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_cases1420_1429.py
```
