# Parametric regions for nearest threshold designs

`docs/491` repairs one nominal threshold design by weighted `l_1` projection onto
a load sublevel.  This chapter treats the nominal design itself as a parameter.
The nearest feasible repair map is a finite rational polyhedral atlas, so a
moving geometric design can be transported without resolving the projection LP
from scratch.

Let `P={theta:A theta<=b}` be a rational threshold-load sublevel and let
`theta^0` be nominal.  For positive rational weights `w`, minimize

```text
sum_i w_i |theta_i-theta_i^0|
```

over `theta in P`, using the usual positive and negative deviation variables.

## 1. Projection fan

### Theorem PP3chv -- PROVED / FINITE PARAMETRIC PROJECTION ATLAS

The optimal projection value is a convex piecewise-affine rational function of
`theta^0`.  After a lexicographic tie rule, the selected nearest feasible design
is piecewise affine on a finite rational polyhedral subdivision of nominal
parameter space.

#### Proof

The deviation formulation is a rational LP whose right-hand side depends
affinely on `theta^0`.  Every primal--dual basis gives affine basic variables and
an affine objective on the region where primal and dual feasibility hold.
There are finitely many bases.  Taking the optimal basis regions gives the value
atlas; lexicographic basis selection makes the projected point single-valued on
each cell. ∎

## 2. Exact path transport and prices

### Theorem PP3chw -- PROVED / PROJECTION BREAKPOINT WALK

Along any rational polygonal path of nominal designs, the selected projection,
its distance, and its active cap prices are affine between finitely many rational
breakpoints.  The next breakpoint is the first zero of a basic variable or
reduced cost.  The active dual prices give the exact one-sided derivative of the
minimum repair distance.

#### Proof

Restrict each affine basis formula to one path segment.  Feasibility becomes a
finite family of one-variable rational inequalities, whose first boundary is an
exact rational ratio.  Standard parametric LP sensitivity identifies the
objective derivative with the active dual solution. ∎

## 3. Localized atlas audit

### Theorem PP3chx -- PROVED / FINITE PROJECTION-REGION CERTIFICATE

A finite certificate consists of each projection cell, its affine projected
point and value, and matching primal--dual prices.  Exact checks of cell
inequalities and shared-wall agreement certify the complete atlas.  Failure
returns one nominal point, wall, primal coordinate, or reduced cost.

#### Proof

These are precisely the finite conditions under which every listed basis is
optimal on its cell and adjacent affine formulas agree where the lexicographic
selection changes. ∎

## 4. Stored exact fixture

The audit `scripts/check_parametric_threshold_projection_regions.py` projects
nominal `(t,t)` with weights `(1,2)` onto

```text
x>=0, y>=0, x+y<=1, y<=3/5.
```

The exact map is

```text
(t,t)                  for t<=1/2,
(1-t,t)                for 1/2<=t<=3/5,
(2/5,3/5)              for t>=3/5.
```

The repair distance has slopes `0,2,3`.  The script audits 101 rational samples,
all candidate vertices, and the exact breakpoints `1/2` and `3/5`.

## 5. Prime-patching consequence

Threshold repairs now vary predictably with the underlying geometric data.  A
whole family of nearby direct-clean designs can reuse one exact projection atlas,
including its active obstruction prices and wall-crossing points.
