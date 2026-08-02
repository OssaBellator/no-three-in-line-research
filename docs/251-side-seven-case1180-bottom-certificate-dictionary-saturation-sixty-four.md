# Sixty-four-order bottom-certificate dictionary saturation

PX804--PX805 extend the case-`1180`, orientation-`0` shared collinear-triple dictionary through the first thirty-two clean concatenated top orders. This chapter doubles that mechanically checked prefix.

## 1. Exact obligation set

### Theorem PX810 -- PROVED FINITE

For each of the first sixty-four clean concatenated top orders, the verifier enumerates all `5,040` bottom permutations and all four selectors. It therefore checks

\[
64\cdot5{,}040\cdot4=\boxed{1{,}290{,}240}
\]

selector-permutation obligations.

For every obligation it deterministically records the lexicographically first collinear edge triple and rechecks the induced integer determinant.

The dictionary has size `363` after 32 top orders and size `404` after 64. Thus the second block of 32 top orders introduces only 41 new triples. The dictionary remains at size `395` for top orders `52` through `60`, then grows to `400`, `401`, and `404` on orders `61`, `62`, and `63`; order `64` adds no new triple.

The ordered obligation transcript has deterministic digest

`4157547873615595023` (`0x39b293c36f89c60f`).

## 2. Saturation and proof size

### Corollary PX811 -- PROVED REDUCTION

Only `404` distinct collinear triples cover all `1,290,240` obligations. The projected shared-dictionary proof payload is

\[
48+64\cdot14+404\cdot3+1{,}290{,}240
=\boxed{1{,}292{,}396}\text{ bytes}.
\]

Sixty-four independent raw certificates at `60,536` bytes each would require `3,874,304` bytes. The shared dictionary removes `2,581,908` bytes, approximately `66.6%`, while preserving one explicit checked collinear triple for every selector-permutation obligation.

This remains a fixed-signature, fixed-orientation, finite top-order prefix. It is a proof-object compression result, not yet a complete signature certificate.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_case1180_orientation0_dictionary_saturation64.cpp \
  -o /tmp/case1180-dict64

/tmp/case1180-dict64
```

The verifier regenerates the exact selector layer, locates multiplicity-four case `1180`, regenerates the first sixty-four clean top orders, checks all `1,290,240` obligations, and asserts every cumulative dictionary size, the final projected byte count, and the transcript digest.
