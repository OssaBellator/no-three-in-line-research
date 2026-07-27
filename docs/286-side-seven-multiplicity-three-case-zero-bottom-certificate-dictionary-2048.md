# Multiplicity-three case zero: 2,048-order bottom-certificate dictionary

This chapter continues the exact shared-triple proof-object experiment for multiplicity-three case `0`, orientation `0`.

## Theorem PX914 — PROVED FINITE

For the first `2,048` clean concatenated top orders, every bottom permutation of each of the three selectors has a concrete collinear triple. The verifier checks

\[
2048\cdot 7!\cdot 3=\boxed{30{,}965{,}760}
\]

selector-permutation obligations using exact integer determinants.

Across the complete ordered prefix, only

\[
\boxed{1{,}202}
\]

distinct triples occur. The projected shared proof payload is

\[
\boxed{30{,}998{,}086\text{ bytes}},
\]

compared with

\[
\boxed{92{,}926{,}000\text{ bytes}}
\]

for direct three-byte triples attached independently to every obligation. This removes approximately `66.64%` of the direct payload.

The exact ordered proof transcript has digest

`8200777914864976615`.

The cumulative dictionary sizes at top-order counts `128`, `256`, `384`, `512`, `768`, `1,024`, `1,280`, `1,536`, `1,792`, and `2,048` are

`521, 601, 722, 781, 950, 1,028, 1,074, 1,148, 1,171, 1,202`.

The dictionary reaches its final size at top order `2,033` and remains unchanged through top order `2,048`, a terminal plateau of 15 additional orders.

## Corollary PX915 — PROVED REDUCTION

Doubling the prefix from `1,024` to `2,048` top orders doubles the obligation count from `15,482,880` to `30,965,760`, while the dictionary grows only from `1,028` to `1,202`. The additional 1,024 top orders introduce 174 new triples.

This is a finite certificate-compression result and does not establish global dictionary saturation over all clean top orders.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case0_orientation0_dictionary_saturation2048.cpp \
  -o /tmp/m3-case0-dict2048

/tmp/m3-case0-dict2048
```

The verifier regenerates the exact layer, locates multiplicity-three case `0`, validates every concrete triple, checks cumulative milestone sizes, and asserts the final obligation, payload, and digest values.
