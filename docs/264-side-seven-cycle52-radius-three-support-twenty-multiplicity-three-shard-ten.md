# Exact `(5,2)` radius-three support-twenty multiplicity-three shard ten

PX846--PX849 close global multiplicity-three cases `900` through `999`. This chapter closes global cases `1000` through `1099`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX852 -- PROVED FINITE

Shard ten contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `1000` through `1099`.

## 2. Exact clean-top census

### Theorem PX853 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 3,310,572 | 28,685,755 |
| Interleaved | 3,116,324 | 26,324,531 |
| **Total** | **6,426,896** | **55,010,286** |

The complete ordered transcript has deterministic digest

`12088490713403663561` (`0xa7c2f2419b08a4c9`).

## 3. Exact shared bottom CSP

### Theorem PX854 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 5,764,370 |
| 1 | 5,514,534 |
| 2 | 5,343,998 |
| 3 | 5,010,578 |
| **Total** | **21,633,480** |

Every exact tree terminates with the active-selector mask empty. Four duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX855 -- PROVED REDUCTION

Adding shard ten gives

\[
29{,}968+300=\boxed{30{,}268}
\]

certified-infeasible selectors and

\[
1{,}868{,}753{,}393+21{,}633{,}480
=\boxed{1{,}890{,}386{,}873}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-30{,}268-1=\boxed{41{,}591}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `1100` and contains `2,444` signatures and `7,332` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard10.cpp \
  -o /tmp/m3s10

/tmp/m3s10
/tmp/m3s10 1000 0
/tmp/m3s10 1099 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
