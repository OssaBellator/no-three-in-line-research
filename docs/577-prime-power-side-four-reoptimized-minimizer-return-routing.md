# Return routing on the reoptimized side-four minimizer responses

This post-ledger support artifact recomputes return-credit routing after the complete-line score invalidates the earlier response-only selectors. It introduces no theorem identifier after CMR4517.

```text
contract = data/prime_power_side_four_reoptimized_minimizer_return_routing.json
contract seal = de7742146a77134b97d3ccb36c6112bd458cf8920e346c2e9e515777a9c5b2b6
checker = scripts/check_prime_power_side_four_reoptimized_minimizer_return_routing.py
selector-score source = c5a7f78ddef889aacdffc152b40945ed4b798f850c9aecbd20d4428f9ea63d0e
```

## Accounting rule

Every recreated credit is counted once. Complete-line energy certifies its existence; the return row records its offspring destination. The owner is the lexicographically maximal entering response edge in the credit, and its return charge is transported to the same-source identity predecessor.

Routing derived from the obsolete responses `2031` and `3012` is not reusable.

## Zero-response sample minimizer face

The complete-line minimizer face is

```text
{2301,2310,3201}.
```

For each of these three responses, the declared background creates no rank-one or rank-two credit and the response itself creates no rank-three credit. Hence each exact return row is empty:

```text
return charges = {00:0,11:0,22:0,33:0}
weighted return expression = 0
```

Return terms therefore preserve the three-way line-score tie. Collision, interface and globally weighted child terms are still needed to resolve the complete coupled selector.

## Blocker-alternative minimizer

The complete-line minimizer is `3210`, with response edges

```text
03,12,21,30.
```

All four points lie on

```text
x + y - 3 = 0.
```

The four response triples are recreated rank-three credits. Exact ownership gives:

```text
03|12|21 -> owner 21 -> returned predecessor 22
03|12|30 -> owner 30 -> returned predecessor 33
03|21|30 -> owner 30 -> returned predecessor 33
12|21|30 -> owner 30 -> returned predecessor 33
```

Thus

```text
return charges = {00:0,11:0,22:1,33:3}
```

and lossless compression yields two exact child classes:

```text
return:22 | rank3:1,1,-3:h0:k4 | collision:02,20 -> coefficient 1
return:33 | rank3:1,1,-3:h0:k4 | collision:02,20 -> coefficient 3
```

The symbolic weighted row is

```text
w_reopt_return_22_rank3_k4 + 3*w_reopt_return_33_rank3_k4.
```

Both weights remain unresolved. The old `3012` return total was five; the reoptimized `3210` return total is four.

## Honesty boundary

```text
joint_sample_reoptimized_return_routing_complete = 1
zero_reoptimized_return_rows_complete = 1
blocker_reoptimized_return_row_complete = 1

reoptimized_child_weights_complete = 0
joint_sample_complete_coupled_selector_terms_complete = 0
joint_sample_full_compulsory_rows_complete = 0
global_binding_constructed = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The checker derives all credits from coordinates and includes sixteen corruption cases. Complete repository execution and workflow success remain separate validation steps.