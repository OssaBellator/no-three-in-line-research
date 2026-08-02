# Multiplicity-two cases 1400 through 1409

This chapter records the selector-aware exact classification of side-seven support-twenty multiplicity-two cases `1400` through `1409`.

## PX1197 — exact selector classification

The ten signatures contain 20 selectors. Every selector is infeasible in all four radix orientations. No constructive selector occurs in this tranche.

GitHub Actions run `30745507166` produced the first exact matrix. Run `30745722667` independently replayed the deterministic expected outputs before promotion.

## PX1198 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 666,128 | 3,207,659 |
| Interleaved | 320,890 | 1,775,264 |
| Total | 987,018 | 4,982,923 |

## PX1199 — rejection-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 1,852,079 |
| 1 | 843,461 |
| 2 | 1,877,031 |
| 3 | 950,823 |
| Total | 5,523,394 |

The exact per-case digests are:

| Case | Digest |
|---:|---:|
| 1400 | `3729959886903785438` |
| 1401 | `17491553376708229085` |
| 1402 | `16249811963486277739` |
| 1403 | `15807777010410543117` |
| 1404 | `8335780563140783661` |
| 1405 | `594254067995011962` |
| 1406 | `7413084282017054975` |
| 1407 | `1367388716652260009` |
| 1408 | `9586278848783989832` |
| 1409 | `2832897585058173214` |

## PX1200 — revised support-twenty boundary

The exact cache now contains:

- `40,419` certified-infeasible selectors;
- two constructive selectors;
- `31,439` unclassified selectors;
- `3,291,140,089` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `2,430` multiplicity-two signatures containing `4,860` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1410`. The classified multiplicity-two prefix uses `524,684,845` certified rejection-CSP nodes.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_cases1400_1409.py
```
