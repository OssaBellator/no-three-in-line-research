# All-n product track: side-seven radius-three cache stage

**Branch:** `research/all-n-product-construction`

This stage continues the exact full-selector classification at base side seven.
It studies the `(5,2)` relative-cycle class inside the radius-three,
support-twenty selector layer of the canonical `[14]^2` host. The task is a
finite obstruction-and-witness census, not an infinite closure theorem.

## Current ledger

The exact support-twenty layer contains `71,860` selectors. Shared-top searches
have classified every top-signature tier of multiplicity at least `5` and the
first 1,480 signatures of multiplicity `4`:

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
| 4, mixed shard 14 | 100 | 400 | 399 infeasible; 1 witnessed |
| **Total** | **3,678 completed classes** | **23,320 rejected; 1 witnessed** | **1,182,736,279 rejection-CSP nodes** |

Thus `48,539` support-twenty selectors remain unclassified and active in this
cache layer.

The latest classified results are PX751--PX755 in
[`docs/235-side-seven-cycle52-radius-three-support-twenty-multiplicity-four-shard-fourteen-mixed.md`](../docs/235-side-seven-cycle52-radius-three-support-twenty-multiplicity-four-shard-fourteen-mixed.md).

## First constructive witness

Global multiplicity-four case `1392`, selector zero, has a verified no-three
embedding in orientation `1`. The mixed verifier checks the selector state,
clean top assignment, bottom permutation, 28 distinct points, and all 3,276
nonzero integer determinants. The other three selectors in that signature are
jointly certified infeasible in all four orientations.

## Solver improvement

The common radius-layer generation, clean-top enumeration, hoisted incidence
masks, scalar point tables, active-selector propagation, and exact count checks
live in `scripts/product_side_seven_cache_engine.hpp`.

The common transcript verifiers print every per-signature count while one
asserted 64-bit digest commits each complete ordered tier or shard transcript.
`scripts/product_side_seven_tier_shard_digest.hpp` adds independently
reproducible lexicographic shard intervals without checking in large case data
tables. Mixed shard fourteen uses a dedicated verifier because it combines 399
obstructions with one constructive witness.

PX743--PX744 add the first explicit proof-object pilot. For case `1180`,
orientation `0`, and the first clean concatenated top order,
`scripts/verify_product_side_seven_case1180_orientation0_bottom_certificate.cpp`
generates a `60,536`-byte certificate containing one concrete collinear triple
for each of `20,160` selector-permutation obligations. Its checker validates
edge membership, exact zero determinants, file length, and digest without
calling `BottomGroupSolver`.

PX749--PX750 extend the format to the first two clean top orders. A shared
dictionary of `84` triples represents `40,320` obligations in a `40,648`-byte
proof object with anchored digest `10705560690873782484`.

PX641--PX642 remain the stronger full selector-choice CSP and proof-logged SAT
route.

## Immediate task

The remaining multiplicity-four frontier begins at global case index `1480` and
contains `912` top signatures and `3,648` selectors. Continue in independently
reproducible intervals, with scan workers retaining witness data rather than
terminating a range. In parallel:

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
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard14_mixed.cpp \
  -o /tmp/m4s14

/tmp/m4s14
/tmp/m4s14 1392

g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_case1180_two_top_dictionary_certificate.cpp \
  -o /tmp/case1180-dict-cert

/tmp/case1180-dict-cert generate /tmp/case1180-two-top.cert
/tmp/case1180-dict-cert check /tmp/case1180-two-top.cert
```

The classical no-three-in-line conjecture and infinite product closure remain
open.
