# Multiplicity-two cases 720 through 799

This chapter records the exact finite census for side-seven support-twenty multiplicity-two cases `720` through `799`. It is not an infinite product theorem.

## PX1058 — exact infeasibility

The eighty signatures contain 160 selectors. Every selector is infeasible in all four radix orientations.

| Shard | Cases | Digest |
|---:|---:|---:|
| 72 | `720`–`729` | `15152283108699527779` |
| 73 | `730`–`739` | `13362156138260302353` |
| 74 | `740`–`749` | `16486546947670781079` |
| 75 | `750`–`759` | `4711295851722750288` |
| 76 | `760`–`769` | `13093882893357327338` |
| 77 | `770`–`779` | `17928620657005057642` |
| 78 | `780`–`789` | `13663757452176296805` |
| 79 | `790`–`799` | `4230035789429227200` |

GitHub Actions run `30319547822` completed all eight jobs.

## PX1059 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 3,404,668 | 12,621,414 |
| Interleaved | 3,412,294 | 12,614,240 |
| Total | 6,816,962 | 25,235,654 |

## PX1060 — bottom-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 5,424,102 |
| 1 | 5,380,230 |
| 2 | 5,104,279 |
| 3 | 4,961,493 |
| Total | 20,870,104 |

The first 800 multiplicity-two signatures therefore use `328,241,368` bottom-CSP nodes.

## PX1061 — revised cache boundary

The exact support-twenty cache now contains:

- `39,200` certified-infeasible selectors;
- one constructive selector;
- `32,659` unclassified selectors;
- `3,094,696,612` certified rejection-CSP nodes.

The unresolved selectors are exactly `3,040` multiplicity-two signatures (`6,080` selectors) and `26,579` multiplicity-one selectors. The next canonical multiplicity-two case is `800`.

## Verification

Compile and run `multiplicity2_shard72.cpp` through `multiplicity2_shard79.cpp`. Each wrapper regenerates its ten-signature interval, all four orientation searches, and the ordered digest.
