# Exact multiplicity-four shard fifteen

PX751--PX755 classify global multiplicity-four cases `1380` through `1479`, including the first constructive witness. This chapter closes global cases `1480` through `1579`.

## 1. Exact shard census

### Theorem PX756 -- PROVED FINITE

Shard fifteen contains one hundred multiplicity-four signatures and 400 selectors. Every selector in this interval is infeasible in every radix orientation.

## 2. Exact clean-top census

### Theorem PX757 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,504,876 | 48,887,465 |
| Interleaved | 4,051,886 | 36,656,613 |
| **Total** | **9,556,762** | **85,544,078** |

The complete ordered transcript has deterministic digest

`3651704852006478728` (`0x32ad7637206aa388`).

## 3. Exact shared bottom CSP

### Theorem PX758 -- PROVED FINITE

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 8,591,057 |
| 1 | 6,162,767 |
| 2 | 8,593,780 |
| 3 | 5,850,288 |
| **Total** | **29,197,892** |

All 400 selectors terminate with an empty active mask. Six duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX759 -- PROVED CLASSIFICATION

After shard fifteen, the cache contains:

- `23,720` certified-infeasible selectors;
- `1` constructively witnessed selector;
- `1,211,934,171` cumulative rejection-CSP nodes;
- `48,139` unclassified active selectors.

The remaining multiplicity-four frontier begins at global case index `1580` and contains 812 signatures and 3,248 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard15.cpp \
  -o /tmp/m4s15

/tmp/m4s15
/tmp/m4s15 1480 0
/tmp/m4s15 1579 3
```
