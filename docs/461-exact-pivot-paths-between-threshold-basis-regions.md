# Exact pivot paths between threshold-basis regions

`docs/455` associates a rational optimality cone to one threshold-kernel basis.
To use those cones algorithmically, one must move from one cone to the next as
source masses or target capacities change.  The needed mechanism is an exact
parametric simplex path.

Consider the standard-form linear program

```text
minimize c^T x
subject to A x=b,
           x>=0,
```

with fixed rational `A,c` and varying rational right-hand side `b`.

## 1. One basis region

### Theorem PP3cdr -- PROVED / AFFINE BASIS CELL

Let `B` be a nonsingular column basis whose reduced costs are nonnegative.  It
is optimal exactly on the rational polyhedron

```text
B^(-1)b>=0.
```

On this region the primal solution and optimum are

```text
x_B=B^(-1)b,
x_N=0,
value=c_B^T B^(-1)b.
```

In particular, both are affine in `b`.

#### Proof

The displayed inequality is precisely primal feasibility of the basic
solution.  Reduced costs depend only on `A,c,B`, so dual feasibility is fixed.
Primal and dual feasibility imply optimality, and the formulas follow by
substitution. ∎

## 2. First exact breakpoint

### Theorem PP3cds -- PROVED / RATIONAL FACET HITTING TIME

Along a rational path

```text
b(t)=b_0+t d,
```

suppose `B` is feasible at `t=0`.  Write

```text
x_B(t)=x_0+t h,
h=B^(-1)d.
```

The first time at which this basis can lose feasibility is

```text
t_* = min_(i:h_i<0) -x_(0,i)/h_i.
```

If the set is empty, the basis remains feasible for all `t>=0`.  Every finite
`t_*` is rational.

#### Proof

Each basic coordinate is affine.  A coordinate with nonnegative slope never
creates the first violation; a negative-slope coordinate reaches zero at the
displayed time.  Taking the earliest such time gives the result. ∎

## 3. Adjacent optimal regions

### Theorem PP3cdt -- PROVED / EXACT ONE-PIVOT CONTINUATION

Assume the path remains feasible and bounded past `t_*`, exactly one basic
coordinate vanishes there, and the adjacent optimal solution is nondegenerate.
Then the next optimal basis differs from `B` by one simplex pivot.  The leaving
coordinate is the one attaining `t_*`; an entering column is selected by the
usual exact dual-feasibility ratio test.  Repeating this procedure traverses the
path through finitely many rational affine pieces.

#### Proof

At a nondegenerate shared facet, two full-dimensional basic cells share all but
one active column.  Thus their bases differ by one exchange.  The simplex ratio
test is exactly the condition that the exchanged basis remain primal and dual
feasible.  There are finitely many bases. ∎

For threshold kernels, each pivot identifies the threshold variable entering or
leaving the sparse certificate as the parameter path crosses a basis wall.

## 4. Exact audit

Run

```bash
python scripts/check_threshold_basis_path_traversal.py
```

The stored program is

```text
min x_1+x_2
x_1+x_3=b_1,
x_2+x_3=b_2,
x>=0
```

along `b(t)=(1+t,2-t)`.  The exact breakpoint is `t=1/2`; the basis pivots from
`{x_2,x_3}` to `{x_1,x_3}`.  The audit checks 101 rational path points and both
nonbasic reduced costs, each equal to `2`.
