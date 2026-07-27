# Exact `(5,2)` radius-three support-twenty multiplicity-three shard eight

PX836--PX839 close global multiplicity-three cases `700` through `799`. This chapter closes global cases `800` through `899`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX842 -- PROVED FINITE

Shard eight contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `800` through `899`.

## 2. Exact clean-top census

### Theorem PX843 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 3,518,306 | 16,368,216 |
| Interleaved | 3,027,808 | 14,499,783 |
| **Total** | **6,546,114** | **30,867,999** |

The complete ordered transcript has deterministic digest

`12170455306990093592` (`0xa8e6249eafe98518`).

## 3. Exact shared bottom CSP

### Theorem PX844 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 6,268,546 |
| 1 | 5,292,350 |
| 2 | 5,610,835 |
| 3 | 4,818,305 |
| **Total** | **21,990,036** |

Every exact tree terminates with the active-selector mask empty. Ten duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX845 -- PROVED REDUCTION

Adding shard eight gives

\[
29{,}368+300=\boxed{29{,}668}
\]

certified-infeasible selectors and

\[
1{,}811{,}189{,}685+21{,}990{,}036
=\boxed{1{,}833{,}179{,}721}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-29{,}668-1=\boxed{42{,}191}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `900` and contains `2,644` signatures and `7,932` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard8.cpp \
  -o /tmp/m3s8

/tmp/m3s8
/tmp/m3s8 800 0
/tmp/m3s8 899 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
