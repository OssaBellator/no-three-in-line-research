# The canonical 188-kind stack has a thirty-nine-checker inherited-coverage regression

This chapter records **CMR3598--CMR3609**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_188_coverage.py
```

## CMR3598 — immutable 38-checker base

The runner imports the complete 188-kind manifest and verifies its chained seal:

```text
7e93cf1e7379a12d4146f13a98d075225a9616321838f17002a9bc6ed120a6ca
```

## CMR3599 — exact coverage extension

The sole extension is:

```text
scripts/check_prime_power_owner_target_wall_coverage.py
3038c3f03bb8485f5dd6c03efaa894a2354e675c74324bd1532c422f1c1a0feb
cmr691_747_existing_operation_coverage_exact
```

## CMR3600 — chained manifest seal

```text
7ac023aecd548ee7c966e8934b149d551a57a30e5569094abd6b26cf8bd29de1
```

## CMR3601 — exact checker count

The canonical coverage manifest contains exactly:

```text
39 checkers
```

## CMR3602 — unchanged operation count

The inherited-coverage audit adds no operation identifier. The canonical installed bank remains exactly 188 kinds.

## CMR3603 — path and source validation

Every checker path is unique, exists under `scripts/check_prime_power_` and compiles before execution.

## CMR3604 — exact contract validation

Every manifest entry binds one lowercase SHA-256 contract and one unique theorem flag.

## CMR3605 — deterministic execution

The runner uses the active interpreter with deterministic hash seed and disabled bytecode generation.

## CMR3606 — one-report requirement

Every checker must terminate successfully and emit one valid JSON object.

## CMR3607 — honesty enforcement

Every checker report must retain:

```text
all_n_proved_by_checker = 0
```

## CMR3608 — static audit and failure isolation

`--static-only` validates source presence, syntax and the chained manifest. Full execution reports the exact failing checker with captured output.

## CMR3609 — validation consequence

```text
installed_transition_regression_188_coverage_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

A passing run validates installed finite claims and the CMR691--CMR747 coverage seal only.
