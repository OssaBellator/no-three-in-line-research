# Anchor-state batch rejection closes fixed-owner target churn

CMR777--CMR784 reduce branch-wide returned-edge ancestry to finite fresh
deletions, paid state/routing churn, or repeated physical restoration. At one
fixed owner there is a stronger monotone response which does not need an a priori
full-token return bound.

Keep one feasible saturated two-layer state as an anchor. Every nonimproving
candidate which destroys the live target has a labelled entering set relative to
the anchor. Delete that entire entering set from the matching hosts and retain
the anchor. The candidate disappears, no inactive state becomes active, and at
least two previously available labelled edges are removed. If all target-
destroying states are exhausted, the physical target is unavoidable. Continue
the same deletion pass against states which change one chosen labelled
same-layer target pair. The pair then becomes fixed in every surviving state and
contracts exactly.

Fix one owner with two labelled layer hosts on a board of side `n`. Let
`mathcal F` be the nonempty family of feasible ordered, layer-disjoint saturated
states under the current mask. Every state contains exactly `2n` labelled edges.
Choose an anchor

\[
S\in\mathcal F
\]

and one physical target triple

\[
T\subseteq |S|,
\]

where `|S|` forgets the layer labels.

## 1. Distinct joint states have at least two entering edges

For `S' in mathcal F`, define the labelled entering set relative to the anchor

