# Cutting-plane elimination of shell critical cycles

`docs/469` follows an exact line search until a new shell cycle becomes critical.
This chapter turns repeated face changes into a finite synthesis algorithm: add
violated critical cycles to a rational attenuation LP until every cycle meets
the requested decrease.

Let `E` be the attenuable shell edges.  For every simple directed cycle `C`, let
`m_(C,e)` be the multiplicity of edge `e` in `C`.  Applying nonnegative
log-attenuation `x_e` decreases the cycle log-product by
`sum_e m_(C,e)x_e`.  Edge `e` has rational cost `c_e`, and cycle `C` requires
rational decrease `Delta_C`.

## 1. Cycle attenuation LP

### Theorem PP3cfh -- PROVED / FRACTIONAL CRITICAL-CYCLE HITTING

The minimum-cost attenuation of a finite cycle set `A` is the rational LP

```text
minimize   sum_e c_e x_e
subject to sum_e m_(C,e)x_e >= Delta_C   for C in A,
           x_e>=0.
```

A cycle containing no allowed attenuable edge and having `Delta_C>0` is an
immediate impossibility witness.

#### Proof

Cycle log-products are additive in the edge log-attenuations, so the displayed
constraints are necessary and sufficient.  Rational data give a rational basic
optimum whenever feasible. ∎

## 2. Dual cycle packing

### Theorem PP3cfi -- PROVED / EDGE-CAPACITATED CYCLE DUAL

The dual LP is

```text
maximize   sum_C Delta_C y_C
subject to sum_C m_(C,e)y_C <= c_e   for every e,
           y_C>=0.
```

Equal primal and dual objectives certify exact optimality.  The dual prices are
a fractional packing of critical cycles into the available edge-cost capacity.

#### Proof

This is the standard rational LP dual.  Strong duality applies to every feasible
bounded instance. ∎

## 3. Finite cutting-plane oracle

### Theorem PP3cfj -- PROVED / FINITE CYCLE-GENERATION TERMINATION

Start with any finite cycle subset, solve its attenuation LP, and use the exact
shell cycle oracle to find a cycle violating its required decrease.  Add that
cycle and repeat.  The process terminates after at most the number of simple
cycles.  At termination, the current primal solution is feasible for the full
cycle system, and the restricted dual remains feasible for the full dual, so
the matching objectives certify global optimality.

#### Proof

Every unsuccessful iteration adds a previously absent simple cycle.  There are
finitely many.  At termination no full-system constraint is violated.  A dual
supported on generated cycles satisfies the same edge-capacity constraints as
the full dual after assigning zero to ungenerated cycles.  Strong duality for
the restricted problem then proves full optimality. ∎

## 4. Stored exact fixture

The audit `scripts/check_shell_cycle_cutting_plane.py` has three two-edge cycles
on three attenuable edges.  Starting with two cycles gives attenuation `(0,1,0)`
of cost one, but the third cycle is untouched.  Adding it yields the exact
optimum `(1/2,1/2,1/2)` of cost `3/2`.  Dual price `1/2` on every cycle saturates
every edge capacity and certifies the same objective.

## 5. Prime-patching consequence

Shell optimization no longer stops when a new critical cycle appears.  Each new
cycle becomes one explicit rational constraint; finite cycle generation either
produces a globally certified attenuation or a concrete unattenuable cycle.
