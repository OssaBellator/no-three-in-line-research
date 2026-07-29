# Column generation for budget-coupled marker controllers

`docs/471` gives one rational controller LP containing every local marker action.
A geometric state may have a large but finite action family generated from local
repair patterns.  This chapter shows that the global controller can be solved by
adding only actions that violate the current dual prices.

Let `U` be the marker states.  State `u` has a finite action set `A_u`.  Action
`(u,a)` has rational cost `c_(u,a)` and rational contribution `G_(k,u,a)` to
global robust requirement `k`.  The required right-hand side is `b_k`.

## 1. Full master formulation

### Theorem PP3cfn -- PROVED / PURE-ACTION MASTER LP

The minimum shared resource needed by a randomized stationary controller is the
finite rational linear program

```text
minimize   sum_(u,a) c_(u,a) pi_(u,a)
subject to sum_(a in A_u) pi_(u,a)=1                 for every u,
           sum_(u,a) G_(k,u,a) pi_(u,a)>=b_k         for every k,
           pi_(u,a)>=0.
```

Every feasible controller is a convex combination of the pure local action
columns, and every feasible master point defines such a controller.

#### Proof

The statewise simplex equations say exactly that `pi_u` is a probability
distribution on the pure actions at state `u`.  Robust contributions and resource
cost are affine in these probabilities.  Thus the displayed master is equivalent
to the original randomized-controller problem.  Rational data admit a rational
basic optimum whenever the problem is feasible and bounded. ∎

## 2. Exact local pricing

### Theorem PP3cfo -- PROVED / REDUCED-COST ACTION ORACLE

Solve a restricted master containing subsets `A'_u subset A_u`.  Let `y_k>=0`
and free `alpha_u` be an optimal restricted dual solution.  The reduced cost of
an omitted action is

```text
r_(u,a)=c_(u,a)-alpha_u-sum_k y_k G_(k,u,a).
```

If every omitted action has `r_(u,a)>=0`, the restricted controller is globally
optimal for the full master.  Otherwise any negative-reduced-cost action is an
exact local witness that the restricted dual is not feasible for the full
problem.  Pricing separates by state: for each `u`, minimize

```text
c_(u,a)-sum_k y_k G_(k,u,a)
```

over `a in A_u` and compare the result with `alpha_u`.

#### Proof

The full dual consists of the inequalities

```text
alpha_u+sum_k y_k G_(k,u,a)<=c_(u,a)
```

for every action.  Nonnegative omitted reduced costs are precisely the missing
dual inequalities, so the restricted dual is then full-dual feasible.  Its
objective equals the restricted primal objective, while the restricted primal
is full-primal feasible; strong duality sandwiches both at the common global
optimum.  A negative reduced cost is exactly a violated full-dual inequality.
The expression contains only data from one state once the global prices are
fixed. ∎

## 3. Finite column generation

### Theorem PP3cfp -- PROVED / FINITE ACTION-GENERATION CERTIFICATE

Start from any feasible restricted master.  Repeatedly solve it exactly, call the
statewise pricing oracles, and add at least one previously absent action of
negative reduced cost.  With any deterministic anti-cycling rule, the process
terminates after finitely many additions.  At termination, the final primal
controller together with the final dual prices is a complete exact global
optimality certificate.

If a proposed budget `B` is below the certified optimum, the same full-dual
prices give a rational contradiction margin equal to `optimum-B`.

#### Proof

Every unsuccessful iteration adds a new action column, and the union of all
`A_u` is finite.  Therefore only finitely many unsuccessful iterations are
possible.  Termination means that every omitted reduced cost is nonnegative, so
`PP3cfo` proves global optimality.  Weak duality then proves the budget
contradiction with the stated exact margin. ∎

## 4. Stored exact fixture

The audit `scripts/check_column_generated_marker_controllers.py` has three marker
states.  Starting with only idle and local actions gives restricted cost
`23/12`.  Pricing finds exactly two improving columns:

```text
state u0 burst: reduced cost -1/2,
state u1 burst: reduced cost -2/3.
```

After adding them, the exact minimum shared budget is `13/9`.  The controller
uses burst mass `1/2` at `u0`, burst mass `1/3` at `u1`, and the local action with
mass one at `u2`.  Final prices make every remaining reduced cost nonnegative.
Budget `7/5` is impossible with exact dual margin `2/45`.

## 5. Prime-patching consequence

A large local catalogue of boundary repairs no longer has to be inserted into
one monolithic controller LP.  Global scenario and resource prices call small
statewise geometric oracles, and only genuinely useful repair columns enter the
certificate.
