# Canonical maximum-compatible selected subbanks

**Branch:** `research/alternating-core-chain`

AC3mq and AC3nr leave arbitrary selected protected subbanks and transition-state
families as genuine set-valued outer data.  Some choices are discretionary, but a
large class of installed banks is specified by an exact candidate set and an exact
pairwise incompatibility graph.  In that setting a declared canonical
maximum-compatible policy reconstructs the selected subbank.  The selected subset
is then an output of the candidate and conflict generators rather than an
independent outer-profile field.

This note concerns pairwise compatibility only.  A higher-arity legality system is
not replaced by its two-section unless a separate theorem proves that pairwise
compatibility is sufficient.  Likewise, membership in a compatible subbank is not
payment; every selected state still needs the AC3v envelope and AC3ke--AC3kf owner
status.

## Candidate-conflict system

Fix a finite totally ordered candidate universe

\[
V=\{v_1,\ldots,v_m\}.
\]

Let `A subseteq V` be the exact currently available candidate set and let

\[
G\subseteq \binom V2
\]

be the exact undirected incompatibility graph.  A legal selected subbank is an
independent set in `G[A]`.

Encode a selected set by its zero-one membership word in the fixed candidate
order.  First maximize cardinality and then choose the lexicographically least
membership word among all maximum independent sets.

## AC3ns -- canonical maximum-compatible subbank -- PROVED

There is one unique canonical selected subbank

\[
\boxed{I^*(A,G)}
\]

obtained as the lexicographically least maximum independent set of `G[A]`.
Consequently:

1. the exact candidate set, incompatibility graph and fixed order determine one
   selected subbank;
2. if any compatible subbank has size at least `q`, then `|I^*|>=q`;
3. `I^*` has maximum possible compatible cardinality;
4. storing another arbitrary selected subset duplicates derived data when this
   canonical policy is declared.

### Proof

The empty set is independent, so the finite feasible family is nonempty.  Maximum
cardinality is defined, and the finite family of maximum independent sets has one
lexicographically least membership word.  Maximum cardinality preserves every
feasible quota. QED.

No computational claim is made.  The theorem is a mathematical reconstruction
interface; finding a maximum independent set may be expensive for an arbitrary
input graph.

## AC3nt -- atomic rank sensitivity and reset alphabet -- PROVED

Write

\[
\alpha(A,G)=|I^*(A,G)|.
\]

Each of the following atomic updates changes `alpha` by at most one:

1. adding or deleting one available candidate;
2. adding or deleting one incompatibility edge.

Thus

