# Side-four return context and compulsory coefficient dependencies

This post-ledger support layer refines the complete normalized side-four host and selector manifests. It does not add theorem identifiers after CMR4517 and does not claim a complete weighted recurrent certificate.

## Exact return-exchange context

```text
contract = data/prime_power_side_four_return_exchange_context_contract.json
contract sha256 = 0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b
compiled row sha256 = fdb2ff3287ce607727740130754230cd9c55a415985f393ea166bb3f7ef626ea
checker = scripts/check_prime_power_side_four_return_exchange_context.py
```

The old selected matching is the fixed identity `00,11,22,33`. Every normalized selected response is a derangement, so every source has one exact returned predecessor and one exact entering edge. Across all 86 rows the compiler records:

```text
same-source exchange entries = 344
alternating-cycle length 4 entries = 68
alternating-cycle length 8 entries = 276
hosts with two alternating 4-cycles = 17
hosts with one alternating 8-cycle = 69
```

Using the repository's absolute last-entering convention—lexicographically maximal entering edge—the selected-response collinear triples give an exact normalized rank-three return subkernel:

```text
recreated rank-three credits = 17
nonzero kernel entries = 13
nonzero rows = 11
charge to returned edge 22 = 2
charge to returned edge 33 = 15
old-overlap 0 / matching-cycle 2 credits = 8
old-overlap 0 / matching-cycle 4 credits = 9
```

This closes only the selected-response rank-three return class. Rank-one, rank-two, selector, token and other residual return classes are not inferred from it.

## Complete normalized dependency map

```text
obligation contract = 62c6c448b40a8b0294a35673aac997eac73c3380b1cceedffe9616c2326f3211
compiled obligation rows = b33e4fa3e442349edacbb14a65b088a92b823c67b6a4f810958076a65e3e797b
dependency contract = 47c765be4b4a79f826dba2ac23fb2d7a69f0d64ba23bb94d1cb1d608178fbacc
compiled dependency records = 4cd91e195393ea226474c3c33f80ac63fcdd9c4b8b0bf95b810f54d0c490d401
checker = scripts/check_prime_power_side_four_compulsory_coefficient_dependency_map.py
```

All 516 compulsory category occurrences have an exact dependency record. The census is:

```text
known coefficients = 86
unresolved coefficients = 430
known prerequisite occurrences = 688
missing prerequisite occurrences = 1462
partially grounded unresolved records = 430
ungrounded records = 0
unresolved child keys = 516
unresolved positive child weights = 516
```

The category boundary is exact:

- `geometric`: the coefficient is known from selected minimum response energy; child key and weight remain unresolved.
- `return`: exact exchange signatures and the rank-three return subkernel are known; residual credit classes, the total coefficient rule, child key and weight remain unresolved.
- `selector`: minimizer face and next-energy gap are known; complete coupled scores and child bindings are unresolved.
- `collision`: exact deletion/collision traces are known; owner/fate/collision child routing and coefficient rules are unresolved.
- `line`: selected-response secant signatures are known; actual background heights, line owners and coefficient rules are unresolved.
- `interface`: the normalized target interface is known; child route, provenance and coefficient rule are unresolved.

## Honesty boundary

```text
return_exchange_context_complete_for_normalized_block = 1
rank_three_return_kernel_complete_for_normalized_block = 1
dependency_map_complete_for_normalized_block = 1

complete_return_coefficient_rule_complete = 0
residual_return_credit_classes_complete = 0
global_child_provenance_complete = 0
unresolved_coefficients_populated = 0
child_weights_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

Both checkers and their corruption audits were reproduced locally. Workflow configuration does not constitute CI success.