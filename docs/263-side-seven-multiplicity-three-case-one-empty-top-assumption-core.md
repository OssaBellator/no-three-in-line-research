# Multiplicity-three case-one empty top-assumption core

PX840--PX841 prove an empty top-assumption core for multiplicity-three case `0`, orientation `0`. This chapter repeats the exact deletion experiment on the next lexicographic multiplicity-three signature.

## 1. Exact literal-deletion sequence

### Theorem PX850 -- PROVED FINITE

For global multiplicity-three case `1`, orientation `0`, begin with the first clean concatenated top assignment

`(0,2,1,6,5,3,4,2,0,4,5,6,1,3)`.

Delete its fourteen column literals in column order. After each deletion, the verifier enumerates every clean top assignment extending the retained literals and checks the three-selector bottom CSP exactly.

| Removed through column | Retained literals | Clean top orders | Top-search nodes | Bottom-CSP nodes |
|---:|---:|---:|---:|---:|
| 0 | 13 | 1 | 2 | 1 |
| 1 | 12 | 1 | 3 | 1 |
| 2 | 11 | 1 | 4 | 1 |
| 3 | 10 | 2 | 9 | 3 |
| 4 | 9 | 10 | 62 | 13 |
| 5 | 8 | 14 | 170 | 18 |
| 6 | 7 | 50 | 812 | 75 |
| 7 | 6 | 50 | 813 | 75 |
| 8 | 5 | 76 | 1,044 | 101 |
| 9 | 4 | 296 | 3,176 | 389 |
| 10 | 3 | 596 | 6,547 | 764 |
| 11 | 2 | 2,176 | 24,027 | 3,022 |
| 12 | 1 | 7,800 | 78,219 | 12,202 |
| 13 | 0 | 62,416 | 211,067 | 96,353 |

Every clean extension is infeasible at every stage. After the final deletion the retained assumption mask is empty.

## 2. Recurrent signature-level master nogood

### Corollary PX851 -- PROVED REDUCTION

The multiplicity-three case-one signature alone refutes all `62,416` clean concatenated top orders in orientation `0`. None of the fourteen values from the original top assignment is necessary.

Cases zero and one therefore both have empty top-assumption cores. The signature-level master-nogood phenomenon is recurrent across consecutive multiplicity-three signatures, not merely inherited from the earlier multiplicity-four example.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case1_orientation0_empty_top_core.cpp \
  -o /tmp/m3-case1-empty-core

/tmp/m3-case1-empty-core
```

The verifier regenerates the exact layer, locates multiplicity-three case one, asserts the first clean top assignment, repeats all fourteen literal deletions, and checks every clean extension against the exact shared bottom CSP.
