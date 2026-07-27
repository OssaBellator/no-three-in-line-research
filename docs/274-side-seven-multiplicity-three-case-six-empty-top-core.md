# Empty top-assumption core for multiplicity-three case six

PX874--PX875 establish an empty top-assumption core for global multiplicity-three case `5`. This chapter repeats the exact deletion experiment on the next lexicographic signature.

## 1. Seventh consecutive empty core

### Theorem PX882 -- PROVED FINITE

For global multiplicity-three case `6`, orientation `0`, begin with the first clean concatenated top assignment

`(0,1,6,3,2,4,5,2,0,3,5,6,4,1)`.

Delete its fourteen assignment literals in column order. After every deletion, regenerate every clean concatenated top assignment extending the retained literals and jointly run the exact three-selector bottom CSP. No extension admits a no-three embedding.

The terminal empty-assumption check contains:

- `51,276` clean top orders;
- `152,166` top-search nodes;
- `83,589` shared bottom-CSP nodes.

Thus the signature alone refutes every clean concatenated top order in orientation `0`.

## 2. Signature-level master nogood recurrence

### Corollary PX883 -- PROVED REDUCTION

Multiplicity-three cases `0` through `6` all have empty orientation-zero top cores. Each bare signature therefore supplies one master nogood covering its full clean concatenated top-order family.

This remains an exact seven-case recurrence, not yet a theorem for every multiplicity-three signature.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case6_orientation0_empty_top_core.cpp \
  -o /tmp/m3-case6-empty-core

/tmp/m3-case6-empty-core
```

The verifier regenerates the exact radius layer, locates case `6`, checks the first clean top assignment, replays all fourteen deletion stages, and asserts every clean-top and shared-bottom count.
