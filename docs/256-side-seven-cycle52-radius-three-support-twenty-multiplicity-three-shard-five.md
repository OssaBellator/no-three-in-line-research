# Exact `(5,2)` radius-three support-twenty multiplicity-three shard five

PX822--PX825 close global multiplicity-three cases `400` through `499`. This chapter closes global cases `500` through `599`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX826 -- PROVED FINITE

Shard five contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `500` through `599`.

## 2. Exact clean-top census

### Theorem PX827 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 11,171,978 | 45,878,006 |
| Interleaved | 6,825,064 | 31,913,022 |
| **Total** | **17,997,042** | **77,791,028** |

The complete ordered transcript has deterministic digest

`17374652970419326891` (`0xf11f2ad25d878fab`).

## 3. Exact shared bottom CSP

### Theorem PX828 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 20,045,993 |
| 1 | 11,769,433 |
| 2 | 18,734,156 |
| 3 | 11,899,396 |
| **Total** | **62,448,978** |

Every exact tree terminates with the active-selector mask empty. Seven duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX829 -- PROVED REDUCTION

Adding shard five gives

\[
28{,}468+300=\boxed{28{,}768}
\]

certified-infeasible selectors and

\[
1{,}673{,}887{,}901+62{,}448{,}978
=\boxed{1{,}736{,}336{,}879}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-28{,}768-1=\boxed{43{,}091}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `600` and contains `2,944` signatures and `8,832` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard5.cpp \
  -o /tmp/m3s5

/tmp/m3s5
/tmp/m3s5 500 0
/tmp/m3s5 599 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
