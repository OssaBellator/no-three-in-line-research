# CMR691--CMR747 are covered by inherited owner, target-return and unit-wall operations

This chapter records **CMR3586--CMR3597**.

Coverage checker:

```text
scripts/check_prime_power_owner_target_wall_coverage.py
```

Contract:

```text
3038c3f03bb8485f5dd6c03efaa894a2354e675c74324bd1532c422f1c1a0feb
```

## CMR3586 — complete theorem interval

The checker assigns every theorem ID from CMR691 through CMR747 to one or more exact historical checker contracts. No theorem ID in the interval is uncovered.

## CMR3587 — descending-path owner binding

CMR691--CMR719 are bound to:

```text
scripts/check_prime_power_installed_owner_scheduler_bank.py
108802c0d4934c7b3d77cc972d5418a2d8b91a6cca9da78b49bc4ab58970ad26
```

## CMR3588 — target handoff and recurrent deletion binding

CMR698--CMR712 and CMR713--CMR719 are bound respectively to the exact target-handoff and recurrent-target deletion contracts.

## CMR3589 — returned-target binding

CMR720--CMR726 are bound to the returned-target edge checker contract:

```text
04a533666c90c2f13bcb18731e10e0bca4d6357a806f8be44ee47af6f90e2382
```

## CMR3590 — essential-return and unit-wall binding

CMR727--CMR747 are bound to the Hall-wall/factor-tree checker and its extended registry contract.

## CMR3591 — exact inherited operation set

Exactly eleven already installed operation kinds cover the operational content of CMR698--CMR747:

```text
target-handoff-internal
target-handoff-envelope-expansion
recurrent-target-entering-edge-deletion
returned-target-edge-restoration
returned-target-edge-redeletion
essential-target-contraction
essential-return-unit-wall-extraction
essential-unit-wall-factor-split
unit-wall-local-edge-deletion
unit-wall-forced-target-dispatch
unit-wall-factor-tree-split
```

## CMR3592 — no duplicate registration

The eleven inherited kinds are disjoint from the fifty CMR629--CMR690 operation identifiers added by the 188-kind registry. No duplicate operation is introduced.

## CMR3593 — owner-stage arithmetic revalidation

For sides `1,...,8` and recurrence thresholds `2,...,5`, the checker revalidates the exact CMR691--CMR695 host-stage, routing-change, owner-stage, owner-edge and owner-certificate formulas.

## CMR3594 — owner target-pair stock

The owner-labelled target-pair formula is checked against the exact owner-stage stock for a side-eight ambient parent.

## CMR3595 — unit-wall factor-tree stock

For factor sides `1,...,7`, the exact recursive split metrics are checked against the installed split, node, leaf, depth, edge-stock and certificate-stock bounds.

## CMR3596 — corruption rejection

Ten mutations are rejected, including interval gaps, missing checker bindings, duplicate or missing operation identifiers, false canonical registry contracts and upgraded honesty flags.

## CMR3597 — coverage consequence and honesty boundary

```text
cmr691_747_existing_operation_coverage_exact = 1
descending_path_owner_stock_revalidated = 1
target_return_unit_wall_coverage_exact = 1
no_duplicate_operation_registration_required = 1

global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

This is a source-to-existing-registry coverage seal. It does not establish global operation exhaustiveness beyond CMR747.
