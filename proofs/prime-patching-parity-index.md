# Prime-patching parity and Hamilton-seed theorem index

This focused index records the quarter-turn Hamilton seed, parity-clean mobility,
charge, frustration, and clean-macro frontier on
`research/all-n-prime-patching`. These results are reductions and finite
certificates; they do not prove asymptotic prime-seed existence or the
no-three-in-line conjecture.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3bmd--PP3bme | Component-root flips sample exactly from a clean orientation fibre; atom size is controlled by parity components | PROVED | `docs/320-parity-fibre-regeneration-forest-transition-and-m9-mobility.md` |
| PP3bmf--PP3bmg | Exact parity-fibre topology through `m=10` and owner-intersecting clean mobility through `m=9` | VERIFIED FINITELY | `docs/320-parity-fibre-regeneration-forest-transition-and-m9-mobility.md` |
| PP3bmh--PP3bmi | Fibre-randomized clean macro and localization of charge loss to the Hamilton-cycle coordinate | PROVED | `docs/320-parity-fibre-regeneration-forest-transition-and-m9-mobility.md` |
| PP3bmj--PP3bmk | Exact labelled predecessor charge under fibre regeneration, including the forest exponent | PROVED | `docs/321-exact-parity-fibre-action-charge-and-charge-aware-rotations.md` |
| PP3bml--PP3bmm | Charge-aware rotations through `m=9`; residual loss is cycle concentration and label merging | PROVED / VERIFIED FINITELY | `docs/321-exact-parity-fibre-action-charge-and-charge-aware-rotations.md` |
| PP3bmn--PP3bmq | Centered secant normal form, impossible-pair classification, `O(m log m)` count, and rarity | PROVED / VERIFIED FINITELY | `docs/322-impossible-owner-pair-ray-classification-and-asymptotic-rarity.md` |
| PP3bmr--PP3bmu | Hosted incidence bound, `O(m^2 log m)` one-XOR pairs, logarithmic edge mass, and sparse pair-safe cycle | PROVED / VERIFIED FINITELY | `docs/323-parity-constraint-incidence-count-and-logarithmic-edge-mass.md` |
| PP3bmv--PP3bmy | Exact merged-column formula, weighted Hall optimum, global lower bound, and expansion criterion | PROVED | `docs/324-merged-fibre-charge-as-weighted-hall-transport.md` |
| PP3bmz--PP3bnc | Incremental descent search and exact five-step strict-descent horizon at `m=8` | PROVED / VERIFIED FINITELY | `docs/325-exact-m8-strict-descent-horizon-and-critical-level.md` |
| PP3bnd--PP3bnh | Frustration basis, deletion core, logarithmic near-clean seed, and exact audit through `m=9` | PROVED / VERIFIED FINITELY | `docs/326-parity-frustration-basis-and-logarithmic-near-clean-seeds.md` |
| PP3bni--PP3bnk | One-step pair-safe frustration descent, marked-edge targeting, and finite termination through `m=9` | VERIFIED FINITELY | `docs/327-pair-safe-frustration-strict-descent-through-m9.md` |
| PP3bnl--PP3bnp | Sharp `m=8` witnesses, implicit clean-macro graph, and three-step complete reachability | PROVED / VERIFIED FINITELY | `docs/328-m8-critical-witnesses-and-parity-clean-macro-graph.md` |
| PP3bnq--PP3bnu | Exact `m=10` frustration census, direct clean repair, connected clean graph, and marked-core targeting | VERIFIED FINITELY | `docs/329-m10-pair-safe-frustration-repair-and-clean-mobility.md` |
| PP3bnv--PP3bny | Fibre-weighted Metropolis kernel, exact heat-kernel charge, spectral bound, and pointwise endpoint | PROVED | `docs/330-clean-cycle-heat-kernel-charge-and-fibre-weighted-metropolis-chain.md` |
| PP3bnz--PP3boa | Through `m=9`, every minimum signed state and every marked violated edge has a strict-descent rotation with zero sign changes | VERIFIED FINITELY | `docs/331-local-sign-coupled-parity-repair-through-m10.md` |
| PP3bob--PP3bod | At `m=10`, 74 fixed-sign exceptions remain, but every signed state and marked edge has direct clean repair using at most two sign changes on the rotated owners | VERIFIED FINITELY | `docs/331-local-sign-coupled-parity-repair-through-m10.md` |
| PP3boe | All `6,727,728` parity-clean signed states at `m=9` reach validity within four clean macro steps | VERIFIED FINITELY | `docs/332-exact-m9-clean-macro-reachability-and-sparse-collateral-cores.md` |
| PP3bof | Exact terminal owner-cover censuses at `m=8` and `m=9` | VERIFIED FINITELY | `docs/332-exact-m9-clean-macro-reachability-and-sparse-collateral-cores.md` |
| PP3bog--PP3boh | Raw support and atomic counts have local minima; the 68 distance-four joint minima reduce to sparse one-to-three-support collateral cores | VERIFIED FINITELY | `docs/332-exact-m9-clean-macro-reachability-and-sparse-collateral-cores.md` |
| PP3boi | Exact weighted Hall transport for every atomic signed-assignment flaw through `m=7` | VERIFIED FINITELY | `docs/333-exact-small-size-weighted-hall-transport.md` |
| PP3boj | Proper Hall bottlenecks are common by `m=7`, with at most a `1.696` finite label-merging penalty | VERIFIED FINITELY | `docs/333-exact-small-size-weighted-hall-transport.md` |
| PP3bok | The worst audited optimal charge is at most `4.422/m^3` through `m=7` | VERIFIED FINITELY | `docs/333-exact-small-size-weighted-hall-transport.md` |

## Current exact frontier

The parity coordinate is no longer merely globally reoptimizable in the audited
range. Through `m=9`, an optimal orientation can be retained unchanged during
strict frustration descent. At the first nonforest size `m=10`, all 74 fixed-sign
exceptions are repaired by changing at most two signs, both among the three
rotated owners. Every selected minimum-core edge remains targetable.

Complete clean-macro reachability now holds through `m=9`:

```text
m=8: maximum macro distance 3,
m=9: maximum macro distance 4.
```

At `m=9`, 68 distance-four states are simultaneous local minima for support and
atomic defect counts. They have only one to three flaw supports and form a sparse
collateral-repair core; eight single-support states require the full four-step
route to validity.

Exact one-step weighted transport through `m=7` remains on the cubic stationary
scale. Proper Hall bottlenecks already occur frequently, but the worst absolute
charge is still attained by a global source-set cut.

## Remaining tasks

1. Prove bounded local-sign repair for the asymptotic `O(log m)` frustration core.
2. Classify and repair the eight one-support four-step clean-macro states by a
   uniform collateral word or structural Lyapunov function.
3. Extend compressed clean-macro reachability to `m=10` without storing all
   `115,586,396` clean orientations.
4. Replace subset enumeration at `m=8` by exact parametric min-cut and seek a
   uniform weighted expansion bound.
5. Combine locally coupled repair and heat-kernel mixing with atomic three-owner
   drift and the trajectory-local causal light cone.

The next available theorem identifier is `PP3bol`.
