# Quantized realization of threshold designs

`docs/491` and `docs/497` return exact rational nearest designs and projection
regions.  A geometric repair schedule may require a prescribed denominator or
period.  This chapter gives denominator-controlled implementations and explicit
loss bounds for downward-closed threshold systems.

Let

```text
P={x in R_+^n : A x <= b},
```

where `A` is entrywise nonnegative.  For integer `M>=1`, write

```text
q_M(x)_i = floor(M x_i)/M.
```

## 1. Feasible denominator rounding

### Theorem PP3cin -- PROVED / MONOTONE GRID REALIZATION

For every `x in P`, the denominator-`M` point `q_M(x)` also belongs to `P`.

#### Proof

Coordinatewise, `0<=q_M(x)<=x`.  Since `A>=0`,
`A q_M(x)<=A x<=b`. ∎

## 2. Exact objective and load loss

### Theorem PP3cio -- PROVED / QUANTIZATION LOSS BOUND

For every nonnegative rational price vector `c`,

```text
0 <= c dot x-c dot q_M(x) < ||c||_1/M.
```

The same estimate applies to any nonnegative target-load row.  If a strict load
margin exceeds the corresponding row bound, quantization preserves that margin.

#### Proof

Every coordinate loss lies in `[0,1/M)`.  Multiply by `c_i>=0` and sum. ∎

## 3. Exact grid optimization

### Theorem PP3cip -- PROVED / FINITE DENOMINATOR ORACLE

The best denominator-`M` design is the finite integer program obtained by
writing `x=z/M` with `z in Z_+^n`.  A candidate is certified by its integer
feasibility and an exact finite comparison or branch-and-bound lower bound.  If
`M` is divisible by the denominator of a rational optimum `x*`, then the grid
optimum equals the continuous optimum.

#### Proof

Substitution gives finitely many integer points inside every bounded design
box.  Exact enumeration or rational branch-and-bound is complete.  When
`M x*` is integral, `x*` itself is grid feasible, so no grid point can improve
on the continuous optimum. ∎

## 4. Stored exact fixture

The audit `scripts/check_quantized_threshold_designs.py` uses continuous optimum

```text
x*=(4/5,3/10)
```

with objective `2x+y=19/10`.  At denominator seven, monotone rounding gives
`(5/7,2/7)` with exact loss `13/70`; exhaustive grid search proves it optimal.
Denominator ten realizes the continuous optimum exactly.  All denominators
through one hundred are checked.

## 5. Prime-patching consequence

A rational direct-clean design can now be converted into a finite-period
geometric schedule with a denominator chosen in advance.  Feasibility is
preserved automatically for monotone load systems, and the contraction loss is
explicitly `O(1/M)`.
