# All-length balanced integerization

The compatibility ledger is rational, whereas a prime-patching construction uses
integer numbers of blocks.  This chapter supplies an all-length rounding rule and
a quantitative threshold at which the ledger's strict slack absorbs every
rounding error.

Let rational target proportions `x_1,...,x_s` be nonnegative and sum to one.

## 1. Largest-remainder integerization

### Theorem PP3cnp -- PROVED / BALANCED ALL-LENGTH ROUNDING

For every positive integer `N`, there are nonnegative integers `k_i` with

```text
sum_i k_i=N,
|k_i-N x_i|<1
```

for every `i`.  The largest-remainder rule constructs such a vector by flooring
all `N x_i` and assigning the remaining units to the largest fractional parts.

#### Proof

The number of missing units is the sum of the fractional parts and is an integer
strictly smaller than `s`.  Raising that many floors by one preserves the total.
Every unraised coordinate has error equal to its fractional part, and every
raised coordinate has error one minus its fractional part; both are below one. ∎

## 2. Strict-slack transfer

### Theorem PP3cnq -- PROVED / ROUNDING-ROBUST LEDGER THRESHOLD

Suppose a normalized implementation penalty is bounded by

```text
sum_i |k_i-Nx_i|/N.
```

For `s` rows this penalty is less than `s/N`.  Hence a fractional ledger with
strict slack `sigma` remains feasible for every

```text
N>s/sigma.
```

#### Proof

Sum the coordinatewise bounds from `PP3cnp` and divide by `N`.  The displayed
threshold makes the total error strictly smaller than the available slack. ∎

## 3. Stored six-row fixture

### Theorem PP3cnr -- PROVED / PERIOD-120 INTEGERIZATION CERTIFICATE

Use the target weights

```text
(28,27,20,15,12,18)/120.
```

Largest-remainder rounding has the exact period-increment law

```text
k(N+120)=k(N)+(28,27,20,15,12,18).
```

For six rows and ledger slack `sigma=1/60`, every `N>=361` is certified because

```text
6/N<1/60.
```

#### Proof

Adding 120 increases every unrounded target by its integer numerator and leaves
all fractional parts unchanged, so the same tie-broken largest-remainder choices
are made.  The threshold is `N>360`. ∎

## 4. Stored exact audit

The audit `scripts/check_all_length_balanced_rounding.py` checks every length
through 2000, verifies the period-increment identity, records maximum total
rounding error `9/4` in that range, and checks the uniform strict-slack bound from
361 onward.

## 5. Prime-patching consequence

Once a fractional six-frontier solution with fixed positive slack is genuinely
realized, denominator divisibility is not an all-`n` obstruction.  Balanced
rounding converts it to integer block counts for every sufficiently large side,
with an explicit threshold.  The remaining task is still the construction of
the fractional geometric interface itself.
