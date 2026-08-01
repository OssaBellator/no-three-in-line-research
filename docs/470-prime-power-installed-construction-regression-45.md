# The forty-five-kind installed construction stack has a sealed twenty-three-checker runner

This chapter records CMR3190--CMR3201.

Executable runner:

```text
scripts/run_prime_power_installed_construction_regression_45.py
```

## CMR3190 — exact twenty-three-checker manifest

The manifest contains the twenty-one CMR3150--CMR3161 entries plus the boundary-theta checker and the forty-five-kind registry.

## CMR3191 — unique paths and flags

Every checker path and expected theorem flag is unique.

## CMR3192 — exact contracts

Every contract is a lowercase SHA-256 value and is bound to its checker path.

## CMR3193 — source compilation

Every checker source must exist and compile in both static and executable modes.

## CMR3194 — deterministic execution

The runner fixes the Python hash seed and disables bytecode generation.

## CMR3195 — one JSON report

Each checker must emit one JSON object and return successfully.

## CMR3196 — contract and theorem binding

The report contract and designated theorem flag must match the manifest exactly.

## CMR3197 — permanent honesty enforcement

Every checker report must preserve:

```text
all_n_proved_by_checker = 0
```

## CMR3198 — static audit

`--static-only` validates the manifest and compiles all twenty-three checker sources without executing them.

## CMR3199 — failure isolation

The runner reports the exact checker path for source, process, JSON, contract, theorem-flag or honesty failures.

## CMR3200 — manifest seal and workflow

Manifest digest:

```text
f44951c9cee6688e892a853a7f925ff9a5e54221b1ce92656efa043718171170
```

The dedicated workflow runs Python 3.10 and 3.12.

## CMR3201 — validation consequence and boundary

```text
installed_transition_regression_45_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

A passing run validates only the currently installed finite operation bank.
