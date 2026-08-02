# Autoprompter continuity handoff

Checkpoint date: 2026-08-02 Australia/Melbourne

## Goal

Develop a rigorous all-`n` prime-patching route for the no-three-in-line program
across boundary, Hall, threshold, prefix, shell, and integration frontiers. The
all-`n` theorem remains open. Finite corrected chains, conditional packing
interfaces, matrix impossibility certificates, and finite coordinate lifts are not
all-length coordinate constructions.

## Current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Branch: `research/all-n-prime-patching`
- Canonical completed tranches: `docs/651--656`, `docs/657--662`, and
  `docs/663--668`.
- Current theorem range: `PP3daz--PP3dbq`.
- Next available theorem identifier: `PP3dbr`.

## Completed canonical tranche: `docs/663--668`

### Boundary — `docs/663-corrected-sixteenth-boundary-transition.md`

Theorems `PP3daz--PP3dbb`.

- The 1,032 raw sixteenth attempts have exact minimum-transversal histogram
  `4:9,5:21,6:88,7:166,8:238,9:8,10:38,11:83,12:157,13:151,14:73`.
- Exactly nine attempts have minimum four, with thirty-nine minimum cores.
- The certified `P1/-37` four-point correction deletes
  `(22,106),(39,165),(48,315),(62,312)` and adds
  `(22,315),(39,312),(48,165),(62,106)`.
- The corrected state has 128 points, sixteen blocks, and no collinear triple.
- All 1,032 raw seventeenth attempts fail. Their exact histogram is
  `3:1,4:2,5:17,6:56,7:192,8:248,9:1,10:18,11:65,12:182,13:162,14:88`.
- The unique minimum-three seventeenth attempt is `P2/-57`, with three minimum
  cores.

### Hall — `docs/664-local-resource-incidence-hall-packing.md`

Theorems `PP3dbc--PP3dbe`.

- For motif resource sets `R(v)` and resource multiplicities `mu_r`, define
  `L_v=sum_{r in R(v)}(mu_r-1)`.
- Exact overlap degree is
  `d_v=L_v-sum_{u!=v}max(|R(u) intersect R(v)|-1,0)`.
- The directly host-auditable packing certificate is
  `ceil(sum_v 1/(L_v+1))`.
- If every motif uses at most `s` resources and every resource occurs in at most
  `lambda` motifs, the uniform corollary is `ceil(M/(s(lambda-1)+1))`.
- With selected-centre matching loss `m`, the two-stage Hall condition is
  `3*ceil(sum_v 1/(L_v+1))-m>=28`.

### Threshold — `docs/665-global-threshold-separation.md`

Theorems `PP3dbf--PP3dbh`.

- The integer functional
  `Phi(M)=M[0,3]+M[1,0]-M[1,1]-M[2,2]+M[3,0]+M[3,2]`
  gives source score `-3`.
- All 4,475 legal four-layer matrices have nonnegative score, with exact
  histogram `0:495,1:956,2:1193,3:1012,4:590,5:176,6:44,7:8,8:1`.
- Every legal endpoint has displacement margin at least three from the source.
- The source is outside the convex hull of the legal catalogue, so no nonempty
  finite legal endpoint-only batch can compensate back to the source.

### Prefix — `docs/666-coordinate-anchor-rerouting-lift.md`

Theorems `PP3dbi--PP3dbk`.

- The lexicographically first minimum-crossing matching of the canonical
  thirteen-pair source is
  `(3,6,5,0,1,2,7,4,10,8,12,9,11)`.
- For each two-pair deletion `{0,2}` and `{3,5}`, there are exactly 144 optimal
  distance-four reroutings.
- Every one of all 288 optimal reroutings passes all `2^10=1,024` ordered
  compositions under the established greedy primitive-direction insertion rule.
- The exhaustive audit covers 294,912 rerouting/composition pairs with no
  mixed-run collinear triple.
- Maximum-coordinate distributions are recorded exactly; best bounds are 87 and
  84, and worst bounds are 144 and 156 for the two deletion cases.

### Shell — `docs/667-interval-shell-cycle-robustness.md`

Theorems `PP3dbl--PP3dbn`.

- Under independent edge burden intervals `[lower_e,upper_e]`, some admissible
  realization amortizes every setup exactly when a reachable cycle has
  `sum_e(3-lower_e)>0`.
- Every admissible realization is guaranteed to amortize every setup exactly when
  a reachable cycle has `sum_e(3-upper_e)>0`.
- This yields exact robust, possible-only, and impossible regimes.
- With guaranteed entry saving `A`, robust cycle gain `G>0`, and setup `S`, the
  least guaranteed repetition count is `max(0,floor((S-A)/G)+1)`.

### Integration — `docs/668-robust-compensation-evidence-gate.md`

Theorems `PP3dbo--PP3dbq`.

- Candidate completion remains `25/30`: boundary `4/5`, Hall `4/5`, threshold
  `5/5`, prefix `5/5`, shell `5/5`, integration `2/5`.
- All six actual rows remain `fixture_derived`; the promoted set is empty.
- The fixture fixed-point total remains
  `705466760524005697/3623878655999606784`.
- Positive slack below one quarter remains
  `200502903475895999/3623878655999606784`.
