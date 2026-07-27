# Exact multiplicity-four shard eighteen

PX766--PX769 close global multiplicity-four cases `1680` through `1779`. This chapter closes global cases `1780` through `1879`.

## 1. Exact shard census

### Theorem PX770 -- PROVED FINITE

Shard eighteen contains one hundred multiplicity-four signatures and 400 selectors. Every selector in this interval is infeasible in every radix orientation.

## 2. Exact clean-top census

### Theorem PX771 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 4,860,380 | 37,929,958 |
| Interleaved | 3,354,182 | 26,845,024 |
| **Total** | **8,214,562** | **64,774,982** |

The complete ordered transcript has deterministic digest

`14735579502432110373` (`0xcc7f4b7c29fe4725`).

## 3. Exact shared bottom CSP

### Theorem PX772 -- PROVED FINITE

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 7,604,985 |
| 1 | 5,287,787 |
| 2 | 7,677,471 |
| 3 | 5,406,203 |
| **Total** | **25,976,446** |

All 400 selectors terminate with an empty active mask. Three duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX773 -- PROVED CLASSIFICATION

After shard eighteen, the cache contains:

- `24,920` certified-infeasible selectors;
- `1` constructively witnessed selector;
- `1,307,062,192` cumulative rejection-CSP nodes;
- `46,939` unclassified active selectors.

The remaining multiplicity-four frontier begins at global case index `1880` and contains 512 signatures and 2,048 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard18.cpp \
  -o /tmp/m4s18

/tmp/m4s18
/tmp/m4s18 1780 0
/tmp/m4s18 1879 3
```
