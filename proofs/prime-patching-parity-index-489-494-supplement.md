# Prime-patching parity index supplement: `docs/489--494`

This supplement continues the cumulative parity index after `docs/488`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cgx--PP3cgz | Rational marker controllers admit exact deterministic periodic realization, finite prefix-discrepancy bounds, and counter-schedule audits | PROVED | `docs/489-periodic-deterministic-realization-of-marker-controllers.md` |
| PP3cha--PP3chc | Linear Hall-color codes admit exact syndrome list counting, information-set bounds, reconstruction, and syndrome-controlled reverse load | PROVED | `docs/490-syndrome-dynamic-programming-for-hall-list-decoding.md` |
| PP3chd--PP3chf | Threshold value sublevels admit exact nearest-design LPs, KKT price certificates, and piecewise-affine cap and ray paths | PROVED | `docs/491-nearest-feasible-designs-on-threshold-value-fans.md` |
| PP3chg--PP3chi | Prefix-code automorphism cycle indices give simultaneous multiplicity-profile orbit inventories and canonical finite audits | PROVED | `docs/492-cycle-index-orbit-inventories-for-prefix-codes.md` |
| PP3chj--PP3chl | Compact shell attenuation LPs have exact parametric basis paths, dual cap sensitivities, and finitely generated cycle-walk certificates | PROVED | `docs/493-parametric-paths-for-shell-cycle-attenuation.md` |
| PP3chm--PP3cho | Bounded-width interaction join trees admit exact separator-indexed Pareto messages, safe local pruning, and minimum-work reconstruction | PROVED | `docs/494-bounded-width-join-tree-pareto-certificates.md` |

## Frontier update

### Boundary recleaning

Rational marker randomization can now be executed deterministically.  Each
marker state keeps a local cyclic counter whose period realizes its policy
exactly.  Full periods have zero discrepancy, while a finite prefix table
bounds every protected linear observable under arbitrary interleavings.  The
stored two-state controller uses six memory states and exact gap/resource
bounds `5/6`, `7/6`, and `5/6`.

### Localized Hall transport

Outer linear Hall-color codes can now be list-decoded by syndrome dynamic
programming.  The table has `q^r` states for parity-check rank `r`, reconstructs
a compatible color, and gives the exact surviving list size and load `L/d`.
The stored `[4,2,3]` code checks all 50,625 singleton/pair observations; the
sharp maximum list size is two.

### Fractional direct-clean layers

A nominal threshold design that violates a load cap now has an exact
minimum-change repair.  Weighted `l_1` projection is one rational LP, and
subgradient plus cap prices certify optimality.  The stored nearest design is
`(4/5,3/10)` at distance `9/20`; its diagonal feasible-ray boundary is `11/20`.

### Support-chord repair words

One cycle-index polynomial now counts symmetry classes for every risk-class
multiplicity profile on a fixed marker tree.  In the complete depth-three
binary tree, 256 assignments collapse to 21 orbits.  The binary orbit inventory
by Hamming weight is

```text
1,1,3,3,5,3,3,1,1.
```

### Clean-macro shells

Shell repairs can now be transported as one attenuation cap changes.  The
compact primal basis, dual circulation, and maximum-cycle oracle remain affine
between exact rational breakpoints.  The stored three-cycle path breaks at
`s=1/2`, with optimum slope changing from `-1` to `0`.

### Integration

Interaction compatibility now extends from chains to arbitrary bounded-width
join trees.  Pareto messages are indexed by separator assignment and work, and
dominance is used only inside a common signature.  The stored treewidth-two
audit reconstructs all 16 global assignments and proves that tolerance `(1,1)`
needs the unique work-four plan.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_489_494.py
```

or individually with

```bash
python scripts/check_periodic_marker_controller_realization.py
python scripts/check_syndrome_hall_list_decoding.py
python scripts/check_nearest_threshold_design.py
python scripts/check_prefix_code_orbit_inventory.py
python scripts/check_parametric_shell_attenuation_path.py
python scripts/check_width_two_interaction_join_tree.py
```

The local audits verify 961 marker occurrence pairs, all 50,625 syndrome list
observations, 56 parametric threshold caps, the complete 128-element tree
automorphism group, 101 shell-cap samples, and every width-two join-tree plan.

The next available theorem identifier is `PP3chp`.
