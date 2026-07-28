# Multiplicity-two cases 1120 through 1199

This chapter records the exact finite census for side-seven support-twenty multiplicity-two cases `1120` through `1199`. It is not an infinite product theorem.

## PX1125 — exact infeasibility

The eighty signatures contain 160 selectors. Every selector is infeasible in all four radix orientations.

| Shard | Cases | Digest |
|---:|---:|---:|
| 112 | `1120`–`1129` | `3128667511060827642` |
| 113 | `1130`–`1139` | `1162254786787950315` |
| 114 | `1140`–`1149` | `6103704461218321733` |
| 115 | `1150`–`1159` | `17913593264151879314` |
| 116 | `1160`–`1169` | `9121395323374095906` |
| 117 | `1170`–`1179` | `1740787177219988686` |
| 118 | `1180`–`1189` | `9647236515249463310` |
| 119 | `1190`–`1199` | `4487626094761021039` |

GitHub Actions run `30325932639` completed all eight jobs.

## PX1126 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 5,061,336 | 21,305,904 |
| Interleaved | 3,811,354 | 15,792,736 |
| Total | 8,872,690 | 37,098,640 |

## PX1127 — bottom-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 7,761,379 |
| 1 | 5,744,416 |
| 2 | 7,236,905 |
| 3 | 5,636,089 |
| Total | 26,378,789 |

The first 1,200 multiplicity-two signatures therefore use `449,170,788` bottom-CSP nodes.

## PX1128 — revised cache boundary

The exact support-twenty cache now contains:

- `40,000` certified-infeasible selectors;
- one constructive selector;
- `31,859` unclassified selectors;
- `3,215,626,032` certified rejection-CSP nodes.

The unresolved selectors are exactly `2,640` multiplicity-two signatures (`5,280` selectors) and `26,579` multiplicity-one selectors. The next canonical multiplicity-two case is `1200`.

## Verification

Compile and run `multiplicity2_shard112.cpp` through `multiplicity2_shard119.cpp`. Each wrapper regenerates its ten-signature interval, all four orientation searches, and the ordered digest.
