# Multiparametric chambers for shell attenuation

`docs/493` follows one shell attenuation cap.  Several cycle targets, edge caps,
or costs may vary simultaneously.  This chapter identifies the finite chamber
complex on which the compact shell LP and its circulation dual are affine.

Consider a fixed rational shell LP

```text
minimize c dot x
subject to A x >= d(lambda), x>=0,
```

where `d(lambda)` is affine in a rational parameter vector `lambda`.

## 1. Shell value chambers

### Theorem PP3cib -- PROVED / FINITE PARAMETRIC SHELL FAN

On every parameter region where the shell LP is feasible and bounded, its value
is a convex piecewise-affine rational function.  It equals the maximum of the
finitely many affine objectives obtained from dual vertices.  A primal--dual
basis is affine on each chamber where it remains feasible.

#### Proof

The dual feasible polyhedron is fixed while its objective is affine in
`lambda`.  An optimum occurs at a dual vertex, so the value is the maximum of
finitely many affine forms.  For a fixed optimal basis, solving the primal and
dual equations gives affine coordinates; their sign inequalities define a
rational chamber. ∎

## 2. Chamber gradients and boundaries

### Theorem PP3cic -- PROVED / CIRCULATION SENSITIVITY REGIONS

Inside a chamber with unique dual circulation `y`, the value gradient is

```text
nabla_lambda V = (Jacobian d)^T y.
```

Shared chamber walls are exact affine equalities between two dual objectives.
At a wall, the directional derivative is the maximum of the active chamber
slopes.

#### Proof

Differentiate the active affine dual objective.  Equality of two affine vertex
objectives defines their common wall.  The directional derivative of a finite
maximum is the maximum directional slope among active pieces. ∎

## 3. Finite chamber walk

### Theorem PP3cid -- PROVED / MULTIPARAMETER SHELL AUDIT

A listed chamber complex is certified by exact dual-vertex dominance, primal
feasibility, and matching values on every shared wall.  A rational polygonal path
can then be walked by solving only the next active wall equation.  Failure
returns one parameter point, violated cycle inequality, dual capacity, or wall.

#### Proof

The finite checks establish the upper envelope and matching primal attainments
on every chamber.  Restricting wall equations to a path gives finitely many
rational crossing parameters. ∎

## 4. Stored exact fixture

The audit `scripts/check_multiparametric_shell_chambers.py` solves

```text
min x1+x2+x3
x1+x2>=a, x2+x3>=b, x1+x3>=c, x>=0.
```

Its exact value is

```text
max(a,b,c,(a+b+c)/2).
```

The central chamber has circulation gradient `(1/2,1/2,1/2)`; three dominant
chambers have coordinate gradients.  The script checks 1,331 rational parameter
triples.  Along `(a,b,c)=(1+2t,1,1)`, the chamber changes exactly at `t=1/2`.

## 5. Prime-patching consequence

A shell repair can now be transported through several changing cycle demands at
once.  The chamber gradient states exactly which packed cycles price each
geometric parameter, while a wall identifies the next critical-cycle regime.
