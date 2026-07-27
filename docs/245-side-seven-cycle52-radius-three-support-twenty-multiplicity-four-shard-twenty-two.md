# Exact multiplicity-four shard twenty-two

PX784--PX787 close global multiplicity-four cases `2080` through `2179`. This chapter closes global cases `2180` through `2279`.

## 1. Exact shard census

### Theorem PX788 -- PROVED FINITE

Shard twenty-two contains one hundred multiplicity-four signatures and 400 selectors. Every selector in this interval is infeasible in every radix orientation.

## 2. Exact clean-top census

### Theorem PX789 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,833,937 | 42,210,376 |
| Interleaved | 4,070,638 | 33,267,205 |
| **Total** | **8,904,575** | **75,477,581** |

The complete ordered transcript has deterministic digest

`6419771693688218342` (`0x59179c578d64e2e6`).

## 3. Exact shared bottom CSP

### Theorem PX790 -- PROVED FINITE

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 9,150,466 |
| 1 | 7,638,873 |
| 2 | 8,515,848 |
| 3 | 7,117,297 |
| **Total** | **32,422,484** |

All 400 selectors terminate with an empty active mask. Eight duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX791 -- PROVED CLASSIFICATION

After shard twenty-two, the cache contains:

- `26,520` certified-infeasible selectors;
- `1` constructively witnessed selector;
- `1,450,319,092` cumulative rejection-CSP nodes;
- `45,339` unclassified active selectors.

The remaining multiplicity-four frontier begins at global case index `2280` and contains 112 signatures and 448 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard22.cpp \
  -o /tmp/m4s22

/tmp/m4s22
/tmp/m4s22 2180 0
/tmp/m4s22 2279 3
```
