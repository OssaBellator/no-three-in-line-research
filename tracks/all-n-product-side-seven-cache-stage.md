# All-n product track: side-seven radius-three cache stage

**Branch:** `research/all-n-product-construction`

This stage continues the exact full-selector classification at base side seven.
It studies the `(5,2)` relative-cycle class inside the radius-three,
support-twenty selector layer of the canonical `[14]^2` host. The task is a
finite obstruction census, not an infinite closure theorem.

## Current ledger

The exact support-twenty layer contains `71,860` selectors. Shared-top searches
have closed every top-signature tier of multiplicity at least `12`:

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
| **Total** | **344 completed classes** | **5,500** | **128,928,336 shared bottom-CSP nodes** |

Thus `66,360` support-twenty selectors remain active in this cache layer.

The latest exact results are PX663--PX666 in
[`docs/212-side-seven-cycle52-radius-three-support-twenty-multiplicity-twelve.md`](../docs/212-side-seven-cycle52-radius-three-support-twenty-multiplicity-twelve.md).

## Solver improvement

The common radius-layer generation, clean-top enumeration, hoisted incidence
masks, scalar point tables, active-selector propagation, and exact count checks
now live in `scripts/product_side_seven_cache_engine.hpp`. New tier scripts are
data tables plus one generic `verify_tier` call.

PX641--PX642 give a stronger exact formulation: one selector-choice CSP, or
one one-hot CNF, can decide an entire selector family at once. The intended
upgrade is assumption-based conflict extraction from the bottom subproblem,
followed by proof-logged SAT or certified dominance and symmetry breaking. See
[`docs/207-selector-choice-csp-and-certified-symmetry.md`](../docs/207-selector-choice-csp-and-certified-symmetry.md).

## Immediate task

There is no multiplicity-11 class. The next nonempty tier has multiplicity `10`:
one hundred sixty-four top signatures containing `1,640` selectors. Its width
makes the proof-producing solver route more urgent. Split the tier into
independently reproducible verifier shards while implementing assumption-based
conflict extraction:

1. add top-assignment assumption literals;
2. extract deletion-minimal bottom infeasibility cores;
3. learn a master nogood covering every top order extending one core;
4. export one selector-choice shard to CNF and check an UNSAT proof independently;
5. add only mechanically verified host/reflection symmetry constraints.

A complete shard result must assert the exact histogram, every clean-top order
and top-node count, every bottom-node count, and either an explicit surviving
configuration or exact infeasibility.

## Stage completion criterion

This cache stage is complete when every selector in the radius-three,
support-twenty `(5,2)` layer is either certified infeasible in all four
orientations or accompanied by an independently checked no-three witness.
Afterward the side-seven classification must still address the remaining
support layers and relative-cycle classes.

## Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity12.cpp \
  -o /tmp/m12

for case_index in $(seq 0 127); do
  for orientation in 0 1 2 3; do
    /tmp/m12 "$case_index" "$orientation"
  done
done
```

The classical no-three-in-line conjecture and infinite product closure remain
open.
