# Exact multiplicity-four shard twenty-one

PX780--PX783 close global multiplicity-four cases `1980` through `2079`. This chapter closes global cases `2080` through `2179`.

## 1. Exact shard census

### Theorem PX784 -- PROVED FINITE

Shard twenty-one contains one hundred multiplicity-four signatures and 400 selectors. Every selector in this interval is infeasible in every radix orientation.

## 2. Exact clean-top census

### Theorem PX785 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 5,334,880 | 40,890,192 |
| Interleaved | 6,322,753 | 38,384,873 |
| **Total** | **11,657,633** | **79,275,065** |

The complete ordered transcript has deterministic digest

`16866968297745794325` (`0xea13824d40e9c515`).

## 3. Exact shared bottom CSP

### Theorem PX786 -- PROVED FINITE

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 9,657,567 |
| 1 | 11,801,429 |
| 2 | 8,907,044 |
| 3 | 10,667,171 |
| **Total** | **41,033,211** |

All 400 selectors terminate with an empty active mask. Six duplicated recovery rows agreed exactly before the canonical transcript was digested.

## 4. Revised cache boundary

### Corollary PX787 -- PROVED CLASSIFICATION

After shard twenty-one, the cache contains:

- `26,120` certified-infeasible selectors;
- `1` constructively witnessed selector;
- `1,417,896,608` cumulative rejection-CSP nodes;
- `45,739` unclassified active selectors.

The remaining multiplicity-four frontier begins at global case index `2180` and contains 212 signatures and 848 selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard21.cpp \
  -o /tmp/m4s21

/tmp/m4s21
/tmp/m4s21 2080 0
/tmp/m4s21 2179 3
```
