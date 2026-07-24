# Monotone termination of controller-shadow repair

The endpoint-permutation trade PP3id strictly decreases the integer
controller-shadow potential whenever its insertion cost is below its removal
credit.  This chapter records the resulting termination theorem.  The point is
that successful paid trades cannot cycle: the remaining open statement is only
the existence of an improving trade whenever the controller-aware label graphs
are too sparse.

## 1. Fixed controller infrastructure

Fix one perfect matching layer and disjoint slab pools

\[
 E_1,\ldots,E_M.
\]

Let `V` be the complete candidate-entry universe consisting of all typed final
labels, all controller edges in the pools, and their movement/refill candidate
cells.  For any saturated no-three source `S'` containing every controller edge,
define

\[
 \Psi_V(S')
 =
 \sum_{\{p,q\}\subseteq S'}w_V(p,q),
\]

where `w_V(p,q)` is the number of entries in `V` whose candidate cell is
collinear with `p,q` and whose controller is neither endpoint.

### Proposition PP3ij -- PROVED

The potential `Psi_V` is a nonnegative integer bounded by

\[
 \boxed{
 \Psi_V(S')
 \le
 |V|\binom{2m}{2}.
 }
\]

More sharply, since blocker pairs through one external cell are
endpoint-disjoint,

\[
 \boxed{
 \Psi_V(S')
 \le m|V|.
 }
\]

#### Proof

Every term is an integer.  The first bound charges every source pair to every
candidate entry.  For one candidate cell, its source blocker pairs form a
matching on the `2m` source points, hence there are at most `m` of them.  Sum
over `V`. ∎

## 2. Infrastructure preservation under endpoint trades

Use a resource matching whose selected blocker endpoints are disjoint from all
controller edges, as in PP3hy.  Apply an endpoint-permutation trade inside one
perfect matching layer.

### Proposition PP3ik -- PROVED

Every source-admissible endpoint-permutation trade has the following
properties.

1. The resulting source is saturated and no-three-in-line.
2. Every controller edge in every pool `E_i` remains present.
3. The controller pools remain pairwise disjoint subsets of one perfect
   matching layer.
4. The same candidate-entry universe `V` and the same typed final labels may be
   used at the next step.

#### Proof

Source validity and saturation are part of source admissibility and PP3ia.
Resource disjointness ensures that no selected blocker endpoint is a controller
point.  Hence the trade changes none of the controller edges.

Permuting row endpoints within one permutation layer leaves that layer a
permutation graph.  The unchanged controller edges therefore remain in one
perfect matching layer and in their original disjoint column slabs.  Candidate
labels and candidate cells are fixed numerical coordinates, so the universe
`V` is unchanged. ∎

This is why controller/blocker resource disjointness was included in PP3hy.

## 3. One-step progress alternative

Fix a density threshold `delta>0`.  Call a source state **ready** when its
controller-aware global graphs satisfy one of the allocation criteria PP3fy or
PP3gl with domain density at least `gamma`.

Call it **convertible** when it is not ready but admits a source-admissible
endpoint, rectangle, cycle, or tomographic trade that preserves all controller
edges and strictly decreases `Psi_V`.

### Proposition PP3il -- PROVED

Suppose every non-ready source state containing the fixed controller
infrastructure is convertible.  Starting from the original source, finitely
many trades produce a ready state.

The number of trades is at most

\[
 \boxed{
 \Psi_V(S_0).
 }
\]

#### Proof

Each trade preserves the infrastructure by hypothesis and decreases the
nonnegative integer potential by at least one.  Therefore no state can repeat
and at most `Psi_V(S_0)` trades occur.  If the process stopped at a non-ready
state, that state would be convertible, contradicting maximality. ∎

This is an exact monotone potential, not a heuristic drift argument.

## 4. Termination through the star/resource dichotomy

Positive-density failure of controller-aware safety gives the alternatives
PP3hy:

1. a blocker star of degree `Omega(m^(19/40))`;
2. a resource-disjoint bank of size `Omega(m^(21/40))`.

The star branch has the alternating endpoint-neutralisation bank AN1--AN4.  The
resource branch has the endpoint-derangement bank PP3ia--PP3ii.

### Theorem PP3im -- PROVED UNDER TWO EXPLICIT CONVERSION HYPOTHESES

Assume there are constants `delta,gamma>0` such that, for every saturated
no-three source containing the fixed controller infrastructure:

1. if the controller-aware graphs fail the allocation criterion by a
   `delta`-density cell-shadow obstruction and PP3hy returns a blocker star,
   the alternating star bank contains a source-admissible state with negative
   `Psi_V` change;
2. if PP3hy returns a resource bank, its endpoint rectangle satisfies the paid
   derangement inequality PP3ih, or another protected trade gives negative
   `Psi_V` change.

Then after finitely many trades the source becomes ready.  Applying PP3hq gives
a saturated no-three patch of width

\[
 \Omega(m^{21/40}).
\]

#### Proof

The two conversion assumptions make every non-ready state convertible.  Apply
PP3il, then PP3hq. ∎

The theorem separates termination from conversion.  No additional global
compactness, recurrence, or second-order iteration argument is needed on this
branch.

## 5. Quantitative strengthening

If every conversion decreases the potential by at least `c q`, where `q` is
the extracted star or resource-bank size and `c>0` is fixed, then the number of
steps is at most

\[
 \frac{\Psi_V(S_0)}{cq}.
\]

At the slab scale, the crude bound `Psi_V<=m|V|` is far too large to make this
an efficient algorithmic estimate.  The statement is nevertheless useful for
proof architecture: any uniform strict conversion theorem automatically
terminates.

## 6. Remaining theorem after monotone termination

The prime-patching route no longer needs a separate termination lemma.  Its
single open geometric statement is:

> Every positive-density controller-shadow obstruction supplies either an
> improving alternating-star state or an improving resource-bank trade.

Equivalently, failure of both paid banks must force a still more rigid
rank-one, rank-two, or rank-three collateral core.  The normalized obstruction
counts are already explicit in AN4 and PP3ih.
