# Multiplicity-three dictionary saturation through sixty-four top orders

PX816--PX817 establish the first multiplicity-three dictionary certificate for case `0`, orientation `0`, across thirty-two clean concatenated top orders. This chapter doubles that exact prefix to sixty-four orders.

## 1. Exact sixty-four-order saturation

### Theorem PX834 -- PROVED FINITE

For global multiplicity-three case `0` in orientation `0`, consider the first sixty-four clean concatenated top orders. For every top order, every one of the `7!=5,040` bottom permutations, and each of the three selectors, the verifier records the lexicographically first collinear edge triple.

The resulting proof workload contains

\[
64\cdot 5{,}040\cdot 3=\boxed{967{,}680}
\]

selector-permutation obligations. Their shared dictionary contains only

\[
\boxed{283}
\]

distinct edge triples. The ordered proof transcript has digest

`1254626597863958761` (`0x11691cf23eb96a29`).

The cumulative dictionary sizes at orders 33 through 64 are

`241, 241, 244, 247, 247, 256, 256, 258, 263, 263, 263, 266, 266, 266, 267, 267, 267, 267, 267, 267, 267, 267, 267, 267, 267, 267, 268, 268, 273, 280, 282, 283`.

Thus the second block of thirty-two top orders introduces only forty-two new triples beyond the 241-triple dictionary of PX816--PX817.

## 2. Proof-object compression

### Corollary PX835 -- PROVED REDUCTION

Using the same one-byte obligation references and three-byte dictionary entries as the thirty-two-order pilot, the projected shared proof payload is

\[
48+64\cdot14+283\cdot3+967{,}680
=\boxed{969{,}473}\text{ bytes}.
\]

Storing one raw three-edge triple per obligation would require

\[
48+64\cdot14+3\cdot967{,}680
=2{,}903{,}984\text{ bytes}.
\]

The shared dictionary therefore removes `1,934,511` bytes, about `66.6%` of the raw proof payload.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case0_orientation0_dictionary_saturation64.cpp \
  -o /tmp/m3-case0-dict64

/tmp/m3-case0-dict64
```

The verifier regenerates the exact radius-three layer, selects multiplicity-three case zero, re-enumerates all sixty-four clean top orders and all 967,680 obligations, checks each recorded collinearity geometrically, asserts every cumulative dictionary size, and checks the final digest.
