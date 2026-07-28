# All-n product track: side-seven low-multiplicity frontier

**Branch:** `research/all-n-product-construction`

This stage is the exact full-selector classification of the `(5,2)` relative cycle class inside the radius-three, support-twenty layer of the canonical `[14]^2` host. It is a finite census, not an infinite closure theorem.

## Current exact ledger

The layer contains `71,860` selectors grouped into `38,553` top signatures. All selectors of multiplicity at least three are classified:

- `37,600` are certified infeasible in all four radix orientations;
- one multiplicity-four selector has a verified no-three embedding.

Multiplicity two contains `3,840` signatures and `7,680` selectors. The first `1,040` signatures, global cases `0` through `1039`, are closed in 104 canonical ten-signature proof units:

- `2,080` multiplicity-two selectors are certified infeasible;
- every shard has a standalone ordered-transcript digest verifier;
- the prefix uses `399,139,256` shared bottom-CSP nodes.

Therefore the committed support-twenty boundary is:

- `39,680` certified-infeasible selectors;
- one constructive selector;
- `32,179` unclassified selectors;
- `3,165,594,500` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `2,800` multiplicity-two signatures containing `5,600` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1040`.

## Exact finite proof units

The common engine is `scripts/product_side_seven_cache_engine.hpp`. The committed multiplicity-two shard family is:

- `multiplicity2_pilot10.cpp` for cases `0`--`9`;
- `multiplicity2_shard1.cpp` through `multiplicity2_shard103.cpp` for cases `10`--`1039`.

Each wrapper asserts the tier size, exact interval, both clean-top and top-node totals, all four bottom-CSP totals, and one ordered transcript digest.

## Certificate compression and master learning

For multiplicity-two case zero, orientation three:

- the first 64 top orders give 128 selector obligations;
- every obligation has a seven-triple cover;
- 55 triples and 93 covers encode 896 cover entries;
- all 64 reference cores have been semantically minimized;
- 30 references retain aligned selector masks and 34 require selector-mask unions;
- the 64 cores deduplicate to 49 actual partial-assignment keys on 30 mask shapes;
- their 169 extension occurrences have an exact union of 92 clean top orders;
- both selector covers are replayed using 1,703,520 exact bottom checks.

An exact census through top index 127 is active. It separately measures reuse of the established 49 keys, new keys, new covered top orders, and incremental bottom verification; it is not counted until promoted.

## Immediate tasks

1. Continue multiplicity-two classification from case `1040`.
2. Promote the semantic vocabulary census through top index 127 and measure vocabulary saturation.
3. Build and verify a compact set-cover basis from the accumulated master keys.
4. Defer multiplicity one until multiplicity-two proof size and symmetry are understood.
5. Continue the independent finite-range, non-affine recursion, protected-spread, bounded-barrier repair, and hyperbola/carry fronts.
6. Keep every finite result separate from an all-`n` claim.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_full64.py

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1..103}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```

The classical no-three-in-line conjecture and infinite product closure remain open.
