# Autoprompter continuity handoff

Checkpoint time: 2026-08-01 13:44 Australia/Melbourne

## Goal

Develop a rigorous all-`n` prime-patching route for the no-three-in-line research
program by advancing six linked frontiers:

1. boundary recleaning / marker-controller realization;
2. localized Hall transport and list decoding;
3. fractional direct-clean threshold layers;
4. support-chord repair words and constrained prefix codes;
5. clean-macro shell attenuation and scheduling;
6. global interaction/integration certificates.

The asymptotic all-`n` theorem remains open. Existing results are finite
reductions, exact certificates, conditional mechanisms, coordinate candidates,
source-typed fixtures, sharp finite correctors, and bounded obstructions; they
must not be described as a completed proof.

## Current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Branch: `research/all-n-prime-patching`
- Verified pre-checkpoint research head: `76f9cea37d661fcd9966e87d2d0bab81a04974d3`
- Pre-checkpoint head title: `Index composition source-generation theorems through docs 620`
- The branch was remotely verified identical to that commit before this refresh.
- Next available theorem identifier: `PP3cwd`.

## Completed work

The branch contains the cumulative six-frontier sequence through `docs/620`. The
latest tranche is `docs/615--620`:

- `docs/615-corrector-aware-boundary-transition-census.md`
  - Theorems `PP3cvl--PP3cvn`.
  - Reconstructs the four corrected six-block states.
  - Among 2,080 raw seventh-block attempts, exactly six have minimum conflict
    transversal four, with eighty-two minimum transversals total.
  - Under the lexicographically first transversal rule, exactly one attempt has a
    degree-preserving correction of size at most six.
  - The corrected seventh state has no raw eighth-block extension among 520
    radius-32 attempts.

- `docs/616-two-matching-spare-resource-hall-lemma.md`
  - Theorems `PP3cvo--PP3cvq`.
  - A residual `K_4,4` has 209 partial matchings.
  - All 43,681 ordered pairs of matching-shaped partner and source exclusions are
    audited; their 7,343 distinct unions retain at least two perfect matchings.
  - Every union survives deletion of any one additional allowed cell.
  - This gives an exact six-resource sufficient condition for conditional Hall
    completion.

- `docs/617-source-preserving-threshold-three-cycle-trades.md`
  - Theorems `PP3cvr--PP3cvt`.
  - The eight nearest legal degree-four matrices remain at entrywise distance six
    from the stored source matrix.
  - Every one is exactly a unit alternating three-cycle trade on three source rows
    and three action columns.
  - Such a trade would avoid the impossible positive-density fifth layer while
    preserving all row and column margins.

- `docs/618-synthetic-source-anchor-support-chords.md`
  - Theorems `PP3cvu--PP3cvw`.
  - Adds two explicit synthetic anchors to every unary-run line.
  - All 1,024 ordered compositions of eleven unary nodes have globally distinct
    anchor and insertion rows and columns, with zero mixed-run triples.
  - Every encoding has exactly eleven anchor-pair blockers.
  - The aggregate profile count is `1850332263780`.

- `docs/619-signed-permuted-shell-source-lattice.md`
  - Theorems `PP3cvx--PP3cvz`.
  - The recorded shell columns generate exactly the even-coordinate-sum integer
    lattice of index two.
  - Signed cancellation, simultaneous composition, and all cycle-coordinate
    permutations preserve the obstruction.
  - The bounded diagnostic audits 4,913 signed/permuted vectors.

- `docs/620-composition-source-generation-evidence-gate.md`
  - Theorems `PP3cwa--PP3cwc`.
  - Candidate field completion remains `24/30`.
  - The fixture fixed-point total remains
    `705466760524005697/3623878655999606784`, with positive slack
    `200502903475895999/3623878655999606784`.
  - All six actual rows remain `fixture_derived`; zero rows are promoted and
    geometric closure remains false.

Machine-readable record:

- `certificates/prime-patching-composition-source-generation-615-620.json`

