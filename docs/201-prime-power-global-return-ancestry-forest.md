# Genuinely restored edges form a forward deletion-ancestry forest

CMR770--CMR776 reduce recurrent physical targets to matching-preserving deletion
or strict double contraction. The remaining return budget must not charge the
same physical restoration once for every local owner label. This chapter uses
absolute parent coordinates and layer labels. Owner relabelling is silent;
only an actual unavailable-to-available transition of one matching-host edge is
a restoration.

The central observation is temporal. When a previously deleted edge returns,
its stored avoiding matching either still survives, or some edge of that stored
matching has been lost later. A structural missing witness therefore points
strictly forward in loss time. Repeated redeletion and structural blocking form
an acyclic out-degree-one ancestry forest. A long branch either uses many
physical labels or repeats one exact labelled edge through many distinct absence
generations, which pays genuine restoration and exact full-token incidence.

Fix an ambient prime-power parent of side

\[
N=p^h.
\]

A labelled physical edge is a pair `(ell,e)`, where `ell` is one of the two
permutation layers and `e` is one absolute grid cell. The labelled universe has
size at most

\[
\boxed{2N^2.}
\]

A **structural deletion generation** `alpha` begins when a labelled edge `e` is
removed from a matchable layer host by a matching-preserving deletion. Store a
perfect matching

\[
M_alpha\in\operatorname{PM}(H_alpha-e)
\]

at that time. The generation ends at the first later genuine restoration of
`e`, contraction of one endpoint, or owner transition which changes the labelled
vertex set.

## 1. Absolute restorations are owner-independent

### Theorem CMR777 -- PROVED

Whether one labelled physical edge is present in the current matching host is an
absolute binary fact. Changing only the envelope, routing, factor, wall, or
certificate owner label does not create a loss or restoration.

Consequently every genuine restoration belongs to exactly one maximal physical
absence run, independently of how many local owner certificates cite it.

### Proof

The edge is identified by its absolute source, target, and layer. An owner label
is bookkeeping attached to the same physical host state. If the host edge set is
unchanged, its indicator is unchanged. A genuine restoration is precisely a
zero-to-one transition of that indicator and therefore ends one unique maximal
zero interval. ∎

This is the global version of the cell--absence-run correction in CMR766.

## 2. Returned deletion generations have four exact responses

Let `alpha` be a structural deletion generation of `e`, and suppose `e` is later
restored before contraction or owner change. Let `H` be the later host on the
same labelled vertex sets.

### Theorem CMR778 -- PROVED

At least one of the following occurs.

1. **Immediate redeletion.** `M_alpha` survives in `H`; then `e` is nonessential
   and may be deleted again, starting a later generation of the same labelled
   edge.
2. **Paid transient loss.** The first edge `f` of `M_alpha` absent from `H` was
   lost through a selected-state or routing transition. That transition has the
   entering/leaving support and exact token payment of CMR416--CMR421 or
   CMR671--CMR676.
3. **Forward structural witness.** The first absent edge `f` of `M_alpha` was
   removed by a later matching-preserving structural deletion. The current
   absence run of `f` is a later structural deletion generation.
4. **Structural exit.** An endpoint contracts, or the factor, routing, wall, or
   envelope owner changes before a same-vertex-set response is completed.

If the returned edge `e` is essential in `H`, branch 1 is impossible and it may
be contracted exactly as in CMR725.

### Proof

If `M_alpha` is contained in `H`, apply CMR720. Otherwise choose the first edge
`f` of `M_alpha` missing from `H`, as in CMR721. At the deletion time of `e`, all
edges of `M_alpha` were present. Trace the first later transition at which `f`
ceased to belong to the current host. It is either a paid selected-state or
routing transition, a matching-preserving structural deletion, or an endpoint/
owner transition. These are branches 2--4. Essential return excludes the
surviving avoiding matching and contracts by CMR725. ∎

No absence is attributed simultaneously to a structural deletion and a routing
or selected-state transition.

## 3. Forward ancestry links strictly increase loss time

In branch 1 of CMR778, link `alpha` to the new redeletion generation of `e`. In
branch 3, link `alpha` to the structural deletion generation of the canonical
missing witness `f`. Do not create a link in the paid or structural-exit branches.

### Theorem CMR779 -- PROVED

Every ancestry link

\[
\alpha\longrightarrow\beta
\]

strictly increases generation start time:

\[
\boxed{s(\beta)>s(\alpha).}
\]

Hence the generation-ancestry graph is acyclic. Every node has out-degree at
most one.

### Proof

For redeletion, the new generation starts at the later restoration time of the
old generation. For a structural witness, its edge belonged to `M_alpha` and was
therefore present when `alpha` started; its structural loss occurs strictly
later. The canonical response selects at most one successor. Strictly increasing
time forbids directed cycles. ∎

Physical edge labels may repeat along a directed path, but deletion generations
cannot.

## 4. Long ancestry paths force one recurrent physical edge

### Theorem CMR780 -- PROVED

Let a directed ancestry path contain `L` deletion generations. For every integer
`mu>=2`, at least one of the following holds.

1. One exact labelled physical edge occurs in at least `mu` distinct generations
   on the path.
2. 
   \[
   \boxed{L\le(\mu-1)2N^2.}
   \]

If one labelled edge occurs in `mu` distinct generations, it undergoes at least
`mu-1` genuine restorations between those generations. Their exact labelled
nonroot full-token incidence is at least

\[
\boxed{(\mu-1)(p+1)(h-1).}
\]

