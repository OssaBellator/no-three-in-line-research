# The eighty-four-kind construction stack has a chained thirty-checker regression

This chapter records **CMR3330--CMR3341**.

Executable runner:

```text
scripts/run_prime_power_installed_construction_regression_84.py
```

## CMR3330 — immutable historical manifest

The runner imports and verifies the complete twenty-eight-checker CMR3299 manifest with exact seal

```text
ecc5043ee6e9c04901e4a1814ca0446b49c3a9c115bfbfd6ab196d02ea13150a
```

The historical manifest content and count must validate before the extension is accepted.

## CMR3331 — exact two-checker extension

The runner appends exactly:

```text
scripts/check_prime_power_persistent_cross_selector_ancestry.py
scripts/check_prime_power_installed_operation_registry_84.py
```

with their exact contracts and unique theorem flags.

## CMR3332 — chained manifest seal

The immutable base seal and literal extension are bound by

```text
041abca9a30cad0f0b97a440b455df2fdbeb4501bac711c681f8f2f202ae0c49
```

## CMR3333 — exact checker count

The final manifest contains exactly thirty unique checker paths and thirty unique theorem flags.

## CMR3334 — path and source validation

Every checker path must exist below `scripts/`, end in `.py`, and compile from its literal UTF-8 source.

## CMR3335 — deterministic execution

Execution uses the current interpreter with

```text
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
```

and the repository root as the working directory.

## CMR3336 — one-report requirement

Each checker must exit zero and emit exactly one JSON object on standard output.

## CMR3337 — exact contract binding

The runner accepts either `contract_sha256` or the historical `contract_digest` field and requires exact equality with the manifest entry.

## CMR3338 — exact theorem-flag binding

Every checker must report its designated theorem flag equal to one.

## CMR3339 — honesty enforcement

Every checker must report

```text
all_n_proved_by_checker = 0
```

or the complete regression fails.

## CMR3340 — static audit

The `--static-only` mode validates the base seal, extension seal, count, uniqueness, paths and syntax without executing mathematical checkers. A mock-repository audit exercised this mode successfully.

## CMR3341 — validation consequence and boundary

The runner reports:

```text
installed_transition_regression_84_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

A passing thirty-checker regression validates the installed finite claims. It does not prove global operation exhaustiveness, termination or the no-three-in-line conjecture.
