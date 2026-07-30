# Normal fans for interaction lattice slices

`docs/536` replaces repeated Minkowski sums by exact lattice slices of a normal
affine semigroup.  Downstream geometry usually assigns rational prices to the
secondary coordinates.  This chapter gives a finite parametric description of
the optimizer for every such price vector.

Let `F_N` be the secondary-vector slice at total length `N`, and let
`lambda` be a rational objective vector.

## 1. Parametric support fan

### Theorem PP3cna -- PROVED / INTERACTION NORMAL-FAN CERTIFICATE

If `F_N` is the lattice-point slice of a fixed rational polyhedral cone, then
weight space is partitioned into finitely many rational polyhedral cones on each
of which the minimizing face of

```text
min_(v in F_N) lambda dot v
```

is constant, apart from residue-dependent empty faces.  The partition is the
normal fan of the slice polytope, refined by the semigroup lattice.

#### Proof

A linear functional on a polytope is minimized on one exposed face.  The set of
functionals exposing a fixed face is its rational normal cone.  Intersecting the
finite face fan with the lattice-residue conditions gives the stated finite
partition. ∎

## 2. Quasipolynomial support values

### Theorem PP3cnb -- PROVED / PARAMETRIC INTERACTION QUASIPOLYNOMIAL

For a normal affine semigroup and fixed rational weight cone, the optimum value,
the number of optimum lattice points, and every fixed-coordinate optimum are
eventually quasipolynomial functions of `N`.  A rational multivariate generating
function provides a finite exact certificate for these formulas.

#### Proof

Normality identifies the slice with all lattice points in a rational polytope.
Weighted lattice-point enumeration over rational dilates is governed by Ehrhart
quasipolynomials.  Restricting to an exposed face gives the optimizer count and
coordinates. ∎

## 3. Three-cone exact fixture

### Theorem PP3cnc -- PROVED / TWO-GENERATOR SUPPORT FORMULA

For

```text
F_N={(N-2b,2b):0<=b<=floor(N/2)},
```

and weight `(alpha,beta)`, the normal fan has three cones:

```text
alpha<beta: unique optimum (N,0), value alpha N;
alpha=beta: every point is optimal, value alpha N;
alpha>beta: unique optimum
    (0,N) for even N,
    (1,N-1) for odd N,
```

with value `beta N` in the even case and `beta(N-1)+alpha` in the odd case.

#### Proof

At parameter `b`, the objective is

```text
alpha N+2b(beta-alpha).
```

It is increasing, constant, or decreasing according to the sign of
`beta-alpha`, giving the formulas. ∎

## 4. Stored exact audit

The audit `scripts/check_interaction_normal_fans.py` checks every length through
300 against 120 nonzero integer weight pairs in `[0,10]^2`, plus a rational
weight pair.  It verifies all optimizer sets, both parity formulas, the exact
frontier count `floor(N/2)+1`, and the multivariate generating function

```text
1/((1-u z)(1-v^2 z^2)).
```

## 5. Prime-patching consequence

The integration frontier can now answer an entire family of downstream resource
tradeoffs without rerunning a Pareto dynamic program.  One finite normal fan and
one residue table give the exact optimum schedule type and value for every side
length and every rational price vector.
