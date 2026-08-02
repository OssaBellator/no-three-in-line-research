# Empty top-assumption core for multiplicity-three case four

PX866--PX867 establish an empty top-assumption core for global multiplicity-three case `3`. This chapter repeats the exact deletion experiment on the next lexicographic signature.

## 1. Fifth consecutive empty core

### Theorem PX872 -- PROVED FINITE

For global multiplicity-three case `4`, orientation `0`, begin with the first clean concatenated top assignment

`(0,1,6,4,5,2,3,2,1,4,3,6,5,0)`.

Delete its fourteen assignment literals in column order. After every deletion, regenerate every clean concatenated top assignment extending the retained literals and jointly run the exact three-selector bottom CSP. No extension admits a no-three embedding.

The terminal empty-assumption check contains:

- `67,044` clean top orders;
- `196,131` top-search nodes;
- `112,185` shared bottom-CSP nodes.

Thus the signature alone refutes every clean concatenated top order in orientation `0`.

## 2. Signature-level master nogood recurrence

### Corollary PX873 -- PROVED REDUCTION

Multiplicity-three cases `0` through `4` all have empty orientation-zero top cores. Their terminal empty-assumption families contain

`75,600`, `62,416`, `51,276`, `34,516`, and `67,044`

clean top orders. Each bare signature therefore supplies one master nogood covering its full clean concatenated top-order family.

This remains an exact five-case recurrence, not yet a theorem for every multiplicity-three signature.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case4_orientation0_empty_top_core.cpp \
  -o /tmp/m3-case4-empty-core

/tmp/m3-case4-empty-core
```

The verifier regenerates the exact radius layer, locates case `4`, checks the first clean top assignment, replays all fourteen deletion stages, and asserts every clean-top and shared-bottom count.
