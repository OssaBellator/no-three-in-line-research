# Exact `(5,2)` radius-three support-twenty multiplicity-three shard six

PX826--PX829 close global multiplicity-three cases `500` through `599`. This chapter closes global cases `600` through `699`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX830 -- PROVED FINITE

Shard six contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `600` through `699`.

## 2. Exact clean-top census

### Theorem PX831 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 8,080,650 | 61,266,632 |
| Interleaved | 6,781,398 | 47,608,431 |
| **Total** | **14,862,048** | **108,875,063** |

The complete ordered transcript has deterministic digest

`4240448745985646561` (`0x3ad919aae8b99fe1`).

## 3. Exact shared bottom CSP

### Theorem PX832 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 14,542,238 |
| 1 | 12,109,860 |
| 2 | 13,433,301 |
| 3 | 12,184,856 |
| **Total** | **52,270,255** |

Every exact tree terminates with the active-selector mask empty. Six duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX833 -- PROVED REDUCTION

Adding shard six gives

\[
28{,}768+300=\boxed{29{,}068}
\]

certified-infeasible selectors and

\[
1{,}736{,}336{,}879+52{,}270{,}255
=\boxed{1{,}788{,}607{,}134}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-29{,}068-1=\boxed{42{,}791}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `700` and contains `2,844` signatures and `8,532` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard6.cpp \
  -o /tmp/m3s6

/tmp/m3s6
/tmp/m3s6 600 0
/tmp/m3s6 699 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
