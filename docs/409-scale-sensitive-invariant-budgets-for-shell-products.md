# Scale-sensitive invariant budgets for shell products

`docs/403` bounds a shell product from its exceedance counts and shows that a
fixed invariant drop controls the number of boundaries above one threshold.
This chapter allows the forced invariant drop to depend on the expansion
scale.  Integrating those scale-dependent drops gives a horizon-free shell
product criterion.

The statements do not construct such an invariant for clean-macro shells.

## 1. Continuous scale-dependent drops

Let

```text
p_j=max(kappa_j,1)
```

be the positive shell factors, assume `p_j<=B`, and let a nonnegative
trajectory invariant decrease by amounts

```text
Delta_j=J_j-J_(j+1)>=0.
```

Suppose a positive function `eta(u)` on `[1,B)` has the property

```text
p_j>u  implies  Delta_j>=eta(u).
```

### Theorem PP3bxp -- PROVED / INVARIANT-TAIL SHELL ENVELOPE

For every `1<=u<B`, the exceedance count satisfies

```text
q(u)<=J_0/eta(u).
```

Consequently

```text
product_j p_j
 <=exp(
   J_0 integral_(1)^B du/[u eta(u)]
 ).
```

Including the exact contractive credit

```text
Cprod=product_j min(kappa_j,1)
```

and terminal factor `tau`, the complete trajectory contracts whenever

```text
tau Cprod
 exp(
   J_0 integral_(1)^B du/[u eta(u)]
 )
 <1.
```

#### Proof

For a fixed threshold `u`, every one of the `q(u)` exceeding boundaries has
drop at least `eta(u)`.  Therefore

```text
q(u)eta(u)
 <=sum_(j:p_j>u)Delta_j
 <=sum_j Delta_j
 <=J_0.
```

Insert this pointwise tail bound into the exact layer-cake identity
`PP3bwv`:

```text
log(product_j p_j)
 =integral_(1)^B q(u)du/u
 <=J_0 integral_(1)^B du/[u eta(u)].
```

Exponentiate and multiply by `tau Cprod`. ∎

A single invariant can therefore pay more for rarer, more expansive gates.

## 2. Exact rational threshold form

Choose rational thresholds

```text
1=B_0<B_1<...<B_s=B
```

and positive drop guarantees `eta_i` such that

```text
p_j>B_i  implies  Delta_j>=eta_i.
```

### Theorem PP3bxq -- PROVED / DISCRETE INVARIANT-PROFILE PRODUCT

Put

```text
Q_i=floor(J_0/eta_i).
```

Then

```text
product_j p_j
 <=product_(i=0)^(s-1)
   (B_(i+1)/B_i)^(Q_i).
```

The exact compensated trajectory contracts whenever

```text
tau Cprod
 product_(i=0)^(s-1)
 (B_(i+1)/B_i)^(Q_i)
 <1.
```

#### Proof

The drop argument from `PP3bxp` gives the integer count bound

```text
q_i=#{j:p_j>B_i}<=floor(J_0/eta_i)=Q_i.
```

Apply the discrete multiscale product theorem `PP3bww` and replace each
exceedance count by its upper bound. ∎

This form uses only rational arithmetic and is suited to exact finite
certificates.

## 3. Power-law invariant profiles

### Corollary PP3bxr -- PROVED / HORIZON-FREE POWER-DROP BUDGET

Assume, for some `a>0` and `beta>0`,

```text
p_j>u  implies  Delta_j>=a u^beta
```

for every `1<=u<p_j`.  Then

```text
product_j p_j
 <=exp(
   J_0(1-B^(-beta))/(a beta)
 )
 <=exp(J_0/(a beta)).
```

Hence the full trajectory contracts under the horizon-free condition

```text
tau Cprod exp(J_0/(a beta))<1.
```

#### Proof

Use `eta(u)=a u^beta` in `PP3bxp` and integrate:

```text
integral_(1)^B du/[a u^(beta+1)]
 =(1-B^(-beta))/(a beta).
```

The second bound drops the negative term. ∎

This criterion remains independent of the number of shell boundaries.  A
power-growing cost for large expansion makes the complete positive shell
product summable.

## 4. Revised shell frontier

The remaining geometric target is no longer a uniform shell ceiling.  It is
enough to find a monotone invariant whose forced drop grows with the local
expansion factor.  The exact tail, rational threshold, and power-law forms
then translate that invariant directly into a product bound while retaining
all contractive-shell credit.

## 5. Finite diagnostic

The script

```bash
python scripts/check_scale_sensitive_shell_invariants.py
```

exhausts rational shell factors and rational invariant drops on a finite grid,
checks every implied threshold count and the discrete envelope exactly, and
verifies the continuous power-profile envelope at 80-digit precision.

The next theorem identifier after this chapter is `PP3bxs`.
