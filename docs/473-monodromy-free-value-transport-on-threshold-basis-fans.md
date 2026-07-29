# Monodromy-free value transport on threshold basis fans

`docs/467` gives canonical continuation through one degenerate threshold wall.
This chapter assembles all rational basis cells into a global value atlas and
shows that exact value transport is path independent even when basis labels
change around a degenerate loop.

For a parametric threshold LP, let `theta` denote the rational source-mass and
target-capacity parameters.  After enumerating the finitely many dual vertices,
the optimum has the form

```text
V(theta)=max_(z in Z) (a_z dot theta+b_z)
```

on its feasible parameter domain.

## 1. Rational basis atlas

### Theorem PP3cfb -- PROVED / FINITE POLYHEDRAL VALUE FAN

For every dual vertex `z`, the activity region

```text
C_z={theta: a_z dot theta+b_z >= a_w dot theta+b_w for all w}
```

is a rational polyhedron.  The nonempty regions cover the parameter domain, and
on each region `V` is affine with gradient `a_z` wherever `z` is uniquely active.

#### Proof

Each activity condition is one rational linear inequality.  Taking all dual
vertices gives a finite rational cover, and the envelope equals the LP optimum
by strong duality. ∎

## 2. Exact path transport

### Theorem PP3cfc -- PROVED / ZERO VALUE MONODROMY

Let `gamma` be a rational polygonal path.  Subdivide it at all basis-wall
crossings.  On every open subsegment choose its unique active gradient `a_z`.
Then

```text
sum_segments a_z dot Delta theta
  = V(gamma(1))-V(gamma(0)).
```

Consequently, the exact integral around every closed polygonal loop is zero,
even if lexicographic basis continuation returns with a different degenerate
basis label.

#### Proof

On one activity interval the affine formula gives exactly
`Delta V=a_z dot Delta theta`.  Summing telescopes.  A closed path has identical
start and end values, so the sum is zero. ∎

## 3. Atlas consistency certificates

### Theorem PP3cfd -- PROVED / WALL-CYCLE AUDIT

A proposed finite basis atlas is globally consistent if every listed cell
satisfies its dominance inequalities and every shared wall gives equal affine
values.  Path transport through the adjacency graph then has zero sum on every
graph cycle.  Failure returns a rational point violating a cell inequality, a
wall equality, or a cycle sum.

#### Proof

Cell and wall conditions make the affine pieces a well-defined continuous
polyhedral function.  Telescoping proves every cycle sum is zero.  Conversely,
any failed finite condition is already the stated rational witness. ∎

## 4. Stored exact fixture

The audit `scripts/check_threshold_value_monodromy.py` uses

```text
V(x,y)=max(x,-x,y,-y).
```

Its four rational basis cells are traversed by an eight-segment closed polygon.
Exact wall subdivision visits all four cells and gives total integral zero.  Two
different routes between the same endpoints also give the same value change.

## 5. Prime-patching consequence

Threshold kernels can now be transported across a global parameter atlas rather
than restarted after every wall.  Degenerate basis monodromy is harmless at the
level that matters for contraction: the exact optimal load and its accumulated
finite differences are single-valued.
