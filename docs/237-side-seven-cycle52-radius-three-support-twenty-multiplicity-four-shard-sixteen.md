# Exact multiplicity-four shard sixteen

PX756--PX759 close global multiplicity-four cases `1480` through `1579`. This chapter closes global cases `1580` through `1679`.

## 1. Exact shard census

### Theorem PX760 -- PROVED FINITE

Shard sixteen contains one hundred multiplicity-four signatures and 400 selectors. Every selector in this interval is infeasible in every radix orientation.

## 2. Exact clean-top census

### Theorem PX761 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 7,768,073 | 61,275,621 |
| Interleaved | 4,544,458 | 40,799,345 |
| **Total** | **12,312,531** | **102,074,966** |

The complete ordered transcript has deterministic digest

`4380135539162214536` (`0x3cc95e10dfd3f088`).

## 3. Exact shared bottom CSP

### Theorem PX762 -- PROVED FINITE

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 12,833,495 |
| 1 | 7,510,941 |
| 2 | 13,211,508 |
| 3 | 7,178,980 |
| **Total** | **40,734,924** |

All 400 selectors terminate with an empty active mask. Six duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX763 -- PROVED CLASSIFICATION

After shard sixteen, the cache contains:

- `24,120` certified-infeasible selectors;
- `1` constructively witnessed selector;
- `1,252,669,095` cumulative rejection-CSP nodes;
- `47,739` unclassified active selectors.

The remaining multiplicity-four frontier begins at global case index `1680` and contains 712 signatures and 2,848 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard16.cpp \
  -o /tmp/m4s16

/tmp/m4s16
/tmp/m4s16 1580 0
/tmp/m4s16 1679 3
```
