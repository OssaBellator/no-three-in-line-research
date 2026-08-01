# The one-hundred-eighty-eight-kind construction stack has a chained thirty-eight-checker regression

This chapter records **CMR3574--CMR3585**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_188.py
```

## CMR3574 — immutable 138-kind base manifest

The runner imports the complete thirty-six-checker manifest from the 138-kind runner and verifies its chained seal:

```text
e04a2859b6d64b738d7e300a4fd42c371ef476aefb73542e4649bda99a8b88b3
```

## CMR3575 — exact two-checker extension

```text
scripts/check_prime_power_product_factor_child_ancestry.py
scripts/check_prime_power_installed_operation_registry_188.py
```

Each path is bound to its exact contract and one unique theorem flag.

## CMR3576 — chained manifest seal

```text
7e93cf1e7379a12d4146f13a98d075225a9616321838f17002a9bc6ed120a6ca
```

## CMR3577 — exact checker count

The canonical installed construction manifest contains exactly:

```text
38 checkers
```

## CMR3578 — path and source validation

Every checker path is unique, lies under `scripts/check_prime_power_`, exists in the repository and compiles before mathematical execution.

## CMR3579 — contract validation

Every contract is one lowercase SHA-256 value. The runner accepts `contract_sha256` or `contract_digest` from the checker report and requires exact equality.

## CMR3580 — theorem-flag binding

Every checker is bound to one unique expected theorem flag and must report that flag as exactly one.

## CMR3581 — deterministic execution

Full execution uses:

```text
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
```

and runs every checker with the active interpreter from the repository root.

## CMR3582 — one-report requirement

Every checker must terminate successfully and emit one valid JSON object. Empty, malformed or multi-report output is rejected.

## CMR3583 — honesty enforcement

Every checker must report:

```text
all_n_proved_by_checker = 0
```

The validation runner cannot upgrade this boundary.

## CMR3584 — static audit and failure isolation

`--static-only` validates the chained manifest, source presence and syntax without executing the mathematical regressions. Full execution identifies the exact failing checker and preserves stdout and stderr.

## CMR3585 — validation consequence

```text
installed_transition_regression_188_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

A passing run validates the finite installed claims and registry bindings only. It does not prove global construction exhaustiveness, branch termination or the no-three-in-line conjecture.
