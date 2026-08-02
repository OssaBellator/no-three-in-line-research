# Exact `(5,2)` radius-three support-twenty multiplicity-four shard thirteen

PX739--PX742 close global multiplicity-four case indices `1180` through `1279`. This chapter closes global cases `1280` through `1379`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX745 -- PROVED FINITE

Shard thirteen contains one hundred top signatures of multiplicity four, hence

\[
100\cdot4=\boxed{400}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all 2,392 multiplicity-four signatures, and selects the lexicographic interval `1280` through `1379`.

## 2. Exact clean-top census

### Theorem PX746 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 3,758,673 | 26,438,341 |
| Interleaved | 3,291,475 | 21,497,250 |
| **Total** | **7,050,148** | **47,935,591** |

The complete ordered transcript has deterministic digest

`8144832165213751731` (`0x710841b37abdc9b3`).

## 3. Exact shared bottom CSP

### Theorem PX747 -- PROVED FINITE

Every one of the 400 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 6,310,580 |
| 1 | 5,544,994 |
| 2 | 6,066,696 |
| 3 | 5,288,007 |
| **Total** | **23,210,277** |

Every exact tree terminates with the active-selector mask empty.

## 4. Revised cache boundary

### Corollary PX748 -- PROVED REDUCTION

Adding shard thirteen gives

\[
22{,}521+400=\boxed{22{,}921}
\]

certified-infeasible selectors and

\[
1{,}132{,}723{,}104+23{,}210{,}277
=\boxed{1{,}155{,}933{,}381}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-22{,}921=\boxed{48{,}939}
\]

support-twenty selectors remain active.

The remaining multiplicity-four frontier begins at global case index `1380` and contains 1,012 signatures and 4,048 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard13.cpp \
  -o /tmp/m4s13

/tmp/m4s13
/tmp/m4s13 1280 0
/tmp/m4s13 1379 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
