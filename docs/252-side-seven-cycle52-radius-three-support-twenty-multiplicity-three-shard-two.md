# Exact `(5,2)` radius-three support-twenty multiplicity-three shard two

PX806--PX809 close global multiplicity-three cases `100` through `199`. This chapter closes global cases `200` through `299`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX812 -- PROVED FINITE

Shard two contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `200` through `299`.

## 2. Exact clean-top census

### Theorem PX813 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,817,048 | 34,249,610 |
| Interleaved | 4,596,184 | 28,692,725 |
| **Total** | **10,413,232** | **62,942,335** |

The complete ordered transcript has deterministic digest

`14334911769310005031` (`0xc6efd64df84a0727`).

## 3. Exact shared bottom CSP

### Theorem PX814 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 10,105,198 |
| 1 | 8,407,578 |
| 2 | 10,234,882 |
| 3 | 7,540,623 |
| **Total** | **36,288,281** |

Every exact tree terminates with the active-selector mask empty. Eleven duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX815 -- PROVED REDUCTION

Adding shard two gives

\[
27{,}568+300=\boxed{27{,}868}
\]

certified-infeasible selectors and

\[
1{,}555{,}998{,}623+36{,}288{,}281
=\boxed{1{,}592{,}286{,}904}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-27{,}868-1=\boxed{43{,}991}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `300` and contains `3,244` signatures and `9,732` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard2.cpp \
  -o /tmp/m3s2

/tmp/m3s2
/tmp/m3s2 200 0
/tmp/m3s2 299 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
