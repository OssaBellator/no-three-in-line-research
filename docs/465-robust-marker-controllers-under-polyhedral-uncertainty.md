# Robust marker controllers under polyhedral uncertainty

`docs/459` synthesizes a marker controller when every candidate action has one
known transition-load row.  Geometric estimates usually arrive as a finite
family of admissible rows: different boundary locations, parity classes, or
rounding cases may realize different transitions.  This chapter makes the
controller robust against that finite adversarial choice.

Fix one marker state `u`.  Let `A(u)` be its candidate actions and let `Sigma(u)`
be a finite scenario set.  Under action `a` and scenario `sigma`, the
nonnegative transition-load row is `R_(u,a)^sigma`.  Protect positive potentials
`w^1,...,w^m` at requested rates `q_j<1`.

For each robust constraint define

```text
g_(a,sigma,j)=<R_(u,a)^sigma,w^j>,
b_(sigma,j)=q_j w^j(u).
```

A stationary randomized controller is a probability vector `pi` on `A(u)`.

## 1. Finite robust synthesis

### Theorem PP3ced -- PROVED / ROBUST CONTROLLER LP

A controller at `u` protects every listed potential in every listed scenario if
and only if

```text
pi_a>=0,
sum_a pi_a=1,
sum_a pi_a g_(a,sigma,j)<=b_(sigma,j)
```

for every `(sigma,j)`.

#### Proof

The closed-loop transition row in scenario `sigma` is the convex combination
`sum_a pi_a R_(u,a)^sigma`.  Pairing it with `w^j` gives exactly the displayed
linear inequality.  Conversely those inequalities are precisely the desired
robust potential bounds. ∎

Applying the theorem independently at every marker state produces a global
closed-loop matrix satisfying

```text
Q^sigma w^j<=q_j w^j
```

for every allowed statewise scenario selection.

## 2. Sparse rational controllers

### Theorem PP3cee -- PROVED / ROBUST SUPPORT BOUND

For rational input data, every nonempty robust controller polytope has a rational
extreme point.  If `r` robust inequalities are linearly independent and active
at that point, its action support has size at most `r+1`, and therefore at most

```text
1+|Sigma(u)|m.
```

#### Proof

An extreme point is a basic feasible solution of the rational system in
`PP3ced`, so it is rational.  On a support of size `s`, the normalization
constraint and at least `s-1` independent active inequalities are needed to
isolate an extreme point.  Hence `s<=r+1`. ∎

Thus robustness does not require diffuse randomization across a large geometric
move bank.

## 3. Localized adversarial obstruction

### Theorem PP3cef -- PROVED / ROBUST SEPARATING WITNESS

The robust controller LP is infeasible if and only if there are nonnegative
weights `eta_(sigma,j)`, not all zero, such that

```text
min_a sum_(sigma,j) eta_(sigma,j) g_(a,sigma,j)
 >sum_(sigma,j) eta_(sigma,j) b_(sigma,j).
```

For rational data the weights may be chosen rational.

#### Proof

The action vectors `g_a=(g_(a,sigma,j))` generate their convex hull.  Feasibility
asks whether that hull meets the coordinate down-set below `b`.  Strict
separation of these disjoint rational polyhedra gives a nonnegative normal
`eta`; minimizing the separating functional over the hull reduces to the
minimum over its action vertices.  The converse follows by averaging the strict
inequality against any proposed policy. ∎

The witness is statewise: it identifies one marker state and one explicit
adversarial mixture of scenarios and observables that defeats every candidate
move.

## 4. Exact audit

Run

```bash
python scripts/check_robust_marker_controller_synthesis.py
```

The stored two-action, two-scenario fixture has the unique robust mix
`pi=(1/2,1/2)`, worst-case rate `1/2`, resolvent load `1/5`, and a rational
separator of margin `1/10` against the impossible proposed rate `2/5`.
