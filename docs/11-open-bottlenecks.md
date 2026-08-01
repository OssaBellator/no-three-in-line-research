# Open bottlenecks and execution roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. The authoritative theorem ledger reaches **CMR3121**. The predecessor typed-transition endpoint **CMR2899** and plain masked-host endpoint **CMR2839** remain part of the synchronized history.

Every checker, bridge, fixture and regression permanently reports or preserves:

```text
all_n_proved_by_checker = 0
```

No source hash, finite census, transition seal, registry digest, selector calculation, runtime manifest or workflow result proves the all-`n` theorem.

## 2. Validation entrypoints

The canonical installed construction runner is:

```text
python scripts/run_prime_power_installed_construction_regression_33.py
```

Its nineteen-checker manifest is sealed by:

```text
50b66679af79082ff57ec0926508482f1efb72eefd6fe0e620d41eb949890fca
```

Direct construction entrypoints include:

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
python scripts/check_prime_power_essential_return_unit_wall_ancestry.py
python scripts/check_prime_power_sparse_rollback_restoration_ancestry.py
python scripts/check_prime_power_extended_installed_operation_registry.py
python scripts/check_prime_power_rollback_optimal_face_scc_ancestry.py
python scripts/check_prime_power_installed_operation_registry_33.py
```

The legacy branch-wide and hard-core stack remains:

```text
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
python scripts/check_prime_power_canonical_frontier_roots.py --self-test
python scripts/check_prime_power_all_open_target_fixture.py --self-test
python scripts/test_prime_power_current_frontier_regression.py
python -B -S -s scripts/check_prime_power_reproducible_runtime_manifest.py --self-test \
  --manifest artifacts/current-frontier-runtime.json
python scripts/run_prime_power_current_frontier_regression.py
python scripts/check_prime_power_final_support_handoff_frontiers_v2.py certificate.json
```

Inspect actual workflow runs before claiming CI success.

## 3. T01 source truth

The source registry remains infrastructure only. Genuine completion requires authoritative primary sources, stable locators, exact transcription, matching hashes, ordinary mathematical verification and human review.

No sealed source record proves its statement true by itself.

## 4. T02 installed construction surface

### Local and factor operations

CMR2888--CMR3033 install typed local restriction/contraction, routing, exact child products, mixed deletion, certificate escape, returned targets, target handoff, recurrent target deletion, closure-envelope rematches and the first owner/payment registry.

### Essential-return unit walls

CMR3034--CMR3047 install:

```text
essential-return-unit-wall-extraction
essential-unit-wall-factor-split
unit-wall-local-edge-deletion
unit-wall-forced-target-dispatch
unit-wall-factor-tree-split
```

Every essential returned edge yields a canonical deficiency-one wall. The exact matching family factors over two children of total side `m-1`. Tree-wide split, edge, token, certificate and deletion stocks are finite.

### Sparse rollback restoration

CMR3048--CMR3059 install:

```text
minimum-rollback-restoration
cheap-rollback-certificate-escape
rollback-forced-core-contraction
rollback-recreated-conflict-support
```

A minimum rollback footprint restores an avoiding matching. Every restored edge is forced in the minimum avoiding host. Cheap rollback has exact token cost; larger rollback contracts a strict forced core.

### Minimum rollback face and SCC factors

CMR3084--CMR3097 install:

```text
rollback-minimum-cost-face-restriction
rollback-tight-host-restriction
rollback-optimal-scc-factor-split
marked-ancestor-reset-optimal-face
```

The tight host contains exactly the minimum rollback states. Its optimal-allowed core factors over strongly connected exchange components, and the same construction normalizes arbitrary marked ancestor-reset profiles.

## 5. Installed registry and exact boundary

The current installed registry has:

```text
33 unique operation kinds
13 exact checker contracts
24 owner-changing kinds
9 same-owner kinds
```

Current exact flags include:

```text
essential_return_unit_wall_ancestry_proved = 1
unit_wall_factorization_exact = 1
unit_wall_factor_tree_stock_exact = 1
sparse_rollback_restoration_ancestry_proved = 1
minimum_rollback_forced_core_exact = 1
rollback_minimum_cost_face_ancestry_proved = 1
rollback_tight_host_exact = 1
rollback_optimal_scc_factorization_exact = 1
marked_ancestor_reset_optimal_face_exact = 1
installed_transition_kind_bank_33_exhaustive = 1
installed_payment_assignment_33_complete = 1
installed_transition_regression_33_complete = 1

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

