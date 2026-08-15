# Side-four blocker sample credit routing

This post-ledger support artifact routes every recreated credit in the explicit blocker-alternative sample to exactly one returned-predecessor child class. It does not introduce a theorem identifier after CMR4517.

```text
sample = data/prime_power_side_four_blocker_actual_background_sample_batch.json
sample seal = 39677a7e68826f9bf9702d3af8f3b4218138fa0bb1d885c6801d220dddcabeaf
routing = data/prime_power_side_four_blocker_sample_credit_routing_contract.json
routing seal = 4b8da717b59a47d8c5f1d4db1308e934c26390804611b0906c81c30cce136aa5
checker = scripts/check_prime_power_side_four_blocker_sample_credit_routing.py
```

## One-count credit partition

The blocker sample contains five recreated credits:

```text
rank one = 2
rank two = 2
rank three = 1
```

Line energy is the certificate source. Return classes are the offspring destination. The same credit is never counted as both a line offspring and a return offspring.

The exact returned-predecessor census is

```text
00 -> 1 credit
11 -> 3 credits
33 -> 1 credit
```

The rank-three credit is the selected-response triple `10|21|32`; it is owned by entering edge `32` and charged to same-source predecessor `33`.

## Lossless child classes

The five credits compress into four full classes:

```text
return:00 | rank1:3,1,-3:h2:k2 | collision:02,20 -> 1
return:11 | rank1:3,1,-3:h2:k2 | collision:02,20 -> 1
return:11 | rank2:3,1,-3:h2:k2 | collision:02,20 -> 2
return:33 | rank3:1,-1,-1:h0:k3 | collision:02,20 -> 1
```

Each child key retains:

```text
structural returned-edge owner
repeated-return fate
collision class 02,20
exact local line class
side-four target-01 interface
background identifier
rank class
CRT-not-applied sample provenance
entering owner
source blocker-alternative fate
minimal blocker b4-8a44614df456
```

## Symbolic weighted row

The exact return expression is

```text
w_return_00_rank1
+ w_return_11_rank1
+ 2*w_return_11_rank2
+ w_return_33_rank3.
```

Every weight is required positive, but no numerical weights or parent budget are bound.

## Honesty boundary

```text
blocker_sample_credit_partition_complete = 1
blocker_sample_child_routing_complete = 1
blocker_sample_child_keys_complete_for_populated_credits = 1

blocker_sample_child_weights_complete = 0
blocker_sample_weighted_row_strict = 0
global_child_provenance_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The contract digest and routing construction were reproduced locally, and the checker source was syntax-compiled. Complete repository execution and workflow success were not independently observed.
