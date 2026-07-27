# All-n product track: side-seven low-multiplicity frontier

**Branch:** `research/all-n-product-construction`

This finite stage continues the side-seven `(5,2)` radius-three support-twenty
census, closes the complete multiplicity-three tier, identifies the exact
low-multiplicity remainder, and advances the multiplicity-two classification.

This stage does **not** prove infinite product closure or the no-three-in-line
conjecture.

## Completed ledger

| Item | Status | Result |
|---|---|---|
| Shared digest verifier | **REPAIRED** | `print_sig` is defined in the common header, so digest wrappers compile from a clean checkout. |
| Generic shard measurement | **COMPLETED** | `measure_product_side_seven_tier_shard.cpp` measures any canonical multiplicity interval, aborts on feasibility, and emits exact verifier constants. |
| Multiplicity-three cases `2200`--`3543` | **CLOSED** | All `1,344` remaining signatures and `4,032` selectors are infeasible in every orientation. |
| Complete multiplicity-three tier | **CLOSED** | All `3,544` signatures and `10,632` selectors are infeasible. |
| Exact signature histogram | **CERTIFIED** | `38,553` signatures partition all `71,860` selectors into the asserted 26 multiplicity tiers. |
| Multiplicity at least three | **CLASSIFIED** | `37,600` selectors are infeasible and one multiplicity-four selector is constructive. |
| Multiplicity-two cases `0`--`239` | **CLOSED** | `240` signatures and `480` selectors are infeasible; twenty-four ten-signature proof objects are committed. |
| Current finite cache boundary | **ADVANCED** | `38,080` selectors are infeasible, one is constructive, and `33,779` remain unclassified. |
| Exact computation | **COMPLETED TO CASE 239** | The cumulative certified cache uses `2,864,005,979` shared bottom-CSP nodes. |
| Residual cache | **IDENTIFIED** | `3,600` multiplicity-two signatures (`7,200` selectors) and all `26,579` multiplicity-one selectors remain. |
| Low-multiplicity proof compression | **REDUCED** | Fixed-top infeasibility is equivalent to explicit bottom-permutation triple covers; generic dictionary and greedy-cover generators are committed. |
| Infinite exact closure | **OPEN** | No recursive all-side theorem follows from this finite census. |

## Canonical artifacts

- [`docs/294-side-seven-cycle52-radius-three-support-twenty-multiplicity-three-completion.md`](../docs/294-side-seven-cycle52-radius-three-support-twenty-multiplicity-three-completion.md)
- [`docs/295-side-seven-cycle52-radius-three-support-twenty-signature-histogram.md`](../docs/295-side-seven-cycle52-radius-three-support-twenty-signature-histogram.md)
- [`docs/296-side-seven-cycle52-radius-three-support-twenty-multiplicity-two-pilot.md`](../docs/296-side-seven-cycle52-radius-three-support-twenty-multiplicity-two-pilot.md)
- [`docs/297-side-seven-cycle52-radius-three-support-twenty-multiplicity-two-shards-one-through-three.md`](../docs/297-side-seven-cycle52-radius-three-support-twenty-multiplicity-two-shards-one-through-three.md)
- [`docs/299-side-seven-cycle52-radius-three-support-twenty-multiplicity-two-shards-four-through-seven.md`](../docs/299-side-seven-cycle52-radius-three-support-twenty-multiplicity-two-shards-four-through-seven.md)
- [`docs/306-side-seven-cycle52-radius-three-support-twenty-multiplicity-two-shards-eight-through-fifteen.md`](../docs/306-side-seven-cycle52-radius-three-support-twenty-multiplicity-two-shards-eight-through-fifteen.md)
- [`docs/309-side-seven-cycle52-radius-three-support-twenty-multiplicity-two-shards-sixteen-through-twenty-three.md`](../docs/309-side-seven-cycle52-radius-three-support-twenty-multiplicity-two-shards-sixteen-through-twenty-three.md)
- [`docs/300-low-multiplicity-bottom-triple-cover-certificates.md`](../docs/300-low-multiplicity-bottom-triple-cover-certificates.md)
- [`scripts/measure_product_side_seven_tier_shard.cpp`](../scripts/measure_product_side_seven_tier_shard.cpp)
- [`scripts/measure_product_side_seven_bottom_certificate_dictionary.cpp`](../scripts/measure_product_side_seven_bottom_certificate_dictionary.cpp)
- [`scripts/measure_product_side_seven_bottom_triple_cover.cpp`](../scripts/measure_product_side_seven_bottom_triple_cover.cpp)
- [`scripts/verify_product_side_seven_signature_histogram.cpp`](../scripts/verify_product_side_seven_signature_histogram.cpp)
- `scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard22.cpp` through `...shard35.cpp`
- `scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp`
- `scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard1.cpp` through `...shard23.cpp`

## Immediate frontier

1. Continue multiplicity-two classification from global case `240` in fixed ten-signature proof shards.
2. Measure and minimize explicit bottom-permutation triple covers, then combine them with assumption-minimized top nogoods.
3. Audit repeated metric patterns for a symmetry quotient or direct two-candidate obstruction certificate.
4. Defer the `26,579` multiplicity-one signatures until the multiplicity-two cost model and certificate structure are understood.
5. Continue the independent finite-range bridge below `10^2874`, complete non-affine double-coset recursion searches, and global repair/resampling work.
6. Keep every finite result explicitly separated from an all-`n` claim.

## Verification

```bash
for shard in $(seq 22 35); do
  source="scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard${shard}.cpp"
  binary="/tmp/m3s${shard}"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done

g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_signature_histogram.cpp \
  -o /tmp/side-seven-histogram
/tmp/side-seven-histogram

for source in \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_pilot10.cpp \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity2_shard{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23}.cpp; do
  binary="/tmp/$(basename "$source" .cpp)"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```
