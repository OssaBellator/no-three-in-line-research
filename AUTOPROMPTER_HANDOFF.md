# Autoprompter continuity handoff

## Current goal

Continue PR #33, `Audit exact recurrent side-four lineage and Lyapunov boundary`, without promoting symbolic side-four results into physical recurrence claims that the repository does not prove.

The immediate engineering objective is to keep the exact audit chain executable and reject-by-default while the physical occurrence/source frontier remains unresolved.

## Repository state

```text
repository = OssaBellator/no-three-in-line-research
active PR = #33
base branch = research/all-n-composite-modulus
work branch = research/exact-recurrent-lyapunov-audit
substantive audit head before this handoff refresh = e0e7040ac0977fc7830aa3dd879e33cbadc99acc
PR state = open, draft
```

Recheck mergeability on the current head rather than carrying forward a cached value.

The no-three-in-line conjecture is not claimed. Physical realization, legal physical transitions, recurrent child rows, a strict Lyapunov certificate, global termination, and `all_n_proved_by_checker` remain unproved/zero.

## Continuation performed on 2026-08-15

The prior handoff existed on the PR branch but predated the current exact recurrent audit work. Repository/CI evidence was used to reconcile it against the active branch.

Three concrete CI defects were fixed:

1. `scripts/check_exact_recurrent_first_host_alternating_lineage_import.py`
   - invalid numeric keyword mutation `update(3012=1)`
   - replaced by mapping update `update({"3012": 1})`
   - commit `2969f35d52bcd7d16a8bcc9792ad73710094d307`

2. `scripts/check_exact_recurrent_first_host_selector_boolean_boundary.py`
   - invalid numeric keyword mutation `update(2031="r20")`
   - replaced by mapping update `update({"2031": "r20"})`
   - commit `9bdbd2c1ddd1684ad580478d5433f9d5453928ea`

3. `data/exact_recurrent_first_host_evidence_scope_overlap_obstruction.json`
   - committed numerical counts/floors matched the checker, but ten registry digests were stale relative to the deterministic compiler
   - regenerated the manifest from the committed checker without changing proof claims
   - commit `e0e7040ac0977fc7830aa3dd879e33cbadc99acc`

A scan of the current PR patch found no remaining `.update(<digit>...)` mutation syntax pattern.

## CI evidence

Run `31853150417` verified the first syntax fix on Python 3.10 and 3.12, then exposed the selector-boundary syntax defect.

Run `31853246012` on head `9bdbd2c1...` passed every exact-audit stage through:

```text
alternating-core lineage import
side-four arithmetic profile import
safe signature quotient and symmetry
restoration menu/selector audits
selector-face worklist/source/leverage
minimizer-face scalar/cost audits
selector Boolean boundary
scalar route cover
menu interaction potential
alternating route budget
closure route source gate
route-cover admission
transition-domain source audit
state-exclusion leverage
action-family leverage/congruence/source import
mixed-source certificate leverage
hybrid source-certificate antichain
```

Both Python versions then failed only at `Check evidence-scope overlap obstruction` because the stored JSON did not equal the checker-recomputed manifest. The substantive summaries matched; the stale registry digests were regenerated in `e0e7040a...`.

Targeted run `31853642404` was triggered for `e0e7040a...`; at the time of this handoff refresh its Python 3.10 and 3.12 jobs were queued, so do not claim that head green until the run result is observed.

## Exact proof boundary to preserve

For the first residual host `s4-75b04c45c1c8eac2`:

```text
required physical fields = 16
source-backed physical fields = 0
physical occurrence records = 0
```

The chart-safe symbolic analysis remains exact, including the restoration-menu/selector calculations and route-cover classifications, but it does not establish physical occurrence coverage or recurrence closure.

The evidence-scope gate remains:

```text
current minimum safe label evidence slots = 11
current minimum safe menu evidence slots = 12
accepted evidence-sharing theorems = 0
```

Identical field names are not permission to merge certificate-instance obligations. Any reduction of those safe floors requires an explicit source-backed sharing/uniformity theorem satisfying the scope-preservation gate.

## Mandatory physical frontier

The next mathematical promotion must be supported by repository evidence supplying at least one of:

- a source-backed empty-domain theorem for the relevant physical occurrence domain;
- a complete or quantified physical occurrence batch;
- a physical chart/exterior-count theorem that reduces the remaining occurrence worklist.

For recurrence import, the source must additionally establish the physically legal directed transition domain and persistent owner identities, then populate accepted routes/capacities or equivalent strict-potential/output evidence and operation/child-row congruence.

Do not infer any of these from synthetic fixtures, symbolic restoration menus, matching field names, or abstract alternating-core contracts.

## Current flags

```text
physical_chart_confinement_proved = 0
physical_occurrence_coverage_proved = 0
physical_transition_legality_proved = 0
persistent_owner_identity_proved = 0
boundary_capacities_populated = 0
recurrent_child_rows_populated = 0
strict_lyapunov_certificate_proved = 0
global_termination_proved = 0
all_n_proved_by_checker = 0
```

## Next executable step

Inspect targeted run `31853642404` for head `e0e7040a...` first. If it fails, fix only the concrete failing checker/artifact demonstrated by the log. If it passes, return to the physical-source frontier rather than extending the symbolic audit surface without new source evidence.
