# The 392-kind installed construction stack has a chained 49-checker regression

This chapter records **CMR3834--CMR3845**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_392.py
```

## CMR3834 — immutable 47-checker base

The runner imports and verifies the 340-kind chained manifest:

```text
2450935467fa22953baeb20f539fdaae0b608680307cd6027501a3a39771560d
```

## CMR3835 — exact extension

```text
scripts/check_prime_power_protected_surplus_target_packing_ancestry.py
scripts/check_prime_power_installed_operation_registry_392.py
```

## CMR3836 — chained manifest seal

```text
0a4e90217d3caaa06bb57f8458939e7cce2f9c68bd05ccddea2ea1c3149321bd
```

## CMR3837 — exact checker count

The canonical manifest contains exactly 49 checkers.

## CMR3838--CMR3843 — deterministic validation

Every checker path is unique and compiles before execution. Every entry binds one exact SHA-256 contract and one unique theorem flag. Full execution requires a successful deterministic subprocess, one JSON object, exact contract equality, the expected flag equal to one and `all_n_proved_by_checker=0`. Static mode validates the complete manifest chain.

## CMR3844 — failure isolation

Missing files, invalid JSON, subprocess failures, contract mismatches and missing theorem flags report the exact checker path with stdout and stderr.

## CMR3845 — validation consequence

```text
installed_transition_regression_392_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The runner validates the installed finite stack and is not a proof certificate for the original construction.
