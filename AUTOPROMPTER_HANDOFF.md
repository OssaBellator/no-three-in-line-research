# Autoprompter continuity handoff

Checkpoint time: 2026-07-31 14:43 Australia/Melbourne

## Goal

Develop a rigorous all-`n` prime-patching route for the no-three-in-line research program by advancing six linked frontiers:

1. boundary recleaning / marker-controller realization;
2. localized Hall transport and list decoding;
3. fractional direct-clean threshold layers;
4. support-chord repair words and constrained prefix codes;
5. clean-macro shell attenuation and scheduling;
6. global interaction/integration certificates.

The asymptotic all-`n` theorem remains open. Existing results are finite reductions, exact certificates, conditional closure mechanisms, and independently enumerated candidate models; they must not be described as a completed proof of the all-`n` theorem.

## Current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Branch: `research/all-n-prime-patching`
- Verified pre-checkpoint head: `edddefecba87208f727d6c11aa63fb04cbb071f9`
- Pre-checkpoint head title: `Index independent extraction theorems through docs 566`
- The branch was remotely verified identical to that commit before this refresh.
- Latest research-content head before this continuity commit: `edddefecba87208f727d6c11aa63fb04cbb071f9`.
- Next available theorem identifier: `PP3cpx`.

## Completed work

The branch contains the cumulative six-frontier sequence through `docs/566`. The latest tranche is the independent extraction and obstruction sequence `docs/561--566`:

- `docs/561-coordinate-level-four-seven-boundary-seam-attempt.md`
  - Theorems `PP3cpf--PP3cph`.
  - Independently enumerates saturated side-four and side-seven blocks with two points in every row and column and no collinear triple.
  - Both blocks have four distinct dihedral variants.
  - All 64 ordered diagonal seams fail; twenty-nine first witnesses have slope one.
  - This rules out the simplest diagonal realization of the four/seven marker semigroup.

- `docs/562-independent-cylinder-microcensus-for-hall-gadgets.md`
  - Theorems `PP3cpi--PP3cpk`.
  - Defines six microscopic states and four local choices before taking any quotient.
  - Enumerates two exact `6 x 6` transition matrices with 36 positive entries and explicit choice witnesses.
  - Of all 15 pair partitions, exactly the syndrome fibres are strongly lumpable for both gadgets.
  - The quotient matrices recover the stored Hall kernels, but no prime-patching geometric decoder is supplied.

- `docs/563-source-layer-alignment-for-threshold-schedules.md`
  - Theorems `PP3cpl--PP3cpn`.
  - Proves layer-sum invariance and refutes direct identity of the `docs/521` and `docs/527` layer fixtures.
  - The `docs/521` layers sum to the conservative matrix `M`; the `docs/527` cyclic alphabet sums to the all-ones matrix.
  - In the later four-layer coordinates, only 6 of 1120 canonical primitive normals with coefficients in `[-3,3]` factor through the two-observable quotient.

- `docs/564-corrected-node-grading-and-risk-marked-prefix-dp.md`
  - Theorems `PP3cpo--PP3cpq`.
  - Refutes the prior interpretation that `z` marks leaves in `T=z(1+T+uT^2)`; it marks total nodes.
  - Correct interpretation: for total nodes `n` and binary nodes `j`, unary nodes are `n-1-2j` and leaves are `j+1`.
  - At total size 30 and 9 binary nodes, the family size remains `168212023980`.
  - An exact unary-to-unary risk DP gives aggregate risk `638045608200`, mean `110/29`, `153857776072` objects with risk at most five, and a deterministic risk-zero witness.

- `docs/565-nonprecancelled-shell-incidence-benchmark.md`
  - Theorems `PP3cpr--PP3cpt`.
  - Applies the `A,A,B,B,C` service multiset to a full-rank physical incidence matrix with determinant `-2`.
  - The physical word is not precancelled.
  - Among all 30 orders, 10 attain minimum physical `l_1` reserve `6/5`; `ABABC` has buffer `(2/5,4/5,0)`.
  - This is an identifiable benchmark, not the actual prime-patching shell incidence system.

- `docs/566-fieldwise-evidence-gate-after-independent-extraction.md`
  - Theorems `PP3cpu--PP3cpw`.
  - Independent extraction completes 22 of 30 candidate source fields.
  - Prefix and shell are internally complete benchmark models; no actual global row is promoted.
  - The exact fixture fixed-point total remains
    `705466760524005697/3623878655999606784`, with positive arithmetic slack.
  - Geometric closure remains false because all six actual rows are still `fixture_derived`.

