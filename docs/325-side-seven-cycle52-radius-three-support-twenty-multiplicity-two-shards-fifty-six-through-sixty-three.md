# Multiplicity-two cases 560 through 639

This chapter records the exact finite census for side-seven support-twenty multiplicity-two cases `560` through `639`. It is not an infinite product theorem.

## PX1040 — exact infeasibility

The eighty signatures contain 160 selectors. Every selector is infeasible in all four radix orientations.

| Shard | Cases | Digest |
|---:|---:|---:|
| 56 | `560`–`569` | `9318782807487620778` |
| 57 | `570`–`579` | `16939193131642798275` |
| 58 | `580`–`589` | `8402579686058060180` |
| 59 | `590`–`599` | `12218205667181486697` |
| 60 | `600`–`609` | `17027528386304151835` |
| 61 | `610`–`619` | `8631982483106294843` |
| 62 | `620`–`629` | `16112937728120265129` |
| 63 | `630`–`639` | `16527610734791035772` |

GitHub Actions run `30317306973` completed all eight jobs.

## PX1041 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 6,712,566 | 32,070,736 |
| Interleaved | 4,974,838 | 23,883,192 |
| Total | 11,687,404 | 55,953,928 |

## PX1042 — bottom-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 10,613,739 |
| 1 | 7,738,291 |
| 2 | 10,023,803 |
| 3 | 7,837,898 |
| Total | 36,213,731 |

The first 640 multiplicity-two signatures therefore use `276,029,803` bottom-CSP nodes.

## PX1043 — revised cache boundary

The exact support-twenty cache now contains:

- `38,880` certified-infeasible selectors;
- one constructive selector;
- `32,979` unclassified selectors;
- `3,042,485,047` certified rejection-CSP nodes.

The unresolved selectors are exactly `3,200` multiplicity-two signatures (`6,400` selectors) and `26,579` multiplicity-one selectors. The next canonical multiplicity-two case is `640`.

## Verification

Compile and run `multiplicity2_shard56.cpp` through `multiplicity2_shard63.cpp`. Each wrapper regenerates its ten-signature interval, all four orientation searches, and the ordered digest.