Reproducibility files:

- `scripts/check_boundary_corrector_transition_state.py`
- `scripts/check_hall_two_matching_exclusion_lemma.py`
- `scripts/check_threshold_three_cycle_replacements.py`
- `scripts/check_prefix_source_anchor_chords.py`
- `scripts/check_shell_signed_permutation_lattice.py`
- `scripts/check_composition_source_generation_evidence_gate.py`
- `scripts/check_frontier_615_620.py`
- `proofs/prime-patching-parity-index-615-620-supplement.md`

The latest combined validation command is:

```bash
python scripts/check_frontier_615_620.py
```

All six new standalone diagnostics and `python -m py_compile` on the seven new
scripts passed in the local execution runtime before commit. The complete chained
runner was not re-executed locally because the repository cannot be cloned into
that runtime; it invokes `scripts/check_frontier_609_614.py` first.

## Decisions and conventions

- Continue on `research/all-n-prime-patching`.
- Use sequential, reviewable commits and exact rational or integer arithmetic.
- Continue theorem numbering from `PP3cwd`.
- Keep the six-frontier organization stable.
- Every tranche must include a stored certificate and checker.
- State explicitly that the all-`n` theorem remains open.
- Do not replace proof obligations with bounded computation.
- Track arithmetic feasibility separately from evidence provenance.
- Treat source-typed finite lifts, bounded correctors, and synthetic source
  geometries as intermediate evidence, not verified global rows.
- Negative results and minimal counterexamples are valid frontier progress.

## Current blockers

- Boundary: the corrected-state transition relation is nonempty, but the unique
  canonical corrected seventh state has no raw eighth extension. A periodic
  corrected-state cycle or another corrected transition is missing.
- Hall: the exact six-resource lemma requires four residual resources per side and
  both real restricted forbidden families to be partial matchings. The asymptotic
  host has not been shown to supply that structure.
- Threshold: source-preserving legal replacements reduce to eight unit
  three-cycle trades. No actual prime-patching source operation realizes one.
- Prefix: the two anchors per run give exact finite source-pair blockers, but they
  are synthetic and have no retained-source identification or removal credit.
- Shell: even signed cancellation and coordinate relabelling stay in the
  even-sum lattice. A genuinely new clean-macro incidence column is required.
- Integration: all direct rows and coupling coefficients remain fixture-derived;
  finite small lengths remain downstream of genuine realization.

## Uncommitted work

- No completed theorem, script, certificate, supplement, or continuity change is
  left uncommitted.
- The research head was remotely verified before this handoff refresh.
- The repository connector cannot inspect unrelated external local clones.

## Exact next steps

1. Fetch this handoff and verify the branch head.
2. Start theorem numbering at `PP3cwd`.
3. Build `docs/621--626` around repeated corrected transitions and actual source
   operation generation.
4. Boundary: allow an eighth block followed by a correction, enumerate all
   minimum transversals and degree-preserving correctors, and search the resulting
   corrected-state graph for a strongly connected or zero-drift component.
5. Hall: derive the six-resource condition from a superregular conditional host;
   prove a quantitative reserve/slack lemma forcing four unused resources per
   side and matching-shaped restricted partner and source exclusions.
6. Threshold: search the earlier source-operation catalogue for a realizable unit
   alternating three-cycle trade; otherwise derive an invariant proving those
   trades are absent from the recorded source moves.
7. Prefix: identify the two synthetic anchors of each run with actual retained
   source cells, verify source validity and row-column saturation, and price their
   removal credit.
8. Shell: search geometric clean-macro moves outside the recorded fixed-column
   family for the smallest odd-sum incidence column and compute its throughput
   and buffer cost; otherwise extend the source-catalogue absence theorem.
9. Integration: promote only rows with complete coordinate source paths;
   otherwise preserve the closed evidence gate and unchanged fixture fixed point.
10. Run all new diagnostics, Python compilation, the chained runner in a complete
    checkout, verify the remote head, and refresh this handoff.
