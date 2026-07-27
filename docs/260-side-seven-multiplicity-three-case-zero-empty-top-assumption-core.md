# Multiplicity-three case-zero empty top-assumption core

PX774--PX775 establish an empty top-assumption core for multiplicity-four case `1180`, orientation `0`. This chapter proves that the same phenomenon recurs at the new multiplicity-three frontier.

## 1. Exact literal-deletion sequence

### Theorem PX840 -- PROVED FINITE

For global multiplicity-three case `0`, orientation `0`, begin with the first clean concatenated top assignment

`(0,1,6,4,5,2,3,2,0,4,3,6,1,5)`.

Delete its fourteen column literals in column order. After each deletion, the verifier enumerates every clean top assignment extending the retained literals and checks the three-selector bottom CSP exactly.

| Removed through column | Retained literals | Clean top orders | Top-search nodes | Bottom-CSP nodes |
|---:|---:|---:|---:|---:|
| 0 | 13 | 1 | 2 | 1 |
| 1 | 12 | 2 | 5 | 3 |
| 2 | 11 | 4 | 13 | 7 |
| 3 | 10 | 7 | 30 | 10 |
| 4 | 9 | 7 | 48 | 10 |
| 5 | 8 | 12 | 163 | 15 |
| 6 | 7 | 48 | 550 | 59 |
| 7 | 6 | 48 | 551 | 59 |
| 8 | 5 | 62 | 901 | 76 |
| 9 | 4 | 254 | 3,070 | 338 |
| 10 | 3 | 684 | 8,134 | 900 |
| 11 | 2 | 2,012 | 28,175 | 2,613 |
| 12 | 1 | 8,856 | 135,315 | 12,077 |
| 13 | 0 | 75,600 | 220,298 | 110,263 |

Every clean extension is infeasible at every stage. After the final deletion the retained assumption mask is empty.

## 2. Signature-level master nogood

### Corollary PX841 -- PROVED REDUCTION

The multiplicity-three case-zero signature alone refutes all `75,600` clean concatenated top orders in orientation `0`. None of the fourteen values from the original top assignment is necessary.

Thus the exact top-assumption core is empty, and the whole signature supplies a signature-level master nogood for this orientation. Together with PX774--PX775, this shows that empty cores occur in both multiplicities four and three rather than being isolated to one tier.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case0_orientation0_empty_top_core.cpp \
  -o /tmp/m3-case0-empty-core

/tmp/m3-case0-empty-core
```

The verifier regenerates the exact layer, locates multiplicity-three case zero, asserts the first clean top assignment, repeats all fourteen literal deletions, and checks every clean extension against the exact shared bottom CSP.
