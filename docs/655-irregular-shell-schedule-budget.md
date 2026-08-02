# Irregular shell schedule budget

The constant-period shell law extends exactly to schedules whose overhead and
collateral vary from period to period.

## PP3dab — Exact irregular saving formula

For periods `i=1,...,k`, let `delta_i` be per-use overhead, let `c_i` be recurring
collateral, and let `S` be one-time setup. Candidate cost is

```text
12k + sum_i(6*delta_i+c_i) + S.
```

Against baseline `15k`, exact saving is

```text
sum_i(3-6*delta_i-c_i) - S.
```

Thus individual periods may tie or lose if other periods compensate them.

## PP3dac — Repeatable-cycle criterion

For a cycle of `m` periods, write its burden and margin as

```text
B = sum_i(6*delta_i+c_i),
M = 3m-B.
```

Repeating the cycle can amortize some finite setup exactly when

```text
M>0,
```

or equivalently when its mean burden is strictly below three.

At unit macro cost, the collateral cycle `(0,3)` has mean burden `3/2` and saves
three controls per two-period cycle even though its second period alone ties the
baseline.

## PP3dad — Exact setup repetition count

For positive cycle margin `M` and fixed setup `S`, the least number of complete
cycle repetitions giving strict improvement is

```text
floor(S/M)+1.
```

The formula is sharp by the strict inequalities

```text
(r-1)M <= S < rM.
```

The exact audit is `scripts/check_shell_irregular_period_schedule.py`.

## Evidence boundary

No coordinate-level `(1,1,1)` macro schedule has supplied a repeatable burden
cycle with mean below three. This is a cost interface, not a geometric macro.
