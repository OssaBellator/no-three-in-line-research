# Prime-patching parity index supplement: `docs/483--488`

This supplement continues the cumulative parity index after `docs/482`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cgf--PP3cgh | Robust marker synthesis admits simultaneous action pricing and scenario separation, with exact finite double-oracle termination | PROVED | `docs/483-double-oracle-generation-for-robust-marker-controllers.md` |
| PP3cgi--PP3cgk | Inner marker lists transfer exactly to outer Hall-color lists; information sets and distance give finite reverse-load bounds and sharp witnesses | PROVED | `docs/484-block-list-decoding-for-hall-color-tags.md` |
| PP3cgl--PP3cgn | Threshold value caps define rational inverse-design polyhedra with finite value-cut generation, dual prices, and exact ray boundaries | PROVED | `docs/485-inverse-design-on-threshold-value-fans.md` |
| PP3cgo--PP3cgq | Recursive tree automorphisms and cycle-index coefficients count optimal prefix-code orbits exactly without listing every labeled schedule | PROVED | `docs/486-recursive-cycle-index-counting-for-prefix-codes.md` |
| PP3cgr--PP3cgt | Additive shell cycle constraints are equivalent to a compact vertex-potential LP, with circulation duality and exact maximum-cycle-mean separation | PROVED | `docs/487-potential-compactification-of-shell-cycle-constraints.md` |
| PP3cgu--PP3cgw | Interaction systems on a factor tree admit exact separator-indexed Pareto messages, safe local pruning, and minimum-work reconstruction certificates | PROVED | `docs/488-tree-decomposed-pareto-messages-for-interactions.md` |

## Frontier update

### Boundary recleaning

The robust marker controller now generates both missing actions and missing
adversarial scenarios.  A restricted rational master is globally certified when
all omitted action reduced costs and all omitted scenario gaps are nonnegative.
The stored trace adds two scenarios and two actions before reaching value `5`
with policy `(0,1/2,1/2,0)`.

### Localized Hall transport

Inner geometric blocks may return symbol lists.  Their exact Cartesian
compatibility set is filtered through the outer Hall-color code.  Any information
set `I` gives list bound

```text
L <= product_(j in I) |L_j|,
```

and the reverse load is `L/d`.  The stored Reed--Solomon audit checks all `50,625`
singleton/pair list observations and all `2,825` true-color observations with at
most two ambiguous blocks.

### Fractional direct-clean layers

Threshold value fans now support inverse design under a load cap.  Each active
affine value piece becomes one rational cut.  The stored problem adds two cuts,
ends at `(9/20,1/2)`, and has matching dual prices `50,51`; its exact diagonal ray
boundary is `7/15`.

### Support-chord repair words

Recursive marker-tree symmetries now have a cycle-index count.  Fixed assignments
are coefficients of a product determined only by automorphism cycle lengths.  In
the complete depth-three tree, 70 balanced assignments under 128 automorphisms
have Burnside fixed sum 640 and five genuine schedule orbits.

### Clean-macro shells

Every additive shell cycle family now has the compact potential form

```text
h_v-h_u >= b_e-sum_r a_(e,r)x_r.
```

A positive maximum cycle mean is the exact obstruction.  The stored bidirected
triangle has trial violation `3/2`, compact primal optimum `3`, and matching
circulation dual value `3`.

### Integration

Interaction blocks may now share finite separator states.  Exact Pareto messages
are indexed by separator signature and work, with dominance pruning only inside a
common signature.  The stored width-one chain has nine compatible plans;
tolerance `(8/5,5/4)` is impossible at budget three and has the unique plan
`B--F--I` at budget four.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_483_488.py
```

or individually with

```bash
python scripts/check_double_oracle_marker_controllers.py
python scripts/check_block_list_hall_decoding.py
python scripts/check_threshold_inverse_design.py
python scripts/check_recursive_prefix_code_orbits.py
python scripts/check_shell_potential_compactification.py
python scripts/check_tree_decomposed_interaction_pareto.py
```

The local audits verify a four-addition double-oracle trace, all 50,625 block-list
observations, a two-cut inverse-design optimum, the complete 128-element recursive
tree group, all five simple shell cycles with compact primal--dual certificates,
and exact width-one Pareto messages at every budget through eight.

The next available theorem identifier is `PP3cgx`.
