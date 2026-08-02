# Exact `(5,2)` radius-three support-twenty multiplicity-four shard eight

PX719--PX722 close global multiplicity-four case indices `680` through `779`. This chapter closes global cases `780` through `879`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX723 -- PROVED FINITE

Shard eight contains one hundred top signatures of multiplicity four, hence

\[
100\cdot4=\boxed{400}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all 2,392 multiplicity-four signatures, and selects the lexicographic interval `780` through `879`.

## 2. Exact clean-top census

### Theorem PX724 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,945,601 | 32,622,543 |
| Interleaved | 3,531,294 | 23,246,273 |
| **Total** | **8,476,895** | **55,868,816** |

The complete ordered transcript has deterministic digest

`3281681937089769951` (`0x2d8ae055ae0d31df`).

## 3. Exact shared bottom CSP

### Theorem PX725 -- PROVED FINITE

Every one of the 400 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 7,655,405 |
| 1 | 5,444,441 |
| 2 | 7,533,438 |
| 3 | 5,117,444 |
| **Total** | **25,750,728** |

Every exact tree terminates with the active-selector mask empty.

## 4. Revised cache boundary

### Corollary PX726 -- PROVED REDUCTION

Adding shard eight gives

\[
20{,}521+400=\boxed{20{,}921}
\]

certified-infeasible selectors and

\[
981{,}104{,}365+25{,}750{,}728
=\boxed{1{,}006{,}855{,}093}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-20{,}921=\boxed{50{,}939}
\]

support-twenty selectors remain active.

The remaining multiplicity-four frontier begins at global case index `880` and contains 1,512 signatures and 6,048 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard8.cpp \
  -o /tmp/m4s8

/tmp/m4s8
/tmp/m4s8 780 0
/tmp/m4s8 879 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
