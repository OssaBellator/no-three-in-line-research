# Side-four residual return-credit worklist

This post-ledger artifact compiles every rank-one and rank-two return-credit dependency on the canonical selected-return rows. It retains exact response geometry, ownership and returned predecessors while leaving all actual-background incidences and child bindings unresolved.

```text
selected-response manifest seal = 0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6
return-context contract seal = 0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b
compiled return-context rows seal = fdb2ff3287ce607727740130754230cd9c55a415985f393ea166bb3f7ef626ea
contract = data/prime_power_side_four_residual_return_credit_worklist_contract.json
contract seal = 606627526d45ca38c216ad036439046b0da8d9f90f12041fa25019fbb2a82808
compiled residual rows seal = 72efb06f92a1af90addde21b06146cdfc5b73f31134953583effae188f8713d2
checker = scripts/check_prime_power_side_four_residual_return_credit_worklist.py
```

## Rank-one structural dependencies

For each selected entering edge, a rank-one recreated credit would consist of that entering edge together with an unresolved collinear background pair. The entering edge is the unique entering owner and is charged to its returned identity predecessor in the same source.

```text
rank-one dependency entries = 344
unresolved background-pair incidences = 344
```

Returned predecessor census:

```text
00 = 86
11 = 86
22 = 86
33 = 86
```

Matching-cycle census:

```text
cycle length 2 = 68
cycle length 4 = 276
```

No background-pair count is assigned before the actual background incidence profile is present.

## Rank-two structural dependencies

For every unordered pair of selected response edges, the checker retains:

```text
exact response pair
canonical real-line equation
response occupancy on that line
lexicographically maximal entering owner
same-source returned identity predecessor
matching-cycle length
```

A rank-two recreated credit would add one unresolved background point on that exact line.

```text
rank-two dependency entries = 516
unresolved background-point incidences = 516
distinct exact line equations = 23
```

Returned predecessor census:

```text
11 = 86
22 = 172
33 = 258
```

Source 00 never owns a rank-two pair because every response pair has a larger source coordinate.

Matching-cycle census:

```text
cycle length 2 = 102
cycle length 4 = 414
```

Response-line occupancy census:

```text
occupancy 2 = 477
occupancy 3 = 27
occupancy 4 = 12
```

The occupancy-three entries are the three pairs on each of the nine selected one-triple responses. The occupancy-four entries are all six pairs on each of the two selected four-triple responses.

## Exact line-equation multiplicities

The 23 canonical line equations have the following occurrence multiplicity distribution across the 516 rank-two entries:

```text
2 equations occur 9 times
8 equations occur 13 times
3 equations occur 15 times
1 equation occurs 27 times
2 equations occur 28 times
5 equations occur 34 times
1 equation occurs 47 times
1 equation occurs 49 times
```

These are response-side geometric counts only. They do not determine how many actual background points lie on the lines.

## Remaining coefficient inputs

The worklist does not populate:

```text
rank-one background-pair incidences
rank-two background-point incidences
background-height profiles
line owner/provenance labels
rank-one child keys and positive weights
rank-two child keys and positive weights
complete return coefficient rule
```

The exact rank-three return subkernel remains supplied separately by `docs/560-prime-power-side-four-return-exchange-context.md`.

## Honesty boundary

```text
side_four_residual_return_credit_worklist_complete = 1
rank_one_return_structure_complete_for_normalized_block = 1
rank_two_return_structure_complete_for_normalized_block = 1

actual_background_profiles_complete = 0
rank_one_return_coefficients_complete = 0
rank_two_return_coefficients_complete = 0
residual_return_credit_classes_complete = 0
return_child_keys_complete = 0
return_child_weights_complete = 0
complete_return_coefficient_rule_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The contract and row seals, all 860 dependency entries, all line equations and ownership labels and twelve corruption cases were reproduced locally. The next task is to attach actual background-height and line-incidence data to these exact entries.
