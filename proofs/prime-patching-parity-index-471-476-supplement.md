# Prime-patching parity index supplement: `docs/471--476`

This supplement continues the cumulative parity index after `docs/470`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cev--PP3cex | Robust marker controllers with shared global resources form one rational LP; basic policies have bounded randomization excess and infeasibility has resource-priced separators | PROVED | `docs/471-budget-coupled-robust-marker-controllers.md` |
| PP3cey--PP3cfa | Outer Hall-color codes and inner marker codes concatenate with product distance, exact error--erasure privacy, and finite blockwise witnesses | PROVED | `docs/472-concatenated-error-erasure-tags-for-hall-colors.md` |
| PP3cfb--PP3cfd | Threshold dual bases form a rational value fan with exact path transport, zero value monodromy, and finite wall-cycle consistency audits | PROVED | `docs/473-monodromy-free-value-transport-on-threshold-basis-fans.md` |
| PP3cfe--PP3cfg | Multiplicity-state prefix-code optima lift constructively to labeled codes; all labeled optima satisfy an exact binomial split-count recurrence | PROVED | `docs/474-lifting-and-counting-optimal-quotient-prefix-codes.md` |
| PP3cfh--PP3cfj | Shell critical cycles admit a rational attenuation LP, a fractional cycle-packing dual, and a finitely terminating exact cutting-plane oracle | PROVED | `docs/475-cutting-plane-elimination-of-shell-critical-cycles.md` |
| PP3cfk--PP3cfm | Multioutput interaction expansion has exact budgeted Pareto frontiers, minimum-work tolerance certificates, and unsupported tradeoff witnesses | PROVED | `docs/476-pareto-frontiers-for-multioutput-interaction-expansion.md` |

## Frontier update

### Boundary recleaning

Robust local marker decisions may now share global resources.  The complete
controller remains one finite rational LP.  If `M` non-simplex inequalities are
active at a basic solution, the total randomization excess is at most `M`.
Failure returns scenario, potential, and resource prices.  The stored fixture has
unique policy `(1/3,1/2)` under budget `5/6`; budget `4/5` fails by margin `1/30`.

### Localized Hall transport

An outer proper-color code and a locally realizable inner marker code compose
with distance at least `delta_out delta_in`.  Hence `2t+e` below that product
preserves exact private load, and general list ambiguity `L` gives load `L/d`.
The stored 25-color concatenated code has length eight, distance six, and passes
28,825 exact corrupted observations.

### Fractional direct-clean layers

The threshold optimum now has a global rational value atlas.  Exact affine
increments telescope along every polygonal route, so closed loops have zero
value monodromy even when degenerate basis labels change.  The stored four-cell
fan visits all cells and has exact closed integral zero.

### Support-chord repair words

A quotient optimum now reconstructs an explicit labeled prefix code.  The exact
number of labeled optimizers obeys a binomial split recurrence.  The stored
`(3,3,2)` multiplicity instance has 47 quotient states, optimum `1/4`, and 2,304
optimal labeled codes.

### Clean-macro shells

Critical-cycle removal is now a finite cutting-plane procedure.  Edge
attenuations solve a rational covering LP, while the dual fractionally packs
cycles into edge costs.  The stored three-cycle fixture ends at attenuation
`(1/2,1/2,1/2)` with matching primal and dual cost `3/2`.

### Integration

Multioutput interaction expansion now keeps the complete nondominated error
frontier.  This detects unsupported Pareto points missed by every weighted sum.
The stored budget-three frontier contains `(11/20,11/20)`, the unique vector
meeting tolerance `(3/5,3/5)`, while the budget-two frontier certifies
impossibility.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_471_476.py
```

or individually with

```bash
python scripts/check_budget_coupled_robust_marker_controllers.py
python scripts/check_concatenated_hall_color_tags.py
python scripts/check_threshold_value_monodromy.py
python scripts/check_quotient_code_reconstruction.py
python scripts/check_shell_cycle_cutting_plane.py
python scripts/check_multioutput_interaction_pareto.py
```

The local audits verify the unique resource-coupled controller, 28,825 corrected
concatenated tag observations, exact zero monodromy on a four-cell fan, 2,304
labeled optimal code lifts, a matching shell covering/packing pair, and an
unsupported multioutput interaction Pareto point.

The next available theorem identifier is `PP3cfn`.
