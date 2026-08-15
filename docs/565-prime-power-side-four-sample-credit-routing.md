# Side-four sample credit routing

This post-ledger support artifact routes the four recreated credits in the explicit side-four background sample exactly once. It does not add a theorem identifier after CMR4517 and does not claim a strict weighted recurrent row.

```text
sample = data/prime_power_side_four_actual_background_sample_batch.json
sample seal = 71ba5fcea70f61c5e94e40a635b7eddaa8cb72c8c0cdda9fb78f0f56a84609a0
routing = data/prime_power_side_four_sample_credit_routing_contract.json
routing seal = f4920483e99ed4d53da28fc5a752391e570cfceab828937e5d63ac36d91553b5
checker = scripts/check_prime_power_side_four_sample_credit_routing.py
```

## One-count accounting

The complete line kernel is used as the certificate source. The return category is the offspring-charge destination. The line coefficient is therefore not added as a second child term.

```text
line role = certificate-source-only
return role = offspring-charge
rank-three credits = 0
```

The four exact credits are:

```text
rank one: response 02 with background pair {44,65} -> returned predecessor 00
rank one: response 23 with background pair {44,65} -> returned predecessor 22
rank two: response pair {02,23} with background point 44 -> returned predecessor 22
rank two: response pair {02,23} with background point 65 -> returned predecessor 22
```

Every credit retains the full declared child key:

```text
structural owner
fate
collision class
local line class
interface label
remaining background, CRT, credit-rank and entering-owner provenance
```

## Compressed child classes

The four credits compress losslessly to three classes:

```text
return:00 | rank1:1,-2,4:h2:k2 -> coefficient 1
return:22 | rank1:1,-2,4:h2:k2 -> coefficient 1
return:22 | rank2:1,-2,4:h2:k2 -> coefficient 2
```

The exact symbolic weighted return expression is

```text
w_return_00_rank1 + w_return_22_rank1 + 2*w_return_22_rank2
```

All three weights are required to be positive, but no numerical weights or parent budget have been supplied.

## Honesty boundary

```text
sample_credit_partition_complete = 1
sample_child_routing_complete = 1
sample_child_keys_complete_for_populated_credits = 1

sample_child_weights_complete = 0
sample_weighted_row_strict = 0
global_child_provenance_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The checker reconstructs the credit set from the sample coordinates, validates the lossless compression and rejects fourteen independent corruptions. The next task is a scoped positive-weight and parent-budget certificate, or an exact statement that no such certificate is currently justified.