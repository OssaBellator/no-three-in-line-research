# Inverse design on threshold value fans

`docs/479` locates points and transports values across the rational threshold
value fan.  The next task is inverse: choose source masses or target capacities
so that the optimal threshold load stays below a requested level while a linear
geometric objective is optimized.

Let

```text
V(theta)=max_(z in Z) (a_z dot theta+b_z)
```

be the finite rational value atlas on a rational design polytope `P`.

## 1. Rational inverse-feasible region

### Theorem PP3cgl -- PROVED / VALUE-SUBLEVEL POLYHEDRON

For rational load cap `tau`, the inverse-feasible region is

```text
P_tau={theta in P: a_z dot theta+b_z <= tau for every z in Z}.
```

It is a rational polyhedron.  Optimizing any rational linear design objective on
`P_tau` is therefore one finite rational LP.

#### Proof

The inequality `V(theta)<=tau` is equivalent to every affine piece being at most
`tau`.  Intersecting those finitely many rational halfspaces with `P` gives the
displayed polyhedron. ∎

## 2. Value-cut generation

### Theorem PP3cgm -- PROVED / FINITE INVERSE-DESIGN ORACLE

Start with any subset of value pieces, solve the restricted inverse-design LP,
and query the exact value point-location oracle at its optimizer.  If an omitted
piece exceeds `tau`, add that piece as a cut and repeat.  The process terminates
finitely.  When no piece is violated, the current design is globally optimal for
the full value cap.

#### Proof

Every failed iteration adds a previously absent affine piece, and `Z` is finite.
At termination the restricted optimizer satisfies all full constraints.  The
restricted feasible region contains the full feasible region, so its objective
is an upper bound for a maximization problem.  Full feasibility of the optimizer
makes the same value attainable, proving equality and global optimality. ∎

## 3. Exact dual and ray certificates

### Theorem PP3cgn -- PROVED / INVERSE-DESIGN PRICE CERTIFICATE

A nonnegative rational combination of active value cuts and design-polytope
facets whose normal equals the design objective is an exact global optimality
certificate.  Along a rational ray `theta_0+t d`, the feasible values of `t` are
the intersection of finitely many rational intervals obtained from the affine
pieces; hence the first load-cap boundary is an exact rational ratio.

#### Proof

Multiplying valid inequalities by nonnegative prices and summing gives the
objective bound.  Equality at the proposed design proves optimality.  Along a
ray, every affine inequality is linear in `t`, so each gives one rational
half-line or interval.  Their finite intersection has rational endpoints. ∎

## 4. Stored exact fixture

The audit `scripts/check_threshold_inverse_design.py` uses four affine pieces on
the unit square and cap `tau=1/2`.  Starting with only the cut `x<=1/2`, the
oracle adds the tilted piece and then the `y` piece.  The exact optimum is

```text
(x,y)=(9/20,1/2)
```

for objective `100x+101y`, with value `191/2`.  Dual prices `50` on
`2x+y<=7/5` and `51` on `y<=1/2` reproduce the objective normal and objective
bound exactly.  The feasible endpoint on the diagonal ray is `t=7/15`.

## 5. Prime-patching consequence

Fractional direct-clean layers can now be designed to a prescribed contraction
budget rather than merely evaluated after construction.  A failed design returns
the specific threshold basis piece that violates the cap; a successful design
returns exact active prices showing which geometric capacities control it.
