# Autoprompter continuity handoff

Checkpoint time: 2026-08-02T17:36:00+10:00 Australia/Melbourne

## Goal

Develop a rigorous all-`n` prime-patching route for the no-three-in-line program
across boundary, Hall, threshold, prefix, shell, and integration frontiers. The
all-`n` theorem remains open. Finite corrected chains, matrix-level schedules,
conditional graph interfaces, and finite source reservoirs are not all-length
coordinate constructions.

## Current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Branch: `research/all-n-prime-patching`
- Verified theorem-bearing head before this refresh:
  `94e87789d94bdd93d09826e449ece872a5cce52f`.
- Completed canonical tranches: `docs/651--656` and `docs/657--662`.
- Latest theorem range: `PP3dah--PP3day`.
- Next available theorem identifier: `PP3daz`.

## Canonical tranche `docs/651--656`

### Boundary — `PP3czp--PP3czr`

- Exact fourteenth spectrum:
  `3:3, 4:13, 5:62, 6:123, 7:173, 8:151, 9:36, 10:61, 11:130, 12:131, 13:98, 14:51`.
- Sixteen minimum-three/four attempts have exactly 125 minimum cores.
- All 125 cores correct through budget seven; first-success budgets:
  `3:2, 4:23, 5:54, 6:38, 7:8`.
- Canonical `P2,+63` three-point correction reaches a legal 112-point,
  fourteen-block state.
- All raw fifteenth attempts fail.

### Hall — `PP3czs--PP3czu`

- Two graph stages separate resource-overlap motif packing from selected-centre
  conflicts.
- Maximum motif-overlap degree `Delta` guarantees
  `ceil(M/(Delta+1))` disjoint motifs.
- Retainable centres equal `3*ceil(M/(Delta+1))-tau(H)`; for bipartite `H`, use
  `tau(H)=nu(H)`.
- Under `nu(H)<=m`, the maximum-degree candidate threshold is
  `(ceil((28+m)/3)-1)*(Delta+1)+1`.

### Threshold — `PP3czv--PP3czx`

- The target-buffer graph has 44 unordered three-round factorizations, 264 ordered
  factorizations, and `4,429,185,024` fully ordered native schedules.
- Every transient matching covers the full `4 x 4` grid with cell-load histogram
  `2:8, 5:8`.
- Target displacements are cellwise sign-coherent; every nonempty target subset has
  `L1` drift `6|S|` and cannot self-neutralize.

### Prefix — `PP3czy--PP3daa`

- Explicit 28-cell no-three source on `14 x 14`:
  `P=(8,6,2,3,10,13,5,12,1,0,4,9,11,7)`,
  `Q=(7,3,8,0,11,1,2,10,9,13,5,12,4,6)`.
- Pairing shift `+5 mod 14` supplies fourteen anchors.
- All 8,192 compositions pass with zero mixed-run triples and maximum coordinate
  magnitude 100.
- The incidence graph is one fourteen-cycle, so the witness is not nested.

### Shell — `PP3dab--PP3dad`

- With burden `b_i=6*delta_i+c_i`, cumulative saving is
  `B_k=sum_{i<=k}(3-b_i)`.
- A prefix beats setup `S` exactly when `B_k>S`.
- Every fixed setup is amortizable exactly when `sup_k B_k=infinity`.
- Periodic schedules are classified by period gain and within-period prefix peaks.

### Integration — `PP3dae--PP3dag`

- Candidate completion remains `25/30`.
- All six actual evidence rows remain `fixture_derived`; zero rows are promoted.
- Fixed-point total:
  `705466760524005697/3623878655999606784`.
- Slack below one quarter:
  `200502903475895999/3623878655999606784`.
- Geometric closure is false.

## Canonical tranche `docs/657--662`

### Boundary — `docs/657-corrected-fifteenth-boundary-transition.md`

Theorems `PP3dah--PP3daj`.

- Ten minimum-four fifteenth attempts have 156 minimum cores.
- All 156 cores correct through budget seven; budgets:
  `4:6, 5:70, 6:74, 7:6`.
- Canonical `P0,-30` four-point correction reaches a legal 120-point,
  fifteen-block state.
- All raw sixteenth attempts fail, with spectrum
  `4:9, 5:21, 6:88, 7:166, 8:238, 9:8, 10:38, 11:83, 12:157, 13:151, 14:73`.

### Hall — `docs/658-two-level-hall-packing.md`

Theorems `PP3dak--PP3dam`.

- The Caro–Wei degree-sequence bound gives
  `ceil(sum_v 1/(d_v+1))` resource-disjoint motifs.
- Average degree gives `ceil(M/(d_bar+1))`.
- Both bounds are sharp for disjoint unions of equal cliques.
- With selected-centre bipartite matching loss `m`, the Hall condition is
  `3*ceil(sum_v 1/(d_v+1))-m>=28`.

### Threshold — `docs/659-threshold-exposure-obstruction.md`

Theorems `PP3dan--PP3dap`.

- Across 12,544 ordered distinct-buffer batches, distinct-intermediate counts are
  `4:7, 5:84, 6:634, 7:2804, 8:9015`.
- Changed-cell union sizes are `14:164, 15:2808, 16:9572`.
- Maximum exposure counts are `2:49, 3:1553, 4:7970, 5:2972`.
- Every one of 49 transient matchings has exactly one perfectly balanced order,
  exposing every cell twice.
- All 392 balanced intermediate occurrences remain matrix-illegal.

### Prefix — `docs/660-two-component-anchor-rerouting-radius.md`

Theorems `PP3daq--PP3das`.

- For every minimum-crossing thirteen-pair anchor matching and either two-pair
  component deletion, boundary flow is exactly `(2 outgoing,2 incoming)`.
