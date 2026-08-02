# Recurring shell collateral barrier

`docs/643` shows that one-time setup cost can be amortized across a batch.  A
geometric macro may also incur collision or repair cost in every period.  This
chapter separates recurring collateral from fixed setup exactly.

## 1. Full batched cost formula

### Theorem PP3czj — PROVED / RECURRING-PLUS-FIXED COST

For `k` periods, per-use overhead `delta`, recurring collateral `c` per period,
and one-time setup `S`, the candidate cost is

```text
k(12 + 6*delta + c) + S.
```

It strictly improves on the baseline `15k` exactly when

```text
6*delta + c + S/k < 3.
```

#### Proof

Add the six macro overheads and recurring collateral to each twelve-control
period, then add the fixed setup once. ∎

## 2. Sharp asymptotic condition

### Theorem PP3czk — PROVED / RECURRING BARRIER

Some finite batch length improves the baseline exactly when

```text
6*delta + c < 3.
```

When this holds, the minimum batch length is

```text
floor(S/(3-6*delta-c)) + 1.
```

Fixed setup disappears asymptotically; recurring collateral does not.

#### Proof

Rearrange `k(3-6*delta-c)>S`.  A positive left-hand coefficient is necessary and
sufficient. ∎

## 3. Unit-cost integer threshold

### Theorem PP3czl — PROVED / AT MOST TWO RECURRING CONTROLS

At unit macro cost (`delta=0`), the largest integer recurring collateral that can
ever beat the baseline is two controls per period.  With `c=2`, a batch of `k`
periods can additionally pay fixed setup exactly when

```text
S <= k-1.
```

With `c=3`, every batch ties or loses even when `S=0`.

#### Proof

Substitute `delta=0` and integer `c` into `PP3czj--PP3czk`.  The exact examples
are checked in `scripts/check_shell_recurring_collateral.py`. ∎

## Consequence

A bounded construction cost can be amortized, but recurring collision repair is
a genuine asymptotic constraint.  Any geometric `(1,1,1)` macro must place its
per-period burden below `3-6*delta`.
