# Shell batch amortization law

`docs/637` gives the one-period collateral condition `6 delta + C < 3` for six
uses of a candidate `(1,1,1)` clean macro. This chapter determines exactly when a
fixed setup or collateral charge can be amortized across several periods.

## 1. Batched cost identity

### Theorem PP3cyr — PROVED / EXACT T-PERIOD COST

For `t` service periods, per-use overhead `delta`, and one fixed batch collateral
charge `C`, the active-equivalent cost is

```text
t(12+6 delta)+C.
```

It beats the recorded baseline `15t` exactly when

```text
t(3-6 delta) > C.
```

#### Proof

Each period uses the twelve-control frontier point with six candidate macro uses.
Add the per-use overhead over `6t` uses and the one-time charge `C`, then compare
with `15t`. ∎

## 2. Sharp amortizability threshold

### Theorem PP3cys — PROVED / AMORTIZABLE IFF DELTA BELOW ONE HALF

A finite fixed collateral charge can be amortized over some number of periods if
and only if

```text
delta < 1/2.
```

When this holds, the minimum period count is the least integer `t` satisfying the
strict inequality in `PP3cyr`.

#### Proof

The coefficient `3-6 delta` is positive exactly below one half. If it is positive,
the left side grows without bound; otherwise it is nonpositive and cannot exceed
nonnegative collateral. ∎

## 3. Exact integer schedules

### Theorem PP3cyt — PROVED / ZERO-OVERHEAD PERIOD FORMULA

At zero per-use overhead, the minimum number of periods required to absorb an
integer fixed charge `C` is

```text
floor(C/3)+1.
```

For example, at `delta=1/6`, charges `C=1,2,5` require respectively `1,2,3`
periods.

#### Proof

Substitute into `t(3-6 delta)>C` and take the least integer solution.
`scripts/check_shell_amortized_collateral.py` audits the formula and examples with
exact rational arithmetic. ∎

## Consequence

A geometric `(1,1,1)` macro need not pay all fixed setup cost in one period. But
its true per-use overhead must still be strictly below one half, and its fixed
collateral must be identified and schedulable before this amortization theorem
can be used.
