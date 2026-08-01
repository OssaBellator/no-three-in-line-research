# The 472-kind installed construction stack has a chained 53-checker regression

This chapter records **CMR3930--CMR3941**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_472.py
```

## CMR3930--CMR3933 — manifest chain

The runner imports the 454-kind 51-checker manifest, adds the universal/base checker and 472-kind registry, and seals the resulting manifest:

```text
base = b5766866f7d04d687fcb56cf32d1f107be34c28fc34be1eae8b75039c269edbe
manifest = 0c4e224bf17c50069b27abc6b48c4133b57e37e4826f28b69cb7abe00febf730
checker count = 53
```

## CMR3934--CMR3939 — deterministic validation

Every checker path is unique and compiles before execution. Every entry binds one exact SHA-256 contract and one theorem flag. Full execution requires a successful deterministic subprocess, one JSON object, exact contract equality, the expected flag equal to one and `all_n_proved_by_checker=0`. Static mode validates the chained manifest.

## CMR3940 — failure isolation

Missing files, invalid JSON, subprocess failures, contract mismatches and missing theorem flags report the exact checker path with stdout and stderr.

## CMR3941 — validation consequence

```text
installed_transition_regression_472_complete = 1
global_target_collateral_inequality_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```
