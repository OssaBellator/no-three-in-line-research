# Exact `(5,2)` radius-three support-twenty multiplicity-three shard twenty-one

PX924--PX927 close global multiplicity-three cases `2000` through `2099`. This chapter closes global cases `2100` through `2199`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX932 -- PROVED FINITE

Shard twenty-one contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `2100` through `2199`.

## 2. Exact clean-top census

### Theorem PX933 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 8,258,402 | 55,510,853 |
| Interleaved | 4,931,106 | 40,759,840 |
| **Total** | **13,189,508** | **96,270,693** |

The complete ordered transcript has deterministic digest

`9853376004029332515` (`0x88be39452e86bc23`).

## 3. Exact shared bottom CSP

### Theorem PX934 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation.

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 15,011,755 |
| 1 | 8,973,290 |
| 2 | 14,619,133 |
| 3 | 8,198,957 |
| **Total** | **46,803,135** |

Every exact tree terminates with the active-selector mask empty. Twelve duplicated recovery rows agreed exactly before the canonical transcript was digested. A fresh rerun of global case `2199` matched the canonical row exactly.

## 4. Revised cache boundary

### Corollary PX935 -- PROVED REDUCTION

Adding shard twenty-one gives

\[
33{,}268+300=\boxed{33{,}568}
\]

certified-infeasible selectors and

\[
2{,}214{,}879{,}329+46{,}803{,}135
=\boxed{2{,}261{,}682{,}464}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-33{,}568-1=\boxed{38{,}291}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `2200` and contains `1,344` signatures and `4,032` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard21.cpp \
  -o /tmp/m3s21

/tmp/m3s21
/tmp/m3s21 2100 0
/tmp/m3s21 2199 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
