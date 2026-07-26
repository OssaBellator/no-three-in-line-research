# Every same-vertex-set host transition normalizes to restriction or contraction

CMR934--CMR949 handle expansions from a nonempty base host.  In a mixed
transition the intersection host can be infeasible.  The same peeling proof still
works: every state of the later host uses at least one edge outside an infeasible
intersection, and deleting all those edges would leave no feasible state.
Therefore an added edge becomes common to the surviving minimum face and
contracts before the batch is exhausted.

This removes the final exceptional expansion case.  Factor an arbitrary
same-vertex-set transition through the intersection host.  Its expansion factor
is now always one of:

- exact same-value rollback to the intersection;
- strict potential improvement;
- exact minimum-core contraction of an added edge.

After rollback, only the restriction factor remains.  Hence a canonical
minimum-anchor history on fixed labelled vertex sets consists of a monotone host
restriction, interrupted only by strict contractions or potential improvement.
It has a coarse polynomial execution bound and needs no independent capacity for
restoration-only activity.

Let `K\subseteq H` be hosts on one finite labelled edge universe `U`, and assume
`\mathcal F(H)` is nonempty.  Put

\[
A=H\setminus K.
\]

## 1. Infeasible bases also give an added-edge transversal

### Theorem CMR950 -- PROVED

Assume `\mathcal F(K)=\varnothing`.  Then every state of `\mathcal F(H)`, and in
particular every state of `\mathcal M(H)`, uses at least one edge of `A`:

\[
\boxed{R\cap A\ne\varnothing.}
\]

### Proof

A state avoiding `A` is contained in `H-A=K` and would be feasible in `K`,
contrary to the hypothesis. ∎

Thus the added batch hits the complete feasible family, not merely its minimum
face.

## 2. Peeling from an infeasible base forces contraction

Order `A=(a_1,...,a_s)` and start at `G_0=H`.  Whenever some current minimum
state omits `a_i`, delete `a_i`; otherwise stop.

### Theorem CMR951 -- PROVED

The procedure preserves `m(H)` at every peel and stops before all edges of `A`
are deleted.  At the stopping step, the current added edge belongs to every state
of the current minimum face and contracts exactly.

The number of peels is at most `|A|-1`.

### Proof

CMR943 preserves the minimum value whenever an avoiding minimum exists.  If all
added edges were peeled, the final host would be `K` and would contain the
surviving minimum state, contradicting `\mathcal F(K)=\varnothing`.  Therefore an
unpeelable edge occurs and lies in the current minimum core.  Apply CMR912. ∎

## 3. Complete normalization of one expansion factor

Let `K\subseteq H` with `\mathcal F(H)` nonempty; `\mathcal F(K)` may be empty.

### Theorem CMR952 -- PROVED

At least one exact expansion response is available.

1. If `\mathcal F(K)` is nonempty and `m(H)=m(K)`, delete all of `H\setminus K`
   and roll back exactly to `K`.
2. If `\mathcal F(K)` is nonempty and `m(H)<m(K)`, peel and contract one added
   edge by CMR942--CMR946.
3. If `\mathcal F(K)` is empty, peel and contract one added edge by CMR950--
   CMR951.

A new global record value may be accepted as strict potential improvement instead
of performing branch 2.

### Proof

These cases exhaust feasibility and the comparison allowed by expansion
monotonicity.  Apply the cited rollback or contraction theorem. ∎

No added batch survives unchanged in the canonical response.

## 4. Arbitrary host-transition normal form

Let `H_0,H_1` be nonempty same-vertex-set hosts and put

\[
K=H_0\cap H_1.
\]

### Theorem CMR953 -- PROVED

The transition `H_0\to H_1` has the following canonical normal form.

1. Restrict from `H_0` to `K`.  This either preserves an old minimum or supplies
   a lost edge of the old canonical minimum.
2. Normalize the expansion from `K` to `H_1` by CMR952.  It rolls back completely,
   contracts an added edge, or gives strict potential improvement.

