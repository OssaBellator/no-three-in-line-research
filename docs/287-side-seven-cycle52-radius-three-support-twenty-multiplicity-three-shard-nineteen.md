# Exact `(5,2)` radius-three support-twenty multiplicity-three shard nineteen

PX908--PX911 close global multiplicity-three cases `1800` through `1899`. This chapter closes global cases `1900` through `1999`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX916 -- PROVED FINITE

Shard nineteen contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `1900` through `1999`.

## 2. Exact clean-top census

### Theorem PX917 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,205,218 | 30,557,339 |
| Interleaved | 3,922,766 | 23,926,433 |
| **Total** | **9,127,984** | **54,483,772** |

The complete ordered transcript has deterministic digest

`18153953954358039500` (`0xfbefccf00e4f13cc`).

## 3. Exact shared bottom CSP

### Theorem PX918 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation.

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 9,166,047 |
| 1 | 6,870,435 |
| 2 | 8,773,636 |
| 3 | 6,467,881 |
| **Total** | **31,277,999** |

Every exact tree terminates with the active-selector mask empty. Twenty-four duplicated recovery rows agreed exactly before the canonical transcript was digested. A fresh rerun of global case `1999` matched the canonical row exactly.

## 4. Revised cache boundary

### Corollary PX919 -- PROVED REDUCTION

Adding shard nineteen gives

\[
32{,}668+300=\boxed{32{,}968}
\]

certified-infeasible selectors and

\[
2{,}153{,}090{,}718+31{,}277{,}999
=\boxed{2{,}184{,}368{,}717}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-32{,}968-1=\boxed{38{,}891}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `2000` and contains `1,544` signatures and `4,632` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard19.cpp \
  -o /tmp/m3s19

/tmp/m3s19
/tmp/m3s19 1900 0
/tmp/m3s19 1999 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
