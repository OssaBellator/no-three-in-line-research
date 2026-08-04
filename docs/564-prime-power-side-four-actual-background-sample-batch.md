# Side-four actual-background sample batch

This post-ledger support artifact populates one explicit integer-coordinate background profile for the normalized side-four block. It does not introduce a theorem identifier after CMR4517 and does not claim that the sample is a globally occurring recurrent state.

```text
sample = data/prime_power_side_four_actual_background_sample_batch.json
sample seal = 71ba5fcea70f61c5e94e40a635b7eddaa8cb72c8c0cdda9fb78f0f56a84609a0
checker = scripts/check_prime_power_side_four_actual_background_sample_batch.py
host = s4-fc915f89dec31fec
selected response = 2031
```

## Explicit profile

The profile is declared independently rather than inferred from the normalized host or the identity matching.

```text
background points = {(4,4), (6,5)}
coordinate scope = integer-lattice sample; no global-board claim
active line = x - 2y + 4 = 0
response points on active line = (0,2), (2,3)
background load h = 2
response occupancy k = 2
```

The point provenance, line-owner label, target-interface label and CRT-not-applied label are all explicit in the sample contract.

## Exact line coefficients

For the six response-pair lines, only `x-2y+4=0` has positive background load. The complete line kernel is

```text
K(h,k) = k*C(h,2) + C(k,2)*h + C(k,3)
K(2,2) = 2 + 2 + 0 = 4
```

The exact coefficient totals are:

```text
rank-one total = 2
rank-two total = 2
rank-three total = 0
complete line-kernel total = 4
```

The rank-one entering-edge incidences are:

```text
02 -> 1
10 -> 0
23 -> 1
31 -> 0
```

The only positive rank-two response-pair incidence is:

```text
02|23 -> 2
```

## Exact return charges

The rank-one credits charge their same-source identity predecessors. Rank-two credits use the lexicographically maximal entering response edge as owner and then its same-source predecessor.

```text
rank-one return charges = {00:1, 11:0, 22:1, 33:0}
rank-two return charges = {00:0, 11:0, 22:2, 33:0}
total return charges = {00:1, 11:0, 22:3, 33:0}
```

Thus this one row numerically populates two non-geometric categories: the complete line coefficient and the rank-one/rank-two return coefficient.

## Validation and honesty boundary

The checker reconstructs every coefficient from the explicit coordinates, verifies the selected-response and profile-obligation seals, and rejects fourteen independent corruptions.

```text
side_four_actual_background_sample_batch_complete = 1
sample_line_coefficients_complete = 1
sample_rank_one_rank_two_return_coefficients_complete = 1

actual_background_profiles_complete = 0
global_child_provenance_complete = 0
child_keys_complete = 0
child_weights_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

This sample proves that the obligation schema can be populated and evaluated numerically. It does not supply a global background batch, child-state bindings, Lyapunov weights, or a strict recurrent row.