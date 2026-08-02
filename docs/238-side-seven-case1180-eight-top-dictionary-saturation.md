# Eight-top shared-triple dictionary saturation

PX749--PX750 show that the first two clean concatenated top orders of multiplicity-four case `1180`, orientation `0`, share a compact dictionary of explicit collinear triples. This chapter measures the same dictionary through the first eight clean top orders.

This is a proof-format scaling result, not a complete case or shard classification.

## 1. Dictionary growth

### Theorem PX764 -- PROVED FINITE

For each of the first eight clean concatenated top orders, enumerate all `5,040` bottom permutations and all four selectors. Store the lexicographically first explicit collinear edge triple for every selector-permutation obligation.

After each additional top order, the cumulative number of distinct triples is:

| Clean top orders | Obligations | Distinct triples |
|---:|---:|---:|
| 1 | 20,160 | 66 |
| 2 | 40,320 | 84 |
| 3 | 60,480 | 107 |
| 4 | 80,640 | 120 |
| 5 | 100,800 | 122 |
| 6 | 120,960 | 124 |
| 7 | 141,120 | 142 |
| 8 | 161,280 | 152 |

Thus the triple vocabulary grows much more slowly than the obligation count and nearly saturates over orders four through six.

## 2. Projected proof payload

### Theorem PX765 -- PROVED FINITE CERTIFICATE FORMAT

Using a 48-byte header, eight 14-byte top assignments, a three-byte representation of each of the 152 dictionary triples, and one one-byte reference for each of the 161,280 obligations gives

\[
48+8\cdot14+152\cdot3+161{,}280=\boxed{161{,}896}
\]

bytes.

Eight independent raw certificates would occupy

\[
8\cdot60{,}536=\boxed{484{,}288}
\]

bytes. The shared dictionary therefore removes 322,392 bytes while retaining one directly checkable geometric obstruction per obligation.

`scripts/verify_product_side_seven_case1180_eight_top_dictionary_saturation.cpp` regenerates the exact layer and first eight top orders, validates every zero determinant, asserts the complete growth sequence, and anchors the transcript with digest `3733902510478128199`.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_case1180_eight_top_dictionary_saturation.cpp \
  -o /tmp/case1180-saturation

/tmp/case1180-saturation
```

The next proof-producing target is partial-top core extraction: identify which top literals are actually needed to preserve a dictionary-backed bottom contradiction, mechanically recheck the reduced assumptions, and promote the result to a reusable master nogood.
