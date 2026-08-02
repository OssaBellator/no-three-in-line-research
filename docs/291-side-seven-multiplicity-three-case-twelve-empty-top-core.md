# Multiplicity-three case twelve: empty top-assumption core

This chapter records the thirteenth consecutive multiplicity-three signature-level master nogood in the side-seven radius-three support-twenty `(5,2)` cache.

## Theorem PX928 — PROVED FINITE

For global multiplicity-three case `12`, orientation `0`, start from the first clean concatenated top order

`0,1,5,6,3,4,2,2,0,5,4,3,1,6`.

Delete its fourteen top literals in column order. After each deletion, the verifier re-enumerates every compatible clean top order and exactly refutes the complete three-selector group with the shared bottom CSP.

All fourteen assumptions can be deleted. With no top literal retained, the bare signature has exactly

\[
\boxed{49{,}584}
\]

clean concatenated top orders. Every one is infeasible in orientation `0`, after exactly

\[
\boxed{76{,}849}
\]

bottom-CSP nodes. The complete top enumeration uses `143,487` search nodes.

Thus case `12` has an empty top-assumption core and supplies one signature-level master nogood covering its entire clean concatenated top-order family.

## Corollary PX929 — PROVED REDUCTION

Multiplicity-three cases `0` through `12` are thirteen consecutive signatures with mechanically verified empty orientation-zero top cores. This remains finite recurrence evidence rather than a universal theorem over the multiplicity-three tier.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case12_orientation0_empty_top_core.cpp \
  -o /tmp/m3-case12-empty-core

/tmp/m3-case12-empty-core
```

The checker regenerates the exact layer, locates global multiplicity-three case `12`, validates the selected top order, and asserts every intermediate top-order, top-node, and bottom-node count through the empty core.
