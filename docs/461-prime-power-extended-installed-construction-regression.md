# The extended installed construction stack has one sealed regression runner

This chapter records CMR3072--CMR3083. It extends the fourteen-checker construction regression with the Hall-wall, rollback and twenty-nine-kind registry checkers.

The executable runner is:

```text
scripts/run_prime_power_extended_installed_construction_regression.py
```

## CMR3072 — exact seventeen-checker manifest

The manifest contains the original fourteen installed construction checkers plus:

```text
check_prime_power_essential_return_unit_wall_ancestry.py
check_prime_power_sparse_rollback_restoration_ancestry.py
check_prime_power_extended_installed_operation_registry.py
```

Every path is unique and bound to one exact contract and one expected theorem flag.

## CMR3073 — source and syntax validation

Every checker must exist and compile as Python before execution. Static mode performs the complete path, syntax, manifest and digest audit without running finite enumerations.

## CMR3074 — deterministic execution environment

Executable mode sets deterministic hash and bytecode controls before launching each checker in an isolated subprocess.

## CMR3075 — one-report requirement

Each checker must exit successfully and emit exactly one JSON object. Empty, malformed or non-object output is rejected.

## CMR3076 — compatible contract-key validation

The runner accepts the historical `contract_sha256` report key and the newer `contract_digest` key, but the reported value must equal the exact manifest contract. This compatibility does not weaken digest checking.

## CMR3077 — theorem-flag binding

Every manifest entry names one theorem flag which must equal one in the checker report. A successful exit without that flag is rejected.

## CMR3078 — permanent honesty enforcement

Every checker report must contain

```text
all_n_proved_by_checker = 0
```

Any nonzero or missing value fails the regression.

## CMR3079 — static audit mode

The `--static-only` option validates all seventeen paths, source files, contracts, flags and the manifest seal without claiming that the finite regressions were executed.

## CMR3080 — isolated failure reporting

Executable failure reports the exact checker path together with captured standard output and standard error. Contract, theorem-flag and honesty failures are distinguished.

## CMR3081 — exact manifest seal

The seventeen-checker manifest digest is:

```text
0595bf48a3cb786cc0e9e79f7534c4c0cf2f3161b072575aaae06976e6bc194a
```

## CMR3082 — dedicated workflow

A Python 3.10/3.12 workflow compiles the extended runner, performs its static audit and executes the full seventeen-checker stack.

Configuration is not evidence of a passing workflow; run status and logs must be observed before CI success is claimed.

## CMR3083 — validation consequence and honesty boundary

A passing run proves only:

```text
extended_installed_transition_regression_complete = 1
```

It validates the installed finite claims and exact contract bindings. It does not prove:

```text
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

Missing operation discovery, recurrent-endpoint closure, global termination and all downstream T01--T43 mathematical obligations remain open.
