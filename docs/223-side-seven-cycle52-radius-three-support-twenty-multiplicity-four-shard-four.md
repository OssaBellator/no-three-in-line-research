# Exact `(5,2)` radius-three support-twenty multiplicity-four shard four

PX703--PX706 close global multiplicity-four case indices `280` through `379`. This chapter closes global cases `380` through `479`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX707 -- PROVED FINITE

Shard four contains one hundred top signatures of multiplicity four, hence

\[
100\cdot4=\boxed{400}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all 2,392 multiplicity-four signatures, and selects the lexicographic interval `380` through `479`.

## 2. Exact clean-top census

### Theorem PX708 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,284,463 | 38,170,524 |
| Interleaved | 3,771,951 | 24,900,473 |
| **Total** | **9,056,414** | **63,070,997** |

The complete ordered transcript has deterministic digest

`1231252113985398192` (`0x11164946330c65b0`).

## 3. Exact shared bottom CSP

### Theorem PX709 -- PROVED FINITE

Every one of the 400 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 9,128,638 |
| 1 | 6,402,119 |
| 2 | 8,731,796 |
| 3 | 6,205,348 |
| **Total** | **30,467,901** |

Every exact tree terminates with the active-selector mask empty.

## 4. Revised cache boundary

### Corollary PX710 -- PROVED REDUCTION

Adding shard four gives

\[
18{,}921+400=\boxed{19{,}321}
\]

certified-infeasible selectors and

\[
871{,}230{,}508+30{,}467{,}901
=\boxed{901{,}698{,}409}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-19{,}321=\boxed{52{,}539}
\]

support-twenty selectors remain active.

The remaining multiplicity-four frontier begins at global case index `480` and contains 1,912 signatures and 7,648 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard4.cpp \
  -o /tmp/m4s4

/tmp/m4s4
/tmp/m4s4 380 0
/tmp/m4s4 479 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
