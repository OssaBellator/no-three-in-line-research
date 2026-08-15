# Side-four blocker sample return-only weight feasibility

This post-ledger support artifact binds an explicit positive local weight witness to the exact blocker-sample credit-routing contract. It does not introduce a theorem identifier after CMR4517 and does not claim compatibility with the global recurrent Lyapunov system.

```text
routing = data/prime_power_side_four_blocker_sample_credit_routing_contract.json
routing seal = 4b8da717b59a47d8c5f1d4db1308e934c26390804611b0906c81c30cce136aa5
weight contract = data/prime_power_side_four_blocker_sample_weight_feasibility_contract.json
weight contract seal = f879314c3ab11b96e3fc09df0c5f540cde441055c6af00f631c4cbbee4deafb5
checker = scripts/check_prime_power_side_four_blocker_sample_weight_feasibility.py
```

## Exact return-only row

The exact blocker-sample return expression is

```text
w_return_00_rank1
+ w_return_11_rank1
+ 2*w_return_11_rank2
+ w_return_33_rank3.
```

For parent weight `w_parent_blocker_sample`, the local row is strict exactly when

```text
w_parent_blocker_sample
> w_return_00_rank1
+ w_return_11_rank1
+ 2*w_return_11_rank2
+ w_return_33_rank3.
```

## Explicit scoped witness

```text
parent weight = 10
four child-class weights = 1,1,1,1
weighted child total = 5
strict slack = 5
```

After normalizing the parent to one, every child weight is `1/10`, the weighted total is `1/2`, and the strict slack is `1/2`.

This proves only that the blocker sample's local return cone is nonempty. The witness is not asserted to match any installed global recurrent block.

## Category accounting

```text
return = locally weighted under the explicit witness
line = certificate source only; no duplicate offspring charge
geometric rank-three term = certificate source only; no duplicate offspring charge
selector = unresolved, not zero
collision = unresolved, not zero
interface = unresolved, not zero
```

The intrinsic selected-response triple has already been routed once to the `return:33` child class. It is not added again as an independent geometric offspring.

## Residual binding worklist

Ten records remain:

```text
parent state key
parent global weight binding
four child-class global weight bindings
selector coefficient and child binding
collision coefficient and child binding
interface coefficient and child binding
global recurrent-block compatibility
```

## Honesty boundary

```text
blocker_sample_return_only_weight_feasibility_proved = 1
blocker_sample_return_only_local_witness_complete = 1

blocker_sample_global_weight_bindings_complete = 0
blocker_sample_full_compulsory_row_complete = 0
blocker_sample_weighted_row_strict = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The contract digest and arithmetic witness were reproduced locally, and the checker source was syntax-compiled. Complete repository execution and workflow success were not independently observed.
