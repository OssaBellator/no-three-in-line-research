# Exact `(5,2)` radius-three support-twenty multiplicity-three shard thirteen

PX862--PX865 close global multiplicity-three cases `1200` through `1299`. This chapter closes global cases `1300` through `1399`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX868 -- PROVED FINITE

Shard thirteen contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `1300` through `1399`.

## 2. Exact clean-top census

### Theorem PX869 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 3,387,028 | 33,130,720 |
| Interleaved | 3,513,002 | 28,472,042 |
| **Total** | **6,900,030** | **61,602,762** |

The complete ordered transcript has deterministic digest

`13401041420045109676` (`0xb9fa102b7615c9ac`).

## 3. Exact shared bottom CSP

### Theorem PX870 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation.

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 5,696,899 |
| 1 | 6,279,800 |
| 2 | 6,018,454 |
| 3 | 5,448,632 |
| **Total** | **23,443,785** |

Every exact tree terminates with the active-selector mask empty. Sixteen duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX871 -- PROVED REDUCTION

Adding shard thirteen gives

\[
30{,}868+300=\boxed{31{,}168}
\]

certified-infeasible selectors and

\[
1{,}950{,}833{,}875+23{,}443{,}785
=\boxed{1{,}974{,}277{,}660}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-31{,}168-1=\boxed{40{,}691}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `1400` and contains `2,144` signatures and `6,432` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard13.cpp \
  -o /tmp/m3s13

/tmp/m3s13
/tmp/m3s13 1300 0
/tmp/m3s13 1399 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
