# The fifty-seven-kind installed construction stack has a sealed twenty-six-checker runner

This chapter records CMR3246--CMR3257.

Executable runner:

```text
scripts/run_prime_power_installed_construction_regression_57.py
```

## CMR3246 — exact twenty-six-checker manifest

The manifest contains the twenty-three CMR3190--CMR3201 entries plus the rooted/pair checker, line-clean availability checker and fifty-seven-kind registry.

## CMR3247 — unique checker paths

Every path occurs exactly once and names a prime-power checker source.

## CMR3248 — unique expected theorem flags

Every manifest entry binds one distinct theorem flag.

## CMR3249 — exact contract syntax

Every contract is a lowercase SHA-256 value and is bound to its checker path.

## CMR3250 — source validation

All twenty-six checker sources must exist and compile before static or executable audit succeeds.

## CMR3251 — deterministic execution

The runner fixes `PYTHONHASHSEED=0` and disables bytecode generation.

## CMR3252 — one JSON report

Every checker must return successfully and emit one JSON object.

## CMR3253 — exact contract binding

The report's `contract_sha256` or `contract_digest` must equal the manifest value.

## CMR3254 — theorem and honesty binding

The designated theorem flag must equal one, while every report must preserve:

```text
all_n_proved_by_checker = 0
```

## CMR3255 — static audit and failure isolation

`--static-only` validates the manifest and compiles all sources without executing them. Failures identify the exact checker path.

## CMR3256 — manifest seal and workflow

Manifest digest:

```text
6e007bd733d40f69a3d23e8c59b721852cccec0240ab36ca16efd28d6bd57027
```

The dedicated workflow runs Python 3.10 and 3.12.

## CMR3257 — validation consequence and boundary

```text
installed_transition_regression_57_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

A passing run validates the currently installed finite bank only.
