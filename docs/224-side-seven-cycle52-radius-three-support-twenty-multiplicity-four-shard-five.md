# Exact `(5,2)` radius-three support-twenty multiplicity-four shard five

PX707--PX710 close global multiplicity-four case indices `380` through `479`. This chapter closes global cases `480` through `579`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX711 -- PROVED FINITE

Shard five contains one hundred top signatures of multiplicity four, hence

\[
100\cdot4=\boxed{400}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all 2,392 multiplicity-four signatures, and selects the lexicographic interval `480` through `579`.

## 2. Exact clean-top census

### Theorem PX712 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,222,004 | 27,070,528 |
| Interleaved | 3,626,774 | 21,962,260 |
| **Total** | **7,848,778** | **49,032,788** |

The complete ordered transcript has deterministic digest

`16120744542518780924` (`0xdfb863c003a623fc`).

## 3. Exact shared bottom CSP

### Theorem PX713 -- PROVED FINITE

Every one of the 400 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 6,641,795 |
| 1 | 5,769,278 |
| 2 | 6,386,903 |
| 3 | 5,293,527 |
| **Total** | **24,091,503** |

Every exact tree terminates with the active-selector mask empty.

## 4. Revised cache boundary

### Corollary PX714 -- PROVED REDUCTION

Adding shard five gives

\[
19{,}321+400=\boxed{19{,}721}
\]

certified-infeasible selectors and

\[
901{,}698{,}409+24{,}091{,}503
=\boxed{925{,}789{,}912}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-19{,}721=\boxed{52{,}139}
\]

support-twenty selectors remain active.

The remaining multiplicity-four frontier begins at global case index `580` and contains 1,812 signatures and 7,248 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard5.cpp \
  -o /tmp/m4s5

/tmp/m4s5
/tmp/m4s5 480 0
/tmp/m4s5 579 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
