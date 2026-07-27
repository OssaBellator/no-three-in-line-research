# Exact `(5,2)` radius-three support-twenty multiplicity-three shard nine

PX842--PX845 close global multiplicity-three cases `800` through `899`. This chapter closes global cases `900` through `999`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX846 -- PROVED FINITE

Shard nine contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `900` through `999`.

## 2. Exact clean-top census

### Theorem PX847 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,613,366 | 38,524,963 |
| Interleaved | 4,495,113 | 27,653,375 |
| **Total** | **10,108,479** | **66,178,338** |

The complete ordered transcript has deterministic digest

`11884124847722068902` (`0xa4ece4958eddfba6`).

## 3. Exact shared bottom CSP

### Theorem PX848 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 10,343,692 |
| 1 | 8,234,478 |
| 2 | 9,276,412 |
| 3 | 7,719,090 |
| **Total** | **35,573,672** |

Every exact tree terminates with the active-selector mask empty. Six duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX849 -- PROVED REDUCTION

Adding shard nine gives

\[
29{,}668+300=\boxed{29{,}968}
\]

certified-infeasible selectors and

\[
1{,}833{,}179{,}721+35{,}573{,}672
=\boxed{1{,}868{,}753{,}393}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-29{,}968-1=\boxed{41{,}891}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `1000` and contains `2,544` signatures and `7,632` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard9.cpp \
  -o /tmp/m3s9

/tmp/m3s9
/tmp/m3s9 900 0
/tmp/m3s9 999 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
