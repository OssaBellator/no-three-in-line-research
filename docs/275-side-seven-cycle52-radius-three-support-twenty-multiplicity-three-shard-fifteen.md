# Exact `(5,2)` radius-three support-twenty multiplicity-three shard fifteen

PX878--PX881 close global multiplicity-three cases `1400` through `1499`. This chapter closes global cases `1500` through `1599`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX884 -- PROVED FINITE

Shard fifteen contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `1500` through `1599`.

## 2. Exact clean-top census

### Theorem PX885 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 7,266,748 | 35,429,821 |
| Interleaved | 4,135,428 | 21,178,323 |
| **Total** | **11,402,176** | **56,608,144** |

The complete ordered transcript has deterministic digest

`2105066167187410418` (`0x1d36b286a3e60df2`).

## 3. Exact shared bottom CSP

### Theorem PX886 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation.

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 12,992,091 |
| 1 | 6,973,894 |
| 2 | 12,496,155 |
| 3 | 7,178,897 |
| **Total** | **39,641,037** |

Every exact tree terminates with the active-selector mask empty. Forty duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX887 -- PROVED REDUCTION

Adding shard fifteen gives

\[
31{,}468+300=\boxed{31{,}768}
\]

certified-infeasible selectors and

\[
2{,}014{,}460{,}576+39{,}641{,}037
=\boxed{2{,}054{,}101{,}613}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-31{,}768-1=\boxed{40{,}091}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `1600` and contains `1,944` signatures and `5,832` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard15.cpp \
  -o /tmp/m3s15

/tmp/m3s15
/tmp/m3s15 1500 0
/tmp/m3s15 1599 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
