# Exact `(5,2)` radius-three support-twenty multiplicity-three shard one

PX800--PX803 close global multiplicity-three cases `0` through `99`. This chapter closes the next lexicographic interval, global cases `100` through `199`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX806 -- PROVED FINITE

Shard one contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `100` through `199`.

## 2. Exact clean-top census

### Theorem PX807 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 6,341,588 | 35,667,482 |
| Interleaved | 5,776,036 | 29,320,319 |
| **Total** | **12,117,624** | **64,987,801** |

The complete ordered transcript has deterministic digest

`6981881274263131756` (`0x60e4a0070067d66c`).

## 3. Exact shared bottom CSP

### Theorem PX808 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 11,184,684 |
| 1 | 9,969,160 |
| 2 | 10,698,436 |
| 3 | 9,962,634 |
| **Total** | **41,814,914** |

Every exact search terminates with the active-selector mask empty.

## 4. Revised cache boundary

### Corollary PX809 -- PROVED REDUCTION

Adding shard one gives

\[
27{,}268+300=\boxed{27{,}568}
\]

certified-infeasible selectors and

\[
1{,}514{,}183{,}709+41{,}814{,}914
=\boxed{1{,}555{,}998{,}623}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-27{,}568-1=\boxed{44{,}291}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `200` and contains `3,344` signatures and `10,032` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard1.cpp \
  -o /tmp/m3s1

/tmp/m3s1
/tmp/m3s1 100 0
/tmp/m3s1 199 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
