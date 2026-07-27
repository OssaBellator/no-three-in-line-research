# Exact `(5,2)` radius-three support-twenty multiplicity-three shard eleven

PX852--PX855 close global multiplicity-three cases `1000` through `1099`. This chapter closes global cases `1100` through `1199`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX856 -- PROVED FINITE

Shard eleven contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `1100` through `1199`.

## 2. Exact clean-top census

### Theorem PX857 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,887,082 | 28,322,709 |
| Interleaved | 3,641,746 | 21,853,698 |
| **Total** | **8,528,828** | **50,176,407** |

The complete ordered transcript has deterministic digest

`4611443749689298654` (`0x3fff23a869ed0ede`).

## 3. Exact shared bottom CSP

### Theorem PX858 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 8,537,948 |
| 1 | 6,260,730 |
| 2 | 8,132,293 |
| 3 | 6,040,063 |
| **Total** | **28,971,034** |

Every exact tree terminates with the active-selector mask empty. Twenty-one duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX859 -- PROVED REDUCTION

Adding shard eleven gives

\[
30{,}268+300=\boxed{30{,}568}
\]

certified-infeasible selectors and

\[
1{,}890{,}386{,}873+28{,}971{,}034
=\boxed{1{,}919{,}357{,}907}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-30{,}568-1=\boxed{41{,}291}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `1200` and contains `2,344` signatures and `7,032` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard11.cpp \
  -o /tmp/m3s11

/tmp/m3s11
/tmp/m3s11 1100 0
/tmp/m3s11 1199 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
