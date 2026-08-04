# Autoprompter continuity handoff

Checkpoint time: 2026-08-04T23:14:00+10:00 Australia/Melbourne

## Goal

Develop a rigorous all-`n` prime-patching route across boundary, Hall, threshold,
prefix, shell, and integration frontiers. The all-`n` theorem remains open.
Finite corrected chains and algebraic obstructions are not all-length coordinate
constructions.

## Current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Branch: `research/all-n-prime-patching`
- Canonical completed tranches through `docs/687--692`.
- Current boundary-heavy tranche: `docs/693--699`.
- Completed in the current tranche: `docs/693--696`.
- Current theorem range: `PP3del--PP3dew`.
- Next theorem identifier: `PP3dex`.

## Corrected boundary chain

The stale nineteenth snapshot point `(42,193)` has been replaced by the certified
predecessor point `(42,378)`. The reconstructed 144-point state passes the full
no-three audit.

### `docs/693-corrected-nineteenth-boundary-transition.md`

Theorems `PP3del--PP3den`.

- Correct raw nineteenth histogram:
  `4:2,5:9,6:47,7:175,8:283,9:3,10:16,11:63,12:121,13:176,14:137`.
- Minimum-four attempts are `P1/-33` with one core and `P2/-64` with five.
- All six cores reject preserving corrections through budget six; budget seven is
  sharp and two `P2/-64` cores repair there.
- Correct low frontier totals are 58 attempts and 495 cores at transversal at
  most six.

### `docs/694-alternative-boundary-continuation-through-twenty-one-blocks.md`

Theorems `PP3deo--PP3deq`.

- The second `P2/-64` budget-seven repair is selected because its raw twentieth
  low frontier contains 90 attempts at transversal at most six, versus 97 for the
  first repair.
- Raw twentieth histogram:
  `4:2,5:14,6:74,7:199,8:227,9:2,10:23,11:91,12:160,13:149,14:91`.
- `P3/-27` core 6 first repairs at budget six, producing a 160-point,
  twenty-block state.
- Raw twenty-first histogram:
  `4:3,5:11,6:63,7:184,8:255,9:3,10:13,11:51,12:117,13:180,14:152`.
- Eleven of 33 minimum-four cores repair at budget six. Comparing every repaired
  state selects `P3/60` core 8.
- The selected endpoint has 168 points and twenty-one blocks, with raw
  twenty-second histogram
  `6:26,7:205,8:285,9:1,10:3,11:38,12:100,13:199,14:175`.
- The minimum-six frontier contains 26 attempts and 178 cores.

### `docs/695-twentysecond-boundary-budget-six-obstruction.md`

Theorems `PP3der--PP3det`.

- Every one of the 178 minimum-six cores rejects every preserving correction at
  deletion budget six.
- Matching-count histogram per core: `180:49,360:92,720:37`.
- The complete layer contains 68,580 rejected replacement permutations and zero
  repairs. Budget seven remains open.

## Threshold all-width obstruction

### `docs/696-threshold-all-window-widths.md`

Theorems `PP3deu--PP3dew`.

- For every rolling width, a forced-alphabet window is legal exactly when it
  contains no identity layer. The score is `-2` times the identity count, while
  legal-layer sums have nonnegative score.
- A cycle of `K` minimum batches has `3K` identity positions and `5K`
  nonidentity positions. The exact maximum number of legal width-`w` windows is
  `max(0,5K-w+1)`.
- For every fixed width the optimal asymptotic legal density remains `5/8`.
- For linearly growing width `w=rho*K`, the limiting upper density is
  `max(0,(5-rho)/8)`.
- Wider rolling memory therefore cannot conceal the forced identity mass; progress
  requires a different alphabet or a genuinely unexposed operation.

## Reproducibility

Boundary:

- `scripts/check_boundary_nineteenth_transition.py`
- `scripts/boundary_spectrum_kernel.cpp`
- `scripts/boundary_exact_cover_kernel.cpp`
- `scripts/boundary_legacy_correction_kernel.cpp`
- `scripts/check_boundary_continuation_694.py`
- `scripts/check_boundary_twentyfirst_selection_694.py`
- `scripts/check_boundary_twentysecond_budget_six_obstruction_695.py`
- `scripts/check_frontier_693_695.py`
- `certificates/prime-patching-boundary-continuation-694.json`

Threshold:

- `scripts/check_threshold_all_window_widths.py`
- `scripts/check_frontier_693_696.py`

The canonical boundary path, eleven-repair comparison, and twenty-second
budget-six obstruction all passed in isolated execution. The threshold checker
contains direct finite censuses for widths one through sixteen, identity-position
censuses for `K=1,2,3`, and the general score/gap proof. The complete historical
chain was not run end-to-end because a full checkout remains unavailable.

## Integration status

- Candidate completion remains `25/30`.
- All actual rows remain `fixture_derived`; no row is promoted.
- Fixed-point total remains
  `705466760524005697/3623878655999606784`.
- Slack below one quarter remains
  `200502903475895999/3623878655999606784`.
- Geometric closure is false and the all-`n` theorem remains open.

## Decisions

- Reconstruct copied boundary states from certified predecessors.
- Select finite continuation states by exact next-frontier spectra.
- Treat the 21-block chain as finite evidence only.
- Treat the all-width threshold result as an obstruction, not a hidden operation.
- Do not promote Hall without an explicit coordinate packet.
- Do not promote the incomplete prefix four-run computation; it exceeded the
  practical execution window and produced no certified result.
- Promote no row without a complete recurrent coordinate path.

## Current blockers

- Boundary: budget seven for the 178 minimum-six twenty-second cores is open; no
  recurrence is known.
- Hall: no coordinate packet supplies explicit motif resources, defect labels,
  boundary states, and repeatable geometry.
- Threshold: every rolling width is obstructed within the forced alphabet; no
  genuinely hidden non-rolling operation is known.
- Prefix: all-route coverage remains certified only for compositions with at most
  three runs; no source-size recurrence is known.
- Shell: no coordinate macro graph supplies positive components, connector costs,
  and a robust burden polytope.
- Integration: all rows and coupling coefficients remain fixture-derived.

## Exact next steps

1. Continue theorem numbering at `PP3dex`.
2. Hall (`docs/697`): instantiate one coordinate packet with explicit resources,
   labels, boundary states, and repeatable transfer.
3. Prefix: optimize the four-run all-route audit by reusing embedded-state checks
   or finer persistent shards; promote nothing until the complete aggregate ends.
4. Shell (`docs/698`): extract an actual coordinate macro graph and certify its
   components, connector losses, and burden polytope.
5. Integration (`docs/699`): preserve `25/30`, the fixed point, and the closed gate
   unless a complete recurrent path is promoted.
6. Boundary parallel work: share candidate precomputation across the 178 cores for
   a budget-seven search.
7. Threshold parallel work: search outside the forced minimum alphabet or model a
   genuinely unexposed non-rolling operation.
8. Run the complete historical chain when a full checkout becomes available,
   verify the remote head, and refresh this handoff.

## Conventions

Continue on `research/all-n-prime-patching`; use exact arithmetic and reviewable
commits; commit each logical unit promptly; separate candidate completion from
geometric evidence; and state explicitly that the all-`n` theorem remains open.
