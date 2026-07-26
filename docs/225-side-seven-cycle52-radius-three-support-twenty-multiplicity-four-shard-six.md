# Exact `(5,2)` radius-three support-twenty multiplicity-four shard six

PX711--PX714 close global multiplicity-four case indices `480` through `579`. This chapter closes global cases `580` through `679`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX715 -- PROVED FINITE

Shard six contains one hundred top signatures of multiplicity four, hence

\[
100\cdot4=\boxed{400}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all 2,392 multiplicity-four signatures, and selects the lexicographic interval `580` through `679`.

## 2. Exact clean-top census

### Theorem PX716 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,509,821 | 30,620,762 |
| Interleaved | 4,158,847 | 22,389,295 |
| **Total** | **9,668,668** | **53,010,057** |

The complete ordered transcript has deterministic digest

`11658676560239131698` (`0xa1cbf08fac39fc32`).

## 3. Exact shared bottom CSP

### Theorem PX717 -- PROVED FINITE

Every one of the 400 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 8,122,756 |
| 1 | 6,161,170 |
| 2 | 7,747,740 |
| 3 | 5,721,623 |
| **Total** | **27,753,289** |

Every exact tree terminates with the active-selector mask empty.

## 4. Revised cache boundary

### Corollary PX718 -- PROVED REDUCTION

Adding shard six gives

\[
19{,}721+400=\boxed{20{,}121}
\]

certified-infeasible selectors and

\[
925{,}789{,}912+27{,}753{,}289
=\boxed{953{,}543{,}201}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-20{,}121=\boxed{51{,}739}
\]

support-twenty selectors remain active.

The remaining multiplicity-four frontier begins at global case index `680` and contains 1,712 signatures and 6,848 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard6.cpp \
  -o /tmp/m4s6

/tmp/m4s6
/tmp/m4s6 580 0
/tmp/m4s6 679 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
