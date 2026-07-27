# All-n product track: side-seven radius-three cache stage

**Branch:** `research/all-n-product-construction`

This stage continues the exact full-selector classification at base side seven.
It studies the `(5,2)` relative-cycle class inside the radius-three,
support-twenty selector layer of the canonical `[14]^2` host. The task is a
finite obstruction-and-witness census, not an infinite closure theorem.

## Current ledger

The exact support-twenty layer contains `71,860` selectors. Shared-top searches
have classified every top-signature tier of multiplicity at least `4` and the
first twenty-two hundred signatures of multiplicity `3`:

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
| 4 | 2,392 | 9,568 | 9,567 infeasible; 1 witnessed |
| 3, shards 0--21 | 2,200 of 3,544 | 6,600 | certified infeasible |
| **Total** | **6,790 completed classes** | **33,568 rejected; 1 witnessed** | **2,261,682,464 rejection-CSP nodes** |

Thus `38,291` support-twenty selectors remain unclassified and active in this
cache layer.

The latest exact results are PX932--PX935 in
[`docs/293-side-seven-cycle52-radius-three-support-twenty-multiplicity-three-shard-twenty-one.md`](../docs/293-side-seven-cycle52-radius-three-support-twenty-multiplicity-three-shard-twenty-one.md).

## Constructive witness

Global multiplicity-four case `1392`, selector zero, has a verified no-three
embedding in orientation `1`. The mixed verifier checks the selector state,
clean top assignment, bottom permutation, 28 distinct points, and all 3,276
nonzero integer determinants. The other three selectors in that signature are
jointly certified infeasible in all four orientations.

## Solver and proof-object improvements

The common radius-layer generation, clean-top enumeration, hoisted incidence
masks, scalar point tables, active-selector propagation, and exact count checks
live in `scripts/product_side_seven_cache_engine.hpp`.

The common transcript verifiers print every per-signature count while one
asserted 64-bit digest commits each complete ordered tier or shard transcript.
`scripts/product_side_seven_tier_shard_digest.hpp` adds independently
reproducible lexicographic shard intervals without checking in large case data
tables. Witness-preserving scan workers retain constructive data and continue
rather than terminating a range.

PX743--PX744 add the first explicit proof-object pilot. For multiplicity-four
case `1180`, orientation `0`, and one clean top order, a `60,536`-byte
certificate supplies a concrete collinear triple for every selector-permutation
obligation and is checked without calling `BottomGroupSolver`.

PX749--PX750 introduce a shared triple dictionary, and PX764--PX765 measure its
saturation over eight top orders. PX804--PX805 and PX810--PX811 extend the
multiplicity-four experiment to 32 and 64 top orders.

PX816--PX817 transfer the dictionary format to multiplicity-three case `0`.
PX834--PX835, PX876--PX877, PX890--PX891, PX898--PX899, PX906--PX907,
PX914--PX915, PX922--PX923, and PX930--PX931 extend the exact prefix through
64, 128, 256, 512, 1,024, 2,048, 4,096, and 8,192 clean top orders. At 8,192
orders, only `1,408` triples cover `123,863,040` obligations in a projected
`123,982,000`-byte payload, rather than `371,703,856` bytes for direct triples.
The ordered proof transcript has digest `7207755927317802285`, and the final 134
orders introduce no new triple.

PX774--PX775 give the first exact top-assumption core. For multiplicity-four
case `1180`, orientation `0`, every top literal can be deleted: the bare
signature refutes all `70,376` clean concatenated top orders after `95,298`
shared bottom-CSP nodes.

PX840--PX841, PX850--PX851, PX860--PX861, PX866--PX867, PX872--PX873,
PX874--PX875, PX882--PX883, PX888--PX889, PX896--PX897, PX904--PX905,
PX912--PX913, PX920--PX921, and PX928--PX929 repeat the experiment on
multiplicity-three cases `0` through `12`. Every one of those thirteen
consecutive signatures has an empty orientation-zero top core and therefore
supplies a signature-level master nogood covering its entire clean concatenated
top-order family.

PX641--PX642 remain the stronger full selector-choice CSP and proof-logged SAT
route. No external SAT solver or DRAT/FRAT checker is available in the current
execution environment, so independently checked native certificates remain the
active proof-producing route.

## Immediate task

The remaining multiplicity-three frontier begins at global case index `2200`
and contains `1,344` top signatures and `4,032` selectors. Continue in
independently reproducible, witness-preserving intervals. In parallel:

1. test how far the empty top-core recurrence extends;
2. generalize signature-level master nogoods across mechanically checked incidence features;
3. continue measuring dictionary saturation over wider top-order batches;
4. export one selector-choice shard to CNF when an independent proof checker is available;
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
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard21.cpp \
  -o /tmp/m3s21
/tmp/m3s21

g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case12_orientation0_empty_top_core.cpp \
  -o /tmp/m3-case12-empty-core
/tmp/m3-case12-empty-core

g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity3_case0_orientation0_dictionary_saturation8192.cpp \
  -o /tmp/m3-case0-dict8192
/tmp/m3-case0-dict8192
```

The classical no-three-in-line conjecture and infinite product closure remain
open.
