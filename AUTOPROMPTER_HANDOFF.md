# Autoprompter continuity handoff

Checkpoint date: 2026-08-01 Australia/Melbourne

## Goal

Develop a rigorous all-`n` prime-patching route for the no-three-in-line research
program across six linked frontiers:

1. boundary recleaning / marker-controller realization;
2. localized Hall transport and list decoding;
3. fractional direct-clean threshold layers;
4. support-chord repair words and constrained prefix codes;
5. clean-macro shell attenuation and scheduling;
6. global interaction/integration certificates.

The asymptotic all-`n` theorem remains open.  The repository contains exact
finite reductions, conditional interfaces, bounded corrected chains, matrix-level
operation reductions, and explicit auxiliary sources; none is an all-length
proof.

## Current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Branch: `research/all-n-prime-patching`
- Verified pre-checkpoint research head: `fc31bed09ed9274993025b371ca2390c590e0da3`.
- Pre-checkpoint title: `Finalize consolidated parity index at 25 of 30`.
- The branch was remotely verified identical to that commit before this refresh.
- Next available theorem identifier: `PP3cwv`.

## Completed canonical tranche: `docs/621--626`

### Boundary — `docs/621-budget-seven-corrected-boundary-chain.md`

Theorems `PP3cwd--PP3cwf`.

- From the corrected seven-block state, the exact eighth minimum-transversal
  spectrum through size six is `4:1, 5:6, 6:21, >6:492`.
- The seven attempts of minimum size four or five have twenty-one minimum
  transversals.
- One seven-point degree-preserving correction gives a legal sixty-four-point
  eight-block state.
- The ninth census has sixteen attempts of minimum transversal at most five and
  120 minimum transversals.
- One seven-point correction gives a legal seventy-two-point nine-block state.
- At the tenth step only `(P2,-32)` and `(P3,-32)` remain at minimum at most five;
  neither admits a degree-preserving correction within budget seven.
- This is a bounded radius-32 path, not a periodic or all-offset construction.

### Hall — `docs/622-sharp-three-matching-hall-reserve-threshold.md`

Theorems `PP3cwg--PP3cwi`.

- In residual `K_{6,6}`, deleting three partial matchings and one arbitrary edge
  always leaves a perfect matching.
- Five residual resources are insufficient, sharply, through a forbidden
  `K_{3,3}` decomposed into three cyclic matchings.
- If `b_L,b_R` are bad-resource counts after selecting the local pair, six good
  residual resources per side exist whenever
  `m >= 8 + max(b_L,b_R)`.
- For `k` forbidden families of maximum degree `Delta`, a matching-shaped reserve
  of size `r` is extracted whenever
  `N >= r(1+2k*C(Delta,2))`.
- For three degree-two families and reserve six, forty-two residual resources
  suffice, or forty-four resources before the pair consumes two.
- The asymptotic host has not yet been shown to satisfy either source condition.

### Threshold — `docs/623-atomic-two-swap-generation-of-threshold-trades.md`

Theorems `PP3cwj--PP3cwl`.

- Each of the eight nearest legal degree-four targets has exactly six ordered
  length-two conservative-swap paths.
- The forty-eight paths use twenty distinct nonnegative, margin-preserving
  intermediate matrices.
- None of those intermediates decomposes into four legal no-three-in-line layers.
- The matrix-level source path is complete, so the threshold candidate rises to
  `5/5`.
- The remaining geometric obligation is an atomic two-swap compound that never
  exposes an illegal intermediate schedule.

### Prefix — `docs/624-retained-anchor-reservoir-price.md`

Theorems `PP3cwm--PP3cwo`.

- At size thirty with nine binary nodes, aggregate maximal unary-run count is
  `1212286655580`, mean `209/29`.
- Two anchors per run require aggregate `2424573311160`, mean `418/29`, with
  worst case twenty-two.
- The internal nineteen-cell source fails under one-cell-one-anchor supply on
  `4858898044` trees, proportion `289/10005`.
- An explicit integer-parabola source realizes all 1,024 ordered run compositions
  with distinct rows and columns, zero mixed-run triples, and maximum coordinate
  magnitude `40802`.
- One deleted anchor per run clears all anchor-pair blockers on that run line.
- The parabola source is not the saturated two-per-row/two-per-column PP3 source.

### Shell — `docs/625-binary-odd-shell-column-frontier.md`

Theorems `PP3cwp--PP3cwr`.

- The symmetric odd column `D=(1,1,1)` completes the integer service lattice.
- Its nondominated `(uses,total active controls)` frontier for target `(12,10,8)`
  is `(2,14)`, `(4,13)`, and `(6,12)`.
