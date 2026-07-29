# Eulerian realization of rational marker flows

`docs/489` and `docs/495` implement each rational marker-state policy through
local counters or binary routers.  A controller may also carry a rational
stationary flow on a finite memory graph.  This chapter turns the entire flow
into one deterministic periodic walk, preserving all average transition,
action, and resource statistics exactly.

Let `G=(V,E)` be a finite directed multigraph.  Edge `e` carries a rational
flow `f_e>=0`, an action label, and rational observable values `g_j(e)`.  Assume

```text
sum_(e out of v) f_e = sum_(e into v) f_e
```

for every vertex, the positive-flow support is strongly connected, and
`sum_e f_e=1`.

## 1. Exact periodic implementation

### Theorem PP3cih -- PROVED / EULERIAN FLOW REALIZATION

There is a positive integer `Q` and a directed period of length `Q` that uses
edge `e` exactly `Q f_e` times.  Consequently, every edge, action, and rational
linear observable has exactly its prescribed average over one period.

#### Proof

Choose `Q` clearing all denominators of the flows.  Replace edge `e` by
`Q f_e` parallel copies.  Flow conservation makes every vertex balanced, and
strong connectivity of the support makes the resulting directed multigraph
Eulerian.  An Euler circuit uses every copy exactly once.  Dividing its edge
counts by `Q` recovers `f`.  Linearity gives every action and observable
average. ∎

## 2. Uniform finite-horizon discrepancy

### Theorem PP3cii -- PROVED / PERIODIC PREFIX CERTIFICATE

For an observable `g`, let

```text
mu_g = sum_e f_e g(e)
S_g(r) = sum_(t<r) (g(e_t)-mu_g),  0<=r<=Q.
```

Starting the controller at its certified phase, every horizon `N` satisfies

```text
|sum_(t<N) g(e_t)-N mu_g| <= max_r |S_g(r)|.
```

For an arbitrary cyclic starting phase, the right-hand side may be replaced by
`max_r S_g(r)-min_r S_g(r)`.

#### Proof

Write `N=qQ+r`.  Every full period has centered sum zero, leaving exactly the
length-`r` prefix.  An arbitrary phase gives the difference of two cyclic
prefix sums, bounded by their range. ∎

## 3. Finite implementation audit

### Theorem PP3cij -- PROVED / EULERIAN WITNESS LOCALIZATION

A proposed deterministic flow implementation is certified by checking integer
edge multiplicities, vertex balance, one closed Euler walk, and the finite
prefix tables for the protected observables.  Failure returns an edge-count
mismatch, an unbalanced vertex, a broken transition, or one explicit prefix
exceeding its claimed discrepancy.

#### Proof

These finite checks are exactly the hypotheses and conclusions of `PP3cih` and
`PP3cii`. ∎

## 4. Stored exact fixture

The audit `scripts/check_eulerian_marker_flow_realization.py` uses ten edge
copies on three memory states.  Its Euler word is

```text
ABABACABAB
```

with action frequencies `(1/2,2/5,1/10)` for `(A,B,C)`.  The fixed-phase
indicator discrepancies are `(1/2,4/5,1/2)`; the arbitrary-phase ranges are
`(1/2,6/5,9/10)`.

## 5. Prime-patching consequence

A rational boundary controller can now be executed as one finite deterministic
state machine whose complete transition flow is exact.  Randomness is removed
without replacing long-horizon estimates by asymptotics: every protected
finite prefix has an explicit rational error bound.
