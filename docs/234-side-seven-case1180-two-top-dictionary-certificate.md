# Shared-dictionary bottom certificate for two clean top orders

PX743--PX744 certify the first clean concatenated top order of multiplicity-four case `1180` by storing one explicit collinear triple for every selector-bottom-permutation obligation. This chapter extends the proof-object format to the first two clean top orders and shares repeated triples through a dictionary.

This is a certificate-format result for two fixed top orders, not a proof of the complete case or shard.

## 1. Two fixed-top obstructions

### Theorem PX749 -- PROVED FINITE

For global multiplicity-four case `1180`, orientation `0`, each of the first two clean concatenated top assignments fails for every one of the four selectors and every bottom-row permutation.

The certificate therefore checks

\[
2\cdot 7!\cdot4=\boxed{40{,}320}
\]

selector-permutation obligations. Each obligation supplies an explicit three-edge subset whose exact integer determinant is zero.

## 2. Shared dictionary certificate

### Theorem PX750 -- PROVED FINITE CERTIFICATE

`scripts/verify_product_side_seven_case1180_two_top_dictionary_certificate.cpp` stores the two top assignments, a shared dictionary of exactly `84` distinct collinear edge triples, and one one-byte dictionary reference for each of the `40,320` obligations.

The resulting deterministic proof object has:

- `10,080` top-order/bottom-permutation combinations;
- `40,320` selector obligations;
- `84` dictionary triples;
- size `40,648` bytes;
- digest `10705560690873782484`.

Two separate uncompressed certificates would occupy `121,072` bytes, so the shared dictionary reduces the proof payload by approximately two thirds.

The checker regenerates the exact selector layer and the first two clean top assignments but does not invoke `BottomGroupSolver`. It validates every dictionary reference, selector-edge membership, exact zero determinant, file length, and the anchored transcript digest.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_case1180_two_top_dictionary_certificate.cpp \
  -o /tmp/case1180-dict-cert

/tmp/case1180-dict-cert generate /tmp/case1180-two-top.cert
/tmp/case1180-dict-cert check /tmp/case1180-two-top.cert
wc -c /tmp/case1180-two-top.cert
```

The expected result includes:

```text
generated top_orders=2 dictionary=84 records=40320 bytes=40648 digest=10705560690873782484
top_orders=2 permutations=10080 obligations=40320 dictionary=84 digest=10705560690873782484 PASS
```

## 4. Next proof-producing step

The next format change is to stream an arbitrary number of clean top orders into one dictionary, measure dictionary saturation, and then replace complete top assignments by mechanically verified partial-assignment cores that can act as master nogoods.
