# Multiplicity-three case zero: 1,024-order bottom-certificate dictionary

This chapter continues the exact shared-triple proof-object experiment for multiplicity-three case `0`, orientation `0`.

## Theorem PX906 — PROVED FINITE

For the first `1,024` clean concatenated top orders, every bottom permutation of each of the three selectors has a concrete collinear triple. The verifier checks

\[
1024\cdot 7!\cdot 3=\boxed{15{,}482{,}880}
\]

selector-permutation obligations using exact integer determinants.

Across the complete ordered prefix, only

\[
\boxed{1{,}028}
\]

distinct triples occur. The projected shared proof payload is

\[
\boxed{15{,}500{,}348\text{ bytes}},
\]

compared with

\[
\boxed{46{,}463{,}024\text{ bytes}}
\]

for direct three-byte triples attached independently to every obligation. This removes approximately `66.64%` of the direct payload.

The exact ordered proof transcript has digest

`3070591403132654440`.

The cumulative dictionary sizes at top-order counts `128`, `256`, `384`, `512`, `768`, and `1,024` are

`521, 601, 722, 781, 950, 1,028`.

The dictionary reaches size `1,028` at top order `955` and remains unchanged through top order `1,024`, a terminal plateau of 69 additional orders.

## Corollary PX907 — PROVED REDUCTION

Doubling the prefix from `512` to `1,024` top orders doubles the obligation count from `7,741,440` to `15,482,880`, while the dictionary grows only from `781` to `1,028`. The additional 512 top orders introduce 247 new triples.

This is a finite certificate-compression result and does not establish global dictionary saturation over all clean top orders.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case0_orientation0_dictionary_saturation1024.cpp \
  -o /tmp/m3-case0-dict1024

/tmp/m3-case0-dict1024
```

The verifier regenerates the exact layer, locates multiplicity-three case `0`, validates every concrete triple, checks cumulative milestone sizes, and asserts the final obligation, payload, and digest values.
