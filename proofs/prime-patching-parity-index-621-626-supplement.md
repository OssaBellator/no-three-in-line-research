# Prime-patching parity index supplement: `docs/621--626`

This supplement continues the cumulative PP3 index after `docs/620`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cwd--PP3cwf | The correction-budget-seven boundary chain has a complete eighth transversal spectrum, explicit eighth and ninth corrected transitions, and no budget-seven tenth transition | PROVED | `docs/621-budget-seven-corrected-boundary-chain.md` |
| PP3cwg--PP3cwi | Three matching-shaped restrictions plus one cell have a sharp six-resource threshold, with bad-vertex and degree-bound extraction criteria | PROVED / CONDITIONAL INTERFACE | `docs/622-sharp-three-matching-hall-reserve-threshold.md` |
| PP3cwj--PP3cwl | Every nearest legal threshold target has six ordered two-swap paths, all through illegal visible intermediates, completing the candidate matrix-level source path | PROVED / FINITE REDUCTION | `docs/623-atomic-two-swap-generation-of-threshold-trades.md` |
| PP3cwm--PP3cwo | Exact maximal-run counts give the retained-anchor price; an integer-parabola source realizes the incidences, while the internal nineteen-cell reservoir fails on a positive fraction | PROVED / CONDITIONAL SOURCE MODEL | `docs/624-retained-anchor-reservoir-price.md` |
| PP3cwp--PP3cwr | The symmetric odd shell column `(1,1,1)` completes the lattice, uniquely minimizes active controls, and admits a zero-buffer period | PROVED / CONDITIONAL SOURCE COLUMN | `docs/625-binary-odd-shell-column-frontier.md` |
| PP3cws--PP3cwu | Candidate coverage is `25/30`, fixture arithmetic is unchanged, and zero global rows are promoted | PROVED | `docs/626-repeated-transition-evidence-gate.md` |

## Frontier update

### Boundary recleaning

The eighth minimum-transversal histogram is

```text
4:1, 5:6, 6:21, 7:68, 8:164,
9:2, 10:4, 11:34, 12:41, 13:107, 14:72.
```

The corrected path reaches nine blocks. Explicit seven-point corrections close
the eighth and ninth steps. At the tenth step only `(P2,-32)` and `(P3,-32)`
have minimum transversal at most five, and neither has a row-column-preserving
correction within budget seven.

### Localized Hall transport

Three partial-matching forbidden families plus one arbitrary cell are always
completable on six residual resources per side, sharply; five fail through a
forbidden `K_3,3` decomposed into three matchings. Bad-vertex counts give

```text
m >= 8 + max(b_L,b_R).
```

For three degree-two families, collision extraction needs forty-two residual
resources, or forty-four before the local pair consumes two.

### Fractional direct-clean layers

Every nearest legal degree-four target has exactly six ordered paths of two
conservative `2x2` swaps, for forty-eight paths total. They use twenty distinct
nonnegative margin-preserving intermediates, none geometrically legal. This
completes the candidate matrix-generation field and leaves one atomic geometric
compound obligation.

### Support-chord repair words

The selected profile has aggregate `1212286655580` maximal unary runs, mean
`209/29`. Two anchors per run require aggregate `2424573311160`, mean `418/29`,
and at most twenty-two cells. The internal nineteen-cell source fails on
`4858898044` trees, proportion `289/10005`.

An explicit integer-parabola source realizes the anchor incidences for all 1,024
run compositions with distinct rows and columns and zero mixed-run triples. It is
not the saturated PP3 retained source.

### Clean-macro shells

The symmetric column `(1,1,1)` completes the service lattice and has nondominated
`(uses,total controls)` points `(2,14)`, `(4,13)`, and `(6,12)`. Among all
nonnegative odd columns of norm at most three it is uniquely optimal. The word
`DABABBBDDDDDIIIIIIII` gives exact target service with zero startup buffer.

### Integration

Candidate completion rises to `25/30` because the threshold matrix-level source
path is complete. The fixture fixed point and positive slack are unchanged. All
direct rows remain fixture-derived and the evidence gate stays closed.

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
python scripts/check_prefix_retained_anchor_budget.py
python scripts/check_prefix_retained_anchor_reservoir.py
python scripts/check_prefix_parabola_source_anchors.py
python scripts/check_shell_binary_odd_column_frontier.py
python scripts/check_shell_all_cycle_odd_column.py
python scripts/check_repeated_transition_evidence_gate.py
```

The next available theorem identifier is `PP3cwv`.
