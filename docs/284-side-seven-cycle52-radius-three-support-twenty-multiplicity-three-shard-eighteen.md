# Exact `(5,2)` radius-three support-twenty multiplicity-three shard eighteen

PX900--PX903 close global multiplicity-three cases `1700` through `1799`. This chapter closes global cases `1800` through `1899`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX908 -- PROVED FINITE

Shard eighteen contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `1800` through `1899`.

## 2. Exact clean-top census

### Theorem PX909 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 7,092,176 | 31,534,459 |
| Interleaved | 4,279,954 | 19,409,414 |
| **Total** | **11,372,130** | **50,943,873** |

The complete ordered transcript has deterministic digest

`4853397229172252623` (`0x435abb10c6ad5fcf`).

## 3. Exact shared bottom CSP

### Theorem PX910 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation.

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 12,693,276 |
| 1 | 7,458,176 |
| 2 | 11,675,532 |
| 3 | 6,811,205 |
| **Total** | **38,638,189** |

Every exact tree terminates with the active-selector mask empty. Nine duplicated recovery rows agreed exactly, and a fresh rerun of boundary case `1899` matched the canonical transcript.

## 4. Revised cache boundary

### Corollary PX911 -- PROVED REDUCTION

Adding shard eighteen gives

\[
32{,}368+300=\boxed{32{,}668}
\]

certified-infeasible selectors and

\[
2{,}114{,}452{,}529+38{,}638{,}189
=\boxed{2{,}153{,}090{,}718}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-32{,}668-1=\boxed{39{,}191}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `1900` and contains `1,644` signatures and `4,932` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard18.cpp \
  -o /tmp/m3s18

/tmp/m3s18
/tmp/m3s18 1800 0
/tmp/m3s18 1899 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
