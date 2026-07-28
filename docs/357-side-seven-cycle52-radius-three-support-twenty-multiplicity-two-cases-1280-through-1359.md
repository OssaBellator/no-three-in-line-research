# Multiplicity-two cases 1280 through 1359 and the second constructive selector

This chapter records the exact finite classification of side-seven support-twenty multiplicity-two cases `1280` through `1359`. It is a bounded census result, not an all-`n` product theorem.

## PX1158 — exact selector classification

The eighty signatures contain 160 selectors.

- Cases `1280` through `1286` and `1288` through `1359` contribute 158 selectors, all infeasible in all four radix orientations.
- Case `1287`, selector one, is infeasible in all four orientations.
- Case `1287`, selector zero, is constructive in orientation zero.

Thus this tranche contributes 159 certified-infeasible selectors and one constructive selector.

The reusable digest units are:

| Unit | Cases | Digest |
|---|---:|---:|
| Prefix | `1280`–`1286` | `12966799060506877054` |
| Tail | `1288`–`1289` | `6909944594185390875` |
| Shard 129 | `1290`–`1299` | `3350805294673612655` |
| Shard 130 | `1300`–`1309` | `8890744816044984291` |
| Shard 131 | `1310`–`1319` | `3796189743782724071` |
| Shard 132 | `1320`–`1329` | `13572297940413613278` |
| Shard 133 | `1330`–`1339` | `6816307819436119681` |
| Shard 134 | `1340`–`1349` | `15976464783720629267` |
| Shard 135 | `1350`–`1359` | `14500902586021413143` |

## PX1159 — explicit side-seven construction

The constructive selector has:

- global case: `1287`;
- multiplicity-two selector: `0` after canonical state sorting;
- orientation: `0`;
- clean-top index: `42984`;
- signature: `[130,768,1028,24,2176,8224,12288]`;
- state: `[130,768,1028,24,2176,8224,12288,257,6,520,3072,17,96,4160]`;
- top permutations: `[4,6,3,1,2,5,0]` and `[2,0,3,5,4,1,6]`;
- bottom permutation: `[6,5,4,3,2,0,1]`.

The resulting 28 points are

```text
(0,6) (0,9) (1,7) (1,10) (2,3) (2,12) (3,1) (3,2)
(4,9) (4,11) (5,5) (5,13) (6,8) (6,13)
(13,4) (13,7) (12,6) (12,3) (11,1) (11,10) (10,12) (10,11)
(9,4) (9,2) (7,5) (7,0) (8,0) (8,8)
```

The witness extractor independently asserts two points in every row, two points in every column, 28 distinct points, and no collinear triple. GitHub Actions run `30331859070` completed that verification. The other selector was independently rejected by run `30332097040`, with orientation-node totals `[99110,53920,97697,47125]`.

## PX1160 — exact search census

The eighty signatures use the following shared clean-top enumeration totals:

| Column order | Clean tops | Search nodes |
|---|---:|---:|
| Concatenated | 3,720,870 | 27,647,071 |
| Interleaved | 3,870,522 | 25,438,520 |
| Total | 7,591,392 | 53,085,591 |

Certified rejection searches, excluding the constructive selector, use:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 5,585,287 |
| 1 | 6,263,979 |
| 2 | 5,770,572 |
| 3 | 5,286,972 |
| Total | 22,906,810 |

## PX1161 — revised support-twenty boundary

The exact cache now contains:

- `40,319` certified-infeasible selectors;
- two constructive selectors;
- `31,539` unclassified selectors;
- `3,265,663,363` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `2,480` multiplicity-two signatures containing `4,960` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1360`.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard128_prefix7.cpp \
  -o /tmp/m2-prefix128
/tmp/m2-prefix128

g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard128_tail2.cpp \
  -o /tmp/m2-tail128
/tmp/m2-tail128

g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity2_case1287_constructive_witness.cpp \
  -o /tmp/m2-case1287-witness
/tmp/m2-case1287-witness

g++ -O3 -std=c++17 \
  scripts/measure_product_side_seven_multiplicity2_case1287_selector1.cpp \
  -o /tmp/m2-case1287-selector1
/tmp/m2-case1287-selector1
```
