# Empty top-assumption core for multiplicity-three case five

PX872--PX873 establish an empty top-assumption core for global multiplicity-three case `4`. This chapter repeats the exact deletion experiment on the next lexicographic signature.

## 1. Sixth consecutive empty core

### Theorem PX874 -- PROVED FINITE

For global multiplicity-three case `5`, orientation `0`, begin with the first clean concatenated top assignment

`(0,1,6,4,5,2,3,2,0,4,3,6,1,5)`.

Delete its fourteen assignment literals in column order. After every deletion, regenerate every clean concatenated top assignment extending the retained literals and jointly run the exact three-selector bottom CSP. No extension admits a no-three embedding.

The terminal empty-assumption check contains:

- `51,932` clean top orders;
- `178,936` top-search nodes;
- `82,849` shared bottom-CSP nodes.

Thus the signature alone refutes every clean concatenated top order in orientation `0`.

## 2. Signature-level master nogood recurrence

### Corollary PX875 -- PROVED REDUCTION

Multiplicity-three cases `0` through `5` all have empty orientation-zero top cores. Each bare signature therefore supplies one master nogood covering its full clean concatenated top-order family.

The six exact terminal family sizes are

`75,600`, `62,416`, `51,276`, `34,516`, `67,044`, and `51,932`.

This remains an exact six-case recurrence, not yet a theorem for every multiplicity-three signature.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case5_orientation0_empty_top_core.cpp \
  -o /tmp/m3-case5-empty-core

/tmp/m3-case5-empty-core
```

The verifier regenerates the exact radius layer, locates case `5`, checks the first clean top assignment, replays all fourteen deletion stages, and asserts every clean-top and shared-bottom count.
