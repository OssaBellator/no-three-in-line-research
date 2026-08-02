# Heterogeneous shell schedule envelope

`docs/655-irregular-shell-schedule-budget.md` treats finite repeatable cycles by
their total margin. A geometric macro may instead have period-dependent repair
and collision costs before any useful cycle is known. This chapter gives the
exact prefix criterion for an arbitrary burden sequence and a complete periodic
classification.

For period `i`, write

```text
b_i = 6*delta_i + c_i,
```

where `delta_i` is the per-use overhead of each of the six `(1,1,1)` uses and
`c_i` is the other recurring collateral in that period.

## PP3dan — Exact heterogeneous prefix criterion

For the first `k` periods and one-time setup `S`, the candidate cost is

```text
12k + sum_{i<=k} b_i + S.
```

Against baseline `15k`, define cumulative saving

```text
B_k = sum_{i<=k} (3-b_i).
```

The first `k` periods strictly improve the baseline exactly when

```text
B_k > S.
```

This criterion permits temporarily expensive periods provided later savings more
than repay both the deficit and setup.

## PP3dao — Arbitrary-setup amortization criterion

A fixed setup value `S` is amortizable exactly when some prefix satisfies
`B_k>S`. Every finite setup is amortizable exactly when

```text
sup_k B_k = infinity.
```

If the average burden converges to `b`, then:

- `b<3` implies unbounded cumulative saving and amortizes every fixed setup;
- `b>3` implies cumulative saving tends to minus infinity and cannot amortize
  arbitrarily large setup;
- `b=3` is a genuine boundary case controlled by fluctuations of `B_k`.

Thus average burden three is not enough by itself; the partial-sum envelope is
the exact invariant.

## PP3dap — Complete periodic classification

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

2. If `G=0`, repetition adds no net saving. Setup `S` is amortizable exactly
   when `max_r p_r>S`.
3. If `G<0`, every later full cycle lowers all prefix savings. Setup `S` is
   again amortizable exactly when `max_r p_r>S`, and the earliest improving
   prefix occurs in the first cycle.

The constant-burden law of `docs/649-recurring-shell-collateral-barrier.md` is
the special case `m=1`, while the positive-cycle law in `docs/655` is the
`G>0` case.

## Verification

`scripts/check_shell_heterogeneous_schedule.py` uses exact rational arithmetic to
check the prefix criterion, the homogeneous reduction, and positive, zero, and
negative period-surplus examples.

## Remaining shell obligation

No geometric `(1,1,1)` macro currently supplies a certified burden sequence with
unbounded cumulative saving. In particular, the values `delta_i` and `c_i`
have not yet been derived from coordinates and exposed-state repairs.
