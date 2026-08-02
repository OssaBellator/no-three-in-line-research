# Heterogeneous shell schedule envelope

`docs/649` treats a constant recurring burden. A geometric macro may instead
have period-dependent repair and collision costs. This chapter gives the exact
prefix criterion for an arbitrary burden sequence and a complete classification
for periodic schedules.

For period `i`, write

```text
b_i = 6*delta_i + c_i,
```

where `delta_i` is the per-use overhead of each of the six `(1,1,1)` uses and
`c_i` is the other recurring collateral in that period.

## PP3dab — Exact heterogeneous prefix criterion

For the first `k` periods and one-time setup `S`, the candidate cost is

```text
12k + sum_{i<=k} b_i + S.
```

Against baseline `15k`, define cumulative saving

```text
B_k = sum_{i<=k} (3-b_i).
```

The first `k` periods strictly improve the baseline exactly when `B_k>S`.
This permits temporarily expensive periods provided later savings more than
repay both the deficit and setup.

## PP3dac — Arbitrary-setup amortization criterion

A fixed setup value `S` is amortizable exactly when some prefix satisfies
`B_k>S`. Every finite setup is amortizable exactly when

```text
sup_k B_k = infinity.
```

If the average burden converges to `b`, then `b<3` implies unbounded cumulative
saving, `b>3` prevents arbitrarily large setup amortization, and `b=3` is a
boundary case controlled by fluctuations of `B_k`.

## PP3dad — Complete periodic classification

Suppose `b_i` is periodic with period `m`. Let

```text
p_r = sum_{i=1}^r (3-b_i),
G   = p_m.
```

Then:

1. If `G>0`, every fixed setup is amortizable. The minimum improving prefix is

   ```text
   min_{1<=r<=m} [m*max(0,floor((S-p_r)/G)+1)+r].
   ```

2. If `G=0`, setup `S` is amortizable exactly when `max_r p_r>S`.
3. If `G<0`, later full cycles lower every prefix saving, so setup `S` is again
   amortizable exactly when `max_r p_r>S`, with the earliest improvement in the
   first cycle.

The constant-burden law is the special case `m=1`. Individual periods may tie or
lose when compensated by a positive-gain cycle.

## Verification

- `scripts/check_shell_heterogeneous_schedule.py` checks the exact prefix and
  periodic formulas with rational arithmetic.
- `scripts/check_shell_irregular_period_schedule.py` independently checks the
  repeatable-cycle mean criterion and finite examples.

## Evidence boundary

No geometric `(1,1,1)` macro supplies a certified burden sequence with unbounded
cumulative saving. The values `delta_i` and `c_i` have not yet been derived from
coordinates and exposed-state repairs.
