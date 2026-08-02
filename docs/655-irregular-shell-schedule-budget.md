# Irregular shell schedule budget

`docs/649` treats a macro with the same overhead and recurring collateral in every
period. A geometric construction may instead alternate several macro variants or
repair regimes. This chapter gives the exact criterion for such irregular
schedules.

## PP3dab — Exact irregular-schedule saving

For `k` periods with per-use overheads `delta_i`, recurring collateral costs
`c_i`, and one-time setup `S`, the saving against the fifteen-control baseline is

```text
sum_i (3 - 6*delta_i - c_i) - S.
```

The schedule strictly improves exactly when this quantity is positive.

### Proof

The candidate cost is

```text
12k + sum_i (6*delta_i+c_i) + S.
```

Subtract it from `15k`. ∎

## PP3dac — Repeatable cycles are governed by mean burden

Let a cycle of `m` periods have burdens `b_i=6*delta_i+c_i`. Some finite number
of repetitions beats any fixed setup cost exactly when

```text
(1/m) sum_i b_i < 3.
```

If the cycle margin is `M=sum_i(3-b_i)>0`, the minimum repetitions needed to pay
setup `S` are

```text
floor(S/M) + 1.
```

### Proof

Repeating the cycle `q` times gives saving `qM-S`. This is positive for some
integer `q` exactly when `M>0`, with the displayed least value. ∎

## PP3dad — Heavy periods may be compensated

An individual period may tie or lose (`b_i>=3`) provided the cycle mean remains
below three. At unit macro cost, the two-period collateral cycle `(0,3)` has mean
burden `3/2` and saves three controls per cycle, despite its second period alone
tying the baseline.

### Proof

Apply `PP3dac`: the cycle burden is three over two periods, so its margin is
`6-3=3`. The exhaustive finite-cycle audit is in
`scripts/check_shell_irregular_period_schedule.py`. ∎

## Evidence boundary

The shell search need not demand that every period satisfy the strict budget
individually. It may use a finite repertoire of macro variants, provided their
repeatable average burden is below three and all geometric interactions are
scheduled consistently.
