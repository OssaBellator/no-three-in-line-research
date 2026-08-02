# The 714-kind installed construction stack has a chained 63-checker regression

This chapter records **CMR4166--CMR4181**.

Canonical runner:

```text
scripts/run_prime_power_installed_construction_regression_714.py
```

## CMR4166--CMR4169 — exact manifest extension

The runner imports the complete 656-kind 61-checker manifest and appends:

```text
scripts/check_prime_power_signature_carry_resource_ancestry.py
scripts/check_prime_power_installed_operation_registry_714.py
```

```text
base manifest = 5678e89e0f0b73946471b3c99cb027448266715a5ae0b0ffc42636dd4aa9bd3d
63-checker manifest = c8a579625e9fba23b4526bf3a1465df985dd1897224104cbc8e863d6873f0811
```

## CMR4170--CMR4177 — deterministic validation

Every checker path is unique and compiles before execution. Every manifest entry binds one exact contract and one theorem flag. Full execution requires successful deterministic subprocesses, one JSON report per checker, exact contract equality, the expected theorem flag equal to one and `all_n_proved_by_checker=0`.

Static mode validates the complete chained manifest without executing the mathematical checkers.

## CMR4178--CMR4179 — recurrent-core honesty enforcement

The runner rejects any checker report claiming:

```text
uniform_signature_payment_certificate_proved = 1
recurrent_root_channel_core_subcritical = 1
repeated_token_reused_edge_core_subcritical = 1
loaded_owner_core_subcritical = 1
same_owner_diagonal_blocks_subcritical = 1
global_target_collateral_inequality_proved = 1
all_n_proved_by_checker = 1
```

## CMR4180--CMR4181 — validation consequence

```text
installed_transition_regression_714_complete = 1
uniform_signature_payment_certificate_proved = 0
recurrent_root_channel_core_subcritical = 0
repeated_token_reused_edge_core_subcritical = 0
loaded_owner_core_subcritical = 0
same_owner_diagonal_blocks_subcritical = 0
global_target_collateral_inequality_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The runner source and chained manifest seal were validated locally. The complete 63-checker repository runner has not been executed locally, and no CI success is claimed.
