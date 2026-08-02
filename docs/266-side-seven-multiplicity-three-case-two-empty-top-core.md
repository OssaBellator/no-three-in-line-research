# Multiplicity-three case-two empty top-assumption core

PX850--PX851 establish an empty top-assumption core for multiplicity-three case `1`. This chapter repeats the exact deletion experiment for case `2`.

## 1. Literal-deletion experiment

### Theorem PX860 -- PROVED FINITE

For multiplicity-three global case `2`, orientation `0`, begin with the first clean concatenated top order

`(0,1,6,3,2,4,5,2,0,3,5,6,1,4)`.

Delete its fourteen top literals in column order. At every intermediate stage, enumerate every clean concatenated top order extending the retained literals and refute the full three-selector group with the exact shared bottom CSP.

The exact sequence is:

| Literals retained | Clean top orders | Top-search nodes | Bottom-CSP nodes |
|---:|---:|---:|---:|
| 13 | 1 | 2 | 1 |
| 12 | 1 | 3 | 1 |
| 11 | 1 | 4 | 1 |
| 10 | 1 | 7 | 1 |
| 9 | 3 | 19 | 5 |
| 8 | 8 | 193 | 13 |
| 7 | 50 | 666 | 62 |
| 6 | 50 | 667 | 62 |
| 5 | 62 | 787 | 75 |
| 4 | 124 | 1,575 | 152 |
| 3 | 276 | 3,939 | 344 |
| 2 | 880 | 11,641 | 1,106 |
| 1 | 5,404 | 71,157 | 8,418 |
| 0 | 51,276 | 152,166 | 83,589 |

No retained-literal level admits a survivor.

## 2. Signature-level master nogood

### Corollary PX861 -- PROVED REDUCTION

After all fourteen literals are deleted, the bare case-two signature still refutes every one of its `51,276` clean concatenated top orders after exactly `83,589` shared bottom-CSP nodes.

Therefore the first three multiplicity-three signatures all have empty top-assumption cores in orientation zero. Each signature itself is a mechanically checked master nogood for every clean concatenated top order it supports.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case2_orientation0_empty_top_core.cpp \
  -o /tmp/m3-case2-empty-core

/tmp/m3-case2-empty-core
```

The verifier regenerates the full radius-three support-twenty layer, locates case `2` lexicographically, checks the selected clean top order, reproduces all fourteen deletion stages, and asserts every exact order, top-node, and bottom-node count.
