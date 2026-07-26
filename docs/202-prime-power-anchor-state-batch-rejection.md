# Anchor-state batch rejection gives a strong normalization branch

CMR777--CMR784 reduce branch-wide returned-edge ancestry to finite fresh
deletions, paid state/routing churn, or repeated physical restoration. At one
fixed owner there is a strong monotone normalization response.

Keep one feasible saturated two-layer state as an anchor. A nonimproving
candidate which destroys the live target has a labelled entering set relative to
the anchor. Deleting that entire entering set preserves the anchor, removes the
candidate, and deletes at least two currently available labelled edges.

This operation is **branch-local**. It may also remove other untested states, so
it is one rigorous structural subbranch rather than a completeness-preserving
search of the original family. The exact completeness correction is CMR830--
CMR837: the union of viable single-edge deletion children preserves every state
except the rejected candidate.

Fix one owner with two labelled layer hosts on a board of side `n`. Let
`\mathcal F` be the current nonempty family of feasible ordered, layer-disjoint
saturated states. Every state contains exactly `2n` labelled edges. Choose an
anchor

\[
S\in\mathcal F
\]

and one physical target triple

\[
T\subseteq |S|,
\]

where `|S|` forgets layer labels.

## 1. Distinct joint states have at least two entering edges

For `S'\in\mathcal F`, put

\[
A(S')=S'\setminus S.
\]

### Theorem CMR785 -- PROVED

If `S'\ne S`, then

\[
\boxed{|A(S')|\ge2,}
\qquad
\boxed{A(S')\cap S=\varnothing.}
\]

### Proof

Some permutation layer differs between `S` and `S'`. The symmetric difference
of two perfect matchings in that layer is a nonempty union of even alternating
cycles, so that layer contributes at least two edges of `S'\setminus S`.
Disjointness is definitional. ∎

## 2. Entering-batch deletion preserves the anchor

For a labelled edge set `A`, write

\[
\mathcal F-A
=
\{R\in\mathcal F:R\cap A=\varnothing\}.
\]

### Theorem CMR786 -- PROVED

For every candidate `S'\ne S`, deleting `A(S')`

1. preserves the anchor and leaves a nonempty surviving family;
2. removes `S'`;
3. cannot activate a previously inactive state or prescription;
4. removes at least two currently available labelled edges.

### Proof

The anchor avoids `A(S')`. The candidate contains the whole batch. Restricting a
state family cannot create a state or extendable prescription. Every entering
edge was available because `S'` was feasible, and CMR785 gives at least two. ∎

The surviving family may be a proper subfamily of the union of all viable
single-edge children from CMR831.

## 3. Canonical aggressive response to a target-destroying candidate

Let `\Phi` be the real-triple potential. Call `S'` target-destroying when

\[
T\not\subseteq |S'|.
\]

### Theorem CMR787 -- PROVED

The aggressive anchor scheduler uses one of two actions.

1. If `\Phi(S')<\Phi(S)`, accept `S'` and obtain strict improvement.
2. If `\Phi(S')\ge\Phi(S)`, pass to the surviving branch
   `\mathcal F-A(S')` and retain `S` and `T`.

### Proof

The first action is the desired endpoint. The second is CMR786, and the target
remains selected in the surviving anchor. ∎

The theorem does not assert that the second action retains every improving state
of the original family.

## 4. Exact aggressive-branch deletion budget

Run CMR787 repeatedly inside its current surviving branch.

### Theorem CMR788 -- PROVED

Before strict improvement, the number `B` of rejected entering batches satisfies

\[
\boxed{B\le n(n-1).}
\]

The total number of deleted labelled edges is at most

\[
\boxed{2n^2-2n.}
\]

### Proof

The two labelled hosts contain at most `2n^2` edges, and the anchor's `2n` edges
are never deleted. Every batch deletes at least two new nonanchor edges. ∎

## 5. Exhaustion forces the target in the surviving branch

### Theorem CMR789 -- PROVED

If no target-destroying state remains in the current surviving branch, then

\[
\boxed{T\subseteq |R|\quad\text{for every surviving }R.}
\]

### Proof

A surviving state omitting a target cell would itself be target-destroying. ∎

This forcedness is branch-local and is not promoted to the original family.

## 6. Branch-local labelled-pair normalization

Choose the lexicographically first same-layer pair

\[
P=\{a,b\}\subseteq S\cap T.
\]

Continue the same aggressive pass while a surviving state omits `P`.

### Theorem CMR790 -- PROVED

The combined target and pair normalization still uses at most `n(n-1)` batches,
and at termination

\[
\boxed{P\subseteq R\quad\text{for every state in the surviving branch}.}
\]

### Proof

All batches are disjoint subsets of the same `2n^2-2n` nonanchor edge universe.
Termination means no surviving state omits `P`. ∎

## 7. Exact contraction inside the surviving branch

Let `\ell` be the layer containing `P`. Remove the matching endpoints of `P` from
that layer and keep the physical cells of `P` unavailable to the opposite layer.
Let `\mathcal F/P` be the residual branch family.

### Theorem CMR791 -- PROVED

Restriction gives an exact branch-local bijection

\[
\boxed{
\mathcal F
\cong
\{P\}\times(\mathcal F/P).
}
\]

The side of layer `\ell` decreases by two, and the physical target transfers to

\[
\boxed{T\setminus P,}
\]

a rank-one trigger.

### Proof

Every surviving state contains `P`. Restriction and adjoining `P` are inverse
operations, and exactly one target cell remains. ∎

## 8. Corrected aggressive-branch endpoint

### Corollary CMR792 -- PROVED

At one fixed owner, the aggressive anchor subbranch reaches at least one of:

1. strict potential improvement;
2. at most `n(n-1)` entering-batch deletions;
3. a physical target forced in the surviving branch;
4. a labelled same-layer target pair forced in the surviving branch;
5. exact branch-local double contraction and a rank-one trigger;
6. owner change, restoration, or envelope expansion.

For a completeness-preserving existence argument, replace one rejected state by
the viable single-edge child union of CMR830--CMR837, or prove separately that a
chosen aggressive branch retains a desired improving witness.

### Proof

Use CMR785--CMR791 and the completeness correction CMR830--CMR837. ∎

No all-`n` theorem is claimed. Entering-set size, anchor preservation, aggressive
branch budgets, branch-local forcing, and contraction are checked in
[`scripts/verify_prime-power-anchor-state-batch-rejection.py`](../scripts/verify_prime_power_anchor_state_batch_rejection.py).
