# Degenerate basis fans for threshold kernels

`docs/461` follows a parametric threshold optimum through a nondegenerate wall by
one exact pivot.  At a degenerate wall several basic variables may vanish and
several bases may represent the same optimal kernel.  This chapter gives a
finite exact continuation procedure without assuming genericity.

Consider a rational standard-form program

```text
min c^T x,
A x=b(t)=b_*+(t-t_*)d,
x>=0,
```

with fixed `A,c`.  Reduced costs of a basis do not depend on `b(t)`.

## 1. The wall basis fan

Call a basis a *wall basis* if it is primal feasible at `b_*` and dual feasible
for `c`.

### Theorem PP3cej -- PROVED / FINITE DEGENERATE WALL FAN

The wall bases are exactly the bases representing optimal points at `t_*`.
Their single-exchange graph is finite, and the bases representing any fixed
optimal face form a connected subgraph.

#### Proof

Primal and dual feasibility is the exact basis optimality criterion.  Finiteness
is immediate from the finite column set.  Bases of a fixed polyhedral face are
bases of the corresponding restricted column matroid; its basis-exchange graph
is connected. ∎

Zero-length pivots therefore suffice to move between all basis descriptions of
the same wall face.

## 2. Exact tangent test

For a wall basis `B`, write

```text
x_B(t)=x_B^*+(t-t_*)v_B,
v_B=A_B^(-1)d.
```

### Theorem PP3cek -- PROVED / TANGENT-FEASIBLE CONTINUATION

The basis `B` remains primal feasible for all sufficiently small `t>t_*` if and
only if

```text
x_(B,i)^*=0  implies  (v_B)_i>=0.
```

Because its reduced costs remain nonnegative, every tangent-feasible wall basis
is also optimal immediately after the wall.

#### Proof

Positive basic coordinates stay positive for sufficiently small motion.  A zero
basic coordinate remains nonnegative exactly when its directional derivative is
nonnegative.  Dual feasibility is independent of the right-hand side. ∎

## 3. Degeneracy-safe pivot oracle

### Theorem PP3cel -- PROVED / FINITE WALL CONTINUATION ORACLE

Starting from an incoming optimal basis, search the connected wall-basis graph
in lexicographic pivot order and apply the tangent test of `PP3cek`.

- If a tangent-feasible basis is found, it gives an exact rational continuation.
- If none exists, the parameter direction leaves the current feasible optimal
  complex; finite polyhedral separation returns a rational tangent obstruction.

The lexicographic order prevents cycling and makes the certificate canonical.

## 4. Exact audit

Run

```bash
python scripts/check_degenerate_threshold_basis_fan.py
```

The stored four-column program has wall time `t=1/2`, three optimal wall bases,
two forward-feasible continuations, and Bland continuation basis `(2,3)`.  The
audit verifies all `101` rational path points.
