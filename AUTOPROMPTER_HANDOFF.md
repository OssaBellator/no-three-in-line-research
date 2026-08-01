# Autoprompter continuity handoff

Checkpoint time: 2026-08-01 12:29 Australia/Melbourne

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
- Verified pre-checkpoint research head: `f42f7a1a2085c4fe77c11c3e97baaf75f235b4af`
- Pre-checkpoint head title: `Index completion-attempt theorems through docs 596`
- The branch was remotely verified identical to that commit before this refresh.
- Next available theorem identifier: `PP3ctj`.

## Completed work

The branch contains the cumulative six-frontier sequence through `docs/596`. The latest tranche is `docs/591--596`:

- `docs/591-saturation-preserving-boundary-refill-obstruction.md`
  - Theorems `PP3csr--PP3cst`.
  - Each of the four sharp three-deletion repairs has exactly three degree-preserving local refills.
  - All twelve exact row-and-column refills recreate a collinear triple.
  - A successful seam corrector must alter a wider resource neighbourhood, replace more points, use new block geometry, or change the preserved saturation invariant.

- `docs/592-complete-grid-hall-robustness-upper-bound.md`
  - Theorems `PP3csu--PP3csw`.
  - The twelve ordered distinct grid-pair geometries intrinsically split into six singleton-blocker and six double-blocker cases.
  - Every complete bijection from quotient choices to these geometries preserves that split.
  - One forbidden residual cell leaves either ten or eleven quotient choices; relabelling the same host cannot give uniform robustness.

- `docs/593-threshold-replacement-price-frontier.md`
  - Theorems `PP3csx--PP3csz`.
  - The eight nearest legal matrices split evenly between aligned-observable losses `(2,1)` and `(3,0)`.
  - Every replacement moves exactly three source-cell mass units.
  - With nonnegative prices `alpha,beta`, the exact frontier is `min(2 alpha+beta,3 alpha)` with switching wall `beta=alpha`.
  - No source residual inequality currently supplies those prices.

- `docs/594-convex-support-chord-embedding-mismatch.md`
  - Theorems `PP3cta--PP3ctc`.
  - Preorder subtree intervals form a laminar family.
  - Embedding encoded node `k` at `(k,k^2)` gives zero support-point collinear triples for every tree.
  - The exact positive aggregates `638045608200` ancestry edges and `4963626417750` interval span therefore do not determine geometric collinearity risk.

- `docs/595-minimal-coset-crossing-shell-action.md`
  - Theorems `PP3ctd--PP3ctf`.
  - Adding any nonnegative unit cycle vector completes the index-two source lattice to `Z^3`.
  - Exact target service `(12,10,8)` uses the odd action an even number of times; the smallest positive count is two.
  - Active controls rise from fifteen to sixteen, giving throughput cost `1/20` per twenty-slot period.
  - The minimum cycle-buffer `l_1` norm remains `2/5`.

- `docs/596-completion-attempt-evidence-gate.md`
  - Theorems `PP3ctg--PP3cti`.
  - Candidate source-field completion remains `23/30`.
  - No new actual coordinate source path is completed.
  - The fixture fixed-point total remains
    `705466760524005697/3623878655999606784` with positive slack
    `200502903475895999/3623878655999606784` below one quarter.
  - All six actual direct rows remain `fixture_derived`; zero rows are promoted.

Machine-readable record:

- `certificates/prime-patching-completion-attempts-591-596.json`

Reproducibility files:

- `scripts/check_boundary_saturation_refill_obstruction.py`
- `scripts/check_hall_bijection_robustness_bound.py`
- `scripts/check_threshold_replacement_price_frontier.py`
- `scripts/check_prefix_convex_chord_embedding.py`
- `scripts/check_shell_coset_crossing_action.py`
- `scripts/check_completion_attempt_evidence_gate.py`
- `scripts/check_frontier_591_596.py`
- `proofs/prime-patching-parity-index-591-596-supplement.md`

The latest combined validation command is:

```bash
python scripts/check_frontier_591_596.py
```

All six new standalone diagnostics and `python -m py_compile` on the seven new scripts passed in the local execution runtime before commit. The complete chained runner was not re-executed locally because the repository cannot be cloned into that runtime; it invokes `scripts/check_frontier_585_590.py` first.

## Decisions and conventions

- Continue on `research/all-n-prime-patching`.
- Use sequential, reviewable commits and exact rational or integer arithmetic.
- Continue theorem numbering from `PP3ctj`.
- Keep the six-frontier organization stable.
- Every tranche must include a stored certificate and checker.
- State explicitly that the all-`n` theorem remains open.
- Do not replace proof obligations with bounded computation.
- Track arithmetic feasibility separately from evidence provenance.
- Treat exact completion obstructions and conditional lattice repairs as intermediate evidence, not verified global rows.
- Negative results and minimal counterexamples are valid frontier progress.

## Current blockers

- Boundary: exact refill inside only the three deficient columns and two deficient rows is impossible. A wider-neighbourhood replacement or different block/seam geometry is required.
- Hall: complete bijective coverage of the current `4 x 4` pair host necessarily contains six singleton-blocker choices. Uniform robustness requires a larger or richer residual host.
- Threshold: every nearest legal matrix loses aligned resource by `(2,1)` or `(3,0)`. No source inequality supplies the required price vector.
- Prefix: the canonical convex coordinate model has zero collinearity despite positive interval risk. Actual support-line incidence or endpoint reuse remains undefined.
- Shell: a unit odd-coset action repairs the lattice conditionally but has no source-level clean-macro realization and costs `1/20` throughput without reducing buffer.
- Integration: all direct rows and coupling coefficients remain fixture-derived; finite small lengths remain downstream of genuine realization.

## Uncommitted work

- No completed theorem, script, certificate, supplement, or continuity change is left uncommitted.
- The research head was remotely verified before this handoff refresh.
- The repository connector cannot inspect unrelated external local clones.

## Exact next steps

1. Fetch this handoff and verify the branch head.
2. Start theorem numbering at `PP3ctj`.
3. Build `docs/597--602` around structural enlargements rather than relabellings of the obstructed finite models.
4. Boundary: enlarge the repair neighbourhood by one additional row or column resource, enumerate minimum replacement size, and require restored saturation plus full inherited-line legality.
5. Hall: search the smallest larger coordinate host whose twelve decoded choices all have residual blocker number at least two; retain an exact impossibility certificate if `4 x 5` or `5 x 4` is insufficient.
6. Threshold: search the repository for a genuine residual inequality yielding fixed/forward prices; otherwise derive the complete dual cone that would make either `(2,1)` or `(3,0)` branch affordable.
7. Prefix: construct the smallest nonconvex or endpoint-reusing support geometry that produces a nonzero collinearity census and extend the exact DP to that incidence coordinate.
8. Shell: search source clean-macro actions for an odd-sum cycle vector; if one exists, derive its cost and recompute the shell row, otherwise prove a source-type absence over the recorded action catalogue.
9. Integration: promote only rows with complete coordinate source paths; otherwise preserve the closed evidence gate and unchanged fixture fixed point.
10. Run all new diagnostics, Python compilation, the chained runner in a complete checkout, verify the remote head, and refresh this handoff.
