# The thirty-nine-kind installed construction stack has a sealed twenty-one-checker runner

This chapter records CMR3150--CMR3161.

Executable runner:

```text
scripts/run_prime_power_installed_construction_regression_39.py
```

## CMR3150 — exact twenty-one-checker manifest

The manifest contains the nineteen CMR3110--CMR3121 entries plus the level/colour/cycle checker and the thirty-nine-kind registry.

## CMR3151 — unique path and theorem-flag binding

Every manifest path and expected theorem flag is unique. Every contract is a lowercase SHA-256 value.

## CMR3152 — source validation

Every checker source must exist and compile before execution or static audit succeeds.

## CMR3153 — deterministic environment

Execution fixes `PYTHONDONTWRITEBYTECODE=1` and `PYTHONHASHSEED=0`.

## CMR3154 — one-report requirement

Every checker must return one JSON object. Empty, malformed or multi-report output is rejected.

## CMR3155 — exact contract binding

The runner accepts either `contract_sha256` or `contract_digest` and requires equality with the manifest entry.

## CMR3156 — theorem-flag binding

The designated theorem flag for every checker must equal one.

## CMR3157 — permanent honesty enforcement

Every report must contain:

```text
all_n_proved_by_checker = 0
```

## CMR3158 — static audit mode

`--static-only` validates the manifest and compiles all twenty-one sources without executing their finite regressions.

## CMR3159 — failure isolation

Missing files, syntax failures, process failures, malformed JSON, contract mismatch, theorem-flag mismatch and honesty violations identify the failing checker path.

## CMR3160 — manifest seal and workflow

Manifest digest:

```text
73694657de93b3b1873f98cbf7a896dee629587641a945d3aa8ba6b76ddd3fee
```

The dedicated workflow runs the stack on Python 3.10 and 3.12.

## CMR3161 — validation consequence and boundary

```text
installed_transition_regression_39_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

A passing run validates the installed finite claims only.