\[
\boxed{|\alpha-\alpha'|\le1.}
\]

The exact canonical set can nevertheless rotate on many candidates after one
atomic update.  No constant bound is claimed for
`|I^* triangle I^{*prime}|`.

For a fixed candidate universe, every strict atomic input change has one least
decoration of the form

\[
(v,+),\ (v,-),\ (\{u,v\},+),\ (\{u,v\},-).
\]

A safe reset alphabet therefore has size

\[
\boxed{
R_{\rm sub}
\le
2m+2\binom m2
=
m(m+1).
}
\]

A weighted family of atomic selected-subbank resets of total weight `W` contains
one exact input-atom/direction class of weight at least

\[
\boxed{W/R_{\rm sub}.}
\]

### Proof

Adding one available vertex can enlarge an independent set by at most that one
vertex; deleting one available vertex removes at most one member from an old
optimum.  Adding one conflict edge can invalidate an old optimum only when it
contains both endpoints, in which case deleting either endpoint leaves an
independent set of size `alpha-1`.  Deleting one conflict edge can create a new
optimum containing both endpoints, but removing either endpoint gives an old-graph
independent set of size at least `alpha'-1`.  These arguments give the rank bound.
Lexicographic tie-breaking may choose a distant optimum after the update.  The
alphabet count and weighted pigeonhole statement are immediate. QED.

A batch input change must retain its exact changed-atom set or be decomposed into
atomic changes before AC3nt is invoked.

## AC3nu -- canonical blocker map and conflict-overload alternative -- PROVED

Put

\[
I=I^*(A,G),
\qquad
\alpha=|I|.
\]

Every candidate in `A minus I` has a neighbour in `I`, because a maximum
independent set is maximal.  Assign each `v in A minus I` to its least neighbour
in `I`; call this canonical blocker `b(v)`.

If `A` is nonempty, then `alpha>=1`, and one selected candidate blocks at least

\[
\boxed{
\left\lceil\frac{|A|-\alpha}{\alpha}\right\rceil
}
\]

unselected candidates.  More generally, for nonnegative candidate weights
`w(v)`, one selected candidate receives canonical blocked weight at least

\[
\boxed{
\frac{\sum_{v\in A\setminus I}w(v)}{\alpha}.
}
\]

If every selected candidate has at most `Delta` neighbours in `A minus I`, then

\[
\boxed{
|A|\le(\Delta+1)\alpha,
\qquad
\alpha\ge\frac{|A|}{\Delta+1}.
}
\]

### Proof

If an unselected available vertex had no neighbour in `I`, adjoining it would
contradict maximality.  The canonical blocker fibres partition `A minus I`; the
ordinary and weighted pigeonhole bounds follow.  Under the degree cap, at most
`Delta alpha` unselected vertices are assigned to the `alpha` selected blockers,
which gives the final inequalities. QED.

The heavy blocker is a structural conflict concentration, not payment.  Its
physical conflict incidences must enter AC2d, the pivot router, GC4, or another
proved paid-overload interface.

## AC3nv -- persistent selected-candidate consumption has a linear potential -- PROVED

Fix the candidate universe and incompatibility graph during one selection epoch.
Let the spent masks be monotone,

\[
F_0\subseteq F_1\subseteq\cdots\subseteq V,
\]

and set `A_i=A_0 minus F_i`.  Recompute the canonical subbank
`I_i^*=I^*(A_i,G)` at every step.  Suppose every accepted consuming transition
spends at least one currently selected candidate:

\[
(F_{i+1}\setminus F_i)\cap I_i^*\ne\varnothing.
\]

Then the number of accepted consuming transitions is at most

\[
\boxed{|A_0\setminus F_0|\le m.}
\]

The potential is

\[
\boxed{\Xi_{\rm sub}=|F|.}
\]

It strictly increases on every accepted transition even when the recomputed
maximum compatible subbank rotates across many unspent candidates.

### Proof

Every accepted transition adds at least one previously unspent candidate to the
persistent mask.  There are only `|A_0 minus F_0|` such candidates.  Recomputing
the canonical optimum cannot restore a spent candidate or decrease the potential.
QED.

If a selected candidate is only a fixed witness and is not consumed, the step must
obtain payment or descent elsewhere.  If the spent mask shrinks, the history has
left the persistent selection epoch and the reset must enter the outer router.

## AC3nw -- corrected selected-subbank frontier -- PROVED UNDER THE PAIRWISE COMPATIBILITY CONTRACT

Assume an installed transition family declares:

- its exact ordered candidate universe and available set;
- a scope-complete pairwise incompatibility graph;
- the canonical maximum-compatible policy AC3ns;
- complete AC3v state envelopes for every selected executable state;
- exact payment, owner and consumption records.

Then:

1. the selected compatible subbank is derived from `(A,G)` and is removed as an
   independent AC3ka profile coordinate;
2. every atomic candidate or conflict change has AC3nt's finite decoration and
   changes the optimum cardinality by at most one;
3. a small maximum subbank returns AC3nu's canonical conflict concentration;
4. persistent consuming selections terminate under AC3nv's linear ticket budget;
5. a selected-subbank change with unchanged `(A,G)` is impossible;
6. every selected-subbank macro cycle is inherited from a candidate-availability
   or conflict-edge reverse atom and therefore enters AC3nn--AC3nr.

The following remain live:

- noncanonical or discretionary selection policies;
- higher-arity incompatibility not captured by the exact graph;
- generators of the candidate set or conflict graph;
- conflict or availability atoms which oscillate without payment or tickets;
- common owners whose payment must be counted once across alternatives;
- selected compatible states which lack complete envelopes or executable repairs.

### Proof

AC3ns gives deterministic reconstruction.  AC3nt localizes every atomic input
change without asserting a false bound on the selected-set symmetric difference.
AC3nu gives the exact failure concentration, and AC3nv gives the persistent
consumption potential.  Since `I^*` is a deterministic function of `(A,G)`, any
cycle changing it must change and later reverse an input atom; AC3nn--AC3nr then
apply.  The exclusions are not determined by the pairwise canonical inputs or
lack one of the stated legality/payment contracts. QED.

## Consequence

A broad class of selected-subbank recurrence is no longer an exponential
set-state frontier.  Under the canonical pairwise policy it is reduced to exact
candidate and conflict generators, a polynomial atomic reset alphabet, one
canonical conflict-overload witness and a finite selected-candidate ticket stock.
The remaining cycle theorem must discharge the actual availability or conflict
reverse atom, not an arbitrary chosen subset.

## Finite check

`scripts/verify_ac_canonical_compatible_subbank.py` exhausts all graphs on at most
five candidates, all availability masks, every one-vertex and one-edge update,
canonical blocker fibres and persistent selected-candidate consumption steps.  It
also records examples where one atomic update rotates several selected candidates
while the optimum cardinality changes by at most one.
