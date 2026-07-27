# Exact multiplicity-four shard seventeen

PX760--PX763 close global multiplicity-four cases `1580` through `1679`. This chapter closes global cases `1680` through `1779`.

## 1. Exact shard census

### Theorem PX766 -- PROVED FINITE

Shard seventeen contains one hundred multiplicity-four signatures and 400 selectors. Every selector in this interval is infeasible in every radix orientation.

## 2. Exact clean-top census

### Theorem PX767 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 6,042,211 | 33,357,244 |
| Interleaved | 3,879,075 | 21,558,956 |
| **Total** | **9,921,286** | **54,916,200** |

The complete ordered transcript has deterministic digest

`14864804958552868545` (`0xce4a655a4a0246c1`).

## 3. Exact shared bottom CSP

### Theorem PX768 -- PROVED FINITE

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 8,464,972 |
| 1 | 5,500,910 |
| 2 | 8,852,913 |
| 3 | 5,597,856 |
| **Total** | **28,416,651** |

All 400 selectors terminate with an empty active mask. No constructive witness occurs in the interval.

## 4. Revised cache boundary

### Corollary PX769 -- PROVED CLASSIFICATION

After shard seventeen, the cache contains:

- `24,520` certified-infeasible selectors;
- `1` constructively witnessed selector;
- `1,281,085,746` cumulative rejection-CSP nodes;
- `47,339` unclassified active selectors.

The remaining multiplicity-four frontier begins at global case index `1780` and contains 612 signatures and 2,448 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard17.cpp \
  -o /tmp/m4s17

/tmp/m4s17
/tmp/m4s17 1680 0
/tmp/m4s17 1779 3
```
