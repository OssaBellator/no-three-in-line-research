# Exact `(5,2)` radius-three support-twenty multiplicity-two shards one through three

PX944--PX947 classify multiplicity-two cases `0` through `9`. This chapter closes the next thirty signatures, cases `10` through `39`, and records the four-shard cost model.

This is a finite obstruction result, not an infinite product theorem and not a proof of the no-three-in-line conjecture.

## 1. Exact shard census

### Theorem PX948 -- PROVED FINITE

Cases `10` through `39` contain thirty multiplicity-two signatures and therefore

\[
30\cdot2=\boxed{60}
\]

selectors. Every selector is infeasible in all four radix orientations.

| Shard | Global cases | Signatures | Selectors | Transcript digest |
|---:|---:|---:|---:|---:|
| 1 | `10`--`19` | 10 | 20 | `13243692266140994388` |
| 2 | `20`--`29` | 10 | 20 | `10542156272579548948` |
| 3 | `30`--`39` | 10 | 20 | `1833162045244562221` |
| **New total** | `10`--`39` | **30** | **60** | three independent digests |

## 2. Exact clean-top census

### Theorem PX949 -- PROVED FINITE

Across cases `10` through `39`, the exact clean-top totals are:

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 1,046,228 | 3,226,163 |
| Interleaved | 1,335,056 | 3,996,197 |
| **Total** | **2,381,284** | **7,222,360** |

The four-shard sample, including the pilot, contains `3,139,954` clean top orders and `9,384,236` top-search nodes.

## 3. Exact shared bottom CSP

### Theorem PX950 -- PROVED FINITE

For cases `10` through `39`, the exact bottom-CSP totals are:

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 1,460,829 |
| 1 | 2,247,458 |
| 2 | 1,930,174 |
| 3 | 1,851,296 |
| **Total** | **7,489,757** |

Combining the pilot gives the first forty multiplicity-two signatures:

| Orientation | Cases `0`--`39` bottom-CSP nodes |
|---:|---:|
| 0 | 1,743,193 |
| 1 | 3,174,299 |
| 2 | 2,334,227 |
| 3 | 2,494,775 |
| **Total** | **9,746,494** |

All eighty selectors terminate with the active mask empty.

## 4. Revised finite cache boundary

### Corollary PX951 -- PROVED REDUCTION

The first forty multiplicity-two signatures add eighty certified-infeasible selectors. The cache boundary is therefore

\[
37{,}600+80=\boxed{37{,}680}
\]

certified-infeasible selectors and

\[
2{,}766{,}455{,}244+9{,}746{,}494
=\boxed{2{,}776{,}201{,}738}
\]

shared rejection-CSP nodes.

Together with the one constructive multiplicity-four selector, exactly

\[
71{,}860-37{,}680-1=\boxed{34{,}179}
\]

selectors remain unclassified:

- `3,800` multiplicity-two signatures containing `7,600` selectors;
- all `26,579` multiplicity-one signatures and selectors.

## 5. Cost-model conclusion

The first four ten-signature shards vary materially in top-order load but remain compact enough for independent replay. The measured totals support the following scheduler:

1. retain fixed lexicographic ten-signature proof boundaries;
2. run each signature independently when the environment imposes sustained-process throttling;
3. combine the ten deterministic rows into one shard digest;
4. schedule concurrent shards by predicted clean-top order count rather than signature count alone.

The bottom search remains shallow per top assignment. The dominant cost is generating and testing clean top orders, especially in the interleaved orientation.

## 6. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard1.cpp \
  -o /tmp/m2s1

g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard2.cpp \
  -o /tmp/m2s2

g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard3.cpp \
  -o /tmp/m2s3

/tmp/m2s1
/tmp/m2s2
/tmp/m2s3
```

Each verifier regenerates the complete layer, asserts the multiplicity-two tier size `3,840`, checks its exact ten-signature interval, and verifies all aggregate counts and the ordered transcript digest.
