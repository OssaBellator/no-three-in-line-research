# Autoprompter continuity handoff

Checkpoint time: 2026-07-31 11:22 Australia/Melbourne

## Goal

Develop a rigorous all-`n` prime-patching route for the no-three-in-line research program by advancing six linked frontiers:

1. boundary recleaning / marker-controller realization;
2. localized Hall transport and list decoding;
3. fractional direct-clean threshold layers;
4. support-chord repair words and constrained prefix codes;
5. clean-macro shell attenuation and scheduling;
6. global interaction/integration certificates.

The asymptotic all-`n` theorem remains open. Existing results are finite reductions, exact certificates, and asymptotic or parametric closure mechanisms; they must not be described as a completed proof of the all-`n` theorem.

## Current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Branch: `research/all-n-prime-patching`
- Verified pre-checkpoint head: `9220efc72207153554d6ad821d5bfbb3f87bd43f`
- Pre-checkpoint head title: `Add repository continuity checkpoint`
- The branch was remotely verified identical to that commit before this refresh.
- Latest research-content head before continuity-only commits: `e97a9d92ecdd7fea86c9ef6c8d6bd76c3ea6ffd0` (`Index frontier reductions through docs 542`).
- Next available theorem identifier: `PP3cnd`.

## Completed work

The branch contains the cumulative six-frontier research sequence through `docs/542`, with exact diagnostics and parity-index supplements. The latest completed research tranche is `docs/537--542`:

- `docs/537-apery-certificates-for-marker-semigroups.md`
  - Theorems `PP3cml--PP3cmn`.
  - Apéry conductor tables, residue correction, and explicit action-rate meshes.
  - Stored fixture: critical lengths four and seven, `Ap(S,4)=(0,21,14,7)`, conductor 18, and exact cost `F(N)=N` for every `N>=18`.

- `docs/538-automaton-constrained-switching-for-hall-transfers.md`
  - Theorems `PP3cmo--PP3cmq`.
  - Max-product envelopes and switching-cycle rates for automaton-constrained Hall transfers.
  - Stored fixture forbids `BB`; eight blocks are the sharp one-percent horizon.

- `docs/539-common-box-concatenation-of-threshold-cycles.md`
  - Theorems `PP3cmr--PP3cmt`.
  - Common prefix boxes and arbitrary-concatenation interval discrepancy.
  - Stored fixture has three optimal phase pairs of width one.

- `docs/540-gaussian-profiles-for-regular-prefix-trees.md`
  - Theorems `PP3cmu--PP3cmw`.
  - Quasi-powers normality and a local Gaussian law for binary-node profiles.
  - Mean `n/3+O(1)` and variance `n/18+O(1)`.

- `docs/541-shared-reserve-pooling-for-shell-schedules.md`
  - Theorems `PP3cmx--PP3cmz`.
  - Exact pooled startup reserves and phase-torus optimization.
  - Stored pair has separate total reserve two but zero pooled reserve in three aligned phases.

- `docs/542-normal-fans-for-interaction-lattice-slices.md`
  - Theorems `PP3cna--PP3cnc`.
  - Rational normal fans and exact parametric optimizer formulas for lattice slices.
  - Stored fan has cones `alpha<beta`, `alpha=beta`, and `alpha>beta`.

Reproducibility files for the latest tranche:

- `scripts/check_apery_marker_certificates.py`
- `scripts/check_automaton_switched_hall_products.py`
- `scripts/check_threshold_cycle_concatenation.py`
- `scripts/check_regular_prefix_profile_clt.py`
- `scripts/check_shared_shell_reserves.py`
- `scripts/check_interaction_normal_fans.py`
- `scripts/check_frontier_537_542.py`
- `proofs/prime-patching-parity-index-537-542-supplement.md`

The latest combined validation command is:

```bash
python scripts/check_frontier_537_542.py
```