- All 208 deletion cases have exact rerouting radius four.
- Every case has exactly 144 optimal distance-four reroutings.

### Shell — `docs/661-shell-repertoire-cycle-mean.md`

Theorems `PP3dat--PP3dav`.

- A finite macro repertoire amortizes every setup exactly when a reachable cycle
  has positive total saving, equivalently mean burden below three.
- Optimal asymptotic saving is the maximum reachable cycle mean saving.
- Entry saving `A`, cycle gain `G>0`, and setup `S` require exactly
  `max(0,floor((S-A)/G)+1)` complete repetitions.

### Integration — `docs/662-compensating-mechanisms-evidence-gate.md`

Theorems `PP3daw--PP3day`.

- Candidate completion remains `25/30`.
- All actual rows remain `fixture_derived`; the promoted set is empty.
- Fixed-point total and slack remain unchanged.
- Geometric closure is false and the all-`n` theorem remains open.

## Reproducibility

### `651--656`

- `scripts/check_frontier_651_656.py`
- `certificates/prime-patching-uniform-mechanisms-651-656.json`
- `proofs/prime-patching-parity-index-651-656-supplement.md`

### `657--662`

- `scripts/check_boundary_fifteenth_corrections.cpp`
- `scripts/check_boundary_fifteenth_transition.py`
- `scripts/check_boundary_sixteenth_spectrum.cpp`
- `scripts/check_hall_degree_sequence_packing.py`
- `scripts/check_hall_two_level_packing.py`
- `scripts/check_threshold_balanced_exposure_batch.py`
- `scripts/check_prefix_two_component_rerouting.py`
- `scripts/check_shell_repertoire_cycle_mean.py`
- `scripts/check_compensating_mechanisms_gate.py`
- `scripts/check_frontier_657_662.py`
- `certificates/prime-patching-compensating-mechanisms-657-662.json`
- `proofs/prime-patching-parity-index-657-662-supplement.md`

Latest chained command:

```bash
python scripts/check_frontier_657_662.py
```

## Validation status

- Fourteenth-step boundary kernels were executed in the isolated runtime used to
  produce `docs/651`.
- The committed fifteenth wrapper compiles and asserts the fifteenth spectrum,
  correction census, corrected state, and sixteenth spectrum; the complete chain
  could not be rerun here because a full checkout was unavailable.
- This response independently reproduced:
  - all 32,768 labelled six-vertex Caro–Wei checks;
  - all 49 balanced threshold batches and their exact histograms;
  - all 208 prefix deletion cases, radius four, and 144 optimum repairs;
  - shell positive-cycle and no-positive-cycle examples;
  - exact fixed-point total and slack.
- The explicit fourteen-pair C++ audit compiled and executed during this work,
  checking all 8,192 compositions and maximum coordinate 100.
- `git clone` and the complete historical chain could not run because this
  environment could not resolve `github.com`.

## Decisions

- Preserve one canonical theorem chapter per frontier number. Duplicate concurrent
  chapters, gates, certificates, and stale audits were removed.
- Keep the fourteen-pair reservoir as canonical `docs/654`; retain the older
  component obstruction only as a supplementary comparison.
- Treat Hall graph quantities as conditional until derived from coordinates.
- Treat balanced threshold exposure as an obstruction, not a legal operation.
- Treat prefix rerouting radius four as a permutation-layer theorem only.
- Treat the shell positive-cycle theorem as a scheduling target, not evidence that
  a geometric macro repertoire exists.
- Promote no row without a complete coordinate source path.

## Current blockers

- Boundary: no corrected sixteenth transition, recurrence, or periodic state
  invariant.
- Hall: no coordinate-derived motif degree sequence, selected-centre matching
  bound, or simultaneous source/host-defect degree-two theorem.
- Threshold: balanced native batches still expose illegal intermediates; no legal
  inverse or replacement primitive is known.
- Prefix: the four-assignment repair has no uniform coordinate insertion
  realization, and no all-size recurrence links the finite reservoirs.
- Shell: no coordinate-level macro transition graph with a reachable sub-three
  mean-burden cycle is known.
- Integration: all rows and coupling coefficients remain fixture-derived.

## Uncommitted work

- No completed repository change is intentionally left only in chat.
- Unsuccessful exploratory source searches were not committed as theorem evidence.

## Exact next steps

1. Verify this handoff and continue theorem numbering at `PP3daz`.
2. Build `docs/663--668` around a corrected sixteenth transition and coordinate-
   level compensating mechanisms.
3. Boundary: enumerate minimum sixteenth cores and search preserving corrections;
   compare corrected-state signatures for recurrence.
4. Hall: derive motif degrees and selected-centre conflicts from explicit host
   coordinates; prove both restricted degree-two properties after packing.
5. Threshold: construct a primitive or hidden-state operation avoiding all illegal
   balanced intermediates and supplying endpoint compensation.
6. Prefix: lift one of the 144 optimal reroutings into integer insertion geometry
   and audit all compositions; seek a recurrence between reservoirs.
7. Shell: construct an explicit finite macro transition graph, calculate every edge
   burden from coordinates, and find a reachable positive-saving cycle.
8. Integration: promote only complete coordinate source paths; otherwise preserve
   the closed gate and fixed point.
9. Run standalone diagnostics and the complete historical chain in a full checkout;
   verify the remote head and refresh this handoff.

## Conventions

Continue on `research/all-n-prime-patching`; use exact arithmetic and reviewable
commits; store a checker and certificate for each tranche; keep candidate
completion separate from geometric evidence; and state explicitly that the all-`n`
theorem remains open.
