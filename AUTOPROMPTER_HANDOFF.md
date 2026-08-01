# Autoprompter continuity handoff

Checkpoint time: 2026-08-01 12:15 Australia/Melbourne

## Goal

Develop a rigorous all-`n` prime-patching route for the no-three-in-line research program by advancing six linked frontiers:

1. boundary recleaning / marker-controller realization;
2. localized Hall transport and list decoding;
3. fractional direct-clean threshold layers;
4. support-chord repair words and constrained prefix codes;
5. clean-macro shell attenuation and scheduling;
6. global interaction/integration certificates.

The asymptotic all-`n` theorem remains open. Existing results are finite reductions, exact certificates, conditional mechanisms, coordinate candidates, source bridges, repair catalogues, and bounded obstructions; they must not be described as a completed proof.

## Current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Branch: `research/all-n-prime-patching`
- Verified pre-checkpoint research head: `6bfb17e7aa2a2f0cc6795c25a883a645e8ebebd6`
- Pre-checkpoint head title: `Index replacement-search theorems through docs 590`
- The branch was remotely verified identical to that commit before this refresh.
- Next available theorem identifier: `PP3csr`.

## Completed work

The branch contains the cumulative six-frontier sequence through `docs/590`. The latest tranche is `docs/585--590`:

- `docs/585-three-point-boundary-seam-repair-catalogue.md`
  - Theorems `PP3crz--PP3csb`.
  - Reconstructs the eight radius-32 five-block survivors and all 4160 sixth-block attempts.
  - No extension is repairable by one or two point deletions.
  - Exactly four symmetric extensions are repairable by three deletions.
  - Each successful repair removes old points from three columns and two rows, leaving a five-resource saturation defect.

- `docs/586-single-exclusion-robustness-of-hall-grid-decoder.md`
  - Theorems `PP3csc--PP3cse`.
  - Six decoded Hall pairs have one legal matching extension and six have two.
  - Minimum residual-cell blocker size is respectively one and two.
  - Exactly six quotient choices survive every single residual-cell exclusion.
  - Microscopic orientation does not change the decoded pair and cannot repair the fragile choices.

- `docs/587-nearest-legal-conservative-threshold-matrix.md`
  - Theorems `PP3csf--PP3csh`.
  - Enumerates all 5985 four-layer multisets from the eighteen legal permutation layers.
  - The nearest legal conservative matrices have entrywise `l_1` distance six from the stored source matrix.
  - Exactly eight matrices attain the bound.
  - A canonical replacement has a legal four-layer decomposition and minimum fixed/forward prefix discrepancy one, attained by eight orderings.

- `docs/588-ancestry-labelled-support-interval-risk.md`
  - Theorems `PP3csi--PP3csk`.
  - Adds parent-child incidence and canonical inorder interval span to the exact prefix DP.
  - At the thirty-leaf, nine-binary profile, family size remains `168212023980`.
  - Aggregate nesting-edge count is `638045608200`, mean `110/29`.
  - Aggregate interval span is `4963626417750`, mean `7186475/243542`.
  - The coordinate label is exact for the encoding but is not yet an actual grid support chord.

- `docs/589-index-two-shell-resource-lattice-obstruction.md`
  - Theorems `PP3csl--PP3csn`.
  - The `docs/517` action-to-cycle incidence matrix has determinant two.
  - Its integer image is exactly the cycle vectors of even coordinate sum.
  - Unit cycle resources have half-integral action preimages, so the identity-debt model is not integrally type-compatible.
  - The stored period `(5,7,3)` and buffer `(2/5,0,0)` remain valid in the source lattice.

- `docs/590-replacement-search-evidence-gate.md`
  - Theorems `PP3cso--PP3csq`.
  - Records the five exact replacement outcomes.
  - Candidate source-field completion remains `23/30`.
  - All six direct ledger rows remain `fixture_derived`; zero rows are promoted.
  - The exact fixture fixed-point total remains
    `705466760524005697/3623878655999606784`, with positive slack
    `200502903475895999/3623878655999606784` below one quarter.

