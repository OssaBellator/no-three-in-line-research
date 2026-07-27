# All-n product track: side-seven radius-three cache stage

**Branch:** `research/all-n-product-construction`

This stage is the exact full-selector classification of the `(5,2)` relative
cycle class inside the radius-three, support-twenty layer of the canonical
`[14]^2` host. It is a finite obstruction-and-witness census, not an infinite
closure theorem.

## Current exact ledger

The layer contains `71,860` selectors grouped into `38,553` top signatures. All
selectors of multiplicity at least three are classified:

- `37,600` are certified infeasible in all four radix orientations;
- one multiplicity-four selector has a verified no-three embedding.

Multiplicity two contains `3,840` signatures and `7,680` selectors. The first
`400` signatures, global cases `0` through `399`, are closed in forty canonical
ten-signature proof units:

- `800` multiplicity-two selectors are certified infeasible;
- every shard has a standalone ordered-transcript digest verifier;
- the complete multiplicity-two prefix uses `155,966,016` shared bottom-CSP
  nodes.

Therefore the committed support-twenty boundary is:

- `38,400` certified-infeasible selectors;
- one constructive selector;
- `33,459` unclassified selectors;
- `2,922,421,260` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `3,440` multiplicity-two signatures containing `6,880` selectors;
- all `26,579` multiplicity-one signatures and selectors.

A durable exact matrix covers cases `400` through `479`. It is not counted until
all eight transcripts are promoted to replay verifiers.

## Constructive witness

Global multiplicity-four case `1392`, selector zero, has a verified no-three
embedding in orientation `1`. The mixed verifier checks the selector state,
clean top assignment, bottom permutation, 28 distinct points, and all 3,276
nonzero integer determinants. The other three selectors in that signature are
jointly certified infeasible in all four orientations.

## Exact finite proof units

The common radius-layer generation, clean-top enumeration, hoisted incidence
masks, scalar point tables, active-selector propagation, and exact count checks
live in `scripts/product_side_seven_cache_engine.hpp`.

The committed multiplicity-two shard family is:

- `multiplicity2_pilot10.cpp` for cases `0`--`9`;
- `multiplicity2_shard1.cpp` through `multiplicity2_shard39.cpp` for cases
  `10`--`399`.

Each wrapper asserts the tier size `3,840`, its exact lexicographic interval,
clean-top and top-node totals in both column orders, all four bottom-CSP totals,
and one ordered transcript digest.

## Certificate compression and master learning

PX960--PX961 reduce fixed-top bottom infeasibility to explicit covers of all
`5,040` bottom permutations by collinear abstract triples.

For multiplicity-two case zero, orientation three:

- the first 64 top orders give 128 selector obligations;
- every obligation has a seven-triple cover;
- 55 unique triples and 93 covers encode all 896 cover entries;
- only 37 top-support masks occur;
- every support fixes at most 11 of 14 columns.

PX1010--PX1012 semantically minimize the two covers at top order `35`:

- selector zero needs six top columns;
- selector one needs five;
- their seven-column union mask `11546` refutes both selectors across four clean
  top extensions and 40,320 exact bottom checks.

This is the first compact two-selector partial-top master nogood at multiplicity
two. The next target is to minimize and deduplicate the repeated cover/support
classes over the 64-top prefix.

## Immediate tasks

1. Promote the `400--479` transcripts, then continue from case `480`.
2. Apply semantic support deletion to repeated cover and support classes.
3. Measure how much of the complete top-order family is covered by a small
   master-nogood vocabulary.
4. Defer multiplicity one until multiplicity-two proof size and symmetry are
   understood.
5. Keep every finite result explicitly separate from an all-`n` claim.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_bottom_cover8.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_bottom_cover64.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_cover_support64.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_cover_core.py

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1..39}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```

The classical no-three-in-line conjecture and infinite product closure remain
open.
