# Prime-patching parity index supplement: `docs/453--458`

This supplement continues the cumulative parity index after `docs/452`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cct--PP3ccv | Cyclic marker automata have exact nonnegative resolvent path sums, rational potential tails, and reachable dual recurrence obstructions | PROVED | `docs/453-cyclic-marker-automata-and-resolvent-certificates.md` |
| PP3ccw--PP3ccy | Proper Hall colors remain private under partial code observation according to an exact list ambiguity; distance protects against erasures | PROVED | `docs/454-erasure-resilient-color-tags-for-hall-banks.md` |
| PP3ccz--PP3cdb | Threshold-kernel bases define exact rational optimality cones, affine value regions, and localized facet or reduced-cost changes | PROVED | `docs/455-parametric-basis-regions-for-threshold-kernels.md` |
| PP3cdc--PP3cde | Unequal-symbol codes satisfy a generalized survival-Kraft bound, a finite exact risk oracle, and safe subset-DP pruning | PROVED | `docs/456-pruned-subset-search-for-unequal-symbol-codes.md` |
| PP3cdf--PP3cdh | Multiple critical shell cycles have an exact directional derivative, convex subgradient certificate, and radical-free stability face | PROVED | `docs/457-multicritical-faces-for-shell-rates.md` |
| PP3cdi--PP3cdk | Higher resolvent interactions are dominated by a finite atom automaton with potential tail bounds and localized truncation budgets | PROVED | `docs/458-interaction-automata-for-resolvent-truncation.md` |

## Frontier update

### Boundary recleaning

Marker-state sharing no longer has to be acyclic. For transition-load matrix `Q` with `rho(Q)<1`, all repeated marker walks sum exactly to

```text
B=b(I-Q)^(-1).
```

A positive potential `Qw<=qw` gives a geometric truncation tail, while a reachable nonnegative witness `zQ>=z` certifies recurrent failure.

### Localized Hall transport

Proper edge colors may be encoded by several short marker coordinates. If at most `e` coordinates are erased and at most `L_e` colors remain compatible at one target, then

```text
lambda<=L_e/d.
```

A code of minimum distance `delta` preserves exact private load `1/d` under any fewer than `delta` erasures.

### Fractional direct-clean layers

One rational threshold basis now certifies a whole polyhedral region of source masses and target capacities. Inside that region the optimum is exactly affine, with the stored dual prices giving exact finite differences. Region failure is localized to one vanishing basic variable or one zero reduced cost.

### Support-chord repair words

The unequal-symbol subset search now has a generalized Kraft lower bound. If `p_0^theta+p_1^theta=1`, every code risk satisfies

```text
R>=(sum_i rho_i^theta)^(1/theta).
```

The optimum lies in a finite leaf-risk candidate set, and this lower bound safely prunes subset splits. The stored six-bank optimum is `125/576`.

### Clean-macro shells

At a critical-cycle tie, the directional derivative of `log mu` is the maximum normalized cycle incidence in the chosen direction. The full subdifferential is the convex hull of active cycle incidences, and the tied stability face is described exactly by cross-power equalities and inequalities.

### Integration

The compatible perturbation-chain expansion now has its own interaction automaton. If `Jw<=qw`, the tail after order `m` is at most

```text
beta_0 alpha^T J^m w/(1-q).
```

Coordinatewise versions rank the perturbation atoms responsible for the remaining uncertainty.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_453_458.py
```

or individually with

```bash
python scripts/check_cyclic_marker_automata.py
python scripts/check_erasure_resilient_hall_colors.py
python scripts/check_parametric_threshold_basis_regions.py
python scripts/check_pruned_unequal_symbol_code_dp.py
python scripts/check_multicritical_shell_faces.py
python scripts/check_interaction_automaton_truncation.py
```

The local audits verify an exact cyclic marker resolvent and dual recurrence witness, all zero/one/two-erasure Hall observations, 160 parametric basis right-hand sides, all 30,240 unequal-symbol assignments with 308 safe prunes, 625 multicritical shell directions, and exact interaction tails through order three.

The next available theorem identifier is `PP3cdl`.
