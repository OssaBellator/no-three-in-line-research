# Exact `(5,2)` radius-three support-twenty multiplicity-four shard three

PX699--PX702 close global multiplicity-four case indices `180` through `279`. This chapter closes global cases `280` through `379`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX703 -- PROVED FINITE

Shard three contains one hundred top signatures of multiplicity four, hence

\[
100\cdot4=\boxed{400}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all 2,392 multiplicity-four signatures, and selects the lexicographic interval `280` through `379`.

## 2. Exact clean-top census

### Theorem PX704 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 8,854,171 | 48,104,878 |
| Interleaved | 3,074,772 | 18,442,760 |
| **Total** | **11,928,943** | **66,547,638** |

The complete ordered transcript has deterministic digest

`6137969857602763612` (`0x552e7310ac77bb5c`).

## 3. Exact shared bottom CSP

### Theorem PX705 -- PROVED FINITE

Every one of the 400 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 16,942,013 |
| 1 | 5,480,731 |
| 2 | 15,819,174 |
| 3 | 5,468,426 |
| **Total** | **43,710,344** |

Every exact tree terminates with the active-selector mask empty.

## 4. Revised cache boundary

### Corollary PX706 -- PROVED REDUCTION

Adding shard three gives

\[
18{,}521+400=\boxed{18{,}921}
\]

certified-infeasible selectors and

\[
827{,}520{,}164+43{,}710{,}344
=\boxed{871{,}230{,}508}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-18{,}921=\boxed{52{,}939}
\]

support-twenty selectors remain active.

The remaining multiplicity-four frontier begins at global case index `380` and contains 2,012 signatures and 8,048 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard3.cpp \
  -o /tmp/m4s3

/tmp/m4s3
/tmp/m4s3 280 0
/tmp/m4s3 379 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
