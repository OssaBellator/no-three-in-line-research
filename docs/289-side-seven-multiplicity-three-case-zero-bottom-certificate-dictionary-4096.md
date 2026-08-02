# Multiplicity-three case zero: 4,096-order bottom-certificate dictionary

This chapter continues the exact shared-triple proof-object experiment for multiplicity-three case `0`, orientation `0`.

## Theorem PX922 — PROVED FINITE

For the first `4,096` clean concatenated top orders, every bottom permutation of each of the three selectors has a concrete collinear triple. The verifier checks

\[
4096\cdot 7!\cdot 3=\boxed{61{,}931{,}520}
\]

selector-permutation obligations using exact integer determinants.

Across the complete ordered prefix, only

\[
\boxed{1{,}258}
\]

distinct triples occur. The projected shared proof payload is

\[
\boxed{61{,}992{,}686\text{ bytes}},
\]

compared with

\[
\boxed{185{,}851{,}952\text{ bytes}}
\]

for direct three-byte triples attached independently to every obligation. This removes approximately `66.64%` of the direct payload.

The exact ordered proof transcript has digest

`13925271990529032304`.

The cumulative dictionary sizes at top-order counts `128`, `256`, `384`, `512`, `768`, `1,024`, `1,280`, `1,536`, `1,792`, `2,048`, `2,560`, `3,072`, `3,584`, and `4,096` are

`521, 601, 722, 781, 950, 1,028, 1,074, 1,148, 1,171, 1,202, 1,211, 1,223, 1,233, 1,258`.

The dictionary reaches its final size at top order `4,074` and remains unchanged through top order `4,096`, a terminal plateau of 22 additional orders.

## Corollary PX923 — PROVED REDUCTION

Doubling the prefix from `2,048` to `4,096` top orders doubles the obligation count from `30,965,760` to `61,931,520`, while the dictionary grows only from `1,202` to `1,258`. The additional 2,048 top orders introduce 56 new triples.

This is a finite certificate-compression result and does not establish global dictionary saturation over all clean top orders.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case0_orientation0_dictionary_saturation4096.cpp \
  -o /tmp/m3-case0-dict4096

/tmp/m3-case0-dict4096
```

The verifier regenerates the exact layer, locates multiplicity-three case `0`, validates every concrete triple, checks cumulative milestone sizes, and asserts the final obligation, payload, and digest values.
