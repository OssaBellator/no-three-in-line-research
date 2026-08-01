# The 525-kind installed construction stack has a chained 55-checker regression

This chapter records **CMR3974--CMR3989**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_525.py
```

## CMR3974--CMR3977 — manifest chain

The runner imports the complete 472-kind 53-checker manifest and appends:

```text
scripts/check_prime_power_collateral_spectral_ancestry.py
scripts/check_prime_power_installed_operation_registry_525.py
```

The chained seal is:

```text
base = 0c4e224bf17c50069b27abc6b48c4133b57e37e4826f28b69cb7abe00febf730
manifest = 6dc1d74abe2d723645dc1e5a26e85bb518e91a80e5ade84c815625504909d5aa
checker count = 55
```

## CMR3978--CMR3986 — deterministic validation

Every checker path is unique and compiles before execution. Every manifest entry binds one exact SHA-256 contract and one unique theorem flag. Full execution requires a successful deterministic subprocess, one JSON object, exact contract equality, the expected flag equal to one, `all_n_proved_by_checker=0`, and—when present—`global_target_collateral_inequality_proved=0`.

Static mode validates the complete manifest chain without running mathematical regressions.

## CMR3987 — failure isolation

Missing files, invalid JSON, subprocess failures, contract mismatches, missing theorem flags and honesty-boundary violations report the exact checker path with stdout and stderr.

## CMR3988--CMR3989 — validation consequence

```text
installed_transition_regression_525_complete = 1
global_target_collateral_inequality_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

A manifest records deterministic validation infrastructure; it is not a global proof certificate.
