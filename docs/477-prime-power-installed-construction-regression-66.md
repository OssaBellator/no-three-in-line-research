# The sixty-six-kind installed construction stack has a sealed twenty-eight-checker runner

This chapter records CMR3288--CMR3299.

Executable runner:

```text
scripts/run_prime_power_installed_construction_regression_66.py
```

## CMR3288 — exact twenty-eight-checker manifest

The manifest contains the twenty-six CMR3246--CMR3257 entries plus the adaptive unavailable/token/temporal checker and the sixty-six-kind registry.

## CMR3289 — unique checker paths

Every path occurs exactly once and names a prime-power checker source.

## CMR3290 — unique theorem flags

Every manifest entry binds one distinct expected theorem flag.

## CMR3291 — exact contract syntax

Every contract is a lowercase SHA-256 value bound to its checker path.

## CMR3292 — source validation

All twenty-eight checker sources must exist and compile before static or executable audit succeeds.

## CMR3293 — deterministic execution

The runner fixes `PYTHONHASHSEED=0` and disables bytecode generation.

## CMR3294 — one JSON report

Every checker must return successfully and emit one JSON object.

## CMR3295 — exact contract binding

The report's `contract_sha256` or `contract_digest` must equal the manifest value.

## CMR3296 — theorem and honesty binding

The designated theorem flag must equal one, while every report must preserve:

```text
all_n_proved_by_checker = 0
```

## CMR3297 — static audit and failure isolation

`--static-only` validates the manifest and compiles all sources without executing them. Failures identify the exact checker path.

## CMR3298 — manifest seal and workflow

Manifest digest:

```text
ecc5043ee6e9c04901e4a1814ca0446b49c3a9c115bfbfd6ab196d02ea13150a
```

The dedicated workflow runs Python 3.10 and 3.12.

## CMR3299 — validation consequence and boundary

```text
installed_transition_regression_66_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

A passing run validates the currently installed finite operation bank only.
