# The ninety-eight-kind construction stack has a chained thirty-two-checker regression

This chapter records **CMR3372--CMR3383**.

Executable runner:

```text
scripts/run_prime_power_installed_construction_regression_98.py
```

## CMR3372 — immutable thirty-checker base

The runner imports the CMR3341 runner and verifies its chained seal

```text
041abca9a30cad0f0b97a440b455df2fdbeb4501bac711c681f8f2f202ae0c49
```

It then reconstructs and validates the complete thirty-checker base manifest.

## CMR3373 — exact two-checker extension

```text
scripts/check_prime_power_canonical_selector_absorption_ancestry.py
scripts/check_prime_power_installed_operation_registry_98.py
```

The extension binds exact contracts and unique theorem flags.

## CMR3374 — chained manifest seal

```text
bf0a209785183ec05e45b93bd9122159251571719bd63488240f34adacb23599
```

## CMR3375 — exact checker count

The complete manifest contains exactly thirty-two unique paths and thirty-two unique theorem flags.

## CMR3376 — literal source validation

Every checker path must exist and its UTF-8 source must compile.

## CMR3377 — deterministic execution

The runner fixes `PYTHONDONTWRITEBYTECODE=1`, `PYTHONHASHSEED=0` and the repository root working directory.

## CMR3378 — one JSON report

Every executed checker must exit zero and emit exactly one JSON object.

## CMR3379 — contract binding

The report contract must equal the literal manifest contract, using `contract_sha256` or the historical `contract_digest` field.

## CMR3380 — theorem-flag binding

Every report must expose its designated theorem flag equal to one.

## CMR3381 — honesty enforcement

Every report must preserve

```text
all_n_proved_by_checker = 0
```

## CMR3382 — static chained audit

The `--static-only` mode validates both historical chained seals, the extension seal, counts, uniqueness, paths and syntax. A mock nested-runner repository exercised this mode successfully.

## CMR3383 — validation consequence

```text
installed_transition_regression_98_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The regression validates the installed finite stack only. It is not a global proof certificate.
