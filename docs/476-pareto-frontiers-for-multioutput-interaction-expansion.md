# Pareto frontiers for multioutput interaction expansion

`docs/470` minimizes scalarized omitted output under an expansion budget.  The
final core correction may have several coordinates with independent tolerances.
Weighted sums can miss feasible tradeoffs, so this chapter keeps the complete
finite Pareto frontier.

Consider a finite interaction forest or a finite budget truncation of an
interaction automaton.  An expansion plan `P` has integer work `w(P)` and exact
nonnegative omitted-output vector `E(P) in Q_+^r`.

## 1. Exact nondominated dynamic program

### Theorem PP3cfk -- PROVED / BUDGETED PARETO RECURRENCE

For every budget `B`, let

```text
F_B=minimal elements of {E(P): w(P)<=B}
```

under coordinatewise order.  Combining child frontier vectors by exact vector
addition and deleting dominated vectors computes `F_B` exactly.  Dominance
pruning is safe: a dominated partial vector can never lead to a nondominated
completion with the same remaining choices and no greater cost.

#### Proof

Every plan decomposes into its root decisions and child plans, so vector addition
enumerates all attainable outputs.  If `u<=v` coordinatewise, adding any
nonnegative continuation preserves `u+h<=v+h`; therefore `v` cannot become
nondominated.  Induction over the finite expansion forest proves exactness. ∎

## 2. Minimum work for coordinatewise tolerances

### Theorem PP3cfl -- PROVED / PARETO TOLERANCE CERTIFICATE

For tolerance vector `tau`, the minimum feasible work is the least `B` for which
some `e in F_B` satisfies `e<=tau`.  The complete frontier `F_(B-1)` is a matching
impossibility certificate for every smaller budget.

#### Proof

Every attainable vector is dominated by some member of its budget frontier.
Thus a feasible plan exists exactly when the frontier contains a vector below
`tau`.  Minimality follows by checking budgets in increasing order. ∎

## 3. Unsupported interaction tradeoffs

### Theorem PP3cfm -- PROVED / SCALARIZATION-INCOMPLETENESS WITNESS

Weighted-sum optimization recovers only supported Pareto points.  A finite exact
frontier may contain an unsupported point that is never a strict minimizer of
`omega dot e` for any nonnegative weight vector `omega`, yet is the unique point
meeting a coordinatewise tolerance.  Retaining the complete nondominated set is
therefore necessary for exact multioutput certification.

#### Proof

Weighted sums expose only points on supporting hyperplanes of the lower convex
hull.  A nondominated point strictly above a chord between two other
nondominated points is unsupported, but it can still lie inside an axis-aligned
tolerance box that excludes both chord endpoints. ∎

## 4. Stored exact fixture

The audit `scripts/check_multioutput_interaction_pareto.py` has four independent
interaction roots.  At budget three its exact frontier is

```text
(3/10,7/10), (11/20,11/20), (7/10,3/10).
```

The middle vector is unsupported by every rational scalarization weight tested
and, analytically, lies above the chord of the two extremes.  Nevertheless it is
the unique plan meeting tolerance `(3/5,3/5)`, proving minimum work three; the
budget-two frontier is the matching impossibility certificate.

## 5. Prime-patching consequence

Interaction truncation can now certify several core entries simultaneously
without hiding tradeoffs inside an arbitrary scalar weight.  The output is a
finite exact Pareto set, a minimum-work feasible plan, or a complete lower-budget
obstruction.
