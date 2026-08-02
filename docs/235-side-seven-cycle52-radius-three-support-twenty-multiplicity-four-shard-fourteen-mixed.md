# Mixed multiplicity-four shard fourteen: 399 obstructions and one witness

PX745--PX748 close global multiplicity-four case indices `1280` through `1379`. This chapter classifies global cases `1380` through `1479`.

Unlike every earlier shard, this interval contains a genuine no-three witness. The result is therefore mixed: 399 selectors are certified infeasible and one selector is constructively realized.

## 1. Exact shard census

### Theorem PX751 -- PROVED FINITE

Shard fourteen contains one hundred multiplicity-four signatures and therefore 400 selectors.

The verifier regenerates the exact radius layers, asserts all 2,392 multiplicity-four signatures, and selects global case indices `1380` through `1479`.

## 2. Exact clean-top census

### Theorem PX752 -- PROVED FINITE

The exact clean-top totals across all one hundred signatures are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,690,759 | 41,015,945 |
| Interleaved | 3,076,808 | 28,518,404 |
| **Total** | **7,767,567** | **69,534,349** |

The complete mixed transcript has deterministic digest

`6967282382830852367` (`0x60b0c269b678590f`).

## 3. Exact infeasibility for 399 selectors

### Theorem PX753 -- PROVED FINITE

All four selectors in each of the 99 ordinary signatures are infeasible in every radix orientation. In exceptional case `1392`, selectors `1`, `2`, and `3` are jointly infeasible in every orientation after exactly

`13,204`, `37,288`, `14,478`, and `25,145`

shared bottom-CSP nodes respectively by orientation.

Across all 399 rejected selectors, the exact shared bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 8,433,604 |
| 1 | 5,303,866 |
| 2 | 8,122,042 |
| 3 | 4,943,386 |
| **Total** | **26,802,898** |

## 4. Constructive no-three witness

### Theorem PX754 -- PROVED FINITE WITNESS

Global case `1392` has signature

`(257,514,1028,2056,17,96,4160)`.

Its lexicographically first selector, with complete row-mask state

`(257,514,1028,2056,17,96,4160,130,260,520,1040,2176,8224,12288)`,

has a no-three embedding in radix orientation `1` using clean interleaved top-order index `6928`:

- top assignment: `(2,3,5,6,1,4,0,4,3,1,0,5,2,6)`;
- bottom assignment: `(6,5,4,3,2,0,1)`.

The resulting 28 points are

`(0,4),(0,7),(1,6),(1,3),(2,10),(2,1),(3,12),(3,11),`
`(4,4),(4,2),(5,8),(5,0),(6,0),(6,5),(13,6),(13,9),`
`(12,10),(12,7),(11,12),(11,3),(10,2),(10,1),(9,9),(9,11),`
`(7,8),(7,13),(8,5),(8,13)`.

They are pairwise distinct, and every one of their \(\binom{28}{3}=3,276\) exact integer determinants is nonzero. Thus this selector is a verified no-three witness rather than an obstruction.

## 5. Revised cache boundary

### Corollary PX755 -- PROVED CLASSIFICATION

Adding shard fourteen gives:

- `22,921 + 399 = 23,320` certified-infeasible selectors;
- `1` constructively witnessed selector;
- `1,155,933,381 + 26,802,898 = 1,182,736,279` cumulative rejection-CSP nodes.

Therefore the unclassified active count is

\[
71{,}860-23{,}320-1=\boxed{48{,}539}.
\]

The remaining multiplicity-four frontier begins at global case index `1480` and contains 912 signatures and 3,648 selectors.

## 6. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard14_mixed.cpp \
  -o /tmp/m4s14

# Full mixed transcript.
/tmp/m4s14

# Independent selected-case witness and rejected-subset check.
/tmp/m4s14 1392
```

The full run verifies all 99 obstruction groups, the jointly rejected three-selector subset of case `1392`, all witness permutations and state data, pairwise point distinctness, all 3,276 nonzero determinants, aggregate counts, and the mixed transcript digest.
