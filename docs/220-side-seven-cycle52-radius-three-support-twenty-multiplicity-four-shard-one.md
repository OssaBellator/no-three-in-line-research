# Exact `(5,2)` radius-three support-twenty multiplicity-four shard one

PX691--PX694 close global multiplicity-four case indices `0` through `99`. This chapter closes the next lexicographic interval, global cases `100` through `179`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX695 -- PROVED FINITE

The exact tier has 2,392 signatures of multiplicity four. Shard one contains eighty signatures and

\[
80\cdot4=\boxed{320}
\]

selectors.

The verifier regenerates the exact radius layers, asserts the complete multiplicity-four histogram, and selects global case indices `100` through `179`.

## 2. Exact clean-top census

### Theorem PX696 -- PROVED FINITE

Across the eighty signatures, the exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,246,738 | 20,641,344 |
| Interleaved | 3,177,407 | 16,423,028 |
| **Total** | **7,424,145** | **37,064,372** |

The complete ordered transcript has deterministic digest

`17854348480538047953` (`0xf7c76358be8175d1`).

## 3. Exact shared bottom CSP

### Theorem PX697 -- PROVED FINITE

Every one of the 320 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 7,291,121 |
| 1 | 5,332,073 |
| 2 | 7,313,196 |
| 3 | 5,049,986 |
| **Total** | **24,986,376** |

Every exact tree terminates with the active-selector mask empty.

## 4. Revised cache boundary

### Corollary PX698 -- PROVED REDUCTION

Adding shard one gives

\[
17{,}801+320=\boxed{18{,}121}
\]

certified-infeasible selectors and

\[
766{,}914{,}256+24{,}986{,}376
=\boxed{791{,}900{,}632}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-18{,}121=\boxed{53{,}739}
\]

support-twenty selectors remain active.

The remaining multiplicity-four frontier begins at global case index `180` and contains 2,212 signatures and 8,848 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard1.cpp \
  -o /tmp/m4s1

/tmp/m4s1
/tmp/m4s1 179 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
