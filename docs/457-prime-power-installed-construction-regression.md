# The installed construction stack has one contract-sealed regression runner

This chapter records CMR3022--CMR3033. The installed owner/scheduler bank binds
operation metadata, but each underlying checker must also remain executable as
the branch evolves. The construction regression runner executes the complete
installed local and ancestry stack and verifies every checker contract, theorem
flag and permanent honesty flag.

The executable runner is:

```text
scripts/run_prime_power_installed_construction_regression.py
```

## CMR3022 — canonical checker manifest

The runner contains a fixed manifest of fourteen construction checkers, from the
asymmetric residual-host generator through the installed owner/scheduler bank.
Each entry contains exactly:

```text
checker path
contract SHA-256
expected theorem flag
```

Checker paths and expected flags are unique.

## CMR3023 — exact contract binding

Every manifest digest is the literal contract digest emitted by its checker.
Substitution of a different checker version or contract is rejected before its
mathematical flag is accepted.

## CMR3024 — source syntax validation

Every installed checker source is compiled before execution. Missing files and
syntax failures are hard errors. The `--static-only` mode performs this audit
without running the finite enumerations.

## CMR3025 — deterministic execution environment

The runner executes every checker with:

```text
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
```

and the active Python interpreter. Standard output and error are captured for
exact failure localization.

## CMR3026 — one JSON report per checker

A successful checker must emit one JSON object. Empty output, mixed prose,
malformed JSON or a nonobject report is rejected.

## CMR3027 — theorem-flag binding

For every checker, the manifest names one exact theorem flag which must equal
one. Thus a checker cannot satisfy the regression merely by exiting successfully
or printing an unrelated report.

## CMR3028 — permanent honesty enforcement

Every checker report must contain

```text
all_n_proved_by_checker = 0
```

The runner itself preserves the same flag and also keeps global transition
exhaustiveness and termination at zero.

## CMR3029 — complete installed stack

The manifest executes:

```text
asymmetric residual-host contraction
asymmetric context generation
asymmetric target dispatch
typed context transition registry
routing-change ancestry and history payment
fixed-routing child-product ancestry
mixed-child deletion ancestry
forced-certificate escape ancestry
returned-target ancestry
target-handoff/envelope ancestry
recurrent-target deletion ancestry
closure-envelope transition ancestry
installed owner/scheduler bank
```

## CMR3030 — checker failure isolation

A failed subprocess report includes the exact command, standard output and
standard error. Contract, theorem-flag and honesty mismatches identify the exact
checker path and expected field.

## CMR3031 — static audit mode

With `--static-only`, all fourteen checker paths, manifest entries and Python
sources are audited without executing finite enumeration. This supports rapid
repository synchronization checks while retaining the full mode for CI.

## CMR3032 — manifest seal and workflow

The manifest digest is:

```text
2fd61262229cbd866d978d7dcf5e19b607a5f81eb843d3d3a48046b598fa5e20
```

The dedicated workflow runs both static and full regression on Python 3.10 and
3.12.

## CMR3033 — validation consequence and honesty boundary

The runner proves only:

```text
installed_transition_regression_complete = 1
installed checker count = 14
```

It preserves:

```text
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

A passing installed regression is evidence that the stated finite construction
claims remain executable and mutually synchronized. It is not evidence that the
installed operation bank is globally exhaustive or that the no-three-in-line
conjecture is proved.
