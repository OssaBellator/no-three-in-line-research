# SRR weighted conflict thinning

The threshold-degree and near-product results produce a weighted family of feasible switching candidates. This note supplies an exact deterministic-compatible subfamily bound from the local conflict graph, going beyond a first-moment count of candidates.

## Setup

Let `G=(V,E)` be the exact conflict graph of feasible switching candidates at one endpoint stage. Candidate `v` has nonnegative weight `w_v`. An independent set is a simultaneously executable subfamily. All conflicts must be represented as edges; omitted higher-order conflicts are outside the contract.

## SRR2ar — random-priority local minima

Give the vertices an independent uniformly random priority and retain every vertex whose priority is smaller than all of its neighbours. The retained set is independent, and vertex `v` is retained with probability

`1/(deg(v)+1)`.

## SRR2as — weighted Caro–Wei bound

There exists an executable subfamily `I` with

`sum_{v in I} w_v >= sum_{v in V} w_v/(deg(v)+1)`.

This is an exact existence statement and allows nonuniform candidate weights.

## SRR2at — maximum-degree corollary

If every candidate conflicts with at most `Delta` others, then

`w(I) >= w(V)/(Delta+1)`.

Thus the threshold/pathwise candidate mass survives deterministic conflict thinning with only the local conflict-degree loss.

## SRR2au — weighted-degree alternative

Partition candidates by any finite degree classes. Applying SRR2as classwise retains the complete sum of local contributions, avoiding replacement of all candidates by the worst global degree when the conflict distribution is uneven.

## SRR2av — endpoint router

Combine with the existing threshold-cost route:

- threshold degree/load and perturbation estimates produce feasible candidate weight;
- the exact conflict graph converts that weight to a simultaneously executable subfamily;
- excessive conflict degree returns one exact high-conflict candidate or conflict atom;
- an omitted non-pairwise interaction returns a conflict-model reset.

The note does not prove small conflict degree for the geometric rank-two/rank-three switching cylinders. That remains the menu-specific local estimate.

No statement here proves SRR2, SRR4 or the no-three-in-line conjecture.