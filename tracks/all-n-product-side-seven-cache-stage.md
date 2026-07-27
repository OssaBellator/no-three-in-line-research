# All-n product track: side-seven radius-three cache stage

**Branch:** `research/all-n-product-construction`

This stage continues the exact full-selector classification at base side seven.
It studies the `(5,2)` relative-cycle class inside the radius-three,
support-twenty selector layer of the canonical `[14]^2` host. The task is a
finite obstruction census, not an infinite closure theorem.

## Current ledger

The exact support-twenty layer contains `71,860` selectors. Shared-top searches
have closed every top-signature tier of multiplicity at least `5` and the first
1,080 signatures of multiplicity `4`:

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
| 4, shards 0--10 | 1,080 of 2,392 | 4,320 | certified infeasible |
| **Total** | **3,278 completed classes** | **21,721** | **1,076,401,986 shared bottom-CSP nodes** |

Thus `50,139` support-twenty selectors remain active in this cache layer.

The latest exact results are PX731--PX734 in
[`docs/229-side-seven-cycle52-radius-three-support-twenty-multiplicity-four-shard-ten.md`](../docs/229-side-seven-cycle52-radius-three-support-twenty-multiplicity-four-shard-ten.md).

## Solver improvement

The common radius-layer generation, clean-top enumeration, hoisted incidence
masks, scalar point tables, active-selector propagation, and exact count checks
live in `scripts/product_side_seven_cache_engine.hpp`.

The common transcript verifiers print every per-signature count while one
asserted 64-bit digest commits each complete ordered tier or shard transcript.
`scripts/product_side_seven_tier_shard_digest.hpp` adds independently
reproducible lexicographic shard intervals without checking in large case data
tables.

PX641--PX642 give the stronger selector-choice CSP and proof-logged SAT route.
A naive family-wide selector-choice prototype was exact but slower because it
weakened top-variable propagation. Assumption-based conflict extraction and
mechanically certified symmetry remain parallel solver-development tasks.

## Immediate task

The remaining multiplicity-four frontier begins at global case index `1080` and
contains `1,312` top signatures and `5,248` selectors. Continue in independently
reproducible intervals using the shard-digest verifier. In parallel:

1. add top-assignment assumption literals;
2. extract mechanically rechecked bottom infeasibility cores;
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
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_shard10.cpp \
  -o /tmp/m4s10

/tmp/m4s10
```

The classical no-three-in-line conjecture and infinite product closure remain
open.
