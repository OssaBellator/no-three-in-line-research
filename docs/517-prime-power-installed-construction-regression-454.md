# The 454-kind installed construction stack has a chained 51-checker regression

This chapter records **CMR3882--CMR3893**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_454.py
```

## CMR3882 — immutable 49-checker base

The runner imports and verifies the 392-kind chained manifest:

```text
0a4e90217d3caaa06bb57f8458939e7cce2f9c68bd05ccddea2ea1c3149321bd
```

## CMR3883 — exact extension

```text
scripts/check_prime_power_selected_scheduler_terminal_wall_ancestry.py
scripts/check_prime_power_installed_operation_registry_454.py
```

## CMR3884 — chained manifest seal

```text
b5766866f7d04d687fcb56cf32d1f107be34c28fc34be1eae8b75039c269edbe
```

## CMR3885 — exact checker count

The canonical manifest contains exactly 51 checkers.

## CMR3886--CMR3891 — deterministic validation

Every checker path is unique and compiles before execution. Every entry binds one exact SHA-256 contract and one unique theorem flag. Full execution requires a successful deterministic subprocess, one JSON object, exact contract equality, the expected flag equal to one and `all_n_proved_by_checker=0`. Static mode validates the complete manifest chain.

## CMR3892 — failure isolation

Missing files, invalid JSON, subprocess failures, contract mismatches and missing theorem flags report the exact checker path with stdout and stderr.

## CMR3893 — validation consequence

```text
installed_transition_regression_454_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The runner validates the installed finite stack and is not a proof certificate for the original construction.
