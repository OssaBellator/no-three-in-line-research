# Empty top-assumption core for multiplicity-three case three

PX860--PX861 establish an empty top-assumption core for global multiplicity-three case `2`. This chapter repeats the exact deletion experiment on the next lexicographic signature.

## 1. Fourth consecutive empty core

### Theorem PX866 -- PROVED FINITE

For global multiplicity-three case `3`, orientation `0`, begin with the first clean concatenated top assignment

`(0,1,6,3,2,4,5,2,0,4,5,6,1,3)`.

Delete its fourteen assignment literals in column order. After every deletion, regenerate every clean concatenated top assignment extending the retained literals and jointly run the exact three-selector bottom CSP. No extension admits a no-three embedding.

The terminal empty-assumption check contains:

- `34,516` clean top orders;
- `123,241` top-search nodes;
- `52,323` shared bottom-CSP nodes.

Thus the top assignment contributes no necessary literal: the signature alone refutes every clean concatenated top order in orientation `0`.

## 2. Signature-level master nogood

### Corollary PX867 -- PROVED REDUCTION

Multiplicity-three cases `0`, `1`, `2`, and `3` all have empty top-assumption cores in orientation `0`. Their exact terminal checks respectively refute

`75,600`, `62,416`, `51,276`, and `34,516`

clean concatenated top orders. Each signature therefore yields a single signature-level master nogood covering its entire orientation-zero top-order family.

This is a mechanically checked recurrence across four consecutive lexicographic signatures, not yet a theorem for every multiplicity-three signature.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case3_orientation0_empty_top_core.cpp \
  -o /tmp/m3-case3-empty-core

/tmp/m3-case3-empty-core
```

The verifier regenerates the exact radius layer, locates case `3`, checks the first clean top assignment, replays all fourteen deletion stages, and asserts every clean-top and shared-bottom count.
