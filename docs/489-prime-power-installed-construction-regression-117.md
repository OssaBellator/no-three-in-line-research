# The one-hundred-seventeen-kind installed construction stack has a chained thirty-four-checker regression

This chapter records **CMR3458--CMR3469**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_117.py
```

## CMR3458 — immutable ninety-eight-kind base manifest

The runner imports the complete thirty-two-checker manifest from the 98-kind runner and verifies chained seal:

```text
bf0a209785183ec05e45b93bd9122159251571719bd63488240f34adacb23599
```

## CMR3459 — exact two-checker extension

```text
scripts/check_prime_power_selector_protected_certificate_ancestry.py
scripts/check_prime_power_installed_operation_registry_117.py
```

## CMR3460 — chained manifest seal

```text
d259fb78a7b8a2ccbf7387c3fdd7a780b1e21f0366179c08af5ebb068cda3507
```

## CMR3461 — exact checker count

The canonical installed construction manifest contains exactly 34 checkers.

## CMR3462 — path and source validation

Every checker path is unique, exists under `scripts/check_prime_power_` and compiles before execution.

## CMR3463 — contract validation

Every checker is bound to one lowercase SHA-256 contract, accepted from `contract_sha256` or `contract_digest` only by exact equality.

## CMR3464 — theorem-flag binding

Every checker has one unique expected theorem flag and must report it as exactly one.

## CMR3465 — deterministic execution

Full execution uses `PYTHONDONTWRITEBYTECODE=1` and `PYTHONHASHSEED=0` from the repository root.

## CMR3466 — one-report requirement

Each checker must terminate successfully and emit one valid JSON object.

## CMR3467 — honesty enforcement

Every checker report must preserve:

```text
all_n_proved_by_checker = 0
```

## CMR3468 — static audit and failure isolation

`--static-only` validates the chained manifest, source existence and syntax without executing finite regressions. Full mode identifies the exact failing checker and captures stdout/stderr.

## CMR3469 — validation consequence

```text
installed_transition_regression_117_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

A passing run validates the installed finite claims and registry bindings only. It does not prove global construction exhaustiveness or termination.
