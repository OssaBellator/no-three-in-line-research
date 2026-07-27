# Multiplicity-three dictionary saturation through 128 top orders

PX834--PX835 cover the first 64 clean concatenated top orders of multiplicity-three case `0`, orientation `0`. This chapter doubles that exact prefix.

## 1. Shared triple dictionary

### Theorem PX876 -- PROVED FINITE

For each of the first `128` clean concatenated top orders, each of the `5,040` bottom permutations, and each of the three selectors in global multiplicity-three case `0`, choose the lexicographically first collinear edge triple.

The resulting

\[
128\cdot 5{,}040\cdot3=\boxed{1{,}935{,}360}
\]

selector-permutation obligations use only `521` distinct triples.

The cumulative dictionary has size `283` after 64 top orders and `521` after 128. Thus the second block of 64 orders introduces only `238` new triples while doubling the obligation count.

The exact ordered proof transcript has digest

`13354808297163209304`.

## 2. Projected certificate size

### Corollary PX877 -- PROVED REDUCTION

Using a 48-byte header, fourteen top-assignment bytes per order, three bytes per dictionary triple, and one dictionary index per obligation, the projected shared certificate payload is

\[
48+128\cdot14+521\cdot3+1{,}935{,}360
=\boxed{1{,}938{,}763}\text{ bytes}.
\]

Storing every triple directly would require

\[
48+128(14+3\cdot15{,}120)
=\boxed{5{,}807{,}920}\text{ bytes}.
\]

The shared dictionary therefore removes about `66.6%` of the direct triple payload while remaining independently checkable by exact integer determinants.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case0_orientation0_dictionary_saturation128.cpp \
  -o /tmp/m3-case0-dict128

/tmp/m3-case0-dict128
```

The verifier regenerates the exact radius layer, locates case `0`, enumerates the first 128 clean top orders and every bottom permutation, asserts all cumulative dictionary sizes, and checks the final obligation count, projected byte count, and transcript digest.
