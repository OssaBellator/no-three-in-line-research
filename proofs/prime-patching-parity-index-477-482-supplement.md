# Prime-patching parity index supplement: `docs/477--482`

This supplement continues the cumulative parity index after `docs/476`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cfn--PP3cfp | Budget-coupled marker controllers admit an exact pure-action master, statewise reduced-cost pricing, and finitely terminating column generation | PROVED | `docs/477-column-generation-for-budget-coupled-marker-controllers.md` |
| PP3cfq--PP3cfs | Heterogeneous inner Hall tags have an exact weighted outer distance, block-list reverse-load transfer, and finite protection-allocation oracle | PROVED | `docs/478-weighted-concatenation-for-heterogeneous-hall-tags.md` |
| PP3cft--PP3cfv | Threshold value fans admit exact active-set point location, rational segment walks, directional derivatives, and global Lipschitz prices | PROVED | `docs/479-point-location-and-transport-in-threshold-value-fans.md` |
| PP3cfw--PP3cfy | Finite survival-preserving symmetries act on optimal prefix codes; Burnside counting and canonical orbit--stabilizer certificates are exact | PROVED | `docs/480-burnside-orbits-of-optimal-prefix-codes.md` |
| PP3cfz--PP3cgb | Shell attenuation has an exact positive-cycle separation oracle, a compact capacitated-circulation dual, and finite oracle optimality certificates | PROVED | `docs/481-positive-cycle-oracles-and-circulation-duals-for-shell-attenuation.md` |
| PP3cgc--PP3cge | Independent interaction blocks compose by exact budgeted Pareto convolution with safe dominance pruning and blockwise minimum-work witnesses | PROVED | `docs/482-blockwise-pareto-convolution-for-interaction-expansions.md` |

## Frontier update

### Boundary recleaning

Large local action catalogues now enter the global robust controller only when
they violate current dual prices.  The exact statewise pricing score is

```text
c_(u,a)-alpha_u-sum_k y_k G_(k,u,a).
```

The stored restricted master starts at `23/12`, adds two negative-reduced-cost
actions, and ends at the globally certified minimum budget `13/9`.  Budget `7/5`
fails by dual margin `2/45`.

### Localized Hall transport

Inner marker protection may vary by outer code position.  The exact guaranteed
distance is

```text
D=min_(c!=c') sum_(j:c_j!=c'_j) delta_j.
```

The stored ternary parity code has 56 admissible length allocations under budget
eight; the only optima are the three permutations of `(2,3,3)`, all with
weighted distance five.  Every one of 3,654 tested error--erasure observations
has Hall-color list size one.

### Fractional direct-clean layers

The rational threshold value atlas now has a point-location and transport oracle.
The stored six-piece fan is audited on 1,681 rational points and a segment with
exact crossings `2/5,1/2,2/3`.  Active gradients give both the one-sided
directional derivative and a global `l_infinity` Lipschitz constant two.

### Support-chord repair words

Optimal prefix codes are now quotiented by label and tree symmetries, not only by
equal-risk multiplicities.  In the stored depth-two fixture, 24 labeled optima
under a group of order 32 have Burnside fixed sum 64 and exactly two genuine
symmetry orbits, of sizes eight and sixteen.

### Clean-macro shells

A positive-cycle oracle now supplies the missing separation step for shell
cutting planes.  The dual cycle packing compresses to one nonnegative circulation
with edge capacities.  In the bidirected-triangle audit, a missed three-cycle has
residual sum `3/2`; after adding it, primal attenuation and compact circulation
both have exact value three.

### Integration

Independent interaction blocks now combine by Minkowski Pareto convolution.  The
stored three-block audit compresses 18 raw plans into frontier sizes
`1,3,3,3,2,1` over budgets zero through five.  Tolerance `(1,1)` is impossible at
budget two and has one reconstructed feasible plan at budget three.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_477_482.py
```

or individually with

```bash
python scripts/check_column_generated_marker_controllers.py
python scripts/check_heterogeneous_concatenated_hall_tags.py
python scripts/check_threshold_value_fan_point_location.py
python scripts/check_prefix_code_burnside_orbits.py
python scripts/check_shell_cycle_separation_and_circulation.py
python scripts/check_blockwise_interaction_pareto_convolution.py
```

The local audits verify two generated controller columns, 3,654 heterogeneous tag
observations, 1,681 exact value-fan point locations, the complete 32-element code
symmetry action, all five simple shell cycles with a compact circulation dual,
and exact convolution of all 18 blockwise interaction plans.

The next available theorem identifier is `PP3cgf`.
