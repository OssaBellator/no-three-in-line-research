# Side-four compulsory coefficient dependency map

This post-ledger artifact refines the complete 86-row compulsory obligation worklist into an exact per-category dependency map. It does not introduce a theorem identifier after CMR4517 and it does not populate an unresolved coefficient by a default zero.

```text
obligation contract = data/prime_power_side_four_compulsory_row_obligation_worklist.json
obligation contract seal = 62c6c448b40a8b0294a35673aac997eac73c3380b1cceedffe9616c2326f3211
compiled obligation rows seal = b33e4fa3e442349edacbb14a65b088a92b823c67b6a4f810958076a65e3e797b

dependency contract = data/prime_power_side_four_compulsory_coefficient_dependency_contract.json
dependency contract seal = 4416e7d13dab1b9154040350e0d2b2fbac59e6f94d3984d0bd2b72456c5fb340
compiled dependency records seal = ac085fd5ec8283e266a603b71deac1d434980b0978780e3e18f23f0d6cd37865
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

The exact census is:

```text
dependency records = 516
known coefficient records = 86
unresolved coefficient records = 430
child-binding unresolved records = 516
known input occurrences = 516
missing input occurrences = 1634
```

The 86 geometric coefficients remain known from the selected minimum response energy, but their child keys and positive weights remain unresolved. All 430 return, selector, collision, line and interface coefficients remain unresolved.

## Category dependency classes

### Return

```text
records = 86
status = ungrounded
known input occurrences = 0
missing input occurrences = 344
```

A return coefficient requires the exact returned-edge exchange class, returned-edge or token state, child key and coefficient rule. The normalized host/selector record contains none of those transition-specific inputs.

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

The deletion/collision trace is known. Exact child owner, child fate, child collision class and the collision coefficient rule remain missing.

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

The dependency compiler preserves the exact finite host information:

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
1. attach return-exchange classes and returned-edge/token states
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

unresolved_coefficients_populated = 0
global_child_provenance_complete = 0
child_weights_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The contract and compiled-record seals, all 516 records, the category and input-occurrence censuses and twelve corruption cases were reproduced locally. The next task is to attach transition-specific return data and actual background/provenance refinements rather than derive coefficients from the normalized host alone.
