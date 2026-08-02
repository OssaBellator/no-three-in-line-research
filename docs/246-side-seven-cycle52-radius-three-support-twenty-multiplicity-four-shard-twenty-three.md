# Exact multiplicity-four shard twenty-three

PX788--PX791 close global multiplicity-four cases `2180` through `2279`. This chapter closes global cases `2280` through `2379`.

## 1. Exact shard census

### Theorem PX792 -- PROVED FINITE

Shard twenty-three contains one hundred multiplicity-four signatures and 400 selectors. Every selector in this interval is infeasible in every radix orientation.

## 2. Exact clean-top census

### Theorem PX793 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,389,029 | 52,264,513 |
| Interleaved | 5,338,754 | 46,557,415 |
| **Total** | **10,727,783** | **98,821,928** |

The complete ordered transcript has deterministic digest

`12832317832074138104` (`0xb2158d1469b091f8`).

## 3. Exact shared bottom CSP

### Theorem PX794 -- PROVED FINITE

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 8,480,369 |
| 1 | 8,664,290 |
| 2 | 8,722,010 |
| 3 | 7,900,957 |
| **Total** | **33,767,626** |

All 400 selectors terminate with an empty active mask. Seven duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX795 -- PROVED CLASSIFICATION

After shard twenty-three, the cache contains:

- `26,920` certified-infeasible selectors;
- `1` constructively witnessed selector;
- `1,484,086,718` cumulative rejection-CSP nodes;
- `44,939` unclassified active selectors.

Only twelve multiplicity-four signatures remain: global cases `2380` through `2391`, containing 48 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard23.cpp \
  -o /tmp/m4s23

/tmp/m4s23
/tmp/m4s23 2280 0
/tmp/m4s23 2379 3
```
