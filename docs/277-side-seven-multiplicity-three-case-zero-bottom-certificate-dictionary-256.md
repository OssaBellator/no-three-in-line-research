# Multiplicity-three case zero: 256-order bottom-certificate dictionary

This chapter continues the exact shared-triple proof-object experiment for multiplicity-three case `0`, orientation `0`.

## Theorem PX890 — PROVED FINITE

For the first `256` clean concatenated top orders, every bottom permutation of each of the three selectors has a concrete collinear triple. The verifier checks

\[
256\cdot 7!\cdot 3=\boxed{3{,}870{,}720}
\]

selector-permutation obligations using exact integer determinants.

Across the complete ordered prefix, only

\[
\boxed{601}
\]

distinct triples occur. The projected shared proof payload is

\[
\boxed{3{,}876{,}155\text{ bytes}},
\]

compared with

\[
\boxed{11{,}615{,}792\text{ bytes}}
\]

for direct three-byte triples attached independently to every obligation. This removes approximately `66.63%` of the direct payload.

The exact ordered proof transcript has digest

`15926051015442839590`.

The dictionary has already reached size `601` by top order `233` and remains at `601` through top order `256`, giving a 23-order terminal plateau in this prefix.

## Corollary PX891 — PROVED REDUCTION

Doubling the multiplicity-three prefix from `128` to `256` top orders doubles the obligation count from `1,935,360` to `3,870,720`, while the dictionary grows only from `521` to `601`. The additional 128 top orders therefore introduce just 80 new triples.

This is a compression result for a finite certificate family, not a proof that the dictionary has globally saturated over all clean top orders.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case0_orientation0_dictionary_saturation256.cpp \
  -o /tmp/m3-case0-dict256

/tmp/m3-case0-dict256
```

The verifier regenerates the exact layer, locates multiplicity-three case `0`, checks every concrete collinear triple, asserts all 256 cumulative dictionary sizes, and verifies the final payload counts and digest.
