# Autoprompter continuity handoff

Checkpoint time: 2026-08-02T21:24:00+10:00 Australia/Melbourne

## Goal

Develop a rigorous all-`n` prime-patching route for the no-three-in-line program
across boundary, Hall, threshold, prefix, shell, and integration frontiers. The
all-`n` theorem remains open. Finite corrected chains, conditional packing
interfaces, matrix impossibility certificates, and finite coordinate lifts are not
all-length coordinate constructions.

## Current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Branch: `research/all-n-prime-patching`
- Canonical completed tranches: `docs/651--656`, `docs/657--662`,
  `docs/663--668`, and `docs/669--674`.
- Current theorem range: `PP3dbr--PP3dci`.
- Next available theorem identifier: `PP3dcj`.
- Latest theorem-bearing head before this continuity commit:
  `7571b22e9f9917ad3816aa1b19be780b03e0e928`.

## Completed canonical tranche: `docs/669--674`

### Boundary — `docs/669-corrected-seventeenth-boundary-transition.md`

Theorems `PP3dbr--PP3dbt`.

- The unique minimum-three raw seventeenth attempt is `P2/-57`, with five conflict
  triples and exactly three minimum cores.
- All three cores first repair at deletion budget five; exact histogram `5:3`.
- Canonical correction deletes
  `(0,110),(42,193),(54,378),(64,253),(66,252)` and adds
  `(0,252),(42,378),(54,253),(64,110),(66,193)`.
- The corrected state has 136 points, seventeen blocks, and no collinear triple.
- Raw eighteenth histogram:
  `4:3,5:16,6:70,7:211,8:218,9:2,10:15,11:68,12:152,13:178,14:99`.
- Seven minimum cores remain across `P0/-39`, `P2/-40`, and `P2/-26`.

### Hall — `docs/670-component-exact-hall-packing.md`

Theorems `PP3dbu--PP3dbw`.

- Componentwise rounded Caro--Wei dominates global rounded Caro--Wei and can be
  strict.
- Exact packing is additive across resource-overlap components.
- Exhaustion of 54,263 motif multisets found three strict improvements and 50,387
  exact component certificates.
- The two-stage Hall condition remains `3q-m>=28`.

### Threshold — `docs/671-threshold-facet-hidden-mass.md`

Theorems `PP3dbx--PP3dbz`.

- The legal hull has affine dimension nine; its 495 score-zero matrices span
  dimension eight, so the separator is a facet.
- Among all 10,147 integer transportation matrices, minimum score is `-8`, uniquely
  at `4I_4`.
- Any same-space compensation requires hidden-state weight at least `3/8`, or at
  least `ceil(3N/8)` hidden states in an equal-weight `N`-state batch.

### Prefix — `docs/672-prefix-matching-orbit-reduction.md`

Theorems `PP3dca--PP3dcc`.

- The full forbidden-incidence bipartition-preserving automorphism group has order
  2,560.
- The 104 minimum-crossing matchings have orbit sizes `8,16,40,40`; the 208
  matching/deletion cases have orbit sizes `16,32,80,80`.
- Only the identity grid-dihedral transformation preserves the coordinate source,
  so incidence automorphisms do not transfer coordinate certificates.
- Supplemental audit: a 160-element diagonal subgroup gives twenty matching
  orbits; forty lexicographically selected all-unit coordinate lifts pass. This
  supplemental result has no additional theorem identifiers.

### Shell — `docs/673-polyhedral-shell-cycle-robustness.md`

Theorems `PP3dcd--PP3dcf`.

- Fixed cycle `C` is robust-positive under polyhedral burden set `U` exactly when
  `max_{b in U}<b,chi_C><3|C|`.
- Revealed-state adaptive margin is
  `min_b max_C g_C(b)` and has an exact mixed-cycle minimax dual.
- In the certified two-cycle segment, every fixed cycle has robust gain `-1`, while
  equal mixed weights certify adaptive margin `1/2`.
- Exact correlated setup repayment is
  `max_u max(0,floor((S-A_u)/G_u)+1)`; the example needs seven repetitions versus
  ten from separate extrema.

### Integration — `docs/674-hidden-compensation-evidence-gate.md`

Theorems `PP3dcg--PP3dci`.

- Candidate completion remains `25/30`: boundary `4/5`, Hall `4/5`, threshold
  `5/5`, prefix `5/5`, shell `5/5`, integration `2/5`.