- Among all thirteen feasible nonnegative odd columns of `l_1` norm at most three,
  `D` uniquely attains twelve active controls.
- The word `DABABBBDDDDDIIIIIIII` gives exact target service with startup buffer
  `(0,0,0)` and eight idle slots.
- No geometric clean macro realizing `D` is known.

### Integration — `docs/626-repeated-transition-evidence-gate.md`

Theorems `PP3cws--PP3cwu`.

- Candidate completion is `25/30`:
  boundary `4/5`, Hall `4/5`, threshold `5/5`, prefix `5/5`, shell `5/5`,
  integration `2/5`.
- The fixture fixed-point total remains
  `705466760524005697/3623878655999606784`.
- Positive slack below one quarter remains
  `200502903475895999/3623878655999606784`.
- All six actual rows remain `fixture_derived`; zero rows are promoted and
  geometric closure remains false.

## Machine-readable and reproducibility files

- `certificates/prime-patching-repeated-transitions-621-626.json`
- `scripts/check_boundary_eighth_corrected_transition.py`
- `scripts/check_boundary_budget_seven_chain.py`
- `scripts/check_hall_bad_vertex_reserve.py`
- `scripts/check_hall_quantitative_reserve_extraction.py`
- `scripts/check_hall_three_matching_reserve_threshold.py`
- `scripts/check_threshold_two_swap_generation.py`
- `scripts/check_prefix_retained_anchor_budget.py`
- `scripts/check_prefix_retained_anchor_reservoir.py`
- `scripts/check_prefix_parabola_source_anchors.py`
- `scripts/check_shell_binary_odd_column_frontier.py`
- `scripts/check_shell_all_cycle_odd_column.py`
- `scripts/check_repeated_transition_evidence_gate.py`
- `scripts/check_frontier_621_626.py`
- `proofs/prime-patching-parity-index-621-626-supplement.md`

Latest group command:

```bash
python scripts/check_frontier_621_626.py
```

## Validation status

- All new standalone diagnostics and Python compilation passed earlier in this
  tranche before commit.
- A fresh split validation reconfirmed the Hall, threshold, prefix, and shell
  diagnostics and their Python compilation.
- A fresh monolithic boundary rerun exceeded the isolated execution window while
  reconstructing the heavy corrected state; it produced no fresh completed
  boundary result.  The previously completed boundary audit remains the stored
  validation basis.
- The complete historical chained runner was not executed locally because the
  isolated runtime does not contain a full repository checkout; the group runner
  begins with `scripts/check_frontier_615_620.py`.
- Overlapping concurrent drafts were reconciled into the six canonical theorem
  paths above.  The runner, certificate, parity index, and handoff use `25/30`.

## Current blockers

- Boundary: no budget-seven tenth transition; larger budget, wider offsets,
  noncanonical cores, or a periodic corrected-state component are missing.
- Hall: no asymptotic derivation of the bad-vertex or degree-two reserve bounds.
- Threshold: every two-swap path exposes an illegal intermediate; no atomic
  geometric compound is known.
- Prefix: the explicit parabola reservoir is not the saturated PP3 source, while
  the internal nineteen-cell reservoir fails on a positive fraction.
- Shell: the exact zero-buffer odd column has no clean-macro realization or
  collateral-interaction cost bound.
- Integration: all actual rows and coupling coefficients remain fixture-derived.

## Exact next steps

1. Verify this handoff and continue theorem numbering at `PP3cwv`.
2. Build `docs/627--632` around escaping the boundary correction-budget stop and
   realizing actual geometric source operations.
3. Boundary: enumerate tenth-step corrections at budget eight over every minimum
   core; then widen offsets or search for a corrected-state cycle.
4. Hall: derive the six-resource interface from one asymptotic superregular host,
   using the bad-vertex or degree-two extraction bounds where applicable.
5. Threshold: realize an atomic two-swap compound on actual source cells while
   keeping every exposed state legal, or prove an invariant excluding it.
6. Prefix: embed or simulate the parabola anchor reservoir inside a saturated PP3
   source and charge the one-deletion-per-run credit.
7. Shell: construct a clean macro with incidence `(1,1,1)` and audit its
   zero-buffer schedule, collateral interactions, and unit cost.
8. Integration: promote only rows with complete coordinate source paths;
   otherwise preserve the closed gate and unchanged fixed point.
9. Run diagnostics, Python compilation, the chained runner in a complete checkout,
   verify the remote head, and refresh this handoff.

## Conventions

Continue on `research/all-n-prime-patching`; use exact arithmetic and reviewable
commits; keep candidate completion separate from geometric evidence; preserve the
six-frontier structure; store a checker and certificate for each tranche; and
state explicitly that the all-`n` theorem remains open.
