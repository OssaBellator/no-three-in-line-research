# Anchor entering batches are private deletion codes

CMR785--CMR792 replace nonimproving fixed-owner target churn by disjoint entering-
batch deletions. This chapter records what a later owner reset must pay to undo
that progress. Each rejected candidate has a private batch of labelled edges.
Because later candidates are feasible only after all earlier batches were
deleted, the batches are pairwise disjoint. Reopening `k` rejected candidates
therefore restores at least `k` distinct labelled physical edges.

Fix one anchor-state pass on a board of side `n`. Let

\[
A_1,A_2,\ldots,A_B
\]

be the entering batches deleted by CMR786, in chronological order. Let the
ambient prime-power parent have side `N=p^h`; the local labelled edge universe is
contained in the absolute universe of size `2N^2`.

## 1. Rejected entering batches are pairwise disjoint

### Theorem CMR793 -- PROVED

For `i\ne j`,

\[
\boxed{A_i\cap A_j=\varnothing.}
\]

Every batch satisfies `|A_i|>=2`, and

\[
\boxed{
\sum_{i=1}^{B}|A_i|
\le
2n^2-2n.
}
\]

### Proof

When `A_j` is chosen, its candidate state is feasible under the mask containing
all earlier batches. Hence it contains no edge of any earlier `A_i`. The batch is
the candidate's entering set, so the batches are disjoint. CMR785 gives the
lower bound two, and CMR788 gives the total nonanchor edge bound. ∎

Thus every rejected candidate receives a private nonempty deletion code.

## 2. A batch remains closed until one private edge is restored

Call batch `A_i` **closed** while none of its edges belongs to the current
matching host.

### Theorem CMR794 -- PROVED

As long as `A_i` remains closed, the rejected candidate which created it cannot
reappear as a feasible selected state. More generally, every selected state
containing an edge of `A_i` remains infeasible.

If such a state becomes feasible later, at least one edge of `A_i` has undergone
a genuine physical restoration.

### Proof

The rejected candidate contains all edges of `A_i`. A current state using any
batch edge is excluded while that edge remains absent from the host. Feasibility
at a later time therefore requires at least one zero-to-one host transition for
a batch edge. CMR777 makes this restoration owner-independent. ∎

Owner relabelling without a physical host change does not reopen a batch.

## 3. Reopening many batches restores many distinct edges

Let one later transition or reset restore a labelled edge set `R`. Say that it
reopens batch `A_i` when

\[
R\cap A_i\ne\varnothing.
\]

### Theorem CMR795 -- PROVED

If one reset reopens `k` anchor batches, then

\[
\boxed{|R|\ge k.}
\]

There is a canonical matching

\[
\{(i,e_i):e_i\in R\cap A_i\}
\]

between the reopened batch indices and `k` distinct restored labelled edges.

### Proof

Choose the first edge of `R\cap A_i` in each batch order. CMR793 makes the batches
pairwise disjoint, so the chosen edges are distinct. ∎

The theorem counts a physical restoration once even if several later
certificates cite the reopened candidate.

## 4. Cumulative reopening is finite or one edge recurs

Consider any sequence of later resets. Count one incidence `(j,i)` whenever reset
`j` reopens batch `A_i`, and let `K` be the total number of such incidences.

### Theorem CMR796 -- PROVED

For every integer `lambda>=2`, at least one of the following holds.

1. One exact labelled physical edge is restored in at least `lambda` batch-
   reopening incidences.
2.
   \[
   \boxed{K\le(\lambda-1)2N^2.}
   \]

If every reset reopens at least `q>=1` batches and there are `J` such resets,
then either the recurrent-edge branch occurs or

\[
\boxed{
J\le
\left\lfloor\frac{(\lambda-1)2N^2}{q}\right\rfloor.
}
\]

### Proof

Use CMR795 to assign every batch-reopening incidence to one restored edge in its
batch. Within one reset the assigned edges are distinct. Over the full history,
there are at most `2N^2` labelled physical edges. If none receives `lambda`
incidences, each receives at most `lambda-1`; double counting gives the first
bound and division by `q` gives the second. ∎

One edge may reopen its own batch in several distinct absence runs; those are
genuine repeated restorations and are not collapsed.

## 5. Exact full-token payment for restored private codes

### Theorem CMR797 -- PROVED

Let resets restore edge sets `R_1,...,R_m`, and let `K` be their total number of
reopened anchor batches. Then

\[
\boxed{
\sum_{j=1}^{m}|R_j|
\ge K.
}
\]

Their exact labelled nonroot full-token incidence satisfies

\[
\boxed{
\mathcal I(R_1,\ldots,R_m)
=
(p+1)(h-1)
\sum_{j=1}^{m}|R_j|
\ge
K(p+1)(h-1).
}
\]

### Proof

Sum CMR795 over the resets and apply the exact incidence identity CMR413. ∎

This payment is unconditional and does not use the earlier one-pass prefix
hypothesis.

## 6. Permanent depletion versus paid reopening

### Theorem CMR798 -- PROVED

For every anchor batch `A_i`, exactly one of the following occurs along a fixed
physical owner lineage.

1. No edge of `A_i` is ever restored; the batch is permanent deleted-mask
   progress and its rejected candidate never returns.
2. The batch is reopened, and its first reopening pays one genuine restored edge
   from `A_i`.
3. An endpoint of every surviving batch edge is contracted or leaves the factor;
   this is strict side descent rather than restoration.
4. The envelope changes; the batch enters the finite envelope-owner transition
   ledger, while any physical edge actually restored is still counted by
   CMR777 and CMR797.

### Proof

If the physical labelled vertices persist, a candidate using `A_i` can return
only after a batch edge returns by CMR794. If no such return occurs, the batch
remains closed. Contraction removes vertices, and envelope change is the only
remaining owner-lineage exit. CMR777 prevents either relabelling case from being
miscounted as a physical restoration. ∎

## 7. Anchor-batch return endpoint

### Corollary CMR799 -- PROVED

Every history generated by the fixed-owner anchor scheduler reaches at least one
of:

1. permanent depletion by pairwise disjoint entering batches;
2. a strict potential improvement;
3. a forced labelled target pair and exact double contraction;
4. finitely many batch-reopening incidences;
5. one recurrent labelled physical edge;
6. exact full-token incidence at least one unit per reopened batch;
7. returned-edge ancestry, contraction, owner change, or envelope expansion.

Consequently a rejected nonimproving state is never paid for twice for free. Its
private entering batch either remains deleted, disappears under strict descent,
or returns through explicit physical-edge and token payment.

### Proof

Combine CMR793--CMR798 with CMR792 and the global ancestry alternatives
CMR777--CMR784. ∎

No all-`n` theorem is claimed. Batch disjointness, private-code reopening,
incidence bounds, and token arithmetic are checked in
[`scripts/verify_prime_power_anchor_batch_restoration_ledger.py`](../scripts/verify_prime_power_anchor_batch_restoration_ledger.py).
