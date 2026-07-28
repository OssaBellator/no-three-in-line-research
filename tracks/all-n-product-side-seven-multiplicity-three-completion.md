# All-n product track: side-seven low-multiplicity frontier

**Branch:** `research/all-n-product-construction`

This stage is the exact full-selector classification of the `(5,2)` relative cycle class inside the radius-three, support-twenty layer of the canonical `[14]^2` host. It is a finite census, not an infinite closure theorem.

## Current exact ledger

The layer contains `71,860` selectors grouped into `38,553` top signatures. All selectors of multiplicity at least three are classified:

- `37,600` are certified infeasible in all four radix orientations;
- one multiplicity-four selector has a verified no-three embedding.

Multiplicity two contains `3,840` signatures and `7,680` selectors. The first `1,360` signatures, global cases `0` through `1359`, are classified:

- `2,719` multiplicity-two selectors are certified infeasible;
- case `1287`, selector zero, supplies a second verified no-three embedding;
- the classified prefix uses `499,208,119` certified rejection-CSP nodes.

Therefore the committed support-twenty boundary is:

- `40,319` certified-infeasible selectors;
- two constructive selectors;
- `31,539` unclassified selectors;
- `3,265,663,363` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `2,480` multiplicity-two signatures containing `4,960` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1360`.

## Exact finite proof units

The common engine is `scripts/product_side_seven_cache_engine.hpp`. The committed multiplicity-two proof family is:

- `multiplicity2_pilot10.cpp` for cases `0`--`9`;
- `multiplicity2_shard1.cpp` through `multiplicity2_shard127.cpp` for cases `10`--`1279`;
- `multiplicity2_shard128_special.cpp` for the nineteen rejections and one construction in cases `1280`--`1289`;
- `multiplicity2_shard129.cpp` through `multiplicity2_shard135.cpp` for cases `1290`--`1359`.

Each ordinary rejection wrapper asserts the tier size, exact interval, both clean-top and top-node totals, all four bottom-CSP totals, and one ordered transcript digest. The special shard rebuilds the case-`1287` signature and state, independently checks the 28-point construction, and separately rejects selector one.

## Certificate compression and master learning

For multiplicity-two case zero, orientation three:

- the first 64 references reduce to 49 actual keys covering 92 clean top orders;
- the first 128 references reduce to 102 actual keys covering 164 clean top orders;
- the first 192 references reduce to 150 actual keys covering 204 clean top orders;
- 15 references in indices `128`--`191` reuse first-128 keys, while 48 genuinely new keys appear;
- selector masks align at 52 of 192 references;
- all 64 newly measured selector covers use seven triples;
- the complete 192-reference replay uses `4,465,440` exact bottom checks.

A deterministic greedy set cover followed by reverse deletion compresses the 150-key vocabulary to a 115-key irredundant basis for the exact 204-top union. The basis has 231 incidences, 177 private top-order witnesses, maximum overlap two, and replay digest `12529763722981785837`. It is an exact upper bound, not a minimum-cardinality proof and not a cover of the complete clean-top family.

The next compression target is to attack the 177 private witnesses: find stronger shared covers or certified equivalences that merge them, while separately measuring the clean top orders outside the current 204-top union.

## Immediate tasks

1. Continue multiplicity two from case `1360`, treating constructive hits as first-class classifications rather than assumed failures.
2. Target the 177 private top-order witnesses in the 115-key semantic basis.
3. Measure which clean top orders remain outside the current 204-top semantic union.
4. Test whether the case-`1287` construction has a symmetry orbit or a reusable local template.
5. Defer multiplicity one until multiplicity-two proof size, construction frequency, and symmetry are understood.
6. Continue the finite-range, non-affine recursion, protected-spread, bounded-barrier repair, and carry/absorber fronts.
7. Keep every finite result separate from an all-`n` claim.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_full192_relaxed.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_set_cover192.py

g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard128_special.cpp \
  -o /tmp/m2-shard128-special
/tmp/m2-shard128-special

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1..127}.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{129..135}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```

The classical no-three-in-line conjecture and infinite product closure remain open.
