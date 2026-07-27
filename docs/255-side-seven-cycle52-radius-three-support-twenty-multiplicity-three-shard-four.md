# Exact `(5,2)` radius-three support-twenty multiplicity-three shard four

PX818--PX821 close global multiplicity-three cases `300` through `399`. This chapter closes global cases `400` through `499`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX822 -- PROVED FINITE

Shard four contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `400` through `499`.

## 2. Exact clean-top census

### Theorem PX823 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 6,509,108 | 33,529,101 |
| Interleaved | 4,316,592 | 21,419,876 |
| **Total** | **10,825,700** | **54,948,977** |

The complete ordered transcript has deterministic digest

`10311187618878375372` (`0x8f18b28223a6c5cc`).

## 3. Exact shared bottom CSP

### Theorem PX824 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 11,154,608 |
| 1 | 6,964,716 |
| 2 | 10,631,223 |
| 3 | 7,242,251 |
| **Total** | **35,992,798** |

Every exact tree terminates with the active-selector mask empty. Seven duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX825 -- PROVED REDUCTION

Adding shard four gives

\[
28{,}168+300=\boxed{28{,}468}
\]

certified-infeasible selectors and

\[
1{,}637{,}895{,}103+35{,}992{,}798
=\boxed{1{,}673{,}887{,}901}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-28{,}468-1=\boxed{43{,}391}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `500` and contains `3,044` signatures and `9,132` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard4.cpp \
  -o /tmp/m3s4

/tmp/m3s4
/tmp/m3s4 400 0
/tmp/m3s4 499 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
