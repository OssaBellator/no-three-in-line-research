# Status and honesty ledger

**Last updated:** 2 August 2026

## External status

The classical no-three-in-line conjecture `D(n)=2n` remains open. This repository does **not** contain a complete proof.

The authoritative theorem ledger reaches **CMR4325**. Every checker, fixture, bridge, manifest and regression preserves:

```text
all_n_proved_by_checker = 0
```

## Canonical construction execution

```text
python scripts/run_prime_power_installed_construction_regression_902.py
```

```text
chained manifest = f8ab06f6f46e08b91b425c10e53c55779e66be9acea6bbc0017d7216130f4857
installed operation kinds = 902
bound checker contracts = 38
owner-changing kinds = 164
same-owner kinds = 738
installed checkers = 69
```

Newest direct entrypoints:

```text
scripts/check_prime_power_superlevel_budget_thin_auxiliary_ancestry.py
scripts/check_prime_power_installed_operation_registry_902.py
scripts/run_prime_power_installed_construction_regression_902.py
```

## Latest installed banks

### Through CMR4277 — source CMR1582--CMR1629

Shared return-selector assignment, line-clean integer budgets, critical-selector localization, prime-field support, fixed-interface/thin tables and labelled CRT gluing are installed as exact certificate interfaces.

### CMR4278--CMR4325 — source CMR1630--CMR1701

The installed bank now contains:

```text
combined return-selector superlevel matching and König-cover certificates
class-supported source/target cover compilers
universal strong, singleton and overlap line-clean budget floors
exact selector-capacity gaps and restoration caps
matching-level fixed-interface symmetry normalization
normalized thin response census through side five
exact nonforced rank-one/two/three thin probability caps
line-clean profile-capacity and overflow compilers
nonnegative rational auxiliary resolvent elimination
constructive rational/integer certificate lifting
```

The side-four thin caps are `3/4`, `2/3`, `1/2`; side-five caps are `2/3`, `2/5`, `1/4`. These are matching-level capacities, not complete geometric offspring certificates.

## Canonical contracts and seals

```text
superlevel/budget/thin/auxiliary checker:
e155ea311c24a9f04e1a603877190d1e60f9928a4607546635a9198344e53ad0

902-kind registry contract:
239245dca95e8a3936fd5700248af65f1534f706ac4aceccca7890c850a955ff

902-kind registry seal:
2c9bf1cc1b551a0560753b5d5de918abaa61e2d602d2ac2ce078ff247cdccdb4

69-checker manifest:
f8ab06f6f46e08b91b425c10e53c55779e66be9acea6bbc0017d7216130f4857
```

## Current exact flags

```text
superlevel_budget_thin_auxiliary_ancestry_proved = 1
installed_transition_kind_bank_902_exhaustive = 1
installed_payment_assignment_902_complete = 1
installed_transition_regression_902_complete = 1

return_superlevel_cover_globally_strict = 0
universal_line_clean_budgets_close_all_classes = 0
selector_capacity_classes_closed = 0
normalized_thin_geometric_rows_subcritical = 0
auxiliary_effective_core_subcritical = 0
same_owner_diagonal_blocks_subcritical = 0
global_target_collateral_inequality_proved = 0
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

## Exact next mathematical frontier

Continue in literal source order from CMR1702:

```text
docs/316-prime-power-prescription-rank-mass-conservation.md
docs/317-prime-power-line-clean-rank-mass-large-load-closure.md
docs/318-prime-power-owner-support-rank-mass-capacities.md
docs/319-prime-power-owner-support-large-load-closure.md
docs/320-prime-power-geometric-prescription-multiplicity-formulas.md
docs/321-prime-power-packed-secant-multiplicity-bounds.md
docs/322-prime-power-background-triple-multiplicity-charge.md
docs/323-prime-power-background-potential-multiplicity-bounds.md
docs/324-prime-power-line-energy-profile-census.md
```

The next success criterion is a strict large-load or owner-support closure, an exact geometric multiplicity bound, or a finite labelled certificate—not another undefined interface.

## Validation status

The checker contract, registry contract/census/seal and runner manifest were reproduced locally. The consolidated nine-verifier checker and complete 69-checker repository runner were not executed locally. Dedicated Python 3.10/3.12 workflows are configured, but no successful workflow run has been observed and CI success is not claimed.
