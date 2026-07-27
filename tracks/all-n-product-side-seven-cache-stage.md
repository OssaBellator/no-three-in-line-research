# All-n product track: side-seven radius-three cache stage

**Branch:** `research/all-n-product-construction`

This stage continues the exact full-selector classification at base side seven.
It studies the `(5,2)` relative-cycle class inside the radius-three,
support-twenty selector layer of the canonical `[14]^2` host. The task is a
finite obstruction census, not an infinite closure theorem.

## Current ledger

The exact support-twenty layer contains `71,860` selectors. Shared-top searches
have closed every top-signature tier of multiplicity at least `5` and the first
1,380 signatures of multiplicity `4`:

| Multiplicity | Signatures | Selectors | Status |
|---:|---:|---:|---|
| 46 | 4 | 184 | certified infeasible |
| 40 | 3 | 120 | certified infeasible |
| 38 | 3 | 114 | certified infeasible |
| 35 | 2 | 70 | certified infeasible |
| 32 | 3 | 96 | certified infeasible |
| 27 | 6 | 162 | certified infeasible |
| 26 | 6 | 156 | certified infeasible |
| 24 | 8 | 192 | certified infeasible |
| 23 | 10 | 230 | certified infeasible |
| 20 | 1 | 20 | certified infeasible |
| 19 | 42 | 798 | certified infeasible |
| 16 | 38 | 608 | certified infeasible |
| 15 | 2 | 30 | certified infeasible |
| 14 | 40 | 560 | certified infeasible |
| 13 | 48 | 624 | certified infeasible |
| 12 | 128 | 1,536 | certified infeasible |
| 10 | 164 | 1,640 | certified infeasible |
| 9 | 64 | 576 | certified infeasible |
| 8 | 277 | 2,216 | certified infeasible |
| 7 | 100 | 700 | certified infeasible |
| 6 | 524 | 3,144 | certified infeasible |
| 5 | 725 | 3,625 | certified infeasible |
| 4, shards 0--13 | 1,380 of 2,392 | 5,520 | certified infeasible |
| **Total** | **3,578 completed classes** | **22,921** | **1,155,933,381 shared bottom-CSP nodes** |

Thus `48,939` support-twenty selectors remain active in this cache layer.

The latest complete cache results are PX745--PX748 in
[`docs/233-side-seven-cycle52-radius-three-support-twenty-multiplicity-four-shard-thirteen.md`](../docs/233-side-seven-cycle52-radius-three-support-twenty-multiplicity-four-shard-thirteen.md).

## Solver improvement

The common radius-layer generation, clean-top enumeration, hoisted incidence
masks, scalar point tables, active-selector propagation, and exact count checks
live in `scripts/product_side_seven_cache_engine.hpp`.

The common transcript verifiers print every per-signature count while one
asserted 64-bit digest commits each complete ordered tier or shard transcript.
`scripts/product_side_seven_tier_shard_digest.hpp` adds independently
reproducible lexicographic shard intervals without checking in large case data
tables.

PX743--PX744 add the first explicit proof-object pilot. For case `1180`,
orientation `0`, and the first clean concatenated top order,
`scripts/verify_product_side_seven_case1180_orientation0_bottom_certificate.cpp`
generates a `60,536`-byte certificate containing one concrete collinear triple
for each of `20,160` selector-permutation obligations. Its checker validates
edge membership, exact zero determinants, file length, and digest without
calling `BottomGroupSolver`.

PX749--PX750 extend the format to the first two clean top orders. A shared
dictionary of `84` triples represents `40,320` obligations in a `40,648`-byte
proof object with anchored digest `10705560690873782484`. The checker again
validates only explicit geometry and dictionary references, not the bottom CSP.

PX641--PX642 remain the stronger full selector-choice CSP and proof-logged SAT
route. A naive family-wide selector-choice prototype was exact but slower
because it weakened top-variable propagation.

## Immediate task

The remaining multiplicity-four frontier begins at global case index `1380` and
contains `1,012` top signatures and `4,048` selectors. Continue in independently
reproducible intervals using the shard-digest verifier. In parallel:

1. stream more clean top orders into the shared triple dictionary and measure saturation;
2. extract mechanically rechecked partial top-assignment cores from repeated certificates;
3. learn a master nogood covering every top order extending one core;
4. export one selector-choice shard to CNF and check an UNSAT proof independently;
5. add only mechanically verified host/reflection symmetry constraints.

## Stage completion criterion

This cache stage is complete when every selector in the radius-three,
support-twenty `(5,2)` layer is either certified infeasible in all four
orientations or accompanied by an independently checked no-three witness.
Afterward the side-seven classification must still address the remaining
support layers and relative-cycle classes.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard13.cpp \
  -o /tmp/m4s13

/tmp/m4s13

g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_case1180_two_top_dictionary_certificate.cpp \
  -o /tmp/case1180-dict-cert

/tmp/case1180-dict-cert generate /tmp/case1180-two-top.cert
/tmp/case1180-dict-cert check /tmp/case1180-two-top.cert
```

The classical no-three-in-line conjecture and infinite product closure remain
open.
