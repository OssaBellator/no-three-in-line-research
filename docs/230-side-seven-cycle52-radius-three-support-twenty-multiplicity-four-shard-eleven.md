# Exact `(5,2)` radius-three support-twenty multiplicity-four shard eleven

PX731--PX734 close global multiplicity-four case indices `980` through `1079`. This chapter closes global cases `1080` through `1179`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX735 -- PROVED FINITE

Shard eleven contains one hundred top signatures of multiplicity four, hence

\[
100\cdot4=\boxed{400}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all 2,392 multiplicity-four signatures, and selects the lexicographic interval `1080` through `1179`.

## 2. Exact clean-top census

### Theorem PX736 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,709,436 | 35,453,073 |
| Interleaved | 3,825,399 | 30,098,760 |
| **Total** | **8,534,835** | **65,551,833** |

The complete ordered transcript has deterministic digest

`16641707327491079352` (`0xe6f338a48f1efcb8`).

## 3. Exact shared bottom CSP

### Theorem PX737 -- PROVED FINITE

Every one of the 400 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 7,168,836 |
| 1 | 5,934,517 |
| 2 | 7,120,880 |
| 3 | 5,830,942 |
| **Total** | **26,055,175** |

Every exact tree terminates with the active-selector mask empty. Six duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX738 -- PROVED REDUCTION

Adding shard eleven gives

\[
21{,}721+400=\boxed{22{,}121}
\]

certified-infeasible selectors and

\[
1{,}076{,}401{,}986+26{,}055{,}175
=\boxed{1{,}102{,}457{,}161}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-22{,}121=\boxed{49{,}739}
\]

support-twenty selectors remain active.

The remaining multiplicity-four frontier begins at global case index `1180` and contains 1,212 signatures and 4,848 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard11.cpp \
  -o /tmp/m4s11

/tmp/m4s11
/tmp/m4s11 1080 0
/tmp/m4s11 1179 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