\[
A(S')=S'\setminus S.
\]

### Theorem CMR785 -- PROVED

If `S'!=S`, then

\[
\boxed{|A(S')|\ge2.}
\]

Moreover `A(S')` is disjoint from the anchor.

### Proof

Some permutation layer differs between `S` and `S'`. The symmetric difference
of two perfect matchings in that layer is a nonempty disjoint union of even
alternating cycles. Hence that layer contributes at least two edges of
`S'\setminus S`. Disjointness from `S` is definitional. ∎

The bound remains valid if both layers change.

## 2. Entering-batch deletion preserves the anchor

For a set `A` of labelled edges, put

\[
\mathcal F-A
=
\{R\in\mathcal F:R\cap A=\varnothing\}.
\]

### Theorem CMR786 -- PROVED

For every candidate `S'!=S`, deleting the complete entering batch `A(S')`

1. preserves the anchor `S` and hence leaves a nonempty feasible family;
2. removes `S'`;
3. cannot activate any state or matching prescription which was inactive before
   the deletion;
4. removes at least two currently available labelled edges.

### Proof

CMR785 gives `A(S') cap S=empty`, so `S` survives. The candidate contains every
edge of its entering set and therefore does not survive. Restricting a state
family cannot create a state or an extendable prescription. Since `S'` was
feasible under the current mask, none of its entering edges had been deleted
earlier; CMR785 gives at least two new deletions. ∎

This is a joint two-layer no-good cut, not a sequential rematching claim.

## 3. Rejecting a nonimproving target-destroying candidate

Let `Phi` be the real-triple potential. Call `S'` target-destroying when

\[
T\not\subseteq |S'|.
\]

### Theorem CMR787 -- PROVED

For every feasible target-destroying candidate `S'`, exactly one of the following
scheduler actions is valid.

1. If `Phi(S')<Phi(S)`, accept `S'` and obtain strict potential improvement.
2. If `Phi(S')>=Phi(S)`, reject `S'`, delete `A(S')` by CMR786, and keep the
   anchor `S` feasible with the original target `T` still selected.

### Proof

The first branch is the desired potential endpoint. In the second branch CMR786
preserves `S`; since `T subseteq |S|`, the anchor and target remain available for
the next search step. ∎

No target load is silently discarded by a rejected candidate.

## 4. Exact fixed-owner batch budget

Run CMR787 repeatedly, always choosing the first feasible target-destroying state
in a fixed order and rejecting it unless it improves.

### Theorem CMR788 -- PROVED

Before strict improvement, the number `B` of rejected entering batches satisfies

\[
\boxed{B\le n(n-1).}
\]

More precisely, the total number of deleted labelled edges is at most

\[
\boxed{2n^2-2n,}
\]

and every batch deletes at least two.

### Proof

There are at most `2n^2` labelled physical edges in the two layer hosts. The
anchor's `2n` labelled edges are never deleted. Every rejected batch deletes at
least two new nonanchor edges by CMR786. Therefore at most `2n^2-2n` labelled
edges are deleted and `2B<=2n^2-2n`. ∎

This bound is independent of the number of feasible two-layer states.

## 5. Exhaustion makes the physical target unavoidable

### Theorem CMR789 -- PROVED

If the CMR787 pass terminates without strict improvement because no feasible
target-destroying candidate remains, then

\[
\boxed{T\subseteq |R|\quad\text{for every surviving }R\in\mathcal F.}
\]

Thus `T` is a forced physical target certificate for the current owner and mask.

### Proof

A surviving state which omitted one physical cell of `T` would be a feasible
target-destroying candidate, contradicting termination. ∎

Layer assignments of the three target cells may still vary; they are normalised
next rather than assumed fixed.

## 6. The same pass forces one labelled target pair

Choose from the anchor target `T` the lexicographically first same-layer pair

\[
P=\{a,b\}\subseteq S.
\]

Such a pair exists because three target cells occupy two layers. Continue the
same monotone deletion pass: while a surviving state `R` does not contain the
exact labelled pair `P`, delete `A(R)=R\setminus S` and retain `S`.

### Theorem CMR790 -- PROVED

The combined target-destruction and labelled-pair-normalisation pass still uses
at most

\[
\boxed{n(n-1)}
\]

rejected batches in total. At termination,

\[
\boxed{P\subseteq R\quad\text{for every surviving }R.}
\]

### Proof

Every additional candidate differs from the same fixed anchor and is processed
by CMR786. All batches over both phases delete disjoint new subsets of the same
`2n^2-2n` nonanchor edge universe, so the single CMR788 budget applies to the
combined pass. Termination means no surviving state omits `P`. ∎

The result fixes a labelled matching prescription, not merely a majority-layer
frequency class.

## 7. Exact joint-state contraction of the forced pair

Let `ell` be the layer containing `P`. Remove the two source and two target
vertices of `P` from the layer-`ell` matching host. Keep the two physical cells of
`P` fixed and forbidden to the opposite layer. Let `mathcal F/P` be the resulting
residual joint-state family.

### Theorem CMR791 -- PROVED

Restriction gives an exact bijection

\[
\boxed{
\mathcal F
\cong
\{P\}\times(\mathcal F/P).
}
\]

The side of layer `ell` decreases by exactly two. The physical target `T`
transfers to the residual singleton trigger

\[
\boxed{T\setminus P.}
\]

### Proof

CMR790 puts `P` in every surviving joint state. Removing its two labelled edges
and their matching endpoints in layer `ell` gives one residual state. Conversely,
adjoining `P` to a residual state reconstructs the unique full state; the
opposite layer continues to avoid the two fixed physical cells. The maps are
inverse. Since `T` has three cells and `P` has two, one physical target cell
remains. ∎

The residual rank-one trigger enters the established essential-transfer,
anchored-deletion, or strict-factor recursion.

## 8. Fixed-owner target-churn endpoint

### Corollary CMR792 -- PROVED

At one fixed owner and mask, the anchor-state scheduler reaches at least one of:

1. a target-destroying state of strictly smaller real-triple potential;
2. at most `n(n-1)` monotone entering-batch deletions;
3. a forced physical target;
4. one exact labelled same-layer target pair fixed in every surviving state;
5. exact double contraction of that pair and a rank-one residual trigger;
6. owner change, edge restoration, or envelope expansion, entering CMR777--CMR784.

Consequently unbounded selected-state churn is not required to resolve a fixed
owner. Every rejected nonimproving reset permanently deletes at least two
nonanchor labelled edges, and terminal failure produces strict factor descent.

### Proof

Use CMR787--CMR790. If the first phase exhausts, CMR789 gives a forced physical
target; normalise its anchor pair by CMR790 and contract by CMR791. Any departure
from the fixed owner or monotone mask enters the global return-ancestry forest. ∎

No all-`n` theorem is claimed. Entering-set size, anchor preservation, deletion
budgets, target forcing, pair normalisation, and contraction are checked in
[`scripts/verify_prime_power_anchor_state_batch_rejection.py`](../scripts/verify_prime_power_anchor_state_batch_rejection.py).
