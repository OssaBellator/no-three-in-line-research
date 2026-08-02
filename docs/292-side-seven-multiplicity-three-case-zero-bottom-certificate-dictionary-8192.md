# Multiplicity-three case zero: 8,192-order bottom-certificate dictionary

This chapter continues the exact shared-triple proof-object experiment for multiplicity-three case `0`, orientation `0`.

## Theorem PX930 — PROVED FINITE

For the first `8,192` clean concatenated top orders, every bottom permutation of each of the three selectors has a concrete collinear triple. The verifier checks

\[
8192\cdot 7!\cdot 3=\boxed{123{,}863{,}040}
\]

selector-permutation obligations using exact integer determinants.

Across the complete ordered prefix, only

\[
\boxed{1{,}408}
\]

distinct triples occur. The projected shared proof payload is

\[
\boxed{123{,}982{,}000\text{ bytes}},
\]

compared with

\[
\boxed{371{,}703{,}856\text{ bytes}}
\]

for direct three-byte triples attached independently to every obligation. This removes approximately `66.64%` of the direct payload.

The exact ordered proof transcript has digest

`7207755927317802285`.

The cumulative dictionary sizes at top-order counts `128`, `256`, `384`, `512`, `768`, `1,024`, `1,280`, `1,536`, `1,792`, `2,048`, `2,560`, `3,072`, `3,584`, `4,096`, `5,120`, `6,144`, `7,168`, and `8,192` are

`521, 601, 722, 781, 950, 1,028, 1,074, 1,148, 1,171, 1,202, 1,211, 1,223, 1,233, 1,258, 1,278, 1,305, 1,395, 1,408`.

The dictionary reaches its final size at top order `8,058` and remains unchanged through top order `8,192`, a terminal plateau of 134 additional orders.

## Corollary PX931 — PROVED REDUCTION

Doubling the prefix from `4,096` to `8,192` top orders doubles the obligation count from `61,931,520` to `123,863,040`, while the dictionary grows only from `1,258` to `1,408`. The additional 4,096 top orders introduce 150 new triples.

This is a finite certificate-compression result and does not establish global dictionary saturation over all clean top orders.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case0_orientation0_dictionary_saturation8192.cpp \
  -o /tmp/m3-case0-dict8192

/tmp/m3-case0-dict8192
```

The verifier regenerates the exact layer, locates multiplicity-three case `0`, validates every concrete triple, checks cumulative milestone sizes, and asserts the final obligation, payload, and digest values.
