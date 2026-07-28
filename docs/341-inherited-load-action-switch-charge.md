# Inherited-load charge across the strict-repair / clean-macro switch

`docs/340` verifies that target-optimal fixed-sign strict repair can be followed
by the parity-clean macro without enlarging the finite reachability horizon
through `m=9`.  The remaining issue is predecessor charge across that action
switch.  This chapter gives the exact static and dynamic formulas.

No asymptotic expansion, mixing, or termination theorem is claimed.

## 1. The inherited terminal load

Fix any family `F` of signed source states, for example the states carrying one
selected flaw.  Let `R` be a substochastic strict-repair kernel from `F` to
parity-clean signed terminal states.  The missing row mass may represent source
states handled by another action.

For a parity-satisfiable Hamilton cycle `rho`, define its inherited load

```text
a_F(rho)
 = sum_(x in F) sum_(e clean over rho) R(x,(rho,e)).
```

Write

```text
v(rho)=2^c(rho)
```

for the clean fibre size.  After the strict phase, forget the terminal
orientation and regenerate uniformly inside the chosen clean fibre.

Let `P(rho,eta)` be any row-stochastic clean-cycle kernel supported on an
allowed switch graph.

### Proposition PP3bpj -- PROVED / EXACT SWITCH COLUMN MASS

For every clean signed output state over target cycle `eta`, the total incoming
mass from `F` after strict repair, cycle transport `P`, and exact target-fibre
regeneration is

```text
M_F(eta)
 = [1/v(eta)] sum_rho a_F(rho) P(rho,eta).
```

Consequently the switched action charge is

```text
gamma_F(P)=max_eta M_F(eta).
```

#### Proof

The total strict-phase mass arriving anywhere in the clean fibre over `rho` is
`a_F(rho)`.  It chooses target cycle `eta` with probability `P(rho,eta)` and
then each of the `v(eta)` clean target orientations with probability
`1/v(eta)`.  Sum over terminal source cycles. ∎

The terminal orientation distribution before regeneration is irrelevant; all
strict predecessor merging is compressed into the scalar cycle load `a_F`.

## 2. Exact optimal charge at the switch

For `U` contained in the support of `a_F`, write

```text
a_F(U)=sum_(rho in U) a_F(rho)
```

and let `N(U)` be its reachable clean target cycles under the switch graph.

### Theorem PP3bpk -- PROVED / INHERITED-LOAD WEIGHTED HALL FORMULA

Among all supported row-stochastic switch kernels, the least possible merged
charge is

```text
gamma_F^*
 = max_(empty != U) a_F(U)/v(N(U)),
```

where

```text
v(N(U))=sum_(eta in N(U)) v(eta).
```

#### Proof

A proposed charge `gamma` gives target cycle `eta` capacity
`gamma v(eta)`.  The supply at source cycle `rho` is `a_F(rho)`.  A complete
transport exists exactly when every source subset satisfies

```text
a_F(U)<=gamma v(N(U)).
```

These are the finite-cut inequalities in the standard source--left--right--sink
network.  Max-flow/min-cut proves sufficiency, and necessity is immediate.
Taking the least feasible `gamma` gives the formula. ∎

Thus the strict phase changes the source weights but not the form of the Hall
problem in `docs/324`.

## 3. Heat evolution of inherited load

Let `K` be the fibre-weighted reversible Metropolis kernel from `docs/330`, with

```text
pi(rho)=v(rho)/V,
V=sum_rho v(rho).
```

Define the inherited fibre-relative density

```text
h_F(rho)=a_F(rho)/v(rho).
```

### Theorem PP3bpl -- PROVED / EXACT SWITCH HEAT-KERNEL CHARGE

If the clean-cycle phase runs `t` steps of `K` before exact fibre regeneration,
then

```text
gamma_F(t)=||K^t h_F||_infinity.
```

#### Proof

Before reversibility, the output column over `eta` is

```text
[1/v(eta)] sum_rho a_F(rho) K^t(rho,eta).
```

Substitute `a_F(rho)=v(rho)h_F(rho)` and use detailed balance

```text
v(rho)K^t(rho,eta)=v(eta)K^t(eta,rho).
```

The fibre factors cancel, leaving

```text
sum_rho K^t(eta,rho)h_F(rho)=(K^t h_F)(eta).
```

Take the largest output column. ∎

This formula includes all strict-path merging, terminal-cycle merging, clean
walk merging, and target-fibre multiplicity.

## 4. The stationary endpoint and warmness

Put

```text
mu_F=[sum_rho a_F(rho)]/V.
```

### Corollary PP3bpm -- PROVED / MASS CONSERVATION AND SWITCH WARMNESS

If every source row of `R` has total mass one, then

```text
sum_rho a_F(rho)=|F|
```

for unit source weights, and hence

```text
mu_F=|F|/V.
```

More generally the numerator is the total initial source mass.  If

```text
K^t(rho,eta)<=(1+epsilon)pi(eta)
```

pointwise, then

```text
gamma_F(t)<=(1+epsilon)mu_F.
```

At finite time the only additional input needed is the warmness profile
`h_F=a_F/v`; the strict phase cannot change the stationary mean, but it can
concentrate inherited load on low-fibre terminal cycles.

#### Proof

Row-stochasticity preserves total mass, proving the first statements.  For the
pointwise bound, apply the pre-reversibility formula from PP3bpl:

```text
[1/v(eta)] sum_rho a_F(rho)K^t(rho,eta)
 <= [(1+epsilon)pi(eta)/v(eta)] sum_rho a_F(rho)
 = (1+epsilon)mu_F.
```

Take the maximum over `eta`. ∎

## 5. Revised action-switch frontier

The finite reachability bridge of `docs/340` and the exact charge formulas above
separate the remaining work.

1. The strict phase supplies an inherited terminal load `a_F`; no additional
   orientation bookkeeping survives fibre regeneration.
2. One-step switching is exactly the weighted Hall problem for `a_F`.
3. A clean trajectory is exactly heat evolution of `h_F=a_F/v`.
4. The stationary endpoint is fixed by total source mass; the open quantitative
   issue is terminal-cycle warmness and clean-cycle mixing.
5. The owner light cone in `docs/338` controls which atomic events can contribute
   to `a_F`, but does not by itself bound its cycle concentration.

The next theorem identifier after this chapter is `PP3bpn`.
