# Prime-patching parity and Hamilton-seed theorem index

This focused index records the current quarter-turn Hamilton seed, parity-clean
mobility, charge, and frustration frontier on
`research/all-n-prime-patching`.  These results are reductions and finite
certificates; they do not prove asymptotic prime-seed existence or the
no-three-in-line conjecture.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3bmd--PP3bme | Component-root flips sample exactly and uniformly from a clean orientation fibre; atom size is controlled by parity components | PROVED | `docs/320-parity-fibre-regeneration-forest-transition-and-m9-mobility.md` |
| PP3bmf--PP3bmg | Exact parity-fibre topology through `m=10` and owner-intersecting clean mobility through `m=9` | VERIFIED FINITELY | `docs/320-parity-fibre-regeneration-forest-transition-and-m9-mobility.md` |
| PP3bmh--PP3bmi | Fibre-randomized parity-clean macro and localization of the remaining charge loss to the Hamilton-cycle coordinate | PROVED | `docs/320-parity-fibre-regeneration-forest-transition-and-m9-mobility.md` |
| PP3bmj--PP3bmk | Exact labelled predecessor charge under fibre regeneration, including the forest-regime exponent | PROVED | `docs/321-exact-parity-fibre-action-charge-and-charge-aware-rotations.md` |
| PP3bml | Every audited clean cycle and owner triple through `m=9` has a clean owner-intersecting labelled rotation of charge at most `1/8` | VERIFIED FINITELY | `docs/321-exact-parity-fibre-action-charge-and-charge-aware-rotations.md` |
| PP3bmm | Remaining action-charge loss is cycle-coordinate concentration and label merging | PROVED / REDUCTION | `docs/321-exact-parity-fibre-action-charge-and-charge-aware-rotations.md` |
| PP3bmn--PP3bmo | Centered secant normal form and exact ray--multiplier classification of locally impossible owner pairs | PROVED | `docs/322-impossible-owner-pair-ray-classification-and-asymptotic-rarity.md` |
| PP3bmp--PP3bmq | Locally impossible compatible pairs number `O(m log m)` and vanish with probability `O(log m/m)` in a uniform Hamilton cycle | PROVED | `docs/322-impossible-owner-pair-ray-classification-and-asymptotic-rarity.md` |
| PP3bmr--PP3bms | Hosted secant incidence bound and `O(m^2 log m)` total one-XOR assignment-pair count | PROVED | `docs/323-parity-constraint-incidence-count-and-logarithmic-edge-mass.md` |
| PP3bmt--PP3bmu | A uniform Hamilton cycle has `O(log m)` expected parity-edge mass; a pair-safe `O(log m)` parity instance exists | PROVED | `docs/323-parity-constraint-incidence-count-and-logarithmic-edge-mass.md` |
| PP3bmv--PP3bmw | Exact merged fibre-column mass and weighted Hall formula for the optimal unlabelled action charge | PROVED | `docs/324-merged-fibre-charge-as-weighted-hall-transport.md` |
| PP3bmx--PP3bmy | Global mass lower bound and sufficient `Theta(m^3)` weighted expansion criterion for stationary-scale charge | PROVED / CONDITIONAL EXPANSION INTERFACE | `docs/324-merged-fibre-charge-as-weighted-hall-transport.md` |
| PP3bmz | Incremental reverse search computes exact strict-descent distance to lower potential levels | PROVED | `docs/325-exact-m8-strict-descent-horizon-and-critical-level.md` |
| PP3bna--PP3bnb | The exact `m=8` strict-descent horizon is five, with all sharp witnesses at `B_3=4` | VERIFIED FINITELY | `docs/325-exact-m8-strict-descent-horizon-and-critical-level.md` |
| PP3bnc | Repeated shortest lower-level walks give a finite bounded-horizon termination policy at `m=8` | VERIFIED FINITELY | `docs/325-exact-m8-strict-descent-horizon-and-critical-level.md` |
| PP3bnd | Signed-cycle inconsistency is supported on inconsistent fundamental chords relative to any spanning forest | PROVED | `docs/326-parity-frustration-basis-and-logarithmic-near-clean-seeds.md` |
| PP3bne | The parity frustration index equals the minimum satisfiability edge-deletion number and is at most cyclomatic rank | PROVED | `docs/326-parity-frustration-basis-and-logarithmic-near-clean-seeds.md` |
| PP3bnf | A pair-safe Hamilton cycle admits an orientation with only `O(log m)` violated owner-pair constraints | PROVED | `docs/326-parity-frustration-basis-and-logarithmic-near-clean-seeds.md` |
| PP3bng | Exact frustration distributions through `m=9`; the maximum values are `0,1,1,1,2,3` for `m=4,...,9` | VERIFIED FINITELY | `docs/326-parity-frustration-basis-and-logarithmic-near-clean-seeds.md` |
| PP3bnh | The signed-cycle frontier reduces to repair or descent of a logarithmic marked parity-edge core | PROVED / REDUCTION | `docs/326-parity-frustration-basis-and-logarithmic-near-clean-seeds.md` |

## Current exact frontier

The clean orientation coordinate can be regenerated exactly.  Pair-local
impossibility is asymptotically negligible, and a pair-safe cycle with only
`O(log m)` parity edges exists.  After the frustration-basis reduction, one can
choose an orientation with only `O(log m)` violated owner-pair constraints.

The remaining tasks are concentrated in the Hamilton-cycle coordinate:

1. repair or descend the logarithmic frustration core while retaining pair
   safety and owner-intersecting mobility;
2. prove weighted Hall expansion at the `Theta(m^3)` scale, possibly after a
   logarithmic clean trajectory;
3. control label merging and predecessor multiplicity under the chosen cycle
   kernel;
4. convert near-clean owner-pair control into atomic three-owner flaw control;
5. extend bounded-horizon descent or parity-clean mobility beyond the audited
   finite sizes.
