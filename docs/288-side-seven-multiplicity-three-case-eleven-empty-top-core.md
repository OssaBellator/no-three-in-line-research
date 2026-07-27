# Multiplicity-three case eleven: empty top-assumption core

This chapter records the twelfth consecutive multiplicity-three signature-level master nogood in the side-seven radius-three support-twenty `(5,2)` cache.

## Theorem PX920 — PROVED FINITE

For global multiplicity-three case `11`, orientation `0`, start from the first clean concatenated top order

`0,1,5,3,2,6,4,4,2,6,3,5,1,0`.

Delete its fourteen top literals in column order. After each deletion, the verifier re-enumerates every compatible clean top order and exactly refutes the complete three-selector group with the shared bottom CSP.

All fourteen assumptions can be deleted. With no top literal retained, the bare signature has exactly

\[
\boxed{33{,}596}
\]

clean concatenated top orders. Every one is infeasible in orientation `0`, after exactly

\[
\boxed{58{,}883}
\]

bottom-CSP nodes. The complete top enumeration uses `126,130` search nodes.

Thus case `11` has an empty top-assumption core and supplies one signature-level master nogood covering its entire clean concatenated top-order family.

## Corollary PX921 — PROVED REDUCTION

Multiplicity-three cases `0` through `11` are twelve consecutive signatures with mechanically verified empty orientation-zero top cores. This remains finite recurrence evidence rather than a universal theorem over the multiplicity-three tier.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case11_orientation0_empty_top_core.cpp \
  -o /tmp/m3-case11-empty-core

/tmp/m3-case11-empty-core
```

The checker regenerates the exact layer, locates global multiplicity-three case `11`, validates the selected top order, and asserts every intermediate top-order, top-node, and bottom-node count through the empty core.
