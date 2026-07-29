# Cycle-product criterion for shell potentials

`docs/415` shows that a multiplicative potential telescopes shell factors. The
remaining problem is to find such a potential. When shell states and adjacent
transitions are reduced to a finite directed graph, existence is governed
exactly by cycle products. This converts potential discovery into a finite
cycle audit.

The statements are general. They do not provide the finite shell-state
classification for the prime-patching process.

## 1. Finite shell transition graph

Let `G=(V,E)` be a finite directed graph. Every transition `e:u->v` carries a
positive shell factor `p_e`. Fix `q>0`. A positive function `Phi:V->(0,infinity)`
is a `q`-potential when

```text
p_e Phi(v)<=q Phi(u)
```

for every directed edge.

For a directed cycle `C`, write

```text
p(C)=product_(e in C) p_e,
|C|=number of edges.
```

### Theorem PP3bzb -- PROVED / FINITE CYCLE-PRODUCT POTENTIAL CRITERION

A positive `q`-potential exists if and only if every directed cycle satisfies

```text
p(C)<=q^|C|.
```

A strict potential satisfying

```text
p_e Phi(v)<q Phi(u)
```

for every edge exists if every directed cycle satisfies the strict inequality.

#### Proof

Necessity follows by multiplying the edge inequalities around a cycle and
cancelling the potentials.

For sufficiency, take logarithms. Writing `z(v)=log Phi(v)`, the constraints
become the difference inequalities

```text
z(v)-z(u)<=log q-log p_e.
```

A finite system of difference constraints is feasible exactly when every
directed cycle has nonnegative total right-hand side. That condition is

```text
sum_(e in C)(log q-log p_e)>=0,
```

which is equivalent to the cycle-product inequality. Under strict cycle
inequalities, decrease `q` slightly and apply the non-strict result. ∎

## 2. Optimal shell rate

Define the maximum cycle geometric mean

```text
q_*=max_C p(C)^(1/|C|),
```

with `q_*=0` when the graph is acyclic.

### Corollary PP3bzc -- PROVED / EXACT FINITE-STATE SHELL RATE

The infimum of the positive `q` admitting a positive `q`-potential is exactly
`q_*`. When the graph contains a directed cycle, the non-strict rate `q_*` is
attained. Consequently, if

```text
q_*<1,
```

then every shell transition path satisfies

```text
product_(i=0)^(r-1) p_(e_i)
 <=q^r Phi(v_0)/Phi(v_r)
```

for every chosen `q` with `q_*<q<1` and a corresponding positive potential.

#### Proof

The characterization follows directly from `PP3bzb`. Multiplying the edge
potential inequalities along a path gives the displayed telescoping bound. ∎

This identifies the only finite-state obstruction to a global shell potential:
a directed cycle whose geometric-mean expansion is at least one.

## 3. Exact rational auditing

### Theorem PP3bzd -- PROVED / RATIONAL CYCLE CERTIFICATE INTERFACE

When every `p_e` and the proposed `q` are rational, each cycle inequality can be
checked exactly without logarithms by comparing the integers in

```text
product_(e in C) p_e <= q^|C|.
```

A rational positive potential satisfying the edge inequalities is an
independent exact certificate. If it is strict with margin

```text
p_e Phi(v)<=q_e Phi(u),
max_e q_e=q<1,
```

then all path products contract at rate `q` up to the endpoint potential ratio.

#### Proof

The cycle comparisons and edge comparisons use only rational multiplication and
ordering. The path conclusion is the same telescoping multiplication as in
`PP3bzc`. ∎

## 4. Revised shell frontier

A finite shell-state quotient can now be closed by either of two exact audits:

1. enumerate its directed cycles and show every cycle product is below one;
2. provide one rational positive potential with a strict edge margin.

Failure returns an explicit noncontracting cycle, rather than an unstructured
long trajectory.

## 5. Exact diagnostic

Run

```bash
python scripts/check_shell_cycle_product_potential.py
```

The checker enumerates every simple directed cycle in a stored rational shell
graph, verifies the cycle products, and checks a rational strict potential on
all transitions.

The next theorem identifier after this chapter is `PP3bze`.