Machine-readable record:

- `certificates/prime-patching-independent-extraction-561-566.json`

Reproducibility files:

- `scripts/check_boundary_coordinate_seam_attempt.py`
- `scripts/check_independent_hall_microcensus.py`
- `scripts/check_threshold_source_layer_alignment.py`
- `scripts/check_node_graded_prefix_risk_dp.py`
- `scripts/check_nonprecancelled_shell_incidence.py`
- `scripts/check_independent_extraction_evidence_gate.py`
- `scripts/check_frontier_561_566.py`
- `proofs/prime-patching-parity-index-561-566-supplement.md`

The latest combined validation command is:

```bash
python scripts/check_frontier_561_566.py
```

All six new local diagnostics and `python -m py_compile` on the seven new scripts were run successfully before commit. The complete chained group runner was not re-executed in the disconnected local runtime because the repository cannot be cloned there; it invokes `scripts/check_frontier_555_560.py` first.

The exact new audit scope is 64 boundary seams, all 15 Hall pair partitions and 511 switch words, 1120 bounded primitive threshold normals, the complete corrected 30-node prefix risk distribution, all 30 shell orders with 500 repeated prefixes, and the exact coupled fixed point.

The final research-content head was remotely verified identical to `edddefecba87208f727d6c11aa63fb04cbb071f9`.

## Decisions and conventions

- Continue on `research/all-n-prime-patching`.
- Use sequential, reviewable commits and exact rational or integer arithmetic.
- Continue theorem numbering from `PP3cpx`.
- Every frontier tranche must include a stored certificate and checker.
- Keep the six-frontier organization stable.
- State explicitly that the all-`n` theorem remains open.
- Do not replace proof obligations with bounded computation.
- Track arithmetic feasibility separately from evidence provenance.
- Preserve the corrected prefix grading: `z` marks total nodes, not leaves.
- No global row may be promoted from an internally complete benchmark without a machine-checkable map to the prime-patching geometry.
- Negative extraction results and minimal counterexamples are valid frontier progress.

## Blockers

- Boundary: the direct diagonal four/seven seam model is now refuted. A realization needs different blocks, seam correctors, or a nontrivial permutation of row and column bands.
- Hall: the independent cylinder microcensus is exact, but its states and choices have no coordinate-level prime-patching decoder.
- Threshold: the source conservative matrix and transient layer alphabet are different fixtures. One aligned matrix/decomposition/observable/normal data set is required.
- Prefix: the grading is corrected and one structural risk is completely enumerated, but the actual geometric support/source risk coordinates remain undefined.
- Shell: a nonprecancelled full-rank benchmark is complete, but the true shell resources and incidence entries are still absent.
- Integration: all direct loss rows and coupling coefficients remain fixture-derived; finite small lengths remain downstream of genuine realization.

## Uncommitted work

- No completed theorem, script, certificate, proof supplement, or continuity change is left uncommitted.
- The latest research-content head was verified remotely before this handoff update.
- The repository connector cannot inspect unrelated external local clones.

## Exact next steps

1. Fetch this handoff and verify the branch head.
2. Start theorem numbering at `PP3cpx`.
3. Build `docs/567--572` around the next source-level conversions, not new abstract optimizers.
4. Boundary: enumerate band-permuted placements and bounded seam-corrector states for the explicit four/seven blocks; preserve a minimal long-range collinearity witness if no cycle exists.
5. Hall: attempt to decode the independent cylinder states into one existing rectangle, resource-star, or local matching gadget from the PP3 chain; otherwise prove a type mismatch.
6. Threshold: choose one conservative source matrix, enumerate all its valid permutation decompositions, attach observables to those exact layers, and compute the complete listed normal coverage.
7. Prefix: propagate the node-grading correction into the affected earlier chapters and add the first repository-defined geometric risk coordinate to the exact DP.
8. Shell: locate or define source-level geometric shell resources and derive incidence entries rather than choosing them; test a nonprecancelled word.
9. Integration: promote only fields with a source path, recompute the evidence meet and fixed point, and keep the closure gate closed otherwise.
10. Run the new diagnostics, `python -m py_compile scripts/*.py`, and the previous group runner when a complete runtime is available; re-verify the remote head and refresh this handoff.
