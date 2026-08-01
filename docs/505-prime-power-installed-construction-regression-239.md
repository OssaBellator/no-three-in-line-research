# The 239-kind installed construction stack has a chained 43-checker regression

This chapter records **CMR3690--CMR3701**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_239.py
```

## CMR3690 — immutable 41-checker base

The runner imports the complete 221-kind manifest and verifies:

```text
5955b80f71ffdf8d2cd9ca1149d346779787521137353b4457bf35096f570f38
```

## CMR3691 — exact two-checker extension

```text
scripts/check_prime_power_complete_branch_distinguishing_rank.py
scripts/check_prime_power_installed_operation_registry_239.py
```

## CMR3692 — chained manifest seal

```text
fdad5ad0e23bd87f4b3f00d736ef70435b6d117e6822b4dc79f5a24557cea315
```

## CMR3693 — exact checker count

The canonical manifest contains exactly 43 checkers.

## CMR3694--CMR3699 — source, contract, theorem and honesty validation

Every path is unique and compiles before execution. Every entry binds one exact lowercase SHA-256 contract and one unique theorem flag. Full execution is deterministic, requires one successful JSON report and enforces `all_n_proved_by_checker=0`. Static mode validates the complete source/manifest chain without running mathematical regressions.

## CMR3700 — failure isolation

A failing checker is reported with its exact path, stdout and stderr.

## CMR3701 — validation consequence

```text
installed_transition_regression_239_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```
