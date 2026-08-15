# Side-four sample return-only weight feasibility

This post-ledger support artifact binds an explicit positive local weight witness to the exact sample credit-routing contract. It does not add a theorem identifier after CMR4517 and does not claim compatibility with the global recurrent Lyapunov system.

```text
routing = data/prime_power_side_four_sample_credit_routing_contract.json
routing seal = f4920483e99ed4d53da28fc5a752391e570cfceab828937e5d63ac36d91553b5
weight contract = data/prime_power_side_four_sample_weight_feasibility_contract.json
weight contract seal = d85580884ba95d368350ee1230890e4b54b86c33466c55fb20cb837de46b7316
checker = scripts/check_prime_power_side_four_sample_weight_feasibility.py
```

## Exact return-only row

The routed sample credits have three exact child classes and weighted expression

```text
w_return_00_rank1
+ w_return_22_rank1
+ 2*w_return_22_rank2.
```

For a parent weight `w_parent_sample`, the return-only local row is strict exactly when

```text
w_parent_sample
> w_return_00_rank1
+ w_return_22_rank1
+ 2*w_return_22_rank2.
```

After normalizing the parent to one, the equivalent cone is

```text
x00_rank1 + x22_rank1 + 2*x22_rank2 < 1.
```

## Explicit scoped witness

The contract uses the integer witness

```text
parent weight = 8
w_return_00_rank1 = 1
w_return_22_rank1 = 1
w_return_22_rank2 = 1
weighted child total = 4
strict slack = 4
```

Equivalently, after parent normalization, every child weight is `1/8`, the weighted total is `1/2`, and the strict slack is `1/2`.

This proves that the local return-only feasibility cone is nonempty. The numbers are not asserted to be the weights of any installed global recurrent block.

## Category accounting

```text
return = locally weighted under the explicit witness
line = certificate source only; no duplicate offspring charge
geometric = exact zero for the selected response
selector = unresolved, not zero
collision = unresolved, not zero
interface = unresolved, not zero
```

Thus the local witness is not a complete compulsory weighted row.

## Residual binding worklist

Nine records remain explicit:

```text
parent state key
parent global weight binding
three child-class global weight bindings
selector coefficient and child binding
collision coefficient and child binding
interface coefficient and child binding
global recurrent-block compatibility
```

## Honesty boundary

```text
sample_return_only_weight_feasibility_proved = 1
sample_return_only_local_witness_complete = 1

sample_global_weight_bindings_complete = 0
sample_full_compulsory_row_complete = 0
sample_weighted_row_strict = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The contract digest and arithmetic witness were reproduced locally, and the checker source was syntax-compiled. A complete repository execution and workflow success were not independently observed.
