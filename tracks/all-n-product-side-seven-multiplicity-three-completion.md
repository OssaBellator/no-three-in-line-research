# All-n product track: side-seven low-multiplicity frontier

**Branch:** `research/all-n-product-construction`

This stage is the exact full-selector classification of the `(5,2)` relative cycle class inside the radius-three, support-twenty layer of the canonical `[14]^2` host. It is a finite census, not an infinite closure theorem.

## Current exact ledger

The layer contains `71,860` selectors grouped into `38,553` top signatures. All selectors of multiplicity at least three are classified:

- `37,600` are certified infeasible in all four radix orientations;
- one multiplicity-four selector has a verified no-three embedding.

Multiplicity two contains `3,840` signatures and `7,680` selectors. The first `1,370` signatures, global cases `0` through `1369`, are classified:

- `2,739` multiplicity-two selectors are certified infeasible;
- case `1287`, selector zero, supplies a second verified no-three embedding;
- the classified prefix uses `505,816,508` certified rejection-CSP nodes.

Therefore the committed support-twenty boundary is:

- `40,339` certified-infeasible selectors;
- two constructive selectors;
- `31,519` unclassified selectors;
- `3,272,271,752` certified rejection-CSP nodes.

The unresolved cache consists exactly of:

- `2,470` multiplicity-two signatures containing `4,940` selectors;
- all `26,579` multiplicity-one selectors.

The next canonical multiplicity-two case is `1370`.

## Exact finite proof units

The common engine is `scripts/product_side_seven_cache_engine.hpp`. The committed multiplicity-two proof family is:

- `multiplicity2_pilot10.cpp` for cases `0`--`9`;
- `multiplicity2_shard1.cpp` through `multiplicity2_shard127.cpp` for cases `10`--`1279`;
- `multiplicity2_shard128_special.cpp` for the nineteen rejections and one construction in cases `1280`--`1289`;
- `multiplicity2_shard129.cpp` through `multiplicity2_shard135.cpp` for cases `1290`--`1359`;
- `verify_product_side_seven_multiplicity2_cases1360_1369.py` for the selector-aware ten-case continuation.

Each ordinary rejection wrapper asserts the tier size, exact interval, both clean-top and top-node totals, all four bottom-CSP totals, and one ordered transcript digest. The special shard rebuilds the case-`1287` signature and state, independently checks the 28-point construction, and separately rejects selector one. The selector-aware continuation treats a verified construction as a successful classification rather than a failed shard.

## Certificate compression and master learning

For multiplicity-two case zero, orientation three:

- the first 64 references reduce to 49 actual keys covering 92 clean top orders;
- the first 128 references reduce to 102 actual keys covering 164 clean top orders;
- the first 192 references reduce to 150 actual keys covering 204 clean top orders;
- 15 references in indices `128`--`191` reuse first-128 keys, while 48 genuinely new keys appear;
- selector masks align at 60 of 192 references;
- the vocabulary has 443 extension occurrences on 57 mask classes;
- all 64 newly measured selector covers use seven triples;
- the complete 192-reference replay uses `4,465,440` exact bottom checks.

A deterministic greedy set cover followed by reverse deletion compresses the 150-key vocabulary to a 115-key irredundant basis for the exact 204-top union. The basis has 231 incidences, 177 private top-order witnesses, maximum overlap two, and replay digest `12529763722981785837`. It is an exact upper bound, not a minimum-cardinality proof.

The complete clean-top family has 35,112 orders, so the current semantic union covers only `17/2926` and leaves 34,908 orders outside it. Expanding the union is now the dominant compression task; optimizing 115 keys inside a 204-top island is secondary.

## Immediate tasks

1. Continue multiplicity two from case `1370` with selector-aware classification.
2. Generate semantic references from clean top orders outside the current 204-top union.
3. Target the 177 private top-order witnesses in the 115-key basis only after the union has expanded materially.
4. Test whether the case-`1287` construction has a symmetry orbit or a reusable local template.
5. Defer multiplicity one until multiplicity-two proof size, construction frequency, and symmetry are understood.
6. Continue the finite-range, non-affine recursion, protected-spread, bounded-barrier repair, and carry/absorber fronts.
7. Keep every finite result separate from an all-`n` claim.

## Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_full192_relaxed.py
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_set_cover192.py

g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_multiplicity2_case0_orientation3_semantic_union_complement192.cpp \
  -o /tmp/verify-semantic-complement192
/tmp/verify-semantic-complement192

python scripts/verify_product_side_seven_multiplicity2_cases1360_1369.py

g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard128_special.cpp \
  -o /tmp/m2-shard128-special
/tmp/m2-shard128-special
```

The classical no-three-in-line conjecture and infinite product closure remain open.
