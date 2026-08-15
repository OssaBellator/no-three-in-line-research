# Side-four compulsory coefficient dependency map

This post-ledger artifact refines the complete 86-row compulsory obligation worklist into an exact per-category dependency map. Version 4 binds the canonical selected-return exchange context, its exact rank-three return subkernel and the complete rank-one/rank-two residual return structure. It does not introduce a theorem identifier after CMR4517 and it does not populate an unresolved coefficient by a default zero.

```text
obligation contract seal = 62c6c448b40a8b0294a35673aac997eac73c3380b1cceedffe9616c2326f3211
compiled obligation rows seal = b33e4fa3e442349edacbb14a65b088a92b823c67b6a4f810958076a65e3e797b

return context contract seal = 0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b
compiled return-context rows seal = fdb2ff3287ce607727740130754230cd9c55a415985f393ea166bb3f7ef626ea

residual return contract seal = 606627526d45ca38c216ad036439046b0da8d9f90f12041fa25019fbb2a82808
compiled residual return rows seal = 72efb06f92a1af90addde21b06146cdfc5b73f31134953583effae188f8713d2

dependency contract = data/prime_power_side_four_compulsory_coefficient_dependency_contract.json
dependency contract seal = b1adfb20df51302092d9b8f7acfde9d8ed602f12895310cd54c64ab44cac4f1a
compiled dependency records seal = 2cb9ef2f8a8962a1e848bfc264ec93e3c85ccbf6dccea1766185d29aa6945505
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

The exact v4 census is:

```text
dependency records = 516
known coefficient records = 86
unresolved coefficient records = 430
child-binding unresolved records = 516
known input occurrences = 774
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
known input occurrences = 258
missing input occurrences = 172
```

Every row now contains three exact return inputs:

```text
selected-return exchange class and returned-edge state
exact rank-three return charges
complete rank-one/rank-two residual structural worklist
```

The residual structure contains 344 rank-one entering-edge dependencies and 516 rank-two response-pair line dependencies. The return coefficient still requires actual background incidences, one exact return child key and the total coefficient rule.

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

## Return structures now bound

The canonical selected-return context supplies:

```text
344 source exchange entries
17 recreated rank-three credits
13 nonzero rank-three kernel entries
11 nonzero rank-three rows
```

The residual worklist supplies:

```text
344 rank-one entering-edge dependencies
516 rank-two response-pair dependencies
23 exact rank-two line equations
477 occupancy-two pair rows
27 occupancy-three pair rows
12 occupancy-four pair rows
```

The all-pair response-transition catalogue in `docs/559-prime-power-side-four-return-exchange-manifest.md` remains a separate selector-switch surface. The dependency map uses the identity-to-selected context in `docs/560-prime-power-side-four-return-exchange-context.md` and the residual worklist in `docs/561-prime-power-side-four-residual-return-credit-worklist.md`.

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
1. attach actual background incidences, an exact return child key and the total return coefficient rule
2. attach actual background-height profiles and line ownership
3. attach collision child owner/fate/class routing
4. attach child interface routes and provenance
5. evaluate complete coupled response scores on full minimizer faces
6. bind every category occurrence to an exact child key and positive weight
```

## Honesty boundary

```text
side_four_compulsory_coefficient_dependency_map_complete = 1
dependency_map_complete_for_normalized_block = 1
return_exchange_inputs_grounded = 1
residual_return_structure_grounded = 1

unresolved_coefficients_populated = 0
actual_background_profiles_complete = 0
global_child_provenance_complete = 0
child_weights_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The v4 contract and compiled-record seals, all 516 records, all 774 available input occurrences, the return-context and residual-return bindings and thirteen corruption cases were reproduced locally. The next task is to attach actual background-height and line-incidence data to the exact return and line structures.