### Proof

There are at most `2N^2` labelled physical edges. Apply the pigeonhole principle
to the path labels. Distinct generations of the same edge have disjoint absence
runs; after the first generation, every later one requires a restoration of the
preceding absence run. Apply CMR413 with multiplicity. ∎

Thus owner changes cannot manufacture repeated-edge payment without a physical
return.

## 5. Fresh unpaid roots have finite owner-edge stock

Fix a recurrence threshold `lambda>=2` for routing changes. For one envelope
of side `q`, let `mathcal E(q,lambda)` be the owner-edge stock of CMR694 and put

\[
F(q)=\frac{q(q+1)(2q+1)}6,
\]

the unit-wall tree owner-edge stock of CMR743. For a closure-envelope chain
`E_0,...,E_s`, define

\[
\mathfrak D(\lambda)
=
\sum_{i=0}^{s}
\bigl(\mathcal E(|E_i|,\lambda)+F(|E_i|)\bigr).
\]

### Theorem CMR781 -- PROVED

Before one physical routing-support edge recurs `lambda` times at one owner,
the number of fresh unpaid structural-deletion roots in the complete branch is
at most

\[
\boxed{\mathfrak D(\lambda).}
\]

Since `s<=h` and `|E_i|<=N`,

\[
\boxed{
\mathfrak D(\lambda)
\le
(h+1)\bigl(\mathcal E(N,\lambda)+F(N)\bigr).
}
\]

A loss caused by selected-state or routing churn is not an unpaid root; it is
already a paid endpoint of CMR778.

### Proof

At a fixed owner-edge pair, the canonical monotone host discipline charges the
first matching-preserving deletion once. CMR694 bounds all such owner-edge pairs
on a strict descent path unless routing recurrence has already occurred.
CMR743 bounds all factor edges over the complete unit-wall tree. Sum over the at
most `h+1` envelope epochs. Both stock functions are nondecreasing in the side,
giving the final bound. ∎

Returned redeletions are descendants of their earlier generation and are not
new roots.

## 6. Forest-wide bound without double counting

### Theorem CMR782 -- PROVED

Fix `lambda,mu>=2`. Suppose the branch has

1. no physical routing-support edge recurring `lambda` times at one owner;
2. no paid transient-loss endpoint from CMR778;
3. no contraction or owner/envelope exit; and
4. no labelled physical edge occurring in `mu` structural deletion generations.

Then the total number `K` of structural deletion generations satisfies

\[
\boxed{
K
\le
\mathfrak D(\lambda)(\mu-1)2N^2.
}
\]

### Proof

CMR779 gives a finite acyclic graph of out-degree at most one. Every node lies on
a directed path beginning at some indegree-zero root. There are at most
`mathfrak D(lambda)` roots by CMR781. CMR780 bounds every root path by
`(mu-1)2N^2`. The union of the root paths contains every node, so summing their
lengths gives the displayed upper bound; mergers only reduce the union size. ∎

This is an owner-consistent bound: one physical restoration is not multiplied by
the number of certificates or nested factors which observe it.

## 7. Repeated labelled edges enter deletion or contraction again

### Theorem CMR783 -- PROVED

If the recurrent-edge branch of CMR780 occurs, then at every later selected
target occurrence containing that labelled edge, the established local response
is available:

1. a recurrent labelled target pair stabilises after at most six types by CMR770--
   CMR771;
2. a nonessential pair edge deletes matching-preservingly by CMR772;
3. two essential pair edges contract and lower side by two by CMR773;
4. a singly essential returned edge contracts and leaves rank at most two by
   CMR725;
5. every noncontracting recurrence pays a new physical absence run and CMR413
   token incidence.

### Proof

Apply CMR770--CMR776 when the recurrence is carried by a physical target. Apply
CMR720--CMR725 to an individually returned deleted edge. Distinct structural
generations are distinct absence runs, so every noncontracting continuation
requires the restoration counted in CMR780. ∎

The theorem does not assert that every recurrent routing or packet edge is itself
part of a current target; those roles retain their existing paid ledgers.

## 8. Branch-wide returned-edge endpoint

### Corollary CMR784 -- PROVED

Every prime-power target-driven branch reaches at least one of the following.

1. Finite fresh structural-deletion stock and the forest bound CMR782.
2. Paid selected-state or routing churn with exact entering/leaving support.
3. One labelled physical edge with many genuine restoration runs and exact
   full-token incidence.
4. Matching-preserving redeletion, stored-avoidance ancestry, or recurrent
   labelled-pair deletion.
5. Essential contraction, double contraction, strict child descent, or unit-wall
   factorisation.
6. A finite owner transition or one of at most `h` strict envelope expansions.
7. Strict target-potential improvement.

Thus branch-wide owner relabelling is no longer a source of duplicate return
charges. The unresolved prime-power step is to turn the genuinely accumulated
full-token incidence in branch 3 into an unconditional return-capacity bound, or
else into inherited target-load decrease, reserve depletion, or global potential
improvement.

### Proof

Combine CMR777--CMR783 with the local target, returned-edge, routing, wall, factor,
and envelope endpoints CMR671--CMR776. ∎

No all-`n` theorem is claimed. Absolute owner-independent restoration, forward
loss-time ancestry, path recurrence, root-stock arithmetic, and forest bounds are
checked in
[`scripts/verify_prime_power_global_return_ancestry_forest.py`](../scripts/verify_prime_power_global_return_ancestry_forest.py).
