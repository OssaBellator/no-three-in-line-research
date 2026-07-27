# Exact multiplicity-four shard nineteen

PX770--PX773 close global multiplicity-four cases `1780` through `1879`. This chapter closes global cases `1880` through `1979`.

## 1. Exact shard census

### Theorem PX776 -- PROVED FINITE

Shard nineteen contains one hundred multiplicity-four signatures and 400 selectors. Every selector in this interval is infeasible in every radix orientation.

## 2. Exact clean-top census

### Theorem PX777 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 6,648,856 | 43,485,293 |
| Interleaved | 5,313,884 | 33,615,316 |
| **Total** | **11,962,740** | **77,100,609** |

The complete ordered transcript has deterministic digest

`14452785419276235217` (`0xc8929bc3c2e7b1d1`).

## 3. Exact shared bottom CSP

### Theorem PX778 -- PROVED FINITE

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 10,568,367 |
| 1 | 8,597,320 |
| 2 | 10,558,691 |
| 3 | 8,608,212 |
| **Total** | **38,332,590** |

All 400 selectors terminate with an empty active mask. Three duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX779 -- PROVED CLASSIFICATION

After shard nineteen, the cache contains:

- `25,320` certified-infeasible selectors;
- `1` constructively witnessed selector;
- `1,345,394,782` cumulative rejection-CSP nodes;
- `46,539` unclassified active selectors.

The remaining multiplicity-four frontier begins at global case index `1980` and contains 412 signatures and 1,648 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard19.cpp \
  -o /tmp/m4s19

/tmp/m4s19
/tmp/m4s19 1880 0
/tmp/m4s19 1979 3
```