- All six actual rows remain `fixture_derived`; no rows are promoted.
- Fixed-point total remains
  `705466760524005697/3623878655999606784`.
- Slack below one quarter remains
  `200502903475895999/3623878655999606784`.
- Geometric closure is false and the all-`n` theorem remains open.

## Reproducibility

- `scripts/check_boundary_seventeenth_corrections.cpp`
- `scripts/check_boundary_eighteenth_spectrum.cpp`
- `scripts/check_boundary_seventeenth_transition.py`
- `scripts/check_hall_component_resource_packing.py`
- `scripts/check_threshold_facet_hidden_mass.py`
- `scripts/check_prefix_matching_orbits.py`
- `scripts/check_prefix_automorphism_orbit_unit_lifts.py`
- `scripts/check_shell_polyhedral_cycle_robustness.py`
- `scripts/check_hidden_compensation_gate.py`
- `scripts/check_frontier_669_674.py`
- `certificates/prime-patching-hidden-compensation-669-674.json`
- `proofs/prime-patching-parity-index-669-674-supplement.md`

Latest chained command:

```bash
python scripts/check_frontier_669_674.py
```

## Validation status

- The seventeenth correction and eighteenth spectrum kernels and wrapper passed in
  isolated local runs.
- Exact local audits covered 54,263 Hall motif multisets; all 4,475 legal and
  10,147 transportation threshold matrices; 2,560 prefix automorphisms, 104
  matchings, and 208 deletion cases; and exact rational shell examples.
- The supplemental prefix script records forty passing all-unit coordinate lifts.
- Standalone scripts authored in this tranche were executed before commit. The
  complete historical chained runner was not executed because a full checkout was
  unavailable in the isolated runtime.

## Decisions

- Preserve one canonical theorem chapter, checker path, certificate, and parity row
  per frontier number.
- Use the first `P2/-57` core as canonical; all three are certified.
- Use component-exact Hall packing when coordinate resource lists have bounded
  overlap components; retain the centre-conflict stage.
- Treat the threshold facet and `3/8` hidden-mass law as necessary obstructions,
  not constructions.
- Treat incidence orbits and supplemental unit lifts as finite prefix evidence;
  do not infer full coordinate symmetry or arbitrary-composition coverage.
- Distinguish fixed-cycle execution, revealed-state adaptation, and mixed-cycle
  dual certificates under correlated shell uncertainty.
- Promote no integration row without a recurrent or asymptotic coordinate source
  path.

## Current blockers

- Boundary: no corrected eighteenth transition, recurrence, or periodic invariant.
- Hall: no asymptotic coordinate motif resource family, centre-conflict bound, or
  simultaneous source/host-defect degree-two theorem.
- Threshold: no hidden-state primitive, alternate source, or expanded model meeting
  the necessary hidden mass.
- Prefix: full incidence orbits do not reduce physical coordinate audits;
  supplemental lifts cover only one route and the all-unit composition per
  representative; no recurrence is known.
- Shell: no coordinate macro graph supplies a certified polyhedral burden set with
  a fixed robust-positive cycle or an executable adaptive policy.
- Integration: all rows and coupling coefficients remain fixture-derived.

## Uncommitted work

- No completed repository change is intentionally left only in chat.
- Failed exploratory searches are not promoted as theorem evidence.

## Exact next steps

1. Continue theorem numbering at `PP3dcj` and build `docs/675--680`.
2. Boundary: exhaustively repair the seven minimum eighteenth cores and measure the
   raw nineteenth spectrum.
3. Hall: instantiate component-exact packing on asymptotic coordinate resource
   lists and certify the centre-conflict stage plus both degree-two restrictions.
4. Threshold: construct a hidden-state or expanded-model primitive carrying the
   necessary separator mass and audit exposed states.
5. Prefix: extend coordinate audits beyond all-unit compositions and one route per
   representative, or prove an equivariant insertion rule.
6. Shell: instantiate a coordinate macro graph and correlated burden polytope;
   separate fixed and adaptive execution guarantees.
7. Integration: promote only complete coordinate paths; otherwise preserve
   `25/30`, the fixed point, and the closed gate.
8. Run the complete historical chain in a full checkout, verify the remote head,
   and refresh this handoff.

## Conventions

Continue on `research/all-n-prime-patching`; use exact arithmetic and reviewable
commits; commit each completed logical unit promptly; separate candidate completion
from geometric evidence; and state explicitly that the all-`n` theorem remains
open.
