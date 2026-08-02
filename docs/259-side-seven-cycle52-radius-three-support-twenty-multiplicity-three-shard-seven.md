# Exact `(5,2)` radius-three support-twenty multiplicity-three shard seven

PX830--PX833 close global multiplicity-three cases `600` through `699`. This chapter closes global cases `700` through `799`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX836 -- PROVED FINITE

Shard seven contains one hundred multiplicity-three signatures and therefore

\[
100\cdot3=\boxed{300}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all `3,544` multiplicity-three signatures, and selects global cases `700` through `799`.

## 2. Exact clean-top census

### Theorem PX837 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 3,599,282 | 28,811,477 |
| Interleaved | 2,996,682 | 25,488,200 |
| **Total** | **6,595,964** | **54,299,677** |

The complete ordered transcript has deterministic digest

`17881519169292883135` (`0xf827eaf1b20a54bf`).

## 3. Exact shared bottom CSP

### Theorem PX838 -- PROVED FINITE

Every one of the 300 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 6,485,138 |
| 1 | 5,387,842 |
| 2 | 5,846,703 |
| 3 | 4,862,868 |
| **Total** | **22,582,551** |

Every exact tree terminates with the active-selector mask empty. Two duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX839 -- PROVED REDUCTION

Adding shard seven gives

\[
29{,}068+300=\boxed{29{,}368}
\]

certified-infeasible selectors and

\[
1{,}788{,}607{,}134+22{,}582{,}551
=\boxed{1{,}811{,}189{,}685}
\]

shared rejection-CSP nodes. Together with the one constructive multiplicity-four witness, this leaves

\[
71{,}860-29{,}368-1=\boxed{42{,}491}
\]

unclassified support-twenty selectors.

The remaining multiplicity-three frontier begins at global case index `800` and contains `2,744` signatures and `8,232` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard7.cpp \
  -o /tmp/m3s7

/tmp/m3s7
/tmp/m3s7 700 0
/tmp/m3s7 799 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
