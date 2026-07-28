# Capacity layer-cake criterion for terminal descent

`docs/361` gives the fibre-capacity-weighted terminal policy, whose reverse load
at a predecessor-shell target cycle `eta` is

```text
kappa_F(eta) = sum_x m(x,eta)/Z(x).
```

`docs/363` bounds this sum by cutting once at `T_m=2^(m+5)`.  This chapter gives
the exact distribution-function identity behind that cut and a reusable
sufficient condition for asymptotic contraction.

No asymptotic estimate for the prime-patching terminal gate is claimed here.

## 1. Exact layer-cake identity

Fix a target cycle `eta`.  Regard every incoming labelled terminal move as one
item whose capacity normalizer is the positive integer `Z(x)` of its source.
Multiplicity `m(x,eta)` simply repeats that item.  Let

```text
C_eta(t) = number of incoming labelled items with Z(x) <= t.
```

Let the distinct incoming normalizers be

```text
z_1 < z_2 < ... < z_r.
```

### Proposition PP3bsn -- PROVED / EXACT CAPACITY LAYER CAKE

The capacity-weighted reverse load has the exact representations

```text
kappa_F(eta)
 = C_eta(z_r)/z_r
   + sum_(j=1)^(r-1) C_eta(z_j) (1/z_j - 1/z_(j+1))
```

and

```text
kappa_F(eta)
 = C_eta(z_r)/z_r
   + integral_(z_1)^(z_r) C_eta(t) dt/t^2,
```

where `C_eta(t)` is the right-continuous step function determined by the
incoming normalizers.

#### Proof

An item with normalizer `z_k` satisfies the telescoping identity

```text
1/z_k = 1/z_r + sum_(j=k)^(r-1) (1/z_j - 1/z_(j+1)).
```

Summing this identity over all incoming items gives the discrete formula,
because the number of items whose index is at most `j` is exactly
`C_eta(z_j)`.  On every interval `[z_j,z_(j+1))`, the step function is constant
with value `C_eta(z_j)`, so integrating `C_eta(t)/t^2` gives the same discrete
sum. ∎

Thus terminal charge is controlled completely by the cumulative population of
small-normalizer incoming labels.  The one-threshold estimate in `docs/363` is
a coarse truncation of this exact identity.

## 2. A power-law counting criterion

### Theorem PP3bso -- PROVED / CUMULATIVE CAPACITY CRITERION

Assume that for some `0 < delta <= 1`, some `A > 0`, and every target `eta`,

```text
C_eta(t) <= A t^(1-delta)
```

for all `t` between the minimum and maximum incoming normalizers.  If every
incoming normalizer is at least `z_min`, then

```text
kappa_F(eta) <= (A/delta) z_min^(-delta).
```

#### Proof

Write `M` for the largest incoming normalizer.  Proposition PP3bsn gives

```text
kappa_F(eta)
 <= A M^(-delta)
    + A integral_(z_min)^M t^(-1-delta) dt
 = A M^(-delta)
   + (A/delta)(z_min^(-delta)-M^(-delta)).
```

Because `delta<=1`, the coefficient of `M^(-delta)` after collecting terms is
nonpositive.  Dropping that term gives the stated bound. ∎

Consequently, a uniform terminal contraction theorem can be obtained without
estimating each harmonic contribution separately.  It is enough to prove a
sublinear cumulative bound for low-normalizer incoming labels together with a
growing minimum normalizer.  More generally, piecewise bounds on `C_eta(t)` can
be inserted directly into the layer-cake integral; the two-scale envelope from
`docs/363` is the first such piecewise estimate.

The next theorem identifier after this chapter is `PP3bsp`.
