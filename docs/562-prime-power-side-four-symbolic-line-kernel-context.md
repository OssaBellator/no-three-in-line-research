# Side-four symbolic line-kernel context

This post-ledger compiler closes the exact line coefficient rule on the normalized 86-host side-four block while retaining the actual background heights and child provenance as unresolved inputs.

```text
contract = data/prime_power_side_four_symbolic_line_kernel_context_contract.json
contract sha256 = 0232bda658189acdb880681ce19192698e049d603a2e779d5f9e287d43fe481e
checker = scripts/check_prime_power_side_four_symbolic_line_kernel_context.py
return contract = 0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b
```

For a real line containing `h` actual background points and `k` selected-response points, the exact local new-triple kernel is

```text
K(h,k) = k*C(h,2) + C(k,2)*h + C(k,3).
```

The compiler enumerates every distinct secant line of each selected response and publishes the symbolic entry

```text
[canonical line, k, rank-one multiplier k, rank-two multiplier C(k,2), rank-three constant C(k,3)].
```

## Exact catalogue

The 86 rows use six selected-response patterns and contain 488 line occurrences:

```text
occupancy 2 occurrences = 477
occupancy 3 occurrences = 9
occupancy 4 occurrences = 2
rank-one multiplier total = 989
rank-two multiplier total = 516
rank-three constant total = 17
```

The rank-three constants agree row-by-row with the exact selected-response return kernel. Therefore the same collinear triples are not counted once symbolically and again as an unrelated return class.

## Relation to the canonical residual return worklist

`docs/561-prime-power-side-four-residual-return-credit-worklist.md` expands response pairs into 516 rank-two ownership entries because each occupancy-three or occupancy-four line contributes several response pairs. This symbolic compiler instead keeps one entry per distinct response line. The two tables agree on geometry but serve different certificate layers.

## Remaining numerical inputs

Every one of the 488 line occurrences still requires:

```text
actual background height on that coordinate line
line-owner/provenance label
child key
positive child weight
```

The formula is exact, but rank-one and rank-two numerical coefficients are not populated until the actual background profile is attached. The fixed identity matching is not silently substituted for that missing background.

## Honesty boundary

```text
symbolic_line_coefficient_rule_complete_for_normalized_block = 1
rank_three_line_constants_match_return_kernel = 1

actual_background_height_profiles_complete = 0
line_owner_labels_complete = 0
numeric_rank_one_rank_two_line_coefficients_complete = 0
line_child_keys_complete = 0
line_child_weights_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The checker recomputes the six selector catalogues from coordinates, binds the exact return context, validates the aggregate multipliers and rejects twelve corruptions.