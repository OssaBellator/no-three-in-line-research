# Side-four compulsory coefficient dependency map

This post-ledger artifact refines the complete 86-row compulsory obligation worklist into an exact per-category dependency map. Version 3 additionally binds the canonical identity-to-selected return context and its exact rank-three return subkernel. It does not introduce a theorem identifier after CMR4517 and it does not populate an unresolved coefficient by a default zero.

```text
obligation contract = data/prime_power_side_four_compulsory_row_obligation_worklist.json
obligation contract seal = 62c6c448b40a8b0294a35673aac997eac73c3380b1cceedffe9616c2326f3211
compiled obligation rows seal = b33e4fa3e442349edacbb14a65b088a92b823c67b6a4f810958076a65e3e797b

return context contract = data/prime_power_side_four_return_exchange_context_contract.json
return context contract seal = 0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b
compiled return-context rows seal = fdb2ff3287ce607727740130754230cd9c55a415985f393ea166bb3f7ef626ea

dependency contract = data/prime_power_side_four_compulsory_coefficient_dependency_contract.json
dependency contract seal = 47c765be4b4a79f826dba2ac23fb2d7a69f0d64ba23bb94d1cb1d608178fbacc
compiled dependency records seal = 4cd91e195393ea226474c3c33f80ac63fcdd9c4b8b0bf95b810f54d0c490d401
checker = scripts/check_prime_power_side_four_compulsory_coefficient_dependency_map.py
```

## Complete dependency surface

Every one of the 86 normalized host contexts contributes one dependency record in each compulsory category:

```text
return
selector
collision
line
interface
geometric
```

The exact v3 census is:

```text
dependency records = 516
known coefficient records = 86
unresolved coefficient records = 430
child-binding unresolved records = 516
known input occurrences = 688
missing input occurrences = 1462
ungrounded records = 0
partially grounded records = 430
coefficient-known but binding-unresolved records = 86
```

The 86 geometric coefficients remain known from selected minimum response energy, but their child keys and positive weights remain unresolved. All 430 return, selector, collision, line and interface coefficients remain unresolved.

## Category dependency classes

### Return

```text
records = 86
status = partially grounded
known input occurrences = 172
missing input occurrences = 172
```

Every row now contains an exact return exchange class and returned-edge state. The state includes all four identity predecessors, selected entering edges, alternating-cycle labels and the exact rank-three return charges. The complete return coefficient still requires the residual non-rank-three credit classes, one exact return child key and the total coefficient rule.

The selected-return context supplies:

```text
344 source exchange entries
17 recreated rank-three credits
13 nonzero rank-three kernel entries
11 nonzero rank-three rows
2 credits charged to returned edge 22
15 credits charged to returned edge 33
```

Total churn is not used as the coefficient.

### Selector

```text
records = 86
status = partially grounded
known input occurrences = 172
missing input occurrences = 258
```

The complete minimizer face and next-energy gap are known. The complete coupled response score, selector child key and coefficient rule remain missing. Response-triple energy alone is not the selector coefficient.

### Collision

```text
records = 86
status = partially grounded
known input occurrences = 86
missing input occurrences = 344
```

The deletion/collision trace is known. Exact child owner, child fate, child collision class and collision coefficient rule remain missing.

### Line

```text
records = 86
status = partially grounded
known input occurrences = 86
missing input occurrences = 258
```

The selected-response line signature is known. The actual background-height profile, line ownership labels and complete line-kernel coefficient rule remain missing. The raw host does not determine the actual background set.

### Interface

```text
records = 86
status = partially grounded
known input occurrences = 86
missing input occurrences = 258
```

The normalized target interface is known. The child interface route, complete interface provenance and coefficient rule remain missing.

### Geometric

```text
records = 86
status = coefficient known; binding unresolved
known input occurrences = 86
missing input occurrences = 172
```

The coefficient equals the selected minimum response energy. The geometric child key and positive child weight are still required before the coefficient can enter a weighted recurrent row.

## Finite normalized censuses

```text
collision ranks = {0: 1, 1: 11, 2: 35, 3: 33, 4: 6}
selected responses = {2031: 34, 2301: 15, 2310: 13, 3012: 9, 3201: 13, 3210: 2}
unique minimizer faces = 42
tied minimizer faces = 44
positive next-energy gaps = 47
no higher-energy response = 39
```

## Resolution priority

```text
1. enumerate residual non-rank-three return credit classes and derive the total return rule and child key
2. attach actual background-height profiles and line ownership
3. attach collision child owner/fate/class routing
4. attach child interface routes and provenance
5. evaluate complete coupled response scores on full minimizer faces
6. bind every category occurrence to an exact child key and positive weight
```

## Relation to the all-pair exchange catalogue

The v3 dependency map uses the canonical identity-to-selected context in `docs/560-prime-power-side-four-return-exchange-context.md`. The separate all-pair catalogue in `docs/559-prime-power-side-four-return-exchange-manifest.md` enumerates all 378 ordered response-to-response transitions and is retained for selector-switch analysis. It is not substituted for the canonical selected-return context.

## Honesty boundary

```text
side_four_compulsory_coefficient_dependency_map_complete = 1
dependency_map_complete_for_normalized_block = 1
return_exchange_context_complete_for_normalized_block = 1
rank_three_return_kernel_complete_for_normalized_block = 1

unresolved_coefficients_populated = 0
residual_return_credit_classes_complete = 0
complete_return_coefficient_rule_complete = 0
global_child_provenance_complete = 0
child_weights_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The v3 contract and compiled-record seals, all 516 records, the return-context binding, category and input-occurrence censuses and twelve corruption cases were reproduced locally. The next task is to enumerate the residual non-rank-three return credit classes and attach actual background/provenance refinements.
