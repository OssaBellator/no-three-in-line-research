# Exact `(5,2)` radius-three support-twenty multiplicity-three shard twelve

PX856--PX859 close global multiplicity-three cases `1100` through `1199`. This chapter closes global cases `1200` through `1299`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX862 -- PROVED FINITE

Shard twelve contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `1200` through `1299`.

## 2. Exact clean-top census

### Theorem PX863 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,899,054 | 24,836,222 |
| Interleaved | 4,287,820 | 22,387,466 |
| **Total** | **9,186,874** | **47,223,688** |

The complete ordered transcript has deterministic digest

`10436604609621675837` (`0x90d64498d1b44f3d`).

## 3. Exact shared bottom CSP

### Theorem PX864 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 8,805,636 |
| 1 | 7,370,353 |
| 2 | 8,101,190 |
| 3 | 7,198,789 |
| **Total** | **31,475,968** |

Every exact tree terminates with the active-selector mask empty. Four duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX865 -- PROVED REDUCTION

Adding shard twelve gives

\[
30{,}568+300=\boxed{30{,}868}
\]

certified-infeasible selectors and

\[
1{,}919{,}357{,}907+31{,}475{,}968
=\boxed{1{,}950{,}833{,}875}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-30{,}868-1=\boxed{40{,}991}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `1300` and contains `2,244` signatures and `6,732` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard12.cpp \
  -o /tmp/m3s12

/tmp/m3s12
/tmp/m3s12 1200 0
/tmp/m3s12 1299 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
