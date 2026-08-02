# Multiplicity-two cases 1200 through 1279

This chapter records the exact finite census for side-seven support-twenty multiplicity-two cases `1200` through `1279`. It is not an infinite product theorem.

## PX1129 — exact infeasibility

The eighty signatures contain 160 selectors. Every selector is infeasible in all four radix orientations.

| Shard | Cases | Digest |
|---:|---:|---:|
| 120 | `1200`–`1209` | `2735525392471744800` |
| 121 | `1210`–`1219` | `13574711017486657864` |
| 122 | `1220`–`1229` | `8162915674535461669` |
| 123 | `1230`–`1239` | `9154343577324608262` |
| 124 | `1240`–`1249` | `13178814025061252983` |
| 125 | `1250`–`1259` | `13781225323153859254` |
| 126 | `1260`–`1269` | `3222192598561150535` |
| 127 | `1270`–`1279` | `14533600534674041241` |

GitHub Actions run `30326589110` completed all eight jobs.

## PX1130 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 4,538,094 | 26,684,879 |
| Interleaved | 4,542,002 | 24,847,306 |
| Total | 9,080,096 | 51,532,185 |

## PX1131 — bottom-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 7,045,625 |
| 1 | 6,871,081 |
| 2 | 6,549,984 |
| 3 | 6,663,831 |
| Total | 27,130,521 |

The first 1,280 multiplicity-two signatures therefore use `476,301,309` bottom-CSP nodes.

## PX1132 — revised cache boundary

The exact support-twenty cache now contains:

- `40,160` certified-infeasible selectors;
- one constructive selector;
- `31,699` unclassified selectors;
- `3,242,756,553` certified rejection-CSP nodes.

The unresolved selectors are exactly `2,560` multiplicity-two signatures (`5,120` selectors) and `26,579` multiplicity-one selectors. The next canonical multiplicity-two case is `1280`.

## Verification

Compile and run `multiplicity2_shard120.cpp` through `multiplicity2_shard127.cpp`. Each wrapper regenerates its ten-signature interval, all four orientation searches, and the ordered digest.
