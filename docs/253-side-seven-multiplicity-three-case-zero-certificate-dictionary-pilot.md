# Multiplicity-three certificate dictionary pilot

PX810--PX811 extend explicit bottom-obstruction dictionary compression through sixty-four top orders of multiplicity-four case `1180`. This chapter tests the same native proof-object format on the new multiplicity-three frontier.

## 1. Exact obligation set

### Theorem PX816 -- PROVED FINITE

For multiplicity-three case `0`, orientation `0`, and each of the first thirty-two clean concatenated top orders, the verifier enumerates all `5,040` bottom permutations and all three selectors. It checks exactly

\[
32\cdot5{,}040\cdot3=\boxed{483{,}840}
\]

selector-permutation obligations.

For every obligation it records the lexicographically first collinear edge triple and independently rechecks the corresponding integer determinant.

The cumulative dictionary sizes after top orders `1` through `32` are

`59, 65, 76, 80, 91, 104, 124, 125, 130, 134, 135, 137, 165, 170, 178, 189, 190, 201, 204, 206, 207, 212, 212, 214, 217, 224, 225, 226, 233, 234, 238, 241`.

The ordered obligation transcript has deterministic digest

`14195751676262351726` (`0xc50170efef46036e`).

## 2. Transfer of dictionary compression

### Corollary PX817 -- PROVED REDUCTION

Only `241` distinct collinear triples cover all `483,840` obligations. The projected shared-dictionary proof payload is

\[
48+32\cdot14+241\cdot3+483{,}840
=\boxed{485{,}059}\text{ bytes}.
\]

The raw triple payload alone would require

\[
3\cdot483{,}840=1{,}451{,}520\text{ bytes}.
\]

Thus the shared dictionary removes `966,461` bytes, approximately `66.6%`, even before counting repeated per-order metadata in independent raw certificates.

This verifies that the certificate-compression mechanism transfers from multiplicity four to multiplicity three. It remains a finite prefix result for one signature and orientation, not a complete tier certificate.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case0_orientation0_dictionary_saturation32.cpp \
  -o /tmp/m3-case0-dict32

/tmp/m3-case0-dict32
```

The verifier regenerates the exact selector layer, locates multiplicity-three case `0`, regenerates the first thirty-two clean top orders, checks all `483,840` obligations, and asserts every cumulative dictionary size, the projected byte count, and the transcript digest.
