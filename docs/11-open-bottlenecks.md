# Open bottlenecks and execution roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. The authoritative theorem ledger
reaches **CMR3033**. The predecessor typed-transition endpoint **CMR2899** and
plain masked-host endpoint **CMR2839** remain part of the synchronized theorem
history.

Every final checker, finite theorem checker, bridge, fixture and regression
permanently reports or preserves:

```text
all_n_proved_by_checker = 0
```

A locator, source hash, finite census, context manifest, transition seal,
selector inequality, runtime manifest or workflow result is not evidence of the
all-`n` theorem.

## 2. Validation entrypoints

The installed construction stack is:

```text
python scripts/check_prime_power_required_prefix_parent_generation.py
python scripts/check_prime_power_asymmetric_residual_host_contraction.py
python scripts/check_prime_power_asymmetric_context_generation.py
python scripts/check_prime_power_asymmetric_target_dispatch.py
python scripts/check_prime_power_context_transition_registry.py
python scripts/check_prime_power_routing_change_context_ancestry.py
python scripts/check_prime_power_routing_change_history_payment.py
python scripts/check_prime_power_factor_child_product_ancestry.py
python scripts/check_prime_power_mixed_child_deletion_ancestry.py
python scripts/check_prime_power_forced_certificate_escape_ancestry.py
python scripts/check_prime_power_target_edge_return_ancestry.py
python scripts/check_prime_power_target_handoff_envelope_ancestry.py
python scripts/check_prime_power_recurrent_target_edge_deletion_ancestry.py
python scripts/check_prime_power_closure_envelope_transition_ancestry.py
python scripts/check_prime_power_installed_owner_scheduler_bank.py
python scripts/run_prime_power_installed_construction_regression.py
```

The legacy branch-wide and hard-core stack remains:

```text
python scripts/check_prime_power_canonical_frontier_roots.py --self-test
python scripts/check_prime_power_all_open_target_fixture.py --self-test
python scripts/test_prime_power_current_frontier_regression.py
python scripts/check_prime_power_canonical_prescription_partition.py
python scripts/check_prime_power_target_trigger_response_partition.py
python scripts/check_prime_power_canonical_target_dispatch.py
python scripts/check_prime_power_masked_host_parent_generation.py
python scripts/check_prime_power_hard_core_exchange_normal_form.py
python scripts/check_prime_power_hard_core_exchange_realisability.py
python scripts/check_prime_power_hard_core_two_point_classification.py
python scripts/check_prime_power_hard_core_collinear_backgrounds.py
python scripts/check_prime_power_hard_core_pivot_line_energy.py
python scripts/check_prime_power_hard_core_extremal_stability.py
python scripts/check_prime_power_hard_core_population_bridge.py --self-test
python -B -S -s scripts/check_prime_power_reproducible_runtime_manifest.py --self-test \
  --manifest artifacts/current-frontier-runtime.json
python scripts/run_prime_power_current_frontier_regression.py
python scripts/check_prime_power_final_support_handoff_frontiers_v2.py certificate.json
```

Dedicated Python 3.10/3.12 workflows include:

```text
.github/workflows/context-transition-frontier.yml
.github/workflows/routing-change-ancestry-frontier.yml
.github/workflows/factor-child-product-frontier.yml
.github/workflows/mixed-child-deletion-frontier.yml
.github/workflows/forced-certificate-escape-frontier.yml
.github/workflows/target-edge-return-frontier.yml
.github/workflows/target-handoff-envelope-frontier.yml
.github/workflows/recurrent-target-deletion-frontier.yml
.github/workflows/closure-envelope-transition-frontier.yml
.github/workflows/installed-owner-scheduler-frontier.yml
.github/workflows/installed-construction-regression.yml
```

Inspect actual workflow runs before claiming CI success.

## 3. T01: source truth remains open

The source registry binds literal UTF-8 statement text, hashes, source kinds and
typed verification artifacts. Genuine completion still requires authoritative
primary sources, stable locators, exact transcription, matching hashes, ordinary
mathematical verification and human review.

No sealed source record proves its statement true by itself.

## 4. T02: installed construction surface

CMR2888--CMR2899 provide typed local restrictions and contractions.
CMR2900--CMR2981 install routing, exact child products, mixed deletion,
forced-certificate escape, one returned-target operation, target handoff and the
fixed-envelope target chain.

CMR2982--CMR2993 install the fixed-owner recurrent entering-target deletion.
The avoidance matching survives the exact child, the complete target star is
destroyed, no new target is activated, and later recurrence requires
reintroduction or owner change.

CMR2994--CMR3007 install the complete closure-rematch envelope partition:

```text
inside current envelope -> internal rematch, same owner
outside current envelope -> strict ancestor expansion, changed owner
crossing target -> generated four-endpoint destruction and strict expansion
```

