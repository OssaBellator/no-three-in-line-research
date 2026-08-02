# Exact `(5,2)` radius-three support-twenty multiplicity-four shard seven

PX715--PX718 close global multiplicity-four case indices `580` through `679`. This chapter closes global cases `680` through `779`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX719 -- PROVED FINITE

Shard seven contains one hundred top signatures of multiplicity four, hence

\[
100\cdot4=\boxed{400}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all 2,392 multiplicity-four signatures, and selects the lexicographic interval `680` through `779`.

## 2. Exact clean-top census

### Theorem PX720 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,141,457 | 34,476,740 |
| Interleaved | 4,043,072 | 29,309,655 |
| **Total** | **9,184,529** | **63,786,395** |

The complete ordered transcript has deterministic digest

`11675003001759290027` (`0xa205f15f8f7b52ab`).

## 3. Exact shared bottom CSP

### Theorem PX721 -- PROVED FINITE

Every one of the 400 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 7,914,701 |
| 1 | 6,080,386 |
| 2 | 7,918,135 |
| 3 | 5,647,942 |
| **Total** | **27,561,164** |

Every exact tree terminates with the active-selector mask empty.

## 4. Revised cache boundary

### Corollary PX722 -- PROVED REDUCTION

Adding shard seven gives

\[
20{,}121+400=\boxed{20{,}521}
\]

certified-infeasible selectors and

\[
953{,}543{,}201+27{,}561{,}164
=\boxed{981{,}104{,}365}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-20{,}521=\boxed{51{,}339}
\]

support-twenty selectors remain active.

The remaining multiplicity-four frontier begins at global case index `780` and contains 1,612 signatures and 6,448 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard7.cpp \
  -o /tmp/m4s7

/tmp/m4s7
/tmp/m4s7 680 0
/tmp/m4s7 779 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
