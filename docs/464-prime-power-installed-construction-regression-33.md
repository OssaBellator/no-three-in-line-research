# The thirty-three-kind installed construction bank has a sealed regression

This chapter records CMR3110--CMR3121. It supersedes the earlier fourteen- and seventeen-checker manifests while preserving them as historical validation layers.

The executable runner is:

```text
scripts/run_prime_power_installed_construction_regression_33.py
```

## CMR3110 — exact nineteen-checker manifest

The manifest contains every checker in the seventeen-checker extended stack plus:

```text
check_prime_power_rollback_optimal_face_scc_ancestry.py
check_prime_power_installed_operation_registry_33.py
```

## CMR3111 — path uniqueness and source validation

Every path must be unique, exist in `scripts/`, use the construction-checker naming convention and compile before execution.

## CMR3112 — exact contract binding

Every checker is bound to one lowercase SHA-256 contract. Reports may expose the historical `contract_sha256` key or the newer `contract_digest` key, but the value must equal the manifest entry exactly.

## CMR3113 — exact theorem-flag binding

Every checker is bound to one unique expected theorem flag. Successful execution without that flag equal to one is rejected.

## CMR3114 — deterministic subprocess execution

Executable mode uses deterministic Python hash settings, suppresses bytecode creation and runs each checker in its own subprocess from the repository root.

## CMR3115 — one JSON report

Each checker must exit with status zero and emit one JSON object. Empty, malformed or non-object output fails the regression.

## CMR3116 — permanent honesty enforcement

Every checker must report:

```text
all_n_proved_by_checker = 0
```

The regression fails if the flag is missing or nonzero.

## CMR3117 — static audit mode

`--static-only` validates the nineteen paths, syntax, contracts, expected flags and manifest digest without executing finite enumerations.

## CMR3118 — isolated failure reporting

Execution failures retain the exact checker path and captured output. Contract, expected-flag and honesty errors are separately identified.

## CMR3119 — exact manifest seal

The nineteen-checker manifest digest is:

```text
50b66679af79082ff57ec0926508482f1efb72eefd6fe0e620d41eb949890fca
```

## CMR3120 — dedicated Python matrix workflow

A Python 3.10/3.12 workflow compiles the runner, performs the static audit and executes all nineteen checkers.

Workflow configuration alone is not evidence of success; run status and logs must be observed.

## CMR3121 — validation consequence and honesty boundary

A passing run proves only:

```text
installed_transition_regression_33_complete = 1
```

It validates the finite claims and exact contract bindings of the currently installed thirty-three-kind bank. It does not prove:

```text
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The remaining operation audit, recurrent-endpoint closure, all T01--T43 populations and semantic implications, ordinary review and root theorem remain open.
