# All-n product track: side-seven low-multiplicity frontier

**Branch:** `research/all-n-product-construction`

This stage is the exact full-selector classification of the `(5,2)` relative cycle class inside the radius-three, support-twenty layer of the canonical `[14]^2` host. It is a finite census, not an infinite closure theorem.

## Current exact ledger

The layer contains `71,860` selectors grouped into `38,553` top signatures. All selectors of multiplicity at least three are classified:

- `37,600` are certified infeasible in all four radix orientations;
- one multiplicity-four selector has a verified no-three embedding.

Multiplicity two contains `3,840` signatures and `7,680` selectors. The first `1,120` signatures, global cases `0` through `1119`, are closed in 112 canonical ten-signature proof units:

- `2,240` multiplicity-two selectors are certified infeasible;
- every shard has a standalone ordered-transcript digest verifier;
- the prefix uses `422,791,999` shared bottom-CSP nodes.

Therefore the committed support-twenty boundary is:

- `39,840` certified-infeasible selectors;
- one constructive selector;
- `32,019` unclassified selectors;
- `3,189,247,243` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `2,720` multiplicity-two signatures containing `5,440` selectors;
- all `26,579` multiplicity-one selectors.

Cases `1120` through `1199` are registered but uncounted.

## Exact finite proof units

The common engine is `scripts/product_side_seven_cache_engine.hpp`. The committed multiplicity-two shard family is:

- `multiplicity2_pilot10.cpp` for cases `0`--`9`;
- `multiplicity2_shard1.cpp` through `multiplicity2_shard111.cpp` for cases `10`--`1119`.

Each wrapper asserts the tier size, exact interval, both clean-top and top-node totals, all four bottom-CSP totals, and one ordered transcript digest.

## Certificate compression and master learning

For multiplicity-two case zero, orientation three:

- the first 64 references reduce to 49 actual keys covering 92 clean top orders;
- the first 128 references reduce to 102 actual keys covering 164 clean top orders;
- seven later references reuse first-prefix keys, while 53 genuinely new keys appear;
- selector masks align at 40 references and require pair unions at 88;
- selector zero has three twelve-triple greedy covers; selector one retains seven-triple covers throughout;
- all extension replays use 3,185,280 exact bottom checks.

The next compression target is to extend beyond top index 127, measure vocabulary growth and reuse, and solve a compact set-cover problem against the complete clean-top family.

## Immediate tasks

1. Promote cases `1120--1199`, then continue multiplicity two.
2. Extend semantic master learning beyond top index 127 and measure vocabulary saturation.
3. Build and verify a compact set-cover basis from the accumulated master keys.
4. Defer multiplicity one until multiplicity-two proof size and symmetry are understood.
5. Continue the finite-range, non-affine recursion, protected-spread, bounded-barrier repair, and carry/absorber fronts.
6. Keep every finite result separate from an all-`n` claim.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_full128_relaxed.py

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1..111}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```

The classical no-three-in-line conjecture and infinite product closure remain open.
