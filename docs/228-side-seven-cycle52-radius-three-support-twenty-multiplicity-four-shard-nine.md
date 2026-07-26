# Exact `(5,2)` radius-three support-twenty multiplicity-four shard nine

PX723--PX726 close global multiplicity-four case indices `780` through `879`. This chapter closes global cases `880` through `979`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX727 -- PROVED FINITE

Shard nine contains one hundred top signatures of multiplicity four, hence

\[
100\cdot4=\boxed{400}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all 2,392 multiplicity-four signatures, and selects the lexicographic interval `880` through `979`.

## 2. Exact clean-top census

### Theorem PX728 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,755,656 | 24,637,240 |
| Interleaved | 4,229,387 | 24,648,351 |
| **Total** | **8,985,043** | **49,285,591** |

The complete ordered transcript has deterministic digest

`12419190773889184606` (`0xac59d4358b79335e`).

## 3. Exact shared bottom CSP

### Theorem PX729 -- PROVED FINITE

Every one of the 400 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 8,468,880 |
| 1 | 7,617,110 |
| 2 | 8,536,783 |
| 3 | 6,945,121 |
| **Total** | **31,567,894** |

Every exact tree terminates with the active-selector mask empty. Three duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX730 -- PROVED REDUCTION

Adding shard nine gives

\[
20{,}921+400=\boxed{21{,}321}
\]

certified-infeasible selectors and

\[
1{,}006{,}855{,}093+31{,}567{,}894
=\boxed{1{,}038{,}422{,}987}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-21{,}321=\boxed{50{,}539}
\]

support-twenty selectors remain active.

The remaining multiplicity-four frontier begins at global case index `980` and contains 1,412 signatures and 5,648 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard9.cpp \
  -o /tmp/m4s9

/tmp/m4s9
/tmp/m4s9 880 0
/tmp/m4s9 979 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
