# Positive-cycle oracles and circulation duals for shell attenuation

`docs/475` gives a finite cutting-plane method once a violated shell cycle can be
found.  This chapter supplies an exact graph oracle and compresses the cycle
packing dual into one capacitated circulation.

Let a directed shell graph have rational additive edge excess `a_e`, rational
attenuation cost `c_e>0`, and chosen nonnegative attenuation `x_e`.  Every directed
cycle `C` requires

```text
sum_(e in C) x_e >= sum_(e in C) a_e.
```

## 1. Exact cycle separation

### Theorem PP3cfz -- PROVED / POSITIVE-RESIDUAL-CYCLE ORACLE

Set residual edge weight `r_e=a_e-x_e`.  The attenuation satisfies every cycle
constraint if and only if the residual graph has no directed cycle of positive
total weight.  A violated constraint is therefore found by an exact positive-
cycle oracle, equivalently by Bellman--Ford on weights `-r_e`.  A maximum-mean
cycle oracle returns the most violated cycle after normalization by length.

#### Proof

The residual sum on `C` is exactly

```text
sum_(e in C) a_e-sum_(e in C) x_e.
```

It is positive precisely when the corresponding cycle inequality fails.
Negating the weights converts a positive cycle to a negative cycle, which
Bellman--Ford detects and reconstructs.  All arithmetic is rational. ∎

## 2. Compact circulation dual

### Theorem PP3cga -- PROVED / CYCLE PACKING AS CAPACITATED CIRCULATION

The full attenuation LP

```text
minimize   sum_e c_e x_e
subject to sum_(e in C) x_e>=sum_(e in C) a_e  for every cycle C,
           x_e>=0
```

has dual equal to the compact rational circulation problem

```text
maximize   sum_e a_e f_e
subject to f is a nonnegative circulation,
           0<=f_e<=c_e.
```

#### Proof

The cycle-variable dual assigns `y_C>=0` and has edge capacities
`sum_C m_(C,e)y_C<=c_e`.  Aggregating cycle flows gives
`f_e=sum_C m_(C,e)y_C`, which is a nonnegative circulation and has objective
`sum_e a_e f_e`.  Conversely, every finite nonnegative circulation decomposes
into directed simple cycles.  Using the decomposition coefficients as `y_C`
recovers a feasible cycle packing with the same objective. ∎

## 3. Oracle cutting planes with a compact witness

### Theorem PP3cgb -- PROVED / FINITE SEPARATION--DUAL CERTIFICATE

Start from any finite cycle subset, solve the restricted attenuation LP exactly,
and call the positive-cycle oracle.  Add the returned violated simple cycle until
none remains.  The process terminates finitely.  At termination, a feasible
attenuation `x` and a capacitated circulation `f` with equal objectives certify
global optimality for all shell cycles.

Failure may instead return an unattenuable positive cycle or a strict primal--
dual objective gap in the proposed certificate.

#### Proof

Every unsuccessful iteration adds a previously absent simple cycle, and there
are finitely many.  Absence of a positive residual cycle is full primal
feasibility by `PP3cfz`.  The compact circulation is full-dual feasible by
`PP3cga`; equality of objectives invokes strong duality. ∎

## 4. Stored exact fixture

The audit `scripts/check_shell_cycle_separation_and_circulation.py` uses the
complete bidirected triangle.  Every edge has excess `1/2` and cost one.  Solving
only the three two-cycle constraints gives cost three but leaves the directed
three-cycle

```text
0 -> 1 -> 2 -> 0
```

violated by total `3/2`, or mean `1/2`.  Adding that cycle yields a full feasible
attenuation of cost three.  Unit circulation on all six directed edges has dual
value three, exactly matching the primal optimum.  The audit checks all five
simple directed cycles.

## 5. Prime-patching consequence

Shell attenuation no longer needs an explicit precomputed list of all critical
cycles.  A rational graph oracle generates only violated cycles, while one
compact circulation records the complete dual obstruction or optimality proof.
