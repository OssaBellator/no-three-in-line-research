# Multiplicity-two cases 880 through 959

This chapter records the exact finite census for side-seven support-twenty multiplicity-two cases `880` through `959`. It is not an infinite product theorem.

## PX1081 — exact infeasibility

The eighty signatures contain 160 selectors. Every selector is infeasible in all four radix orientations.

| Shard | Cases | Digest |
|---:|---:|---:|
| 88 | `880`–`889` | `1447120913300419263` |
| 89 | `890`–`899` | `3470846642447975920` |
| 90 | `900`–`909` | `587821386895714243` |
| 91 | `910`–`919` | `12938349699372377995` |
| 92 | `920`–`929` | `14788916645976880020` |
| 93 | `930`–`939` | `13473758246526618952` |
| 94 | `940`–`949` | `2609057623375550414` |
| 95 | `950`–`959` | `11676461390096745129` |

GitHub Actions run `30321624749` completed all eight jobs.

## PX1082 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 4,194,630 | 21,315,767 |
| Interleaved | 4,732,731 | 22,521,356 |
| Total | 8,927,361 | 43,837,123 |

## PX1083 — bottom-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 6,959,062 |
| 1 | 7,437,077 |
| 2 | 6,101,529 |
| 3 | 6,965,764 |
| Total | 27,463,432 |

The first 960 multiplicity-two signatures therefore use `380,801,559` bottom-CSP nodes.

## PX1084 — revised cache boundary

The exact support-twenty cache now contains:

- `39,520` certified-infeasible selectors;
- one constructive selector;
- `32,339` unclassified selectors;
- `3,147,256,803` certified rejection-CSP nodes.

The unresolved selectors are exactly `2,880` multiplicity-two signatures (`5,760` selectors) and `26,579` multiplicity-one selectors. The next canonical multiplicity-two case is `960`.

## Verification

Compile and run `multiplicity2_shard88.cpp` through `multiplicity2_shard95.cpp`. Each wrapper regenerates its ten-signature interval, all four orientation searches, and the ordered digest.
