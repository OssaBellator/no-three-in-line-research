# The 221-kind installed construction stack has a chained 41-checker regression

This chapter records **CMR3646--CMR3657**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_221.py
```

## CMR3646 — immutable 39-checker base

The runner imports the complete 188-kind inherited-coverage manifest and verifies:

```text
7ac023aecd548ee7c966e8934b149d551a57a30e5569094abd6b26cf8bd29de1
```

## CMR3647 — exact two-checker extension

```text
scripts/check_prime_power_target_anchor_lineage_ancestry.py
scripts/check_prime_power_installed_operation_registry_221.py
```

## CMR3648 — chained manifest seal

```text
5955b80f71ffdf8d2cd9ca1149d346779787521137353b4457bf35096f570f38
```

## CMR3649 — exact checker count

The canonical manifest contains exactly 41 checkers.

## CMR3650--CMR3655 — source, contract, theorem and honesty validation

Every checker path is unique and compiles before execution. Every entry binds one exact lowercase SHA-256 contract and one unique theorem flag. Full execution uses deterministic hashing, requires one successful JSON report and enforces `all_n_proved_by_checker=0`. Static mode validates the complete source and manifest chain without mathematical execution.

## CMR3656 — failure isolation

A failing checker is reported with its exact path, stdout and stderr.

## CMR3657 — validation consequence

```text
installed_transition_regression_221_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

A passing run validates installed finite claims only.
