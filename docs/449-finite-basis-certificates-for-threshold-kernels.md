# Finite basis certificates for randomized threshold kernels

`docs/443` gives the exact primal--dual gap identity for randomized multiplicity
thresholds. This chapter turns that identity into a finite rational certificate
format suitable for exact enumeration.

## 1. Threshold linear program

For source `x` and threshold option `h`, let `p_(x,h,y)` be the resulting target
probability. The primal variables are `alpha_(x,h)` and `lambda`:

```text
sum_h alpha_(x,h)=1,
L_y=sum_(x,h) alpha_(x,h) p_(x,h,y)<=lambda,
alpha_(x,h)>=0.
```

### Theorem PP3cch -- PROVED / SPARSE BASIC OPTIMUM

There exists an optimal basic solution with at most

```text
|X|+|Y|-1
```

positive threshold variables.

#### Proof

At a basic optimum let `T` be the active target columns. The row equations and
active column equations provide at most `|X|+|T|` independent constraints on the
positive threshold variables together with `lambda`. Hence at most
`|X|+|T|-1<=|X|+|Y|-1` threshold variables are positive. ∎

## 2. Exact basis reconstruction

Choose a threshold support `B` and an active target set `T` satisfying

```text
|B|+1=|X|+|T|.
```

Solve the row equations and `L_y=lambda` for `y in T` using only the variables in
`B`.

### Theorem PP3cci -- PROVED / PRIMAL--DUAL BASIS CERTIFICATE

Assume the basis matrix is nonsingular and the resulting solution has positive
support weights, satisfies every inactive column inequality, and admits target
prices `z` such that:

```text
z_y>=0, sum_y z_y=1, supp(z) subseteq T,
```

and every used threshold minimizes its source's priced cost. Then the basis
solution and `z` are exactly optimal.

#### Proof

Primal feasibility is part of the assumptions. The target prices are dual
feasible. Active priced columns are saturated and all used thresholds have zero
reduced cost, so every term in the complementary-slackness gap identity vanishes.
Strong duality follows directly. ∎

## 3. Finite exact search

### Theorem PP3ccj -- PROVED / BASIS-ENUMERATION ORACLE

The optimum of every finite rational threshold instance can be recovered by
enumerating supports of size at most `|X|+|Y|-1`, active target sets, and the
corresponding nonsingular rational basis systems. Each accepted candidate has a
finite exact primal--dual certificate.

#### Proof

`PP3cch` guarantees that one enumerated support contains an optimal basic
solution. Gaussian elimination over the rationals reconstructs it, and
`PP3cci` verifies it exactly. ∎

## Frontier consequence

The mixed-threshold frontier no longer depends on a floating-point LP solve.
Every optimum can be stored as a small rational basis, an active target list,
and a target-price vector; every rejected candidate returns a specific primal or
reduced-cost defect.
