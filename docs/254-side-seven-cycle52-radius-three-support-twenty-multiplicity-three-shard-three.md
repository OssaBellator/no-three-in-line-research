# Exact `(5,2)` radius-three support-twenty multiplicity-three shard three

PX812--PX815 close global multiplicity-three cases `200` through `299`. This chapter closes global cases `300` through `399`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX818 -- PROVED FINITE

Shard three contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `300` through `399`.

## 2. Exact clean-top census

### Theorem PX819 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 6,392,150 | 27,881,020 |
| Interleaved | 6,458,168 | 27,065,957 |
| **Total** | **12,850,318** | **54,946,977** |

The complete ordered transcript has deterministic digest

`5218863638130273781` (`0x486d20d401f52df5`).

## 3. Exact shared bottom CSP

### Theorem PX820 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 11,591,307 |
| 1 | 11,417,428 |
| 2 | 11,239,407 |
| 3 | 11,360,057 |
| **Total** | **45,608,199** |

Every exact tree terminates with the active-selector mask empty. Nineteen duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX821 -- PROVED REDUCTION

Adding shard three gives

\[
27{,}868+300=\boxed{28{,}168}
\]

certified-infeasible selectors and

\[
1{,}592{,}286{,}904+45{,}608{,}199
=\boxed{1{,}637{,}895{,}103}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-28{,}168-1=\boxed{43{,}691}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `400` and contains `3,144` signatures and `9,432` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard3.cpp \
  -o /tmp/m3s3

/tmp/m3s3
/tmp/m3s3 300 0
/tmp/m3s3 399 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
