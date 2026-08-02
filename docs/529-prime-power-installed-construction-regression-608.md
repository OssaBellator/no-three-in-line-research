# The 608-kind installed construction stack has a chained 59-checker regression

This chapter records **CMR4070--CMR4085**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_608.py
```

## CMR4070--CMR4073 — exact manifest extension

The runner imports the complete 552-kind 57-checker manifest and appends:

```text
scripts/check_prime_power_inherited_coordinate_diagonal_block_ancestry.py
scripts/check_prime_power_installed_operation_registry_608.py
```

```text
base manifest = aab192d2cd4682e51be31a09285141377b5786d231006950a898f36cf43b39fd
59-checker manifest = 06e533ad5145c771fd0083ce94ca149124f10dcdd157043fd5bb2cea1facbb43
```

## CMR4074--CMR4081 — deterministic validation

Every checker path is unique and compiles before execution. Every manifest entry binds one exact contract and one theorem flag. Full execution requires successful deterministic subprocesses, one JSON report per checker, exact contract equality, the expected theorem flag equal to one and `all_n_proved_by_checker=0`.

Static mode validates the complete chained manifest without executing the mathematical checkers.

## CMR4082--CMR4083 — diagonal-block honesty enforcement

The runner explicitly rejects any checker report claiming:

```text
same_owner_diagonal_blocks_subcritical = 1
independent_line_kernel_sufficient = 1
global_target_collateral_inequality_proved = 1
all_n_proved_by_checker = 1
```

## CMR4084--CMR4085 — validation consequence

```text
installed_transition_regression_608_complete = 1
same_owner_diagonal_blocks_subcritical = 0
independent_line_kernel_sufficient = 0
global_target_collateral_inequality_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The runner source and chained manifest seal were validated locally. The complete 59-checker repository runner has not been executed locally, and no CI success is claimed.