Installed-bank exhaustiveness is not global construction exhaustiveness.

## 6. Immediate T02 operation audit

The next source range is CMR462--CMR521. The following possible operations are not represented by the thirty-three kinds and must be inspected literally:

1. rollback level-cut and level-skeleton generation;
2. balanced residual-level factorization;
3. same-level source/target colour splitting;
4. mixed-colour alternating-cycle packing and sparse-tail deletion;
5. boundary fan/cut and theta-fan private-edge operations;
6. rooted-star, pair-cylinder and line-clean splices;
7. minimum-cost line-clean restoration and forced restoration cores;
8. weighted cheap-clean selection;
9. adaptive unavailable-edge absorption and row-column covers;
10. unavailable-star token splices;
11. absence-run, reintroduction and free-absorption temporal scheduler actions.

For every genuine action, install:

```text
literal parent context
literal child context or exact restricted family
theorem-derived owner effect
finite stock, reintroduction charge, strict descent, or mandatory scheduler continuation
contract seal and corruption rejection
```

Later construction chapters must then be audited for additional operations.

## 7. Global exhaustiveness blocker

After every operation has been installed, prove that every construction step belongs to exactly one registered kind. This requires a direct audit of the original construction definitions, not merely a complete list of checkers.

Any action requiring an unmodelled restriction must be isolated and added to the context schema rather than silently assigned to a nearby kind.

## 8. Global termination blocker

The current bank has many finite stocks and strict descents, but recurrent endpoints remain. A global theorem must close:

- recurrent routing edges;
- recurrent owner edges and certificates;
- recurrent Hall-wall signatures;
- repeated restored edges and rollback-active level cells;
- recurrent cell-target pairs;
- same-envelope target chains; and
- all mandatory scheduler dispatches.

Only after these endpoints are paid or shown to descend can the installed finite bounds imply branch termination.

## 9. T03--T04 population

Every real T02 operation still needs genuine slot records with literal contexts, points, removals, survivor backgrounds, owner-fate witnesses, response families, selector data, routed credits, row loads and transitions.

Records remain `populated`, not `proved`, until their T01 source and T02 ancestry are verified. T04 must assemble genuine recurrent blocks and interfaces from those records.

## 10. T05--T19 semantic work

T05 must prove arbitrary-`n` coverage. T06--T18 must prove score, fate, state, resource, routed-credit, recurrence, scale, interface, rank, predicate and final-row semantics. T19 must prove genuine global-family exhaustiveness.

## 11. T20--T21 exceptional chambers

All 232 T20 zero-selector chambers remain open. The finite T21 bridge remains exact only for supplied backgrounds and still reports:

```text
actual_t03_population_supplied_by_bridge = 0
t21_semantic_chambers_proved = 0
```

All 20 hard-core semantic chamber arguments remain open.

## 12. T22--T43 final implications

All ten T22--T31 premise implications, all six T35--T40 handoff arguments, T41 ordinary review, T42 dossier sign-off and the T43 implication to `D(n)=2n` remain open. T32--T34 remain documentary aggregation gates.

## 13. Immediate work order

1. Install every genuine CMR462--CMR521 operation absent from the thirty-three-kind registry.
2. Extend the registry and nineteen-checker regression after each installed bank.
3. Audit all later construction chapters for missing owner, restoration, return, envelope and scheduler actions.
4. Prove global transition-kind exhaustiveness.
5. Close all recurrent endpoints and prove global termination.
6. Populate and verify T01 sources and genuine T02/T03/T04 records.
7. Run T05--T21 on real populations.
8. Prove every remaining chamber, premise, handoff, review and root implication.

No local context checker, finite registry, regression runner, documentary interface or runtime manifest substitutes for the missing mathematical proofs.
