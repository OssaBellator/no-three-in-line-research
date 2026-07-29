# Descent linear programs on multicritical shell faces

`docs/457` describes the subdifferential of the shell rate when several cycles
are tied.  The next constructive question is whether an allowed local change can
move the rate downward.  At first order this is a finite linear program.

Let `A` be the active critical-cycle set.  For each `C in A`, let `a_C` be its
normalized edge-incidence vector.  Let `D` be a rational polytope of allowed
logarithmic edge directions.

## 1. Exact descent problem

### Theorem PP3cdx -- PROVED / MULTICRITICAL DESCENT LP

The best first-order logarithmic rate change is

```text
tau_* = min_(d in D) max_(C in A) a_C dot d.
```

It is the optimum of the rational linear program

```text
minimize tau
subject to a_C dot d <= tau       for C in A,
           d in D.
```

Whenever `D` is nonempty and bounded, a rational optimum exists.

#### Proof

`docs/457` identifies the directional derivative of `log(mu)` with the displayed
maximum.  Introducing its epigraph variable `tau` gives the linear program.
A bounded rational polyhedron has a rational optimal extreme point. ∎

## 2. Dual obstruction

### Theorem PP3cdy -- PROVED / CONVEX-CYCLE NO-DESCENT CERTIFICATE

The LP dual supplies nonnegative weights on active cycles summing to one,
together with multipliers for the constraints defining `D`.  If the certified
optimum satisfies `tau_*>=0`, these weights prove that no allowed direction has
negative first-order rate change.

#### Proof

The maximum of the active linear forms is the support function of their convex
hull.  Linear-programming duality separates that convex hull from the set of
strictly descending allowed directions. ∎

Thus failure to find a descent direction is witnessed by a concrete convex
combination of critical cycles rather than by a numerical optimizer status.

## 3. From first order to an actual perturbation

### Theorem PP3cdz -- PROVED / STRICT DESCENT PERSISTENCE

If `tau_*<0`, then the optimizing direction strictly lowers the exact shell rate
for all sufficiently small positive perturbation sizes.

#### Proof

Every active cycle has logarithmic slope at most `tau_*<0`.  Every inactive
cycle begins below the critical rate by a positive gap.  There are finitely many
simple cycles, so for sufficiently small perturbation the inactive cycles
remain below the decreasing active maximum. ∎

## 4. Exact audit

Run

```bash
python scripts/check_multicritical_descent_lp.py
```

The stored face has two active incidences

```text
(1/2,1/2,0),
(0,1/2,1/2)
```

and allowed directions `d_1+d_2+d_3=0`, `-1<=d_i<=1`.  Among 217 exact grid
directions, the unique optimum is

```text
(1/2,-1,1/2)
```

with both active slopes equal to `-1/4`.  Equal dual cycle weights `(1/2,1/2)`
prove no direction can do better.
