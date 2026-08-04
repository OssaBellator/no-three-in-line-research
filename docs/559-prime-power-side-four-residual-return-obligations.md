# Side-four residual return obligations

This post-ledger worklist separates the exact selected-response rank-three return kernel from every residual return credit class that is still missing. It does not add theorem identifiers after CMR4517.

```text
contract = data/prime_power_side_four_residual_return_obligation_contract.json
contract sha256 = c256cedf67c092ecb7229fd7bfda9d5b4194ce630777de6ea2011bd179e6974f
checker = scripts/check_prime_power_side_four_residual_return_obligations.py
return context contract = 0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b
return context rows = fdb2ff3287ce607727740130754230cd9c55a415985f393ea166bb3f7ef626ea
```

Every normalized host has five explicit return classes:

```text
rank-three-selected-response
rank-one-background
rank-two-background
selector-token
other-labelled
```

The rank-three class is exact. Its coefficient is the recreated collinear-triple count and its physical charge is the exact returned-edge kernel. The other four classes remain unresolved and cannot be treated as zero.

## Exact census

```text
rows = 86
return class slots = 430
known rank-three coefficients = 86
rank-three coefficient total = 17
positive rank-three rows = 11
zero rank-three rows = 75
rank-three kernel entries = 13
unresolved residual coefficient slots = 344
unresolved return child keys = 430
unresolved return child weights = 430
```

Each residual class has 86 unresolved slots:

```text
rank-one-background = 86
rank-two-background = 86
selector-token = 86
other-labelled = 86
```

The `other-labelled` class is an explicit temporary obligation, not a permitted coarse zero. Completion requires refining it into finite credit classes or proving that it is empty from the full provenance state.

## Required continuation

1. Attach the actual background-height and line-owner profile to rank-one and rank-two return credits.
2. Attach selector/token state and return child routing.
3. Refine every `other-labelled` slot.
4. Bind every return class occurrence to one exact child key and positive weight.
5. Sum all completed classes into the total return coefficient.

## Honesty boundary

```text
residual_return_worklist_complete_for_normalized_block = 1
rank_three_return_coefficients_complete = 1

residual_return_credit_classes_complete = 0
complete_return_coefficient_rule_complete = 0
return_child_keys_complete = 0
return_child_weights_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The checker binds the repaired return context and rejects hidden-zero, truncated-class, premature-completeness and all-n corruptions.