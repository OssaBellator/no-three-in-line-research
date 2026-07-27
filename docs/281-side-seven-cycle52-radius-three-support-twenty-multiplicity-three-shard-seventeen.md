# Exact `(5,2)` radius-three support-twenty multiplicity-three shard seventeen

PX892--PX895 close global multiplicity-three cases `1600` through `1699`. This chapter closes global cases `1700` through `1799`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX900 -- PROVED FINITE

Shard seventeen contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `1700` through `1799`.

## 2. Exact clean-top census

### Theorem PX901 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,302,962 | 32,972,336 |
| Interleaved | 4,215,652 | 24,912,718 |
| **Total** | **9,518,614** | **57,885,054** |

The complete ordered transcript has deterministic digest

`13427787607035111628` (`0xba5915af64b868cc`).

## 3. Exact shared bottom CSP

### Theorem PX902 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation.

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 8,890,568 |
| 1 | 7,194,248 |
| 2 | 8,855,909 |
| 3 | 6,877,928 |
| **Total** | **31,818,653** |

Every exact tree terminates with the active-selector mask empty. Thirty-six duplicated recovery rows agreed exactly, and a fresh rerun of boundary case `1799` matched the canonical transcript.

## 4. Revised cache boundary

### Corollary PX903 -- PROVED REDUCTION

Adding shard seventeen gives

\[
32{,}068+300=\boxed{32{,}368}
\]

certified-infeasible selectors and

\[
2{,}082{,}633{,}876+31{,}818{,}653
=\boxed{2{,}114{,}452{,}529}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-32{,}368-1=\boxed{39{,}491}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `1800` and contains `1,744` signatures and `5,232` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard17.cpp \
  -o /tmp/m3s17

/tmp/m3s17
/tmp/m3s17 1700 0
/tmp/m3s17 1799 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
