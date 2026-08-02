# Multiplicity-two cases 1040 through 1119

This chapter records the exact finite census for side-seven support-twenty multiplicity-two cases `1040` through `1119`. It is not an infinite product theorem.

## PX1118 — exact infeasibility

The eighty signatures contain 160 selectors. Every selector is infeasible in all four radix orientations.

| Shard | Cases | Digest |
|---:|---:|---:|
| 104 | `1040`–`1049` | `13851204348897764996` |
| 105 | `1050`–`1059` | `2257177977923349832` |
| 106 | `1060`–`1069` | `11786549827740883811` |
| 107 | `1070`–`1079` | `9459744099503416523` |
| 108 | `1080`–`1089` | `14195405686816500006` |
| 109 | `1090`–`1099` | `6179261871308072922` |
| 110 | `1100`–`1109` | `15829640899376239907` |
| 111 | `1110`–`1119` | `10104821057997949307` |

GitHub Actions run `30324314590` completed all eight jobs.

## PX1119 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 4,577,900 | 23,739,851 |
| Interleaved | 3,301,378 | 17,458,828 |
| Total | 7,879,278 | 41,198,679 |

## PX1120 — bottom-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 6,982,216 |
| 1 | 5,012,013 |
| 2 | 6,759,954 |
| 3 | 4,898,560 |
| Total | 23,652,743 |

The first 1,120 multiplicity-two signatures therefore use `422,791,999` bottom-CSP nodes.

## PX1121 — revised cache boundary

The exact support-twenty cache now contains:

- `39,840` certified-infeasible selectors;
- one constructive selector;
- `32,019` unclassified selectors;
- `3,189,247,243` certified rejection-CSP nodes.

The unresolved selectors are exactly `2,720` multiplicity-two signatures (`5,440` selectors) and `26,579` multiplicity-one selectors. The next canonical multiplicity-two case is `1120`.

## Verification

Compile and run `multiplicity2_shard104.cpp` through `multiplicity2_shard111.cpp`. Each wrapper regenerates its ten-signature interval, all four orientation searches, and the ordered digest.
