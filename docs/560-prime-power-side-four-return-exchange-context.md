# Side-four selected-return exchange context

This post-ledger artifact fixes the old selected matching to the normalized identity matching and the new matching to the canonical selected response on each of the 86 side-four hosts. It is the canonical return context consumed by the v3 compulsory coefficient dependency map.

```text
selected-response manifest seal = 0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6
contract = data/prime_power_side_four_return_exchange_context_contract.json
contract seal = 0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b
compiled return-context rows seal = fdb2ff3287ce607727740130754230cd9c55a415985f393ea166bb3f7ef626ea
checker = scripts/check_prime_power_side_four_return_exchange_context.py
```

## Exact selected-return exchange

The old matching is

```text
00,11,22,33
```

and the new matching is the canonical selected response. Every source contributes one exact exchange entry

```text
[source, returned identity edge, selected entering edge, alternating-cycle length, exchange class]
```

The finite census is:

```text
rows = 86
exchange entries = 344
returned 00 = 86
returned 11 = 86
returned 22 = 86
returned 33 = 86
alternating length 4 entries = 68
alternating length 8 entries = 276
hosts with two alternating 4-cycles = 17
hosts with one alternating 8-cycle = 69
```

The exchange class retains source, returned edge, entering edge and alternating-cycle length. Total churn alone is not used as the return state.

## Exact rank-three return subkernel

The physical credit system in this finite context is the set of collinear triples in the selected response. Every recreated triple is assigned to its lexicographically maximal entering edge and then transported to the returned identity predecessor in the same source row.

The exact rank-three census is:

```text
recreated rank-three credits = 17
nonzero kernel entries = 13
nonzero host rows = 11
charge to returned edge 22 = 2
charge to returned edge 33 = 15
coarse old-overlap-0 / matching-cycle-2 credits = 8
coarse old-overlap-0 / matching-cycle-4 credits = 9
```

All 75 zero-response rows have zero rank-three return charge. The 11 blocker-alternative rows contain the complete nonzero rank-three subkernel.

## Relation to the all-pair exchange catalogue

```text
data/prime_power_side_four_return_exchange_manifest_contract.json
scripts/check_prime_power_side_four_return_exchange_manifest.py
```

The all-pair catalogue enumerates 378 ordered transitions between distinct allowed responses and is useful for selector-switch and response-to-response analysis. This canonical context instead fixes the actual normalized old identity matching and selected destination and is the source used by the dependency map.

The two artifacts are complementary. Neither may replace the other by an arbitrary projection.

## Remaining return coefficient inputs

The selected-return context supplies:

```text
return exchange class
returned edge
entering edge
alternating-cycle label
exact rank-three recreated-credit ownership
exact rank-three K_{f,b} entries
```

The complete return coefficient still requires:

```text
residual non-rank-three recreated-credit classes
complete owner/fate/collision/line/interface provenance
one exact return child key per class
one positive child weight per class
complete coefficient rule summing all classes without double counting
```

## Honesty boundary

```text
return_exchange_context_complete_for_normalized_block = 1
rank_three_return_kernel_complete_for_normalized_block = 1

complete_return_coefficient_rule_complete = 0
residual_return_credit_classes_complete = 0
return_child_keys_complete = 0
return_child_weights_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The contract and row seals, all 344 exchange entries, all rank-three charges and twelve corruption cases were reproduced locally. The next return task is to enumerate the residual rank-one, rank-two, selector, collision and interface credit classes on these exact exchange rows.
