# Multiplicity-two cases 800 through 879

This chapter records the exact finite census for side-seven support-twenty multiplicity-two cases `800` through `879`. It is not an infinite product theorem.

## PX1072 — exact infeasibility

The eighty signatures contain 160 selectors. Every selector is infeasible in all four radix orientations.

| Shard | Cases | Digest |
|---:|---:|---:|
| 80 | `800`–`809` | `2741874371339139127` |
| 81 | `810`–`819` | `16772310416434152769` |
| 82 | `820`–`829` | `8488868181964210369` |
| 83 | `830`–`839` | `14980970733442961720` |
| 84 | `840`–`849` | `866350994586011106` |
| 85 | `850`–`859` | `8314562979571188860` |
| 86 | `860`–`869` | `5676021412180323776` |
| 87 | `870`–`879` | `16425776743378338066` |

GitHub Actions run `30320492357` completed all eight jobs.

## PX1073 — clean-top census

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 4,370,882 | 21,179,787 |
| Interleaved | 3,731,087 | 16,750,078 |
| Total | 8,101,969 | 37,929,865 |

## PX1074 — bottom-CSP census

| Orientation | Nodes |
|---:|---:|
| 0 | 7,027,982 |
| 1 | 5,993,527 |
| 2 | 6,554,813 |
| 3 | 5,520,437 |
| Total | 25,096,759 |

The first 880 multiplicity-two signatures therefore use `353,338,127` bottom-CSP nodes.

## PX1075 — revised cache boundary

The exact support-twenty cache now contains:

- `39,360` certified-infeasible selectors;
- one constructive selector;
- `32,499` unclassified selectors;
- `3,119,793,371` certified rejection-CSP nodes.

The unresolved selectors are exactly `2,960` multiplicity-two signatures (`5,920` selectors) and `26,579` multiplicity-one selectors. The next canonical multiplicity-two case is `880`.

## Verification

Compile and run `multiplicity2_shard80.cpp` through `multiplicity2_shard87.cpp`. Each wrapper regenerates its ten-signature interval, all four orientation searches, and the ordered digest.
