# Exact `(5,2)` radius-three support-twenty multiplicity-four shard two

PX695--PX698 close global multiplicity-four case indices `100` through `179`. This chapter closes global cases `180` through `279`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX699 -- PROVED FINITE

Shard two contains one hundred top signatures of multiplicity four, hence

\[
100\cdot4=\boxed{400}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all 2,392 multiplicity-four signatures, and selects the lexicographic interval `180` through `279`.

## 2. Exact clean-top census

### Theorem PX700 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,897,928 | 25,036,685 |
| Interleaved | 5,589,872 | 23,895,638 |
| **Total** | **11,487,800** | **48,932,323** |

The complete ordered transcript has deterministic digest

`2103545732133771940` (`0x1d314bb2c49f5aa4`).

## 3. Exact shared bottom CSP

### Theorem PX701 -- PROVED FINITE

Every one of the 400 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 9,065,985 |
| 1 | 8,914,440 |
| 2 | 9,042,029 |
| 3 | 8,597,078 |
| **Total** | **35,619,532** |

Every exact tree terminates with the active-selector mask empty.

## 4. Revised cache boundary

### Corollary PX702 -- PROVED REDUCTION

Adding shard two gives

\[
18{,}121+400=\boxed{18{,}521}
\]

certified-infeasible selectors and

\[
791{,}900{,}632+35{,}619{,}532
=\boxed{827{,}520{,}164}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-18{,}521=\boxed{53{,}339}
\]

support-twenty selectors remain active.

The remaining multiplicity-four frontier begins at global case index `280` and contains 2,112 signatures and 8,448 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard2.cpp \
  -o /tmp/m4s2

/tmp/m4s2
/tmp/m4s2 279 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