The exact envelope-depth chain has at most `h` strict expansions and `h+1`
epochs.

## 5. T02: installed owner and scheduler bank

CMR3008--CMR3021 enumerate twenty installed operation kinds and bind them to ten
checker contracts, theorem ancestry, seven owner-effect classes and eleven
payment/dispatch classes.

The registry proves only installed-bank exhaustiveness:

```text
installed_transition_kind_bank_exhaustive = 1
installed_operation_payment_assignment_complete = 1
```

It does not prove global construction completeness.

The CMR691--CMR719 nonrecurrent scheduler arithmetic is executable. For the
sample `d=4, p=2, h=3, lambda=3, mu=2`:

```text
owner stages = 912
owner edges = 12,272
owner-token labels = 73,632
owner certificates = 370,940
owner cell-target pairs = 113,992,704
fixed-envelope target bound = 666,624
coarse nonrecurrent scheduler bound = 115,043,458
```

## 6. T02: installed construction regression

CMR3022--CMR3033 add a contract-sealed fourteen-checker runner:

```text
python scripts/run_prime_power_installed_construction_regression.py
```

It compiles and executes every installed construction checker, requires one JSON
report, checks the exact contract digest and expected theorem flag, and enforces
`all_n_proved_by_checker = 0`.

Manifest digest:

```text
2fd61262229cbd866d978d7dcf5e19b607a5f81eb843d3d3a48046b598fa5e20
```

A passing regression validates the installed finite claims; it does not prove
that the installed bank is globally exhaustive.

## 7. Exact flags and current global blocker

```text
recurrent_target_edge_deletion_ancestry_proved = 1
closure_branch_envelope_transition_bank_exhaustive = 1
installed_transition_kind_bank_exhaustive = 1
installed_operation_payment_assignment_complete = 1
installed_nonrecurrent_scheduler_finite = 1
installed_transition_regression_complete = 1

all_owner_operations_proved = 0
all_scheduler_operations_proved = 0
all_restoration_operations_proved = 0
all_returned_edge_operations_proved = 0
all_envelope_operations_proved = 0
all_construction_ancestry_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The immediate T02 blocker is no longer construction arithmetic. It is proving
that the twenty installed kinds actually exhaust the original construction.
The audit must locate and install any remaining:

- owner-stage operation;
- rollback, restoration or returned-edge action;
- essential-return Hall-wall or unit-wall transition;
- recurrent scheduler dispatch; and
- envelope use outside the row-preserving closure-rematch bank.

Start with CMR727--CMR747: essential-return Hall batching, unit-wall
factorisation, and the finite factor tree. Then inspect the rollback/restoration
chapters CMR439--CMR521 for operations not already represented.

After every missing operation is installed, prove global transition
exhaustiveness. Only then can the finite installed stocks be combined with
closure of every recurrent endpoint to prove global termination.

## 8. T03--T04: genuine population

Every real T02 operation slot still needs literal parent/child contexts, points,
removals, survivor backgrounds, owner-fate witnesses, response families,
selector data, labelled vectors, routed credits, row loads and transitions.

Keep records `populated` rather than `proved` until exact T01/T02 source and
construction ancestry are established. T04 must assemble genuine recurrent
blocks and interfaces from those slots.

## 9. T05--T19: semantic and global quotient work

T05 must prove arbitrary-`n` construction coverage of the context class and all
geometry uses. T06--T18 must prove score, fate, state, transition, resource,
routed-credit, recurrence, scale, interface, rank, predicate and final-row
semantics. T19 must prove genuine global-family exhaustiveness.

## 10. T20--T21: exceptional chambers

All 232 T20 zero-selector chambers remain open. The finite T21 scalar selector
and population bridge are exact for supplied backgrounds, but record:

```text
actual_t03_population_supplied_by_bridge = 0
t21_semantic_chambers_proved = 0
```

All 20 hard-core semantic chamber arguments remain open.

## 11. T22--T43: final implications and review

All ten T22--T31 premise implications, all six T35--T40 handoff arguments, T41
ordinary mathematical review, T42 dossier sign-off and the T43 implication to
`D(n)=2n` remain open. T32--T34 remain documentary aggregation gates.

## 12. Immediate work order

1. Audit CMR727--CMR747 and CMR439--CMR521 against the twenty-kind registry.
2. Install every missing owner, restoration, returned-edge, Hall-wall and
   scheduler transition with literal contexts and exact payment.
3. Prove the resulting transition bank globally exhaustive.
4. Close all recurrent owner-edge, certificate and cell-target endpoints and
   prove global termination.
5. Populate and verify the required T01 source records and genuine T02/T03/T04
   populations.
6. Run T05--T21 on real records and prove the remaining rows, chambers,
   premises, handoffs and root theorem.

No local context checker, finite registry, regression runner, documentary
interface or runtime manifest substitutes for the missing mathematical proofs.