After a rollback, the normalized final host is exactly `K`; after contraction,
residual state cardinality is strictly smaller.

### Proof

The intersection gives the exact restriction/expansion factorisation.  CMR926
and CMR928 handle the restriction, and CMR952 handles every possible expansion
factor, including an infeasible intersection. ∎

## 5. Fixed-vertex histories become monotone between contractions

Run the canonical response CMR953 repeatedly.  Whenever an expansion rolls back,
retain the intersection host.  Whenever an added edge contracts, pass to the
residual labelled vertex sets.

### Theorem CMR954 -- PROVED

Between two contractions, the normalized hosts form a nested decreasing chain.
Every strict same-vertex-set transition deletes at least one new edge.  If the
current state cardinality is `k` on an edge universe of size `u`, that segment has
at most

\[
\boxed{u-k}
\]

strict transitions.

### Proof

CMR952 removes every surviving added batch.  Thus only restrictions remain.
The final nonempty host contains a size-`k` state whose edges survive the whole
nested segment, leaving at most `u-k` deletable edges. ∎

## 6. Total fixed-vertex execution budget

Suppose the initial equal-cardinality states have size `k_0` and the initial edge
universe has size `u_0`.  Every minimum-core contraction removes at least one
state edge.

### Theorem CMR955 -- PROVED

Before strict potential improvement or structural owner/envelope exit:

1. at most `k_0` contraction events occur;
2. at most `k_0+1` monotone restriction segments occur;
3. the total number `J` of strict same-vertex-set restriction transitions obeys
   the coarse bound
   \[
   \boxed{
   J\le(k_0+1)u_0.
   }
   \]

For a saturated two-layer side-`N` state,

\[
k_0=2N,
\qquad
u_0\le2N^2,
\]

so

\[
\boxed{J\le(2N+1)2N^2.}
\]

### Proof

Each contraction lowers residual cardinality by at least one, so there are at
most `k_0`.  These contractions separate at most `k_0+1` same-vertex-set
segments.  CMR954 bounds each segment by its current edge-universe size, which is
at most `u_0`. ∎

The estimate is intentionally coarse and polynomial.

## 7. Restoration-only capacity is no longer needed locally

### Theorem CMR956 -- PROVED

In the canonical fixed-vertex history, every restored or newly added edge batch
has one of three outcomes:

1. it is rolled back completely at the same minimum value;
2. one of its edges contracts through the minimum core;
3. it yields strict potential improvement.

Therefore genuine restoration incidence may still be recorded, but no local
termination proof needs to upper-bound an indefinitely accumulating
restoration-only token mass.

### Proof

This is CMR952 applied to every expansion factor. ∎

Mixed transitions still expose lost edges in their restriction factors, but the
added edges cannot remain as an independent recurrence class.

## 8. Complete same-vertex-set endpoint

### Corollary CMR957 -- PROVED

Every minimum-anchor execution on fixed labelled vertex sets reaches at least one
of:

1. a finite monotone restriction segment;
2. a lost edge of the old canonical minimum and deletion ancestry;
3. exact minimum-core contraction and strict residual-cardinality descent;
4. exact rollback of all added edges;
5. strict potential improvement;
6. owner, factor, unit-wall, or envelope change.

Thus same-vertex-set host dynamics are well founded after canonical
normalization.  The remaining prime-power frontier is structural vertex-set and
owner descent: transport the induced minimum objective and target-load/reserve
budgets through contractions, wall factors, child factors, and closure-envelope
changes.

### Proof

Combine CMR950--CMR956 with CMR926--CMR949. ∎

No all-`n` theorem is claimed.  Infeasible-base transversality, peeling,
expansion normalization, mixed-transition factorisation, monotone segments,
contraction counts, and polynomial execution bounds are checked in
[`scripts/verify_prime_power_complete_host_transition_normalization.py`](../scripts/verify_prime_power_complete_host_transition_normalization.py).