The recorded exact audit scope is 500 marker lengths, every allowed Hall word through length 20, all 12 threshold phase pairs with 350 repeated slots, every legal-tree profile through 200 leaves, all nine shell phase pairs with 100 repeated periods, and every interaction length through 300 against 120 integer weight pairs.

No theorem, script, or project-document change was started after the prior checkpoint. This refresh changes continuity metadata only.

## Decisions and conventions

- Continue on `research/all-n-prime-patching`; do not switch branches without an explicit repository decision.
- Use sequential, reviewable commits, normally theorem chapter first, then its exact checker, followed by a group runner and parity-index supplement.
- Preserve exact rational or integer arithmetic in diagnostics whenever possible.
- Every theorem receives a unique `PP3...` identifier; continue from `PP3cnd`.
- Every frontier tranche should include one exact stored fixture and a checker that reconstructs the claimed certificate.
- Keep the six-frontier organization stable so boundary, Hall, threshold, prefix-code, shell, and integration claims remain independently auditable.
- State explicitly that the all-`n` theorem remains open until a genuine global closure theorem is proved.
- Do not replace mathematical proof obligations with bounded computation; bounded audits support, but do not establish, asymptotic statements unless paired with a proved finite-state, semigroup, spectral, algebraic, or polyhedral closure argument.
- Prioritize cross-frontier compatibility over accumulating isolated refinements.

## Blockers

The central blocker is global closure: the current frontier theorems provide strong local and asymptotic mechanisms, but no theorem proves that all six certificates can be instantiated simultaneously for every sufficiently large `n` with compatible constants and then extended to every remaining small `n`.

More specifically:

- Boundary: connect marker semigroup and rate certificates to the exact geometric boundary defects arising in the prime-patching construction.
- Hall: derive a uniform reverse-load degree bound from the actual family of local syndrome gadgets used globally.
- Threshold: prove that common discrepancy boxes and conservative schedules preserve every geometric threshold inequality required by the final patch.
- Prefix codes: turn counting and profile abundance into an existence theorem with the exact risk and support constraints required globally.
- Shells: prove pooled reserves remain compatible with the true coupled shell incidence system, not only stored finite fixtures.
- Integration: combine the normal-fan or lattice-slice optimizer with the preceding five frontiers and produce one strict global feasibility or contraction margin.

## Uncommitted work

- No completed, reviewable in-session theorem, script, documentation, or continuity change is left uncommitted before this refresh.
- The remote branch was verified identical to `9220efc72207153554d6ad821d5bfbb3f87bd43f` before updating this file.
- No new project work was started during this checkpoint response.
- The repository connector cannot inspect unrelated external local clones; changes outside this connected branch are not represented here.

## Exact next steps

1. Fetch `AUTOPROMPTER_HANDOFF.md` and verify the branch head before beginning new work.
2. Start theorem numbering at `PP3cnd`.
3. Build the next tranche as `docs/543--548`, prioritizing a cross-frontier compatibility theorem rather than six isolated refinements.
4. Derive one parameter ledger listing, for every frontier, required input constants, produced output constants, denominator or period data, and strict slack.
5. Formulate an integration proposition in which boundary discrepancy, Hall reverse load, threshold rounding loss, prefix-code risk, shell reserve overhead, and interaction correction sum to strictly less than the global admissible margin.
6. Create one exact synthetic fixture exercising the entire ledger end to end; add a checker that rejects incompatible parameter choices and reconstructs a compatible choice.
7. Only after the compatibility ledger is proved, add frontier-specific refinements needed to make its inequalities hold for arbitrary sufficiently large `n`.
8. Run all new diagnostics, `python -m py_compile scripts/*.py`, and the latest prior group runner before committing.
9. Commit each reviewable file sequentially, then add a combined runner and parity-index supplement ending with the next unused theorem identifier.
10. Re-verify the final commit remotely and refresh this handoff at the next continuity checkpoint.
