# The 286-kind installed construction stack has a chained 45-checker regression

This chapter records **CMR3738--CMR3749**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_286.py
```

## CMR3738 — immutable 43-checker base

The runner imports the complete 239-kind manifest and verifies:

```text
fdad5ad0e23bd87f4b3f00d736ef70435b6d117e6822b4dc79f5a24557cea315
```

## CMR3739 — exact two-checker extension

```text
scripts/check_prime_power_scc_branch_minimum_face_ancestry.py
scripts/check_prime_power_installed_operation_registry_286.py
```

## CMR3740 — chained manifest seal

```text
3b206d44e2c243f0d32e91b4cc15381afc9f8b2251af980c88ce6c221fdf1beb
```

## CMR3741 — exact checker count

The canonical manifest contains exactly 45 checkers.

## CMR3742--CMR3747 — source, contract, theorem and honesty validation

Every checker path is unique and compiles before execution. Every entry binds one exact lowercase SHA-256 contract and one unique expected theorem flag. Full execution requires a successful deterministic subprocess, one JSON object, exact contract equality, the expected flag equal to one and `all_n_proved_by_checker=0`. Static mode validates the complete manifest chain without executing mathematical regressions.

## CMR3748 — failure isolation

A failing checker is reported with its exact repository path, stdout and stderr. Contract mismatches, malformed JSON and missing theorem flags fail the run.

## CMR3749 — validation consequence

```text
installed_transition_regression_286_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The runner validates the installed finite stack. It is not a proof certificate for the original construction or the all-`n` conjecture.
