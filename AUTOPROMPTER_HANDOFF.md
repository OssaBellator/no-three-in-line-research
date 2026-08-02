# Autoprompter continuity handoff

Checkpoint time: 2026-08-02 11:56 Australia/Melbourne

## Goal

Develop a rigorous all-`n` prime-patching route for the no-three-in-line research
program across six linked frontiers:

1. boundary recleaning / marker-controller realization;
2. localized Hall transport and list decoding;
3. fractional direct-clean threshold layers;
4. support-chord repair words and constrained prefix codes;
5. clean-macro shell attenuation and scheduling;
6. global interaction/integration certificates.

The asymptotic all-`n` theorem remains open. The repository contains exact finite
reductions, conditional interfaces, bounded corrected chains, matrix-level
operation reductions, and explicit finite source models; none is an all-length
proof.

## Current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Branch: `research/all-n-prime-patching`
- Verified pre-checkpoint research head: `208422665488c9071ebc854ee83a5c6219457304`.
- Pre-checkpoint title: `Index scaling mechanisms theorems through docs 644`.
- The branch was remotely verified identical to that commit before this refresh.
- Next available theorem identifier: `PP3cyx`.

## Completed canonical tranche: `docs/639--644`

### Boundary — `docs/639-corrected-twelfth-boundary-transition.md`

Theorems `PP3cyf--PP3cyh`.

- The exact radius-64 twelfth minimum-transversal histogram is
  `3:1, 4:4, 5:8, 6:101, 7:173, 8:239, 9:8, 10:25, 11:75, 12:146, 13:158, 14:94`.
- Five attempts have minimum transversal at most four, with sixty-one minimum
  cores total.
- Every one of those attempts has a row-and-column-preserving correction within
  budget seven.
- The canonical `P2` offset-64 correction deletes
  `(2,1),(14,48),(32,98),(46,257),(47,258)` and adds
  `(2,257),(14,258),(32,98),(46,1),(47,48)`.
- The corrected state has ninety-six points and twelve blocks.
- All 1,032 raw thirteenth attempts in radius 64 fail.

### Hall — `docs/640-source-star-centre-pruning.md`

Theorems `PP3cyi--PP3cyk`.

- The stored binary source-star fixture has four centres with partner-fibre
  records `(size,max degree,matching,completions)` equal to
  `(3,3,no,0)`, `(1,1,yes,4)`, `(0,0,yes,6)`, and `(2,1,yes,3)`.
- Three quarters of the centres therefore satisfy the partner-matching condition.
- If `b` bad centre resources are pruned, the mixed-degree Hall pipeline needs
  `28+b` resources on the centred side and twenty-eight on the opposite side,
  assuming the source and host-defect restrictions have degree at most two.
- Ten copies of the numerical four-centre pattern are the first count supplying
  at least twenty-eight good centre resources, but no geometric cross-copy theorem
  is known.

### Threshold — `docs/641-threshold-transient-buffer-cell.md`

Theorems `PP3cyl--PP3cyn`.

- Every one of the forty-eight native two-swap factorizations has union support
  seven: the six target `C6` cells plus one cancelling transient cell.
- The possible transient cells are exactly the eight source entries of
  multiplicity one.
- Each transient cell occurs in exactly six ordered factorizations.
- A native atomic batch must therefore protect a seven-cell geometric footprint;
  hiding the swap order does not produce a six-cell exposed operation.

### Prefix — `docs/642-thirteen-pair-saturated-anchor-reservoir.md`

Theorems `PP3cyo--PP3cyq`.

- The permutations
  `P=(9,4,7,3,0,1,12,8,11,10,2,6,5)` and
  `Q=(7,12,9,1,4,3,8,0,2,11,5,10,6)` form a twenty-six-cell no-three source on
  `13 x 13`, with degree two in every row and column.
- The pairing permutation `(1,0,3,2,5,4,7,8,6,10,12,9,11)` supplies thirteen
  disjoint anchor pairs.
- All 4,096 ordered compositions of thirteen unary nodes embed with zero mixed-run
  triples and maximum coordinate magnitude 180.
- The incidence component pair-sizes are `2,2,4,5`; deleting either two-pair
  component leaves an induced eleven-pair saturated source.
- No anchor matching respects those incidence components, so the nested source
  does not give a nested anchor construction.

### Shell — `docs/643-shell-batch-amortization.md`

