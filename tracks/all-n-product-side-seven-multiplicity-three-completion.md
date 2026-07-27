# All-n product track: side-seven multiplicity-three completion

**Branch:** `research/all-n-product-construction`

This finite stage continues the side-seven `(5,2)` radius-three support-twenty census documented through shard twenty-one and closes the entire multiplicity-three tier.

This stage does **not** prove infinite product closure or the no-three-in-line conjecture.

## Completed ledger

| Item | Status | Result |
|---|---|---|
| Shared digest verifier | **REPAIRED** | `print_sig` is now defined in the common header, so every digest wrapper compiles from a clean checkout. |
| Generic shard measurement | **COMPLETED** | `measure_product_side_seven_tier_shard.cpp` measures any canonical multiplicity interval, aborts on feasibility, and emits exact verifier constants. |
| Cases `2200`--`3543` | **CLOSED** | All `1,344` remaining signatures and all `4,032` selectors are infeasible in every orientation. |
| Multiplicity-three tier | **CLOSED** | All `3,544` signatures and `10,632` selectors are infeasible. |
| Replay certificates | **COMPLETED** | Shards 22--35 each have a standalone digest verifier. |
| Exact computation | **COMPLETED** | The new frontier used `504,772,780` bottom-CSP nodes; the cumulative certified cache uses `2,766,455,244`. |
| Finite support-twenty boundary | **ADVANCED** | `37,600` selectors are certified infeasible, one multiplicity-four selector is constructive, and `34,259` selectors remain unclassified. |
| Infinite exact closure | **OPEN** | No recursive all-side theorem follows from this finite census. |

## Canonical artifacts

- [`docs/294-side-seven-cycle52-radius-three-support-twenty-multiplicity-three-completion.md`](../docs/294-side-seven-cycle52-radius-three-support-twenty-multiplicity-three-completion.md)
- [`scripts/measure_product_side_seven_tier_shard.cpp`](../scripts/measure_product_side_seven_tier_shard.cpp)
- `scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard22.cpp`
- `...`
- `scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard35.cpp`
- [`.github/workflows/product-side-seven-frontier.yml`](../.github/workflows/product-side-seven-frontier.yml), retained as a manual replay matrix.

## Immediate frontier

1. Identify the next nonempty unclassified multiplicity tier and partition it into canonical digest shards.
2. Search that tier for constructive selectors before spending a full infeasibility census.
3. Separate host-level obstructions from selector-level obstructions so finite failures can inform a recursive product theorem.
4. Continue the independent infinite-closure work: successful cycle-type families, extension from produced bases, or a global product repair/resampling theorem.
5. Keep every finite result explicitly separated from an all-`n` claim.

## Verification

```bash
for shard in $(seq 22 35); do
  source="scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity3_shard${shard}.cpp"
  binary="/tmp/m3s${shard}"
  g++ -O3 -std=c++17 "$source" -o "$binary"
  "$binary"
done
```
