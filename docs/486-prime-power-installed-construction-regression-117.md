# The one-hundred-seventeen-kind installed construction stack has a chained thirty-four-checker regression

This chapter records **CMR3416--CMR3427**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_117.py
```

## CMR3416 — immutable ninety-eight-kind base manifest

The runner imports the complete thirty-two-checker manifest from the 98-kind runner and verifies its chained seal:

```text
bf0a209785183ec05e45b93bd9122159251571719bd63488240f34adacb23599
```

## CMR3417 — exact two-checker extension

The extension is:

```text
scripts/check_prime_power_selector_protected_certificate_ancestry.py
scripts/check_prime_power_installed_operation_registry_117.py
```

Each path is bound to its exact contract and one unique theorem flag.

## CMR3418 — chained manifest seal

The complete extension is sealed by:

```text
d259fb78a7b8a2ccbf7387c3fdd7a780b1e21f0366179c08af5ebb068cda3507
```

## CMR3419 — exact checker count

The canonical installed construction manifest contains exactly:

```text
34 checkers
```

## CMR3420 — path and source validation

Every checker path is unique, lies under `scripts/check_prime_power_`, exists in the repository and compiles as Python source before execution.

## CMR3421 — contract validation

Every manifest contract is one lowercase SHA-256 value. The runner accepts either `contract_sha256` or `contract_digest` from one checker report and requires exact equality.

## CMR3422 — theorem-flag binding

Every checker is bound to one unique expected theorem flag and must report that flag as exactly one.

## CMR3423 — deterministic execution environment

Full execution uses:

```text
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
```

and invokes each checker with the active Python interpreter from the repository root.

## CMR3424 — one-report requirement

Every checker must terminate successfully and emit one valid JSON object. Empty, malformed or multi-report output is rejected.

## CMR3425 — honesty enforcement

Every checker report must contain:

```text
all_n_proved_by_checker = 0
```

A validation runner cannot upgrade this boundary.

## CMR3426 — static audit and failure isolation

`--static-only` validates the chained manifest, all source files and syntax without executing mathematical regressions. Full mode reports the exact failing checker, stdout and stderr.

## CMR3427 — validation consequence

```text
installed_transition_regression_117_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

A passing run validates the installed finite claims and registry bindings only. It does not prove that the 117 kinds exhaust the original construction or that every construction branch terminates.
