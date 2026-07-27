# Empty top-assumption core for case 1180, orientation 0

PX743--PX765 develop explicit bottom proof objects for selected clean top orders of multiplicity-four case `1180`. This chapter moves to assumption-core extraction.

## 1. Greedy deletion trace

### Theorem PX774 -- PROVED FINITE CORE

Start from the lexicographically first clean concatenated top assignment

`(0,1,3,2,5,4,6,0,3,1,2,6,5,4)`

for global case `1180`, orientation `0`. Delete its fourteen top literals in column order. After each deletion, enumerate every clean top completion consistent with the retained literals and run the exact four-selector bottom CSP.

Every deletion preserves infeasibility. The exact completion counts are

`1, 1, 1, 3, 6, 15, 55, 55, 55, 230, 568, 1,228, 11,974, 70,376`,

and the corresponding bottom-CSP totals are

`1, 1, 1, 3, 6, 16, 80, 80, 80, 373, 982, 2,013, 15,826, 95,298`.

Thus the greedy deletion process reaches the empty top-assumption set.

## 2. Signature-level master nogood

### Theorem PX775 -- PROVED FINITE NOGOOD

With no retained top literals, the verifier enumerates all `70,376` clean concatenated top orders for the case-`1180` signature after `232,939` top-search nodes. Every order is bottom-infeasible for the four-selector group in orientation `0`, after exactly `95,298` shared bottom-CSP nodes.

Therefore the signature and orientation alone form a valid master nogood: no additional top-assignment literal is needed to refute any clean concatenated top order in this case.

This is stronger than a deletion-minimal partial assignment. The extracted assumption core is empty, so one learned signature-level clause covers the complete clean-top family for this orientation.

## 3. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_case1180_orientation0_empty_top_core.cpp \
  -o /tmp/case1180-empty-core

/tmp/case1180-empty-core
```

The verifier regenerates the exact selector layer, checks the fixed assignment is the first clean top order, replays all fourteen deletion tests, and asserts every completion count, top-node count, and bottom-node count.

## 4. Next core frontier

The next step is cross-signature generalization: identify geometric or incidence features shared by several signatures whose orientation-level top cores are empty or small, then mechanically check whether one learned nogood can cover multiple signature classes rather than only every top order inside one class.
