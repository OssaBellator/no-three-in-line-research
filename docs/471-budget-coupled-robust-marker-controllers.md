# Budget-coupled robust marker controllers

`docs/465` treats robust marker synthesis state by state.  Geometric repair
moves may also consume a shared resource: a rare direction, a protected residue
class, or a bounded marker budget.  This chapter adds exact global coupling
without losing finite rational certificates.

Let `U` be a finite marker-state set.  State `u` has actions `A_u`, and a
stationary controller chooses probabilities `pi_(u,a)`.  For every adversarial
scenario `s` and protected potential `j`, action `(u,a)` has rational signed gap
`g_(u,a,s,j)`, where nonnegative averaged gap means the requested contraction
is met.  It also consumes rational resource `c_(u,a,r)` from budget `B_r`.

## 1. Global robust synthesis

### Theorem PP3cev -- PROVED / BUDGET-COUPLED CONTROLLER LP

A controller satisfying

```text
sum_(a in A_u) pi_(u,a)=1,
pi_(u,a)>=0,
sum_a pi_(u,a) g_(u,a,s,j)>=0,
sum_(u,a) c_(u,a,r) pi_(u,a)<=B_r
```

for every state, scenario, potential, and shared resource exists if and only if
the displayed finite rational linear program is feasible.

#### Proof

Every closed-loop transition row is affine in the action probabilities.  Each
robust potential inequality and each resource budget is therefore linear.
Conversely, any feasible LP point defines the required stationary randomized
controller.  All coefficients are rational, so a feasible basic solution may
be chosen rational. ∎

## 2. Sparse global randomization

### Theorem PP3cew -- PROVED / RANDOMIZATION-EXCESS BOUND

At a basic feasible controller, let `M` be the number of linearly independent
active robust and resource inequalities.  Then

```text
sum_u (|supp pi_u|-1) <= M.
```

In particular, global coupling creates only finitely many extra randomized
actions beyond one action per state.

#### Proof

There are `|U|` independent simplex equalities.  A basic solution has at most
`|U|+M` positive variables after restricting to the active inequality system.
Subtracting one mandatory positive action from every state gives the bound. ∎

## 3. Exact infeasibility witnesses

### Theorem PP3cex -- PROVED / RESOURCE-PRICED SEPARATOR

If the controller LP is infeasible, there are nonnegative rational prices on
scenario--potential constraints and shared resources, together with free
state-simplex prices, whose priced score is strictly unfavorable for every
candidate action.  The resulting positive contradiction margin is an exact
finite certificate of failure.

#### Proof

Apply rational Farkas separation to the complete controller system.  Grouping
dual variables by robust constraints, resources, and state simplex equalities
produces the stated per-action priced inequalities.  Strictly positive dual
objective gives the contradiction margin. ∎

## 4. Stored exact fixture

The audit `scripts/check_budget_coupled_robust_marker_controllers.py` has two
states and one shared budget.  Robust constraints force

```text
x>=1/3,  y>=1/2,
```

while the resource budget gives `x+y<=5/6`.  Hence the unique controller is
`(x,y)=(1/3,1/2)`.  Tightening the budget to `4/5` is impossible with exact dual
margin `1/30`.  The resulting closed-loop row loads are `19/60` and `3/8`.

## 5. Prime-patching consequence

Marker choices from different local boundary states may now share a scarce
geometric resource without being optimized independently.  Success returns one
rational distributed controller; failure returns explicit scenario and resource
prices identifying the incompatible local actions.
