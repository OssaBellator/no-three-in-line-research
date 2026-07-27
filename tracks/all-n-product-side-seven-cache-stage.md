# All-n product track: side-seven radius-three cache stage

**Branch:** `research/all-n-product-construction`

This stage is the exact full-selector classification of the `(5,2)` relative
cycle class inside the radius-three, support-twenty layer of the canonical
`[14]^2` host. It is a finite obstruction-and-witness census, not an infinite
closure theorem.

## Current exact ledger

The support-twenty layer contains `71,860` selectors grouped into `38,553` top
signatures. The complete multiplicity histogram is independently verified.

All selectors of multiplicity at least three are classified:

- `37,600` are certified infeasible in all four radix orientations;
- one multiplicity-four selector has a verified no-three embedding.

Multiplicity two contains `3,840` signatures and `7,680` selectors. The first
`320` signatures, global cases `0` through `319`, are now closed in thirty-two
canonical ten-signature proof units:

- `640` multiplicity-two selectors are certified infeasible;
- every shard has a standalone ordered-transcript digest verifier;
- the complete multiplicity-two prefix uses `133,108,986` shared bottom-CSP
  nodes.

Therefore the current support-twenty boundary is:

- `38,240` certified-infeasible selectors;
- one constructive selector;
- `33,619` unclassified selectors;
- `2,899,564,230` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `3,520` multiplicity-two signatures containing `7,040` selectors;
- all `26,579` multiplicity-one signatures and selectors.

The next canonical finite frontier begins at multiplicity-two case `320`.

## Constructive witness

Global multiplicity-four case `1392`, selector zero, has a verified no-three
embedding in orientation `1`. The mixed verifier checks the selector state,
clean top assignment, bottom permutation, 28 distinct points, and all 3,276
nonzero integer determinants. The other three selectors in that signature are
jointly certified infeasible in all four orientations.

## Exact proof objects

The common radius-layer generation, clean-top enumeration, hoisted incidence
masks, scalar point tables, active-selector propagation, and exact count checks
live in `scripts/product_side_seven_cache_engine.hpp`.

The canonical finite proof unit is a ten-signature shard. Each wrapper asserts:

- the multiplicity-two tier size `3,840`;
- its exact lexicographic case interval;
- clean-top counts and top-search nodes in both column orders;
- bottom-CSP nodes in all four orientations;
- an ordered 64-bit transcript digest.

The committed shard family is:

- `multiplicity2_pilot10.cpp` for cases `0`--`9`;
- `multiplicity2_shard1.cpp` through `multiplicity2_shard31.cpp` for cases
  `10`--`319`.

## Certificate compression frontier

PX960--PX961 prove that fixed-top bottom infeasibility is equivalent to an
explicit set cover of all `5,040` bottom permutations by collinear abstract
triples. Two generic generators are committed:

1. a first-bad-triple dictionary format;
2. a deterministic greedy triple-subcover format.

A durable experiment is measuring multiplicity-two case zero on the first eight
clean top orders in each orientation. The next proof-object target is to
quantify repeated triple and cover reuse across selectors and top orders, then
combine stored covers with assumption-minimized top nogoods.

## Immediate tasks

1. Continue multiplicity-two classification from global case `320` in fixed
   ten-signature proof shards.
2. Promote every completed transcript immediately; never count queued or
   unpromoted jobs in the exact boundary.
3. Measure and deduplicate explicit bottom-permutation covers.
4. Add exact top-assumption minimization and signature-level master nogoods where
   the bottom verifier supports them.
5. Defer multiplicity one until the multiplicity-two proof size and symmetry
   structure are understood.
6. Keep every finite result explicitly separate from an all-`n` claim.

## Verification

```bash
for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1..31}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```

The classical no-three-in-line conjecture and infinite product closure remain
open.
