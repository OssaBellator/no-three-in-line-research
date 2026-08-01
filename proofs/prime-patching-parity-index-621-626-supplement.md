# Prime-patching parity index supplement: `docs/621--626`

This supplement continues the cumulative PP3 index after `docs/620`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cwd--PP3cwf | The correction-budget-seven boundary state has explicit eighth and ninth corrected transitions and no budget-seven tenth transition | PROVED | `docs/621-budget-seven-corrected-boundary-chain.md` |
| PP3cwg--PP3cwi | Three matching-shaped restrictions plus one cell have a sharp six-resource completion threshold, with auxiliary extraction criteria | PROVED / CONDITIONAL INTERFACE | `docs/622-sharp-three-matching-hall-reserve-threshold.md` |
| PP3cwj--PP3cwl | Every nearest legal threshold target has six shortest two-swap source paths, all through illegal visible intermediates, completing the candidate matrix-level source path | PROVED / FINITE REDUCTION | `docs/623-atomic-two-swap-generation-of-threshold-trades.md` |
| PP3cwm--PP3cwo | Maximal-run counts give the exact retained-anchor price; an integer-parabola source realizes the incidences, while the internal nineteen-cell reservoir fails on a positive fraction | PROVED / CONDITIONAL SOURCE MODEL | `docs/624-retained-anchor-reservoir-price.md` |
| PP3cwp--PP3cwr | The unique optimal small odd shell column is `(1,1,1)`, giving twelve active controls and a zero-buffer period | PROVED / CONDITIONAL SOURCE COLUMN | `docs/625-binary-odd-shell-column-frontier.md` |
| PP3cws--PP3cwu | Candidate coverage is `25/30`, fixture arithmetic slack remains positive, and no geometric row is promoted | PROVED | `docs/626-repeated-transition-source-generation-evidence-gate.md` |

## Frontier update

### Boundary recleaning

The corrected path reaches nine blocks. The eighth step has seven attempts of
transversal number at most five and twenty-one minimum transversals; the ninth
has sixteen and 120. Explicit seven-point corrections close both steps. At the
tenth step only `(P2,-32)` and `(P3,-32)` have minimum transversal at most five,
and neither admits a row-column-preserving correction within budget seven.

### Localized Hall transport

Three matching-shaped restrictions plus one arbitrary cell are always
completable on six residual resources per side, sharply; five fail through a
forbidden `K_3,3` decomposed into three matchings. A conditioned local pair
therefore needs eight total resources per side and matching-shaped partner,
source, and host-defect restrictions.

Auxiliary bad-vertex and bounded-degree audits give sufficient larger-pool
conditions for extracting this sharp core. Those bounds are source interfaces,
not replacements for the canonical six-resource theorem.

### Fractional direct-clean layers

Every nearest legal degree-four target has exactly six shortest paths of two
conservative `2x2` swaps, for forty-eight paths total. They use twenty distinct
nonnegative margin-preserving intermediates, none geometrically legal. This
completes the candidate matrix-generation field while reducing geometry to one
atomic two-swap compound.

### Support-chord repair words

The selected profile has aggregate `1212286655580` maximal unary runs, mean
`209/29`. Two retained anchors per run require aggregate `2424573311160`, mean
`418/29`, and at most twenty-two cells. The internal nineteen-cell source fails
on `4858898044` trees, proportion `289/10005`.

An explicit integer-parabola source realizes the anchor incidences for all 1,024
run compositions with distinct rows and columns and zero mixed-run triples. It
is not the saturated PP3 source.

### Clean-macro shells

Among all feasible nonnegative odd columns of norm at most three, `(1,1,1)` is
uniquely best. The identity

```text
2A+4B+6D=(12,10,8)
```

uses twelve active controls and eight idle slots. The word
`DABABBBDDDDDIIIIIIII` satisfies every prefix service inequality with zero
startup buffer.

### Integration

Candidate coverage rises to `25/30` because the threshold matrix-level source
path is complete. The fixture fixed point and positive slack are unchanged. All
direct rows remain fixture-derived and the evidence gate remains closed.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_621_626.py
```

or the consolidated audits individually:

```bash
python scripts/check_boundary_eighth_corrected_transition.py
python scripts/check_boundary_budget_seven_chain.py
python scripts/check_hall_bad_vertex_reserve.py
python scripts/check_hall_quantitative_reserve_extraction.py
python scripts/check_hall_three_matching_reserve_threshold.py
python scripts/check_threshold_two_swap_generation.py
python scripts/check_prefix_retained_anchor_reservoir.py
python scripts/check_prefix_parabola_source_anchors.py
python scripts/check_shell_binary_odd_column_frontier.py
python scripts/check_repeated_transition_source_generation_gate.py
```

The next available theorem identifier is `PP3cwv`.
