# Exact `(5,2)` radius-three support-twenty multiplicity-four shard ten

PX727--PX730 close global multiplicity-four case indices `880` through `979`. This chapter closes global cases `980` through `1079`.

This is a finite obstruction result, not an infinite product theorem.

## 1. Exact shard census

### Theorem PX731 -- PROVED FINITE

Shard ten contains one hundred top signatures of multiplicity four, hence

\[
100\cdot4=\boxed{400}
\]

selectors.

The verifier regenerates the exact radius layers, asserts all 2,392 multiplicity-four signatures, and selects the lexicographic interval `980` through `1079`.

## 2. Exact clean-top census

### Theorem PX732 -- PROVED FINITE

The exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 6,721,748 | 36,472,101 |
| Interleaved | 3,646,959 | 22,274,418 |
| **Total** | **10,368,707** | **58,746,519** |

The complete ordered transcript has deterministic digest

`5499058393039379395` (`0x4c509479243e1bc3`).

## 3. Exact shared bottom CSP

### Theorem PX733 -- PROVED FINITE

Every one of the 400 selectors fails in every radix orientation. The exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 12,773,829 |
| 1 | 6,614,905 |
| 2 | 12,378,517 |
| 3 | 6,211,748 |
| **Total** | **37,978,999** |

Every exact tree terminates with the active-selector mask empty. Three duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX734 -- PROVED REDUCTION

Adding shard ten gives

\[
21{,}321+400=\boxed{21{,}721}
\]

certified-infeasible selectors and

\[
1{,}038{,}422{,}987+37{,}978{,}999
=\boxed{1{,}076{,}401{,}986}
\]

shared bottom-CSP nodes. Therefore

\[
71{,}860-21{,}721=\boxed{50{,}139}
\]

support-twenty selectors remain active.

The remaining multiplicity-four frontier begins at global case index `1080` and contains 1,312 signatures and 5,248 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard10.cpp \
  -o /tmp/m4s10

/tmp/m4s10
/tmp/m4s10 980 0
/tmp/m4s10 1079 3
```

The full run asserts the tier histogram, shard interval, every coordinate search, aggregate counts, absence of every embedding, and the ordered transcript digest.
