# Multiplicity-three case seven: empty top-assumption core

This chapter records the eighth consecutive multiplicity-three signature-level master nogood in the side-seven radius-three support-twenty `(5,2)` cache.

## Theorem PX888 — PROVED FINITE

For global multiplicity-three case `7`, orientation `0`, begin with the first clean concatenated top order

`0,1,6,3,2,4,5,2,0,4,5,6,3,1`.

Delete its fourteen top literals in column order. After each deletion the verifier re-enumerates every clean top order compatible with the retained assumptions and exactly refutes the whole three-selector group by the shared bottom CSP.

All fourteen assumptions can be deleted. With no top literal retained, the bare signature has exactly

\[
\boxed{41{,}176}
\]

clean concatenated top orders. Every one is infeasible in orientation `0`, after exactly

\[
\boxed{68{,}510}
\]

bottom-CSP nodes. The complete top enumeration uses `151,691` search nodes.

Thus case `7` has an empty top-assumption core and contributes one signature-level master nogood covering its entire clean concatenated top-order family.

## Corollary PX889 — PROVED REDUCTION

Multiplicity-three cases `0` through `7` are eight consecutive signatures with mechanically verified empty orientation-zero top cores. This strengthens the recurrence evidence but does not by itself prove that every multiplicity-three signature has an empty core.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case7_orientation0_empty_top_core.cpp \
  -o /tmp/m3-case7-empty-core

/tmp/m3-case7-empty-core
```

The checker regenerates the exact radius layer, locates global multiplicity-three case `7`, validates the selected top order, and asserts every intermediate top-order, top-node, and bottom-node count through the empty core.