Machine-readable record:

- `certificates/prime-patching-replacement-search-585-590.json`

Reproducibility files:

- `scripts/check_boundary_three_point_seam_repair.py`
- `scripts/check_hall_single_exclusion_robustness.py`
- `scripts/check_nearest_legal_threshold_matrix.py`
- `scripts/check_prefix_ancestry_span_dp.py`
- `scripts/check_shell_index_two_resource_lattice.py`
- `scripts/check_replacement_evidence_gate.py`
- `scripts/check_frontier_585_590.py`
- `proofs/prime-patching-parity-index-585-590-supplement.md`

The latest combined validation command is:

```bash
python scripts/check_frontier_585_590.py
```

All six new standalone diagnostics and `python -m py_compile` on all new scripts passed in the local execution runtime before commit. The complete chained runner was not re-executed locally because the repository cannot be cloned into that runtime; it invokes `scripts/check_frontier_579_584.py` first.

## Decisions and conventions

- Continue on `research/all-n-prime-patching`.
- Use sequential, reviewable commits and exact rational or integer arithmetic.
- Continue theorem numbering from `PP3csr`.
- Keep the six-frontier organization stable.
- Every tranche must include a stored certificate and checker.
- State explicitly that the all-`n` theorem remains open.
- Do not replace proof obligations with bounded computation.
- Track arithmetic feasibility separately from evidence provenance.
- Treat sharp repair catalogues and nearest replacements as intermediate evidence, not verified global rows.
- Negative results and minimal counterexamples are valid frontier progress.

## Current blockers

- Boundary: a sixth block can be obtained after three point deletions, but the repair leaves deficits on three columns and two rows. A saturation-preserving refill or replacement catalogue is still missing.
- Hall: half of the decoded pairs are destroyed by one residual-cell exclusion. The actual endpoint host and its exclusion table remain unidentified.
- Threshold: a fully legal four-layer matrix exists only after moving at least three units of source-cell mass. No prime-patching inequality source justifies that replacement yet.
- Prefix: ancestry-aware interval spans are exact, but the canonical inorder intervals are not embedded as coordinate-level support chords.
- Shell: the stored action system reaches only the even-sum cycle-resource lattice. Actual clean-macro resources must be placed in that lattice or require an additional coset-crossing action.
- Integration: all direct rows and coupling coefficients remain fixture-derived; finite small lengths remain downstream of genuine realization.

## Uncommitted work

- No completed theorem, script, certificate, supplement, or continuity change is left uncommitted.
- The research head was remotely verified before this handoff refresh.
- The repository connector cannot inspect unrelated external local clones.

## Exact next steps

1. Fetch this handoff and verify the branch head.
2. Start theorem numbering at `PP3csr`.
3. Build `docs/591--596` around completion attempts for the new finite obligations.
4. Boundary: enumerate point replacements or refill cells for the four sharp three-deletion repairs; require restoration of row and column saturation and recheck all inherited lines.
5. Hall: combine the robust-subset census with one explicit host exclusion pattern; search alternative quotient-to-cell maps maximizing the minimum blocker number.
6. Threshold: enumerate the eight nearest legal matrices against candidate source-cell prices and identify whether any mass move can be charged by an existing residual inequality.
7. Prefix: embed canonical inorder intervals into an explicit support-chord coordinate model and compare interval span with actual collinearity conflicts.
8. Shell: search for a minimal additional action whose cycle vector crosses the odd-sum coset, then recompute buffers and the shell ledger row conditionally.
9. Integration: promote only rows with complete coordinate source paths; otherwise preserve the closed evidence gate and unchanged fixture fixed point.
10. Run all new diagnostics, Python compilation, the chained runner in a complete checkout, verify the remote head, and refresh this handoff.
