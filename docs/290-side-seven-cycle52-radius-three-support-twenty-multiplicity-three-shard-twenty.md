# Exact `(5,2)` radius-three support-twenty multiplicity-three shard twenty

PX916--PX919 close global multiplicity-three cases `1900` through `1999`. This chapter closes global cases `2000` through `2099`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX924 -- PROVED FINITE

Shard twenty contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `2000` through `2099`.

## 2. Exact clean-top census

### Theorem PX925 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,912,632 | 24,609,044 |
| Interleaved | 4,230,024 | 21,813,621 |
| **Total** | **9,142,656** | **46,422,665** |

The complete ordered transcript has deterministic digest

`13076377016111339538` (`0xb5789f9d52661812`).

## 3. Exact shared bottom CSP

### Theorem PX926 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation.

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 8,523,632 |
| 1 | 7,261,420 |
| 2 | 8,070,294 |
| 3 | 6,655,266 |
| **Total** | **30,510,612** |

Every exact tree terminates with the active-selector mask empty. Six duplicated recovery rows agreed exactly before the canonical transcript was digested. A fresh rerun of global case `2099` matched the canonical row exactly.

## 4. Revised cache boundary

### Corollary PX927 -- PROVED REDUCTION

Adding shard twenty gives

\[
32{,}968+300=\boxed{33{,}268}
\]

certified-infeasible selectors and

\[
2{,}184{,}368{,}717+30{,}510{,}612
=\boxed{2{,}214{,}879{,}329}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-33{,}268-1=\boxed{38{,}591}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `2100` and contains `1,444` signatures and `4,332` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard20.cpp \
  -o /tmp/m3s20

/tmp/m3s20
/tmp/m3s20 2000 0
/tmp/m3s20 2099 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