Theorems `PP3cyr--PP3cyt`.

- Across `t` periods, per-use overhead `delta`, and fixed collateral `C`, the
  candidate cost is `t(12+6 delta)+C`.
- It beats the recorded baseline exactly when `t(3-6 delta)>C`.
- Fixed collateral is amortizable over some finite number of periods exactly when
  `delta<1/2`.
- At zero overhead the minimum period count is `floor(C/3)+1`.

### Integration — `docs/644-scaling-mechanisms-evidence-gate.md`

Theorems `PP3cyu--PP3cyw`.

- Candidate completion remains `25/30`:
  boundary `4/5`, Hall `4/5`, threshold `5/5`, prefix `5/5`, shell `5/5`,
  integration `2/5`.
- The fixture fixed-point total remains
  `705466760524005697/3623878655999606784`.
- Positive slack below one quarter remains
  `200502903475895999/3623878655999606784`.
- All six actual rows remain `fixture_derived`; zero rows are promoted and
  geometric closure remains false.

## Machine-readable and reproducibility files

- `certificates/prime-patching-scaling-mechanisms-639-644.json`
- `scripts/check_boundary_twelfth_spectrum.cpp`
- `scripts/check_boundary_twelfth_corrections.cpp`
- `scripts/check_boundary_twelfth_transition.py`
- `scripts/check_hall_source_center_pruning.py`
- `scripts/check_threshold_transient_cell_batch.py`
- `scripts/check_prefix_saturated_anchor_reservoir_13.py`
- `scripts/check_shell_amortized_collateral.py`
- `scripts/check_scaling_mechanisms_gate.py`
- `scripts/check_frontier_639_644.py`
- `proofs/prime-patching-parity-index-639-644-supplement.md`

Latest group command:

```bash
python scripts/check_frontier_639_644.py
```

## Validation status

- All six new standalone diagnostics passed in the isolated local runtime.
- Both twelfth-step C++ kernels compiled and executed successfully.
- Python compilation passed for all seven new Python scripts.
- The complete historical chained runner was not executed locally because the
  isolated runtime does not contain a full repository checkout; the group runner
  begins with `scripts/check_frontier_633_638.py`.

## Current blockers

- Boundary: the corrected path reaches twelve blocks but has no raw thirteenth
  extension; a corrected thirteenth transition or periodic state invariant is
  missing.
- Hall: the actual source supplies a three-quarter good-centre fixture rate, but no
  asymptotic bad-centre bound or compatible source/host-defect degree-two theorem.
- Threshold: no legal geometric source operation protects either the seven-cell
  native batch or a primitive six-cell circuit.
- Prefix: saturated sources exist at eleven, twelve, and thirteen pairs, but no
  anchor-preserving nested or uniform all-size construction is known.
- Shell: the true per-use overhead and fixed collateral of a geometric `(1,1,1)`
  macro are unknown.
- Integration: all actual rows and coupling coefficients remain fixture-derived.

## Exact next steps

1. Verify this handoff and continue theorem numbering at `PP3cyx`.
2. Build `docs/645--650` around a corrected thirteenth transition and source-level
   uniformity.
3. Boundary: enumerate minimum thirteenth conflict cores in radius 64 and search
   degree-preserving corrections, then test drift or recurrence across the last
   three corrected states.
4. Hall: prove an asymptotic bound on bad centre fibres and derive degree at most
   two for source and host-defect restrictions after pruning.
5. Threshold: test all eight transient buffer choices against actual source-cell
   geometry, or construct a primitive six-cell atomic edit.
6. Prefix: search for a fourteen-pair source and an anchor pairing compatible with
   component deletion, or prove a structural obstruction to componentwise nesting.
7. Shell: build a geometric `(1,1,1)` macro, measure `delta` and `C`, and apply the
   exact amortization law.
8. Integration: promote only rows with complete coordinate source paths;
   otherwise preserve the closed gate and unchanged fixed point.
9. Run diagnostics, Python compilation, the chained runner in a complete checkout,
   verify the remote head, and refresh this handoff.

## Conventions

Continue on `research/all-n-prime-patching`; use exact arithmetic and reviewable
commits; keep candidate completion separate from geometric evidence; preserve the
six-frontier structure; store a checker and certificate for each tranche; and
state explicitly that the all-`n` theorem remains open.
