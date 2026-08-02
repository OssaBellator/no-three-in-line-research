# Multiplicity-two cases 1430 through 1439

This chapter records the selector-aware exact classification of side-seven support-twenty multiplicity-two cases `1430` through `1439`.

## PX1218 — exact selector classification

The ten signatures contain 20 selectors. Every selector is infeasible in all four radix orientations. No constructive selector occurs in this tranche.

GitHub Actions run `30747166521` produced the first exact matrix. Run `30747345046` independently replayed the deterministic expected outputs before promotion.

## PX1219 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 188,468 | 615,015 |
| Interleaved | 192,060 | 638,842 |
| Total | 380,528 | 1,253,857 |

## PX1220 — rejection-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 464,818 |
| 1 | 488,262 |
| 2 | 483,551 |
| 3 | 464,332 |
| Total | 1,900,963 |

The exact per-case digests are:

| Case | Digest |
|---:|---:|
| 1430 | `9022283284995776830` |
| 1431 | `13086807189344959278` |
| 1432 | `18158334224973120649` |
| 1433 | `18429921265688731684` |
| 1434 | `14206178255592492007` |
| 1435 | `9947680513117902040` |
| 1436 | `7034531801571772175` |
| 1437 | `14608730979352190165` |
| 1438 | `17007583894268159062` |
| 1439 | `10584922255083157802` |

## PX1221 — revised support-twenty boundary

The exact cache now contains:

- `40,479` certified-infeasible selectors;
- two constructive selectors;
- `31,379` unclassified selectors;
- `3,297,611,555` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `2,400` multiplicity-two signatures containing `4,800` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1440`. The classified multiplicity-two prefix uses `531,156,311` certified rejection-CSP nodes.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_cases1430_1439.py
```
