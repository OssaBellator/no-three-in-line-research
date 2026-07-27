# Exact `(5,2)` radius-three support-twenty multiplicity-three shard sixteen

PX884--PX887 close global multiplicity-three cases `1500` through `1599`. This chapter closes global cases `1600` through `1699`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX892 -- PROVED FINITE

Shard sixteen contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `1600` through `1699`.

## 2. Exact clean-top census

### Theorem PX893 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,443,596 | 44,929,457 |
| Interleaved | 3,160,465 | 29,856,543 |
| **Total** | **8,604,061** | **74,786,000** |

The complete ordered transcript has deterministic digest

`4422199473448535567` (`0x3d5ecefdc4d1c60f`).

## 3. Exact shared bottom CSP

### Theorem PX894 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation.

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 9,200,669 |
| 1 | 5,162,024 |
| 2 | 8,942,845 |
| 3 | 5,226,725 |
| **Total** | **28,532,263** |

Every exact tree terminates with the active-selector mask empty. A fresh rerun of boundary case `1699` agreed exactly with the canonical transcript before the shard digest was committed.

## 4. Revised cache boundary

### Corollary PX895 -- PROVED REDUCTION

Adding shard sixteen gives

\[
31{,}768+300=\boxed{32{,}068}
\]

certified-infeasible selectors and

\[
2{,}054{,}101{,}613+28{,}532{,}263
=\boxed{2{,}082{,}633{,}876}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-32{,}068-1=\boxed{39{,}791}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `1700` and contains `1,844` signatures and `5,532` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard16.cpp \
  -o /tmp/m3s16

/tmp/m3s16
/tmp/m3s16 1600 0
/tmp/m3s16 1699 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
