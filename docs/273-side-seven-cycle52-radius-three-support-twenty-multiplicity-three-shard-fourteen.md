# Exact `(5,2)` radius-three support-twenty multiplicity-three shard fourteen

PX868--PX871 close global multiplicity-three cases `1300` through `1399`. This chapter closes global cases `1400` through `1499`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX878 -- PROVED FINITE

Shard fourteen contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `1400` through `1499`.

## 2. Exact clean-top census

### Theorem PX879 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 6,400,098 | 24,666,412 |
| Interleaved | 4,974,886 | 19,854,597 |
| **Total** | **11,374,984** | **44,521,009** |

The complete ordered transcript has deterministic digest

`15279610700182069842` (`0xd40c14fa1a9c2252`).

## 3. Exact shared bottom CSP

### Theorem PX880 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation.

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 11,347,949 |
| 1 | 8,886,433 |
| 2 | 11,563,218 |
| 3 | 8,385,316 |
| **Total** | **40,182,916** |

Every exact tree terminates with the active-selector mask empty. Twenty-five duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX881 -- PROVED REDUCTION

Adding shard fourteen gives

\[
31{,}168+300=\boxed{31{,}468}
\]

certified-infeasible selectors and

\[
1{,}974{,}277{,}660+40{,}182{,}916
=\boxed{2{,}014{,}460{,}576}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-31{,}468-1=\boxed{40{,}391}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `1500` and contains `2,044` signatures and `6,132` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard14.cpp \
  -o /tmp/m3s14

/tmp/m3s14
/tmp/m3s14 1400 0
/tmp/m3s14 1499 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
