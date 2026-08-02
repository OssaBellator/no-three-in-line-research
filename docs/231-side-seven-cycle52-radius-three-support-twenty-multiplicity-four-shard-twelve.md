# Exact `(5,2)` radius-three support-twenty multiplicity-four shard twelve

PX735--PX738 close global multiplicity-four case indices `1080` through `1179`. This chapter closes global cases `1180` through `1279`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX739 -- PROVED FINITE

Shard twelve contains one hundred top signatures of multiplicity four, hence

\[
100\cdot4=\boxed{400}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all 2,392 multiplicity-four signatures, and selects the lexicographic interval `1180` through `1279`.

## 2. Exact clean-top census

### Theorem PX740 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,883,671 | 30,556,288 |
| Interleaved | 3,657,672 | 25,402,649 |
| **Total** | **8,541,343** | **55,958,937** |

The complete ordered transcript has deterministic digest

`7039424060371606348` (`0x61b10ee2edc99b4c`).

## 3. Exact shared bottom CSP

### Theorem PX741 -- PROVED FINITE

Every one of the 400 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 8,920,257 |
| 1 | 6,660,138 |
| 2 | 8,563,368 |
| 3 | 6,122,180 |
| **Total** | **30,265,943** |

Every exact tree terminates with the active-selector mask empty. Six duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX742 -- PROVED REDUCTION

Adding shard twelve gives

\[
22{,}121+400=\boxed{22{,}521}
\]

certified-infeasible selectors and

\[
1{,}102{,}457{,}161+30{,}265{,}943
=\boxed{1{,}132{,}723{,}104}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-22{,}521=\boxed{49{,}339}
\]

support-twenty selectors remain active.

The remaining multiplicity-four frontier begins at global case index `1280` and contains 1,112 signatures and 4,448 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard12.cpp \
  -o /tmp/m4s12

/tmp/m4s12
/tmp/m4s12 1180 0
/tmp/m4s12 1279 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
