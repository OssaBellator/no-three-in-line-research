# Side-four joint sample weight compatibility

This post-ledger support artifact combines the zero-response and blocker-alternative sample weight contracts in one exact child-class namespace. It does not introduce a theorem identifier after CMR4517 and does not prove compatibility with the global recurrent Lyapunov system.

```text
zero weight seal = d85580884ba95d368350ee1230890e4b54b86c33466c55fb20cb837de46b7316
blocker weight seal = f879314c3ab11b96e3fc09df0c5f540cde441055c6af00f631c4cbbee4deafb5
joint contract = data/prime_power_side_four_joint_sample_weight_compatibility_contract.json
joint seal = 1fef7cdd2e3554800e3c9c2ace9b78fa02b0df655b57556c21eb681233287dd5
checker = scripts/check_prime_power_side_four_joint_sample_weight_compatibility.py
```

## Exact namespace correction

The two local contracts each use the alias

```text
w_return_00_rank1.
```

The corresponding full child keys are different:

```text
zero sample:
return:00 | rank1:1,-2,4:h2:k2

blocker sample:
return:00 | rank1:3,1,-3:h2:k2 | collision:02,20
```

They must not be merged. The joint namespace therefore contains seven exact child classes even though there are only six local aliases.

```text
local aliases = 6
exact child classes = 7
colliding aliases = 1
```

The two `return:00` classes receive separate joint symbols:

```text
w_zero_return_00_rank1
w_blocker_return_00_rank1.
```

## Joint local rows

The zero-response return-only row is

```text
w_zero_return_00_rank1
+ w_zero_return_22_rank1
+ 2*w_zero_return_22_rank2.
```

The blocker return-only row is

```text
w_blocker_return_00_rank1
+ w_blocker_return_11_rank1
+ 2*w_blocker_return_11_rank2
+ w_blocker_return_33_rank3.
```

## Explicit joint local witness

```text
both parent weights = 16
all seven exact child-class weights = 1
```

This gives

```text
zero weighted total = 4
zero strict slack = 12
blocker weighted total = 5
blocker strict slack = 11.
```

After parent normalization, every child weight is `1/16`; the zero row has total `1/4` and slack `3/4`, while the blocker row has total `5/16` and slack `11/16`.

The witness proves simultaneous local return-only feasibility in the direct exact-class namespace. It does not bind either parent or any child to an installed global weight.

## Residual binding surface

Sixteen records remain explicit:

```text
two parent state keys
two parent global weight bindings
seven exact child-class global weight bindings
two selector/collision/interface binding groups
global recurrent-block compatibility
global weight normalization
global transition occurrence
```

## Honesty boundary

```text
joint_sample_exact_weight_namespace_complete = 1
joint_sample_local_positive_assignment_complete = 1
joint_sample_return_only_rows_strict_under_local_witness = 1

joint_sample_global_weight_bindings_complete = 0
joint_sample_full_compulsory_rows_complete = 0
joint_sample_global_recurrent_compatibility_proved = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The contract digest, alias audit and arithmetic witness were reproduced locally, and the checker source was syntax-compiled. Complete repository execution and workflow success were not independently observed.
