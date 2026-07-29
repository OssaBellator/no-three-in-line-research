# Nearest feasible designs on threshold value fans

`docs/485` asks whether a threshold parameter lies below a prescribed optimal
load cap.  When a nominal geometric design violates the cap, the next problem
is constructive: change it as little as possible while entering the feasible
sublevel polyhedron.

Let

```text
V(theta)=max_(z in Z) (a_z dot theta+b_z)
```

be the finite rational threshold value fan on a rational design domain `P`.
Fix a cap `tau`, nominal design `theta_0`, and positive rational weights `w_i`.

## 1. Exact nearest-design linear program

### Theorem PP3chd -- PROVED / WEIGHTED L1 PROJECTION

The nearest capped design for weighted `l_1` distance is the rational LP

```text
minimize   sum_i w_i u_i
subject to theta in P,
           a_z dot theta+b_z <= tau       for every z,
           -u_i <= theta_i-theta_(0,i) <= u_i,
           u_i>=0.
```

Whenever the capped design set is nonempty, the LP has a rational optimum.

#### Proof

The value cap is equivalent to all affine-piece inequalities.  The two
inequalities defining `u_i` are equivalent at optimum to
`u_i=|theta_i-theta_(0,i)|`.  Rational polyhedra have rational basic optima. ∎

## 2. Exact optimality prices

### Theorem PP3che -- PROVED / PROJECTION KKT CERTIFICATE

A proposed design is optimal when primal feasibility, nonnegative rational
prices on active value/domain constraints, an admissible weighted-`l_1`
subgradient, stationarity, and complementary slackness all hold.

These data give a finite lower bound matching the proposed distance.  Failure
localizes to one violated cap piece, domain inequality, subgradient interval,
stationarity equation, or slackness product.

#### Proof

This is LP strong duality written in subgradient form after eliminating the
absolute-value auxiliaries.  The subgradient inequality plus the priced active
constraints gives the matching global lower bound. ∎

## 3. Parametric caps and rays

### Theorem PP3chf -- PROVED / PIECEWISE-AFFINE DESIGN PATH

As the rational cap `tau` varies on a compact interval, the nearest-design
optimum and value are piecewise rational affine.  Breakpoints occur only when
the active LP basis changes.

For any rational ray `theta=t v+theta_base`, the largest feasible `t` is the
minimum of finitely many rational affine-piece crossing values.

#### Proof

A parametric rational LP has finitely many bases.  On the region where one
basis remains feasible and optimal, its solution and objective are affine in
the right-hand side.  The ray statement follows by substituting the ray into
every value-piece and domain inequality. ∎

## 4. Stored exact fixture

The audit `scripts/check_nearest_threshold_design.py` uses

```text
V(x,y)=max(x,y,x+y-1/5),
theta_0=(4/5,3/4),
tau=9/10,
distance=2|x-4/5|+|y-3/4|.
```

The unique nearest design is `(4/5,3/10)` at distance `9/20`.  The active
piece is `x+y-1/5`; subgradient `(-1,-1)` and cap price one give the matching
lower bound.  The cap path is checked at 56 exact rational samples, and the
diagonal ray boundary is `11/20`.

## 5. Prime-patching consequence

A failed threshold cap now produces a minimum-change repair rather than only a
separating affine piece.  The dual prices identify which active target-load
constraints make geometric movement expensive.
