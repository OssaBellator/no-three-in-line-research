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
`560` signatures, global cases `0` through `559`, are closed in fifty-six
canonical ten-signature proof units:

- `1,120` multiplicity-two selectors are certified infeasible;
- every shard has a standalone ordered-transcript digest verifier;
- the prefix uses `239,816,072` shared bottom-CSP nodes.

Therefore the committed support-twenty boundary is:

- `38,720` certified-infeasible selectors;
- one constructive selector;
- `33,139` unclassified selectors;
- `3,006,271,316` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `3,280` multiplicity-two signatures containing `6,560` selectors;
- all `26,579` multiplicity-one selectors.

An exact eight-shard workflow is registered for cases `560` through `639`. It is
not counted until every transcript is promoted.

## Constructive witness

Global multiplicity-four case `1392`, selector zero, has a verified no-three
embedding in orientation `1`. The mixed verifier checks 28 distinct points and
all 3,276 nonzero integer determinants. The other three selectors in that
signature are jointly certified infeasible.

## Exact finite proof units

The common engine is `scripts/product_side_seven_cache_engine.hpp`. The committed
multiplicity-two shard family is:

- `multiplicity2_pilot10.cpp` for cases `0`--`9`;
- `multiplicity2_shard1.cpp` through `multiplicity2_shard55.cpp` for cases
  `10`--`559`.

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
Semantic deletion gives pair-mask `6936` at eleven references and pair-mask
`6920` at one. Deduplicating the actual partial assignments yields only five
master-nogood keys:

- four six-column assignments on mask `6936`;
- one five-column assignment on mask `6920`.

Their extension lists contain 40 occurrences but only 14 distinct clean top
orders, so 26 occurrences are overlap. Both selectors are replayed on every
extension, for 403,200 exact bottom checks.

The next compression target is to generate semantic cores for the remaining
support classes, deduplicate their actual assignments, and measure total coverage
against the complete orientation-three top-order family.

## Immediate tasks

1. Promote cases `560--639`, then continue the multiplicity-two census.
2. Extend semantic support deletion beyond the repeated `6975` class.
3. Measure union coverage of the full semantic vocabulary and select a compact
   set-cover basis for the top-master problem.
4. Defer multiplicity one until multiplicity-two proof size and symmetry are
   understood.
5. Keep every finite result explicitly separate from an all-`n` claim.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_bottom_cover8.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_bottom_cover64.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_cover_support64.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_repeated_semantic_cores.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary.py

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1..55}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```

The classical no-three-in-line conjecture and infinite product closure remain
open.
