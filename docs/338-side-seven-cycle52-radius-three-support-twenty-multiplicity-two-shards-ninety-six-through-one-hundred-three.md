# Multiplicity-two cases 960 through 1039

This chapter records the exact finite census for side-seven support-twenty multiplicity-two cases `960` through `1039`. It is not an infinite product theorem.

## PX1088 — exact infeasibility

The eighty signatures contain 160 selectors. Every selector is infeasible in all four radix orientations.

| Shard | Cases | Digest |
|---:|---:|---:|
| 96 | `960`–`969` | `9681559467231383948` |
| 97 | `970`–`979` | `764748930000373914` |
| 98 | `980`–`989` | `5207635067091122284` |
| 99 | `990`–`999` | `1567631251581117598` |
| 100 | `1000`–`1009` | `11512103508428254606` |
| 101 | `1010`–`1019` | `12802408152367890407` |
| 102 | `1020`–`1029` | `6499844922641713310` |
| 103 | `1030`–`1039` | `15081963100796215239` |

GitHub Actions run `30323357750` completed all eight jobs. A later duplicate PR evaluation is not used.

## PX1089 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 3,249,356 | 38,409,302 |
| Interleaved | 2,820,982 | 32,443,403 |
| Total | 6,070,338 | 70,852,705 |

## PX1090 — bottom-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 5,011,925 |
| 1 | 4,481,682 |
| 2 | 4,897,752 |
| 3 | 3,946,338 |
| Total | 18,337,697 |

The first 1,040 multiplicity-two signatures therefore use `399,139,256` bottom-CSP nodes.

## PX1091 — revised cache boundary

The exact support-twenty cache now contains:

- `39,680` certified-infeasible selectors;
- one constructive selector;
- `32,179` unclassified selectors;
- `3,165,594,500` certified rejection-CSP nodes.

The unresolved selectors are exactly `2,800` multiplicity-two signatures (`5,600` selectors) and `26,579` multiplicity-one selectors. The next canonical multiplicity-two case is `1040`.

## Verification

Compile and run `multiplicity2_shard96.cpp` through `multiplicity2_shard103.cpp`. Each wrapper regenerates its ten-signature interval, all four orientation searches, and the ordered digest.
