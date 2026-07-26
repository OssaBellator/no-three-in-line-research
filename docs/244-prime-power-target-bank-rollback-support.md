# Rolled-back target banks expose recurrent or dispersed missing-edge support

The target-hypergraph and robust-surplus chapters construct full-parent saturated
states which destroy designated targets.  A current restricted host need not
contain every edge of such a bank state.  Canonical expansion normalization may
therefore roll the attempted execution back to the old host.

Rollback is not an anonymous no-progress outcome.  Every infeasible candidate
uses at least one currently unavailable labelled edge.  Exact duplicate attempts
at the same normalized host are cycle-erasable.  A large family of distinct
rolled-back candidates therefore concentrates on one unavailable edge or exposes
a large distinct blocker inventory.  If a concentrated blocker is restored, the
minimum-face edge dichotomy deletes it again or contracts it.

Fix one normalized host `H` on an ambient labelled edge universe `U`, and let
`B` be a finite family of labelled candidate states of equal cardinality.  Every
`Q in B` is a valid matching or joint state on the ambient vertices and destroys
at least one designated target of the stored minimum anchor.

For a candidate infeasible in `H`, define its missing support

\[
A_H(Q)=Q\setminus E(H).
\]

## 1. Every infeasible bank state has missing support

### Theorem CMR1118 -- PROVED

If `Q notin F(H)`, then

\[
\boxed{A_H(Q)\ne\varnothing.}
\]

### Proof

Feasibility of the already valid labelled state `Q` in a host is equivalent to
containment of all its selected edges.  If `A_H(Q)` were empty, then `Q subseteq
E(H)` and `Q` would be feasible. ∎

## 2. Rollback records the same missing support

Let `H_Q` be any expansion of `H` which makes `Q` feasible.  Assume the stored
minimum anchor survives and the minimum value does not decrease.

### Theorem CMR1119 -- PROVED

The canonical expansion response rolls back to `H`.  Every edge of `A_H(Q)` is
removed again, and `Q` becomes infeasible again.

### Proof

The base host is feasible and has the same minimum value as the expansion because
the stored anchor survives and no lower state appears.  Apply the same-value
rollback branch of CMR952. ∎

Thus the rollback certificate is the nonempty physical edge set `A_H(Q)`.

## 3. Exact duplicate rollback is erasable

### Theorem CMR1120 -- PROVED

At an unchanged normalized host `H`, a second attempt to execute the same candidate
`Q` has the same missing support and normalizes to the identical host state.
Deleting the repeated attempt does not change any later feasible family or minimum
value.

### Proof

Both feasibility and the canonical same-value rollback depend only on `H` and the
fixed selected edge set `Q`.  The second transition has the same input and output
as the first. ∎

Hence a shortest canonical history uses each exact candidate at most once per
normalized host.

## 4. Canonical blocker concentration

Order the labelled edge universe and choose

\[
\sigma_H(Q)=\min A_H(Q)
\]

for every infeasible candidate.

### Theorem CMR1121 -- PROVED

For `J` distinct rolled-back candidates and every integer `lambda>=2`, at least one
of the following holds.

1. One exact labelled unavailable edge is the canonical blocker for at least
   `lambda` candidates.
2.
   \[
   \boxed{J\le(\lambda-1)|U|.}
   \]

For a saturated side-`N` two-layer universe,

\[
\boxed{J\le2(\lambda-1)N^2}
\]

unless one blocker has multiplicity `lambda`.

### Proof

Assign every candidate to its canonical blocker.  If no edge receives `lambda`
assignments, every one of the `|U|` labels receives at most `lambda-1`. ∎

This bound is independent of the number of possible bank constructions.

## 5. Support-incidence concentration or dispersed inventory

Put

\[
I_H(\mathcal B)
=
\sum_{Q\in\mathcal B}|A_H(Q)|,
\qquad
W_H(\mathcal B)
=
\bigcup_{Q\in\mathcal B}A_H(Q).
\]

### Theorem CMR1122 -- PROVED

For every `lambda>=2`, either one unavailable edge belongs to at least `lambda`
missing supports, or

\[
\boxed{
|W_H(\mathcal B)|
\ge
\frac{I_H(\mathcal B)}{\lambda-1}.
}
\]

The distinct blocker inventory has exact all-depth, all-direction token membership
mass

\[
\boxed{
(p+1)(h-1)|W_H(\mathcal B)|.
}
\]

This is static token membership; it becomes restoration payment only when those
edges actually return.

### Proof

If every edge belongs to at most `lambda-1` supports, double-count the incidences
`(Q,e)` with `e in A_H(Q)`.  The token identity is the same prefix-membership count
as CMR413 applied once to the distinct edge set. ∎

## 6. A recurrent blocker has an immediate minimum response

### Theorem CMR1123 -- PROVED

Suppose one exact blocker edge `e` supports many rolled-back candidates.

1. While `e` remains unavailable, every candidate whose missing support contains
   `e` remains infeasible.
2. If `e` is restored and activates one of those candidates, then at the current
   minimum face `e` is either minimum-preservingly deletable, belongs to the
   minimum core and contracts, or the activation yields strict improvement or
   structural exit.
3. Every later noncontracting activation through `e` requires another genuine
   restoration and exact CMR413 token incidence.

### Proof

The first statement is containment.  Newly activated states use the newly
available edge by CMR814.  Apply the minimum-face dichotomy CMR914 and the repeated
activation theorem CMR818. ∎

Thus blocker concentration is a paid fixed-edge branch, not a new bank-specific
recurrence.

## 7. Branch-wide rollback stock

### Theorem CMR1124 -- PROVED

On the selected minimum path, route once to the anchor skeleton at every host stage
and erase exact duplicate attempts.  Before blocker restoration, contraction,
loss ancestry, structural exit, or strict improvement, the number of distinct
rolled-back candidates at one normalized host is at most

\[
2(\lambda-1)N^2
\]

unless one exact blocker has multiplicity `lambda`.

Across the finite selected owner-stage stock of CMR1098 and the wall/envelope
multipliers, all nonconcentrated rollback families have a finite parameterized
branch-wide stock.

### Proof

Apply CMR1121 at every normalized host.  CMR1098, CMR742, and the closure-envelope
bound give finitely many selected host owners. ∎

The parameter is used only to isolate one recurrent physical blocker; routing no
longer contributes a recurrence threshold.

## 8. Target-bank rollback endpoint

### Corollary CMR1125 -- PROVED

Every rolled-back target-destroying bank reaches at least one of:

1. exact duplicate cycle erasure;
2. an explicit finite distinct-candidate bound;
3. one recurrent unavailable blocker edge;
4. a large distinct unavailable-edge inventory with exact token membership;
5. minimum-preserving blocker deletion;
6. blocker minimum-core contraction;
7. lost-anchor ancestry, strict factor/wall/envelope exit, or strict improvement.

Combined with CMR1094--CMR1117, rollback does not supply an uncontrolled escape
from the finite routing, protected-growth, loss, and fixed-core reopening ledgers.
The remaining frontier is to aggregate recurrent blocker and loaded-line
certificates across the final selected structural descent tree, or else obtain a
strictly lower physical minimum.

### Proof

Combine CMR1118--CMR1124. ∎

No all-`n` theorem is claimed.  Missing-support nonemptiness, duplicate erasure,
blocker concentration, incidence dispersion, and restoration responses are checked
in
[`scripts/verify_prime_power_target_bank_rollback_support.py`](../scripts/verify_prime_power_target_bank_rollback_support.py).
