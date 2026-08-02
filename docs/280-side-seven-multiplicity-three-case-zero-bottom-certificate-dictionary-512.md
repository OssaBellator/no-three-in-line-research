# Multiplicity-three case zero: 512-order bottom-certificate dictionary

This chapter continues the exact shared-triple proof-object experiment for multiplicity-three case `0`, orientation `0`.

## Theorem PX898 — PROVED FINITE

For the first `512` clean concatenated top orders, every bottom permutation of each of the three selectors has a concrete collinear triple. The verifier checks

\[
512\cdot 7!\cdot 3=\boxed{7{,}741{,}440}
\]

selector-permutation obligations using exact integer determinants.

Across the complete ordered prefix, only

\[
\boxed{781}
\]

distinct triples occur. The projected shared proof payload is

\[
\boxed{7{,}750{,}999\text{ bytes}},
\]

compared with

\[
\boxed{23{,}231{,}536\text{ bytes}}
\]

for direct three-byte triples attached independently to every obligation. This removes approximately `66.64%` of the direct payload.

The exact ordered proof transcript has digest

`11796239806324865731`.

The cumulative dictionary sizes at top-order counts `128`, `256`, `384`, and `512` are respectively

`521, 601, 722, 781`.

The dictionary reaches size `781` at top order `490` and remains unchanged through top order `512`, a terminal plateau of 22 additional orders.

## Corollary PX899 — PROVED REDUCTION

Doubling the prefix from `256` to `512` top orders doubles the obligation count from `3,870,720` to `7,741,440`, while the dictionary grows only from `601` to `781`. The additional 256 top orders introduce 180 new triples.

This is a finite certificate-compression result and does not establish global dictionary saturation over all clean top orders.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case0_orientation0_dictionary_saturation512.cpp \
  -o /tmp/m3-case0-dict512

/tmp/m3-case0-dict512
```

The verifier regenerates the exact layer, locates multiplicity-three case `0`, validates every concrete triple, checks the cumulative milestone sizes, and asserts the final obligation, payload, and digest values.
