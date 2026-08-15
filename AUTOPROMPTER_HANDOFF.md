# Autoprompter continuity handoff

## Current goal

Continue PR #33, `Audit exact recurrent side-four lineage and Lyapunov boundary`, without promoting symbolic side-four results into physical recurrence claims that the repository does not prove.

Keep the exact audit chain executable and reject-by-default while the physical occurrence/source frontier remains unresolved.

## Repository state

```text
repository = OssaBellator/no-three-in-line-research
active PR = #33
base branch = research/all-n-composite-modulus
base head = 0194af18247a81ff989c9e73bd7742b32072fa78
work branch = research/exact-recurrent-lyapunov-audit
current head before this handoff refresh = ad1565f42d5f394eac59b302e8566356a50e40e1
PR state = open, draft, mergeable
base ancestry = integrated; branch is 0 commits behind base
```

The no-three-in-line conjecture is not claimed. Physical realization, legal physical transitions, recurrent child rows, a strict Lyapunov certificate, global termination, and `all_n_proved_by_checker` remain unproved/zero.

## CI repair completed on 2026-08-15

Three concrete defects were fixed on the exact-audit branch:

1. `scripts/check_exact_recurrent_first_host_alternating_lineage_import.py`
   - invalid `update(3012=1)` mutation
   - replaced by `update({"3012": 1})`
   - commit `2969f35d52bcd7d16a8bcc9792ad73710094d307`

2. `scripts/check_exact_recurrent_first_host_selector_boolean_boundary.py`
   - invalid `update(2031="r20")` mutation
   - replaced by `update({"2031": "r20"})`
   - commit `9bdbd2c1ddd1684ad580478d5433f9d5453928ea`

3. `data/exact_recurrent_first_host_evidence_scope_overlap_obstruction.json`
   - numerical counts/floors matched the deterministic checker, but ten registry digests were stale
   - regenerated from the committed checker without changing proof claims
   - commit `e0e7040ac0977fc7830aa3dd879e33cbadc99acc`

Targeted run `31853642404` on `e0e7040a...` completed successfully on Python 3.10 and 3.12. Every exact-audit stage passed, including `Check evidence-scope overlap obstruction`. The CI-repair thread is closed at that substantive head.

## Base-branch integration completed on 2026-08-15

PR #33 had become `mergeable_state = dirty` because `research/all-n-composite-modulus` had advanced independently from the old merge base.

The conflict analysis established:

- the base branch changed many side-four support files plus `AUTOPROMPTER_HANDOFF.md`, `STATUS.md`, and `docs/11-open-bottlenecks.md`;
- the exact-audit branch changed the branch-local `AUTOPROMPTER_HANDOFF.md` and added its exact-recurrent artifacts;
- the handoff was the only overlapping textual conflict requiring manual policy.

The integration was performed without retargeting PR #33 and without discarding either branch's support artifacts:

```text
temporary handoff alignment commit = 5ba1371c5caa74387a10c01ce1af5ee7eba6ee82
temporary integration PR = #34
GitHub merge commit = 1fc0f8d804124809a685d2832aa667a14220b1ab
exact-audit handoff restore commit = ad1565f42d5f394eac59b302e8566356a50e40e1
```

After the merge, comparison against `research/all-n-composite-modulus` reports:

```text
status = ahead
behind_by = 0
merge base = 0194af18247a81ff989c9e73bd7742b32072fa78
```

The PR no longer proposes deletion of the base-only side-four workflows, data, docs, or checker files. PR #33 is mergeable again.

## Current post-integration CI boundary

Restoring the exact-audit handoff triggered a broad PR workflow fan-out on head `ad1565f4...`.

At the time of this handoff refresh, relevant runs include:

```text
31854221384  Exact recurrent first-host alternating lineage import  queued
31854221385  Exact recurrent Lyapunov audit                         queued
31854221416  Exact recurrent first-host physical fibre gate         queued
31854221473  Side-four raw-fibre lineage and selector manifests     queued
31854221592  Installed operation registry 1166                      queued
31854221460  Installed construction regression 1166                 queued
```

Many additional exact-recurrent, installed-regression, and side-four support workflows are also queued. Do not claim the integrated head green until the relevant runs complete.

If a post-integration run fails, fix only the concrete checker/artifact demonstrated by the failure. Do not change mathematical proof claims merely to satisfy CI.

## Exact physical proof boundary

For first residual host `s4-75b04c45c1c8eac2`:

```text
required physical fields = 16
source-backed physical fields = 0
physical occurrence records = 0
```

The chart-safe symbolic analysis, restoration-menu calculations, selector calculations, scalar covers, route-cover admission, and evidence-scope accounting are exact as symbolic/conditional statements. They do not establish physical occurrence coverage or recurrence closure.

The evidence-scope gate remains:

```text
current minimum safe label evidence slots = 11
current minimum safe menu evidence slots = 12
accepted evidence-sharing theorems = 0
```

Identical field names are not permission to merge certificate-instance obligations. Any reduction requires an explicit source-backed sharing/uniformity theorem satisfying the scope-preservation gate.

## Post-CI physical-source recheck

The integrated all-n base contains several artifacts that look superficially close to the first-host source requirement, but they still do not promote the first host physically:

- `data/prime_power_side_four_blocker_actual_background_sample_batch.json` is explicitly an integer-lattice blocker sample with `global_recurrent_state_claim = 0`.
- `data/prime_power_side_four_recurrent_state_population_table.json` has empty parent and child populations and `first_manifest_record_populated = 0`.
- `data/prime_power_side_four_population_record_candidate.json` has `candidate = null`.
- `data/prime_power_side_four_blocker_3210_collision_semantic_obstruction.json` marks `global_transition_occurrence_witness` missing and `global_transition_occurrence_complete = 0`.

This negative source audit was recorded on issue #18 in comment `5299523781`.

No symbolic restoration/route certificate should be added as a substitute for missing physical evidence.

## Mandatory physical frontier

The next mathematical promotion requires repository evidence supplying at least one of:

- a source-backed empty-domain theorem for the relevant physical occurrence domain;
- a complete or quantified physical occurrence batch;
- a physical chart/exterior-count theorem that reduces the remaining occurrence worklist.

For recurrence import, the source must additionally establish the physically legal directed transition domain and persistent owner identities, then populate accepted routes/capacities or equivalent strict-potential/output evidence and operation/child-row congruence.

Do not infer these facts from synthetic fixtures, symbolic restoration menus, matching field names, abstract alternating-core contracts, operation-kind registries, or coordinate/sample artifacts that explicitly disclaim global recurrence occurrence.

## Current proof flags

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

First inspect the post-integration runs on the current head, especially `31854221384` and `31854221385`.

- If either fails, repair only the demonstrated integration/checker defect and rerun.
- If both pass, the branch-integration thread is complete. Return to issue #18 and wait for repository-backed occurrence-faithful evidence before making another substantive mathematical promotion.

The existing 16-field physical batch gate and 12-field-per-edge transition-domain gate are the required ingestion path for any such new evidence.
