# Multipotential marker-controller synthesis

`docs/453` certifies a cyclic marker automaton after its transition matrix has
already been chosen.  A local repair construction usually has several admissible
moves at each marker state.  This chapter gives a finite synthesis problem for
choosing among them.

Let `V` be a finite state set.  At state `u`, action `a` has a nonnegative
transition-load row `R_(u,a)`.  A stationary controller chooses probabilities
`pi_(u,a)`, producing the closed-loop row

```text
Q_(u,.)=sum_a pi_(u,a) R_(u,a).
```

Fix positive test potentials `w^1,...,w^m` and requested rates
`q_1,...,q_m<1`.

## 1. Statewise synthesis

### Theorem PP3cdl -- PROVED / MULTIPOTENTIAL CONTROLLER LP

A stationary controller satisfying

```text
Q w^j <= q_j w^j                 for every j
```

exists if and only if, independently for every state `u`, the simplex problem

```text
pi_(u,a)>=0,
sum_a pi_(u,a)=1,
sum_a pi_(u,a) R_(u,a) w^j <= q_j w^j_u   for every j
```

is feasible.

For rational action rows, potentials, and rates, feasibility has a rational
controller certificate.

#### Proof

The global inequalities split row by row.  The row at `u` depends only on the
probabilities selected at `u`, so the global controller exists exactly when all
local systems are feasible.  Each local system is a rational polytope; every
nonempty rational polytope contains a rational point. ∎

Every certified potential may then be used in `PP3ccu` to bound the closed-loop
marker-walk tail.  Several potentials can protect different terminal classes or
different geometric observables simultaneously.

## 2. Sparse controllers

### Theorem PP3cdm -- PROVED / SMALL ACTION SUPPORT

If the local controller polytope at a state is nonempty, it has an extreme point
using at most `m+1` actions.

#### Proof

A basic feasible solution has the simplex equality together with at most `m`
independent active potential inequalities.  Hence at most `m+1` probability
variables are basic and positive. ∎

Thus a controller protecting a fixed number of observables does not need a
large randomized action menu, even when many candidate local moves were
enumerated.

## 3. Localized failure

### Theorem PP3cdn -- PROVED / STATEWISE SEPARATING WITNESS

If the local controller problem fails at state `u`, there are nonnegative
multipliers `eta_1,...,eta_m`, not all zero, such that every action `a` obeys

```text
sum_j eta_j [R_(u,a) w^j - q_j w^j_u] > 0.
```

For rational input, the multipliers may be chosen rational.

#### Proof

The convex hull of the action gap vectors is compact.  Local feasibility says
that this hull intersects the nonpositive orthant.  If it does not, strict
separation gives a normal in the dual cone, which is the nonnegative orthant.
Rational polyhedral separation gives a rational normal. ∎

The obstruction is therefore one marker state and one weighted combination of
promised observables.  It does not require a global search through all
controllers.

## 4. Exact audit

Run

```bash
python scripts/check_marker_controller_synthesis.py
```

The stored three-state fixture has two competing actions at its root.  Neither
action protects both potentials, while the unique feasible mixture is `1/2`
of each.  The resulting resolvent load is

```text
(1,5/8,5/8).
```

At the stricter rate `2/5`, the rational separator `(1,1)` has margin `1/5`
against both actions.

This synthesis theorem still requires candidate marker moves supplied by the
prime-patching geometry; it does not itself construct those moves.
