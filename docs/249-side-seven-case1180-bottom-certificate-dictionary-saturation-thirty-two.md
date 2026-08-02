# Thirty-two-order bottom-certificate dictionary saturation

PX764--PX765 measure the shared collinear-triple dictionary across the first eight clean concatenated top orders of multiplicity-four case `1180`, orientation `0`. This chapter extends the same mechanically checked experiment through the first thirty-two top orders.

## 1. Exact obligation set

### Theorem PX804 -- PROVED FINITE

For each of the first thirty-two clean concatenated top orders, the verifier enumerates all `5,040` bottom permutations and all four selectors. Thus it checks exactly

\[
32\cdot5{,}040\cdot4=\boxed{645{,}120}
\]

selector-permutation obligations.

For every obligation it deterministically records the lexicographically first collinear edge triple and independently rechecks that the three induced integer points are collinear.

The cumulative dictionary sizes after top orders `1` through `32` are

`66, 84, 107, 120, 122, 124, 142, 152, 234, 253, 277, 281, 303, 320, 324, 331, 336, 341, 344, 346, 352, 356, 357, 357, 358, 358, 361, 361, 361, 363, 363, 363`.

The ordered obligation transcript has deterministic digest

`6386682151196533169` (`0x58a27631fbf17ac1`).

## 2. Saturation and proof size

### Corollary PX805 -- PROVED REDUCTION

Only `363` distinct collinear triples cover all `645,120` obligations. The dictionary does not grow after the thirtieth top order in this batch.

Using the established shared-dictionary format, the projected proof payload is

\[
48+32\cdot14+363\cdot3+645{,}120
=\boxed{646{,}705}\text{ bytes}.
\]

Thirty-two independent raw certificates at `60,536` bytes each would require `1,937,152` bytes. The shared dictionary therefore removes `1,290,447` bytes, approximately `66.6%`, while preserving one explicit checked collinear triple for every selector-permutation obligation.

This is a proof-object compression result for a fixed signature, orientation, and top-order prefix. It is not yet a complete certificate for every clean top order of the signature.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_case1180_orientation0_dictionary_saturation32.cpp \
  -o /tmp/case1180-dict32

/tmp/case1180-dict32
```

The verifier regenerates the exact selector layer, locates multiplicity-four case `1180`, regenerates the first thirty-two clean top orders, checks all `645,120` obligations, and asserts every cumulative dictionary size, the final projected byte count, and the transcript digest.
