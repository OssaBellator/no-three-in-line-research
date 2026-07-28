# Multiplicity-two cases 640 through 719

This chapter records the exact finite census for side-seven support-twenty multiplicity-two cases `640` through `719`. It is not an infinite product theorem.

## PX1050 — exact infeasibility

The eighty signatures contain 160 selectors. Every selector is infeasible in all four radix orientations.

| Shard | Cases | Digest |
|---:|---:|---:|
| 64 | `640`–`649` | `9118922863212401361` |
| 65 | `650`–`659` | `10672074734858696060` |
| 66 | `660`–`669` | `13670699828197759913` |
| 67 | `670`–`679` | `11247092659769912659` |
| 68 | `680`–`689` | `5893286243712271176` |
| 69 | `690`–`699` | `13237971452873956928` |
| 70 | `700`–`709` | `7186785514344635808` |
| 71 | `710`–`719` | `3876622946876399712` |

GitHub Actions run `30318376832` completed all eight jobs.

## PX1051 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 6,643,404 | 34,775,032 |
| Interleaved | 3,332,872 | 20,320,902 |
| Total | 9,976,276 | 55,095,934 |

## PX1052 — bottom-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 11,003,622 |
| 1 | 5,273,269 |
| 2 | 9,973,111 |
| 3 | 5,091,459 |
| Total | 31,341,461 |

The first 720 multiplicity-two signatures therefore use `307,371,264` bottom-CSP nodes.

## PX1053 — revised cache boundary

The exact support-twenty cache now contains:

- `39,040` certified-infeasible selectors;
- one constructive selector;
- `32,819` unclassified selectors;
- `3,073,826,508` certified rejection-CSP nodes.

The unresolved selectors are exactly `3,120` multiplicity-two signatures (`6,240` selectors) and `26,579` multiplicity-one selectors. The next canonical multiplicity-two case is `720`.

## Verification

Compile and run `multiplicity2_shard64.cpp` through `multiplicity2_shard71.cpp`. Each wrapper regenerates its ten-signature interval, all four orientation searches, and the ordered digest.