- Geometric closure is false and the all-`n` theorem remains open.

## Reproducibility

- `scripts/check_boundary_sixteenth_spectrum.cpp`
- `scripts/check_boundary_seventeenth_spectrum.cpp`
- `scripts/check_boundary_sixteenth_transition.py`
- `scripts/check_hall_local_resource_incidence.py`
- `scripts/check_threshold_global_separation.py`
- `scripts/check_prefix_coordinate_rerouting_lift.py`
- `scripts/check_prefix_rerouting_geometry.cpp`
- `scripts/check_prefix_rerouting_geometry.py`
- `scripts/check_shell_interval_cycle_robustness.py`
- `scripts/check_robust_compensation_gate.py`
- `scripts/check_frontier_663_668.py`
- `certificates/prime-patching-robust-compensation-663-668.json`
- `proofs/prime-patching-parity-index-663-668-supplement.md`

Latest chained command:

```bash
python scripts/check_frontier_663_668.py
```

## Validation status

- The sixteenth spectrum, certified correction, corrected 128-point state, and
  complete seventeenth spectrum were executed successfully in isolated local
  runs.
- The Hall canonical audit records exhaustive checks of all 54,263 multisets of
  at most six nonempty motif types on four resources against exact independence
  numbers.
- The threshold separator was independently reconstructed over all eighteen legal
  permutation layers and all 4,475 legal four-layer matrices.
- The exhaustive prefix C++ audit compiled and ran successfully, checking all
  294,912 rerouting/composition pairs and the exact coordinate-bound histograms.
- The shell interval checker was reviewed and its exact robust, possible-only, and
  impossible examples are committed.
- Exact fixed-point arithmetic and the closed integration gate are committed.
- The complete historical chained runner was not executed in this environment
  because a full repository checkout was unavailable; earlier clone attempts could
  not resolve `github.com`.

## Decisions

- Preserve one canonical theorem chapter, audit path, gate, and certificate per
  frontier number. Concurrent duplicate Hall, threshold, and integration artifacts
  were removed.
- Use the certified `P1/-37` repair without claiming exhaustive repair of all
  thirty-nine sixteenth cores.
- Treat local Hall resource incidence as a promotion interface until instantiated
  by actual host coordinates and both degree-two restrictions.
- Treat the threshold separator as a complete obstruction for the present legal
  four-layer endpoint catalogue; future work must change or enlarge the state
  model.
- Treat the 288 prefix lifts as strong finite coordinate evidence for one
  canonical minimum-crossing matching, not an all-size recurrence.
- Treat shell interval cycles as scheduling interfaces until coordinate burdens
  and compatibility edges are certified.
- Promote no integration row without a complete asymptotic or recurrent coordinate
  source path.

## Current blockers

- Boundary: no corrected seventeenth transition, recurrence, or periodic state
  invariant.
- Hall: no coordinate-derived asymptotic motif resource family, centre-conflict
  matching bound, or simultaneous source/host-defect degree-two theorem.
- Threshold: the present legal endpoint catalogue cannot compensate the source; no
  hidden-state primitive, alternate source state, or expanded matrix model is
  known.
- Prefix: the exhaustive lift covers both deletions for one canonical matching,
  but not all 104 minimum-crossing matchings and supplies no all-size recurrence.
- Shell: no coordinate macro transition graph supplies certified burden intervals
  with a robust positive cycle.
- Integration: all rows and coupling coefficients remain fixture-derived.

## Uncommitted work

- No completed repository change is intentionally left only in chat.
- Exhaustive correction of all thirty-nine sixteenth minimum cores was not
  completed; the theorem records only the verified correction.
- Unsuccessful exploratory searches were not promoted as theorem evidence.

## Exact next steps

1. Verify this handoff and continue theorem numbering at `PP3dbr`.
2. Build `docs/669--674` around a corrected seventeenth transition and genuinely
   coordinate-instantiated compensation mechanisms.
3. Boundary: search the three minimum cores of `P2/-57` for a preserving
   seventeenth correction, measure the raw eighteenth spectrum, and compare
   corrected-state signatures for recurrence.
4. Hall: extract actual motif resource lists from conditional-host coordinates,
   evaluate the local-load certificate, and prove both restricted degree-two
   conditions after selection.
5. Threshold: enlarge or alter the source-state model to escape the separating
   functional, or construct a hidden-state primitive not represented by exposed
   legal endpoints.
6. Prefix: extend the coordinate audit to all 104 minimum-crossing matchings and
   seek a deterministic coordinate-safe repair selector and recurrence between
   finite reservoirs.
7. Shell: construct a coordinate macro transition graph, derive certified burden
   intervals from repairs and collateral, and search for a reachable robust
   positive cycle.
8. Integration: promote only complete coordinate source paths; otherwise preserve
   `25/30`, the fixed point, and the closed gate.
9. Run all standalone diagnostics and the complete historical chained runner in a
   full checkout, verify the remote head, and refresh this handoff.

## Conventions

Continue on `research/all-n-prime-patching`; use exact arithmetic and reviewable
commits; store a checker and certificate for each tranche; keep candidate
completion separate from geometric evidence; and state explicitly that the all-`n`
theorem remains open.
