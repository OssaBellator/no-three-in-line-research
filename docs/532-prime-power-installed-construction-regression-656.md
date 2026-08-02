# The 656-kind installed construction stack has a chained 61-checker regression

This chapter records **CMR4118--CMR4133**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_656.py
```

## CMR4118--CMR4121 — exact manifest extension

The runner imports the complete 608-kind 59-checker manifest and appends:

```text
scripts/check_prime_power_candidate_transversal_rook_capacity_ancestry.py
scripts/check_prime_power_installed_operation_registry_656.py
```

```text
base manifest = 06e533ad5145c771fd0083ce94ca149124f10dcdd157043fd5bb2cea1facbb43
61-checker manifest = 5678e89e0f0b73946471b3c99cb027448266715a5ae0b0ffc42636dd4aa9bd3d
```

## CMR4122--CMR4129 — deterministic validation

Every checker path is unique and compiles before execution. Every manifest entry binds one exact contract and one theorem flag. Full execution requires successful deterministic subprocesses, one JSON report per checker, exact contract equality, the expected theorem flag equal to one and `all_n_proved_by_checker=0`.

Static mode validates the complete chained manifest without executing the mathematical checkers.

## CMR4130--CMR4131 — quantitative honesty enforcement

The runner rejects any checker report claiming:

```text
uniform_cross_line_owner_policy_proved = 1
same_owner_diagonal_blocks_subcritical = 1
global_target_collateral_inequality_proved = 1
all_n_proved_by_checker = 1
```

## CMR4132--CMR4133 — validation consequence

```text
installed_transition_regression_656_complete = 1
uniform_cross_line_owner_policy_proved = 0
same_owner_diagonal_blocks_subcritical = 0
independent_line_kernel_sufficient = 0
global_target_collateral_inequality_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The runner source and chained manifest seal were validated locally. The complete 61-checker repository runner has not been executed locally, and no CI success is claimed.
