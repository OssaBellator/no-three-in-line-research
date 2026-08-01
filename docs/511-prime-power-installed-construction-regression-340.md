# The 340-kind installed construction stack has a chained 47-checker regression

This chapter records **CMR3786--CMR3797**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_340.py
```

## CMR3786 — immutable 45-checker base

The runner imports the complete 286-kind manifest and verifies:

```text
3b206d44e2c243f0d32e91b4cc15381afc9f8b2251af980c88ce6c221fdf1beb
```

## CMR3787 — exact two-checker extension

```text
scripts/check_prime_power_minimum_transition_product_target_ancestry.py
scripts/check_prime_power_installed_operation_registry_340.py
```

## CMR3788 — chained manifest seal

```text
2450935467fa22953baeb20f539fdaae0b608680307cd6027501a3a39771560d
```

## CMR3789 — exact checker count

The canonical manifest contains exactly 47 checkers.

## CMR3790--CMR3795 — source, contract, theorem and honesty validation

Every checker path is unique and compiles before execution. Every entry binds one exact lowercase SHA-256 contract and a unique expected theorem flag. Full execution requires a successful deterministic subprocess, one JSON object, exact contract equality, the expected flag equal to one and `all_n_proved_by_checker=0`. Static mode validates the complete manifest chain without running the mathematical regressions.

## CMR3796 — failure isolation

A failing checker is reported with its exact path, stdout and stderr. Missing checkers, malformed reports, contract mismatches and missing theorem flags fail the run.

## CMR3797 — validation consequence

```text
installed_transition_regression_340_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The runner validates the installed finite construction stack. It does not prove the original operation list complete or the conjecture.
