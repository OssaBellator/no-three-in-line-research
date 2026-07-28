# Side-seven multiplicity-two cases 1280 through 1359

This chapter classifies the next eighty multiplicity-two signatures in the canonical side-seven support-twenty census. Unlike every earlier multiplicity-two tranche, this block contains a constructive selector.

## PX1158 — exact mixed classification

Cases `1280` through `1359` contain eighty signatures and 160 selectors.

- `159` selectors are certified infeasible in all four radix orientations;
- one selector is constructive.

Every signature except case `1287` has both selectors infeasible. At case `1287`, selector zero is constructive and selector one is infeasible.

## PX1159 — explicit case-1287 construction

For case `1287`, signature

`[130,768,1028,24,2176,8224,12288]`,

selector zero has a no-three realization in orientation zero at clean-top index `42984`.

The exact top assignment is

`[4,6,3,1,2,5,0,2,0,3,5,4,1,6]`,

and the bottom permutation is

`[6,5,4,3,2,0,1]`.

The selected host state is

`[130,768,1028,24,2176,8224,12288,257,6,520,3072,17,96,4160]`.

The resulting 28 grid points are

`(0,6),(0,9),(1,7),(1,10),(2,3),(2,12),(3,1),(3,2),`
`(4,9),(4,11),(5,5),(5,13),(6,8),(6,13),(13,4),(13,7),`
`(12,6),(12,3),(11,1),(11,10),(10,12),(10,11),(9,4),(9,2),`
`(7,5),(7,0),(8,0),(8,8)`.

The witness verifier independently checks:

- all 28 cells are distinct;
- every row and every column contains exactly two points;
- every one of the `C(28,3)` triples has nonzero determinant.

GitHub Actions run `30331859070` extracted and verified this witness.

## PX1160 — the second case-1287 selector is obstructed

The other selector in case `1287` is infeasible in all four orientations. Its exact bottom-CSP node totals are

`[99,110, 53,920, 97,697, 47,125]`.

Its clean-top counts are `[79,488,40,560]`, and its top-search node counts are `[933,498,588,812]`.

GitHub Actions run `30332097040` independently verified this selector.

## PX1161 — exact tranche complexity

Across all eighty signatures, the clean-top totals are

`[3,720,870, 3,870,522]`,

with top-search node totals

`[27,647,071, 25,438,520]`.

The 159 rejection proofs use bottom-CSP node totals

`[5,585,287, 6,263,979, 5,770,572, 5,286,972]`,

for a combined rejection total of `22,906,810` nodes.

The special shard-128 verifier records nineteen rejections and the one construction. Shards `129` through `135` remain ordinary ten-signature all-infeasible replay units.

## PX1162 — revised support-twenty boundary

After promoting cases `1280` through `1359`, the full support-twenty cache contains:

- `40,319` certified-infeasible selectors;
- `2` constructive selectors;
- `31,539` unclassified selectors;
- `3,265,663,363` certified rejection-CSP nodes.

The unresolved set is exactly:

- `2,480` multiplicity-two signatures containing `4,960` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1360`.

This remains a finite census result and does not prove an all-side product theorem.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard128_special.cpp \
  -o /tmp/side7-m2-shard128-special
/tmp/side7-m2-shard128-special

for shard in {129..135}; do
  source="scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard${shard}.cpp"
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```
