# The one-hundred-thirty-two-kind installed construction stack has a chained thirty-six-checker regression

This chapter records **CMR3502--CMR3513**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_132.py
```

## CMR3502 — immutable 117-kind base

The runner imports the complete 34-checker manifest from the 117-kind runner and verifies:

```text
d259fb78a7b8a2ccbf7387c3fdd7a780b1e21f0366179c08af5ebb068cda3507
```

## CMR3503 — exact extension

```text
scripts/check_prime_power_protected_interface_execution_ancestry.py
scripts/check_prime_power_installed_operation_registry_132.py
```

## CMR3504 — chained manifest seal

```text
260cc38054f3ecfede323d6057bbbecad46bb191e90410b6a4523479cc6b696d
```

## CMR3505 — exact checker count

The canonical manifest contains exactly 36 checkers.

## CMR3506--3511 — validation contract

The runner enforces unique paths and flags, source existence, Python compilation, exact SHA-256 contracts, deterministic execution, one JSON report, expected theorem flags, and permanent `all_n_proved_by_checker = 0`. `--static-only` validates the chained manifest and source tree without running finite regressions.

## CMR3512 — failure isolation

Full execution reports the exact failing checker with captured stdout and stderr.

## CMR3513 — validation consequence

```text
installed_transition_regression_132_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

A passing run validates only the installed finite claims and registry bindings.
