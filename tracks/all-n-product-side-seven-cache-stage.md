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
`480` signatures, global cases `0` through `479`, are closed in forty-eight
canonical ten-signature proof units:

- `960` multiplicity-two selectors are certified infeasible;
- every shard has a standalone ordered-transcript digest verifier;
- the prefix uses `208,563,563` shared bottom-CSP nodes.

Therefore the committed support-twenty boundary is:

- `38,560` certified-infeasible selectors;
- one constructive selector;
- `33,299` unclassified selectors;
- `2,975,018,807` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `3,360` multiplicity-two signatures containing `6,720` selectors;
- all `26,579` multiplicity-one selectors.

A durable exact matrix covers cases `480` through `559`. It is not counted until
all eight transcripts are promoted.

## Constructive witness

Global multiplicity-four case `1392`, selector zero, has a verified no-three
embedding in orientation `1`. The mixed verifier checks 28 distinct points and
all 3,276 nonzero integer determinants. The other three selectors in that
signature are jointly certified infeasible.

## Exact finite proof units

The common engine is `scripts/product_side_seven_cache_engine.hpp`. The committed
multiplicity-two shard family is:

- `multiplicity2_pilot10.cpp` for cases `0`--`9`;
- `multiplicity2_shard1.cpp` through `multiplicity2_shard47.cpp` for cases
  `10`--`479`.

Each wrapper asserts the tier size, exact interval, both clean-top and top-node
totals, all four bottom-CSP totals, and one ordered transcript digest.

## Certificate compression and master learning

Fixed-top bottom infeasibility is equivalent to covering all `5,040` bottom
permutations by collinear abstract triples. For case zero, orientation three:

- the first 64 top orders give 128 selector obligations;
- every obligation has a seven-triple cover;
- 55 triples and 93 covers encode 896 cover entries;
- only 37 syntactic top-support masks occur.

The repeated support mask `6975` occurs for both selectors at twelve top orders.
Semantic deletion gives only two pair-mask shapes:

- mask `6936`, size six, at eleven top orders;
- mask `6920`, size five, at one top order.

The twelve pair cores certify 40 clean top extensions and 403,200 exact bottom
checks. At every measured reference, the two selector masks coincide, so no
union penalty is required.

The next compression target is to deduplicate the actual partial assignments on
these shapes and measure the union of their clean-extension families against the
complete orientation-three top-order set.

## Immediate tasks

1. Promote cases `480--559`, then continue the multiplicity-two census.
2. Deduplicate semantic partial assignments and quantify master-nogood coverage.
3. Extend semantic learning to additional support classes and orientations.
4. Defer multiplicity one until multiplicity-two proof size and symmetry are
   understood.
5. Keep every finite result explicitly separate from an all-`n` claim.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_bottom_cover8.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_bottom_cover64.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_cover_support64.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_repeated_semantic_cores.py

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1..47}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```

The classical no-three-in-line conjecture and infinite product closure remain
open.
