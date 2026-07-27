# Exact multiplicity-four shard twenty

PX776--PX779 close global multiplicity-four cases `1880` through `1979`. This chapter closes global cases `1980` through `2079`.

## 1. Exact shard census

### Theorem PX780 -- PROVED FINITE

Shard twenty contains one hundred multiplicity-four signatures and 400 selectors. Every selector in this interval is infeasible in every radix orientation.

## 2. Exact clean-top census

### Theorem PX781 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,803,527 | 44,165,080 |
| Interleaved | 4,057,775 | 31,402,420 |
| **Total** | **9,861,302** | **75,567,500** |

The complete ordered transcript has deterministic digest

`5938082048004485873` (`0x52684e294e6e72f1`).

## 3. Exact shared bottom CSP

### Theorem PX782 -- PROVED FINITE

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 9,618,083 |
| 1 | 6,520,597 |
| 2 | 8,862,808 |
| 3 | 6,467,127 |
| **Total** | **31,468,615** |

All 400 selectors terminate with an empty active mask. Seven distinct overlapped cases produced eight agreeing duplicate rows before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX783 -- PROVED CLASSIFICATION

After shard twenty, the cache contains:

- `25,720` certified-infeasible selectors;
- `1` constructively witnessed selector;
- `1,376,863,397` cumulative rejection-CSP nodes;
- `46,139` unclassified active selectors.

The remaining multiplicity-four frontier begins at global case index `2080` and contains 312 signatures and 1,248 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard20.cpp \
  -o /tmp/m4s20

/tmp/m4s20
/tmp/m4s20 1980 0
/tmp/m4s20 2079 3
```
