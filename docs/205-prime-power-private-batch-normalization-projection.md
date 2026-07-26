# Private-batch normalization erases pure reopening cycles

CMR800--CMR806 show that a surviving anchor can re-delete every restored private
batch at once. The operation is canonical: delete the complete private union
whenever it is present. This defines an idempotent normalization projection on
later hosts. A reset which changes only private edges vanishes under the
projection. A nonerasable normalized transition must change at least one edge
outside the already-paid private stock.

Fix a stored anchor `S` and its private deleted union

\[
D=A_1\sqcup\cdots\sqcup A_B,
\qquad
D\cap S=\varnothing.
\]

For every same-vertex-set host `H` containing the anchor, define

\[
\mathcal N_D(H)=H-(D\cap E(H)).
\]

Equivalently, `mathcal N_D(H)=H-D` on the labelled edge universe.

## 1. Canonical anchor-preserving projection

### Theorem CMR807 -- PROVED

For every host `H` containing `S`,

1. `S` is feasible in `\mathcal N_D(H)`;
2. no edge of `D` belongs to `\mathcal N_D(H)`;
3.
   \[
   \boxed{
   \mathcal N_D(\mathcal N_D(H))
   =
   \mathcal N_D(H).
   }
   \]

### Proof

The anchor is disjoint from `D`, so removing `D` preserves it. The second
assertion is definitional. Removing the same set a second time changes nothing. ∎

Thus every later host with the same surviving anchor has one canonical
private-closed representative.

## 2. Pure private reopening normalizes to the same host

### Theorem CMR808 -- PROVED

Let `H` contain `S`, and let `R\subseteq D` be any set of restored private edges.
Then

\[
\boxed{
\mathcal N_D(H\cup R)
=
\mathcal N_D(H).
}
\]

The same identity holds if a reset both restores and deletes edges of `D` but
changes no edge outside `D`.

### Proof

Both hosts have the same edge set outside `D`, and normalization removes every
edge inside `D`. ∎

The number and arrangement of reopened private batches are irrelevant after
normalization.

## 3. Exact pure-reopening cycle erasure

### Theorem CMR809 -- PROVED

Suppose a later reset begins at normalized anchor state

\[
(S,\mathcal N_D(H)),
\]

changes only availability of edges in `D`, and is followed by CMR800 bulk
redeletion. The final selected state and normalized host are exactly the initial
ones. The intervening reset/redeletion segment is cycle-erasable.

### Proof

The selected state remains or returns to the same stored anchor `S`. CMR808 gives
the same normalized host before and after the segment. Every later operation
therefore sees the identical selected state and available normalized host, so the
segment can be removed exactly as in CMR410. ∎

The physical restorations inside the erased segment retain their token charge;
cycle erasure says they cannot create new structural progress.

## 4. Nonerasable normalized changes use nonprivate edges

### Theorem CMR810 -- PROVED

For two anchor-containing hosts `H,H'`, if

\[
\mathcal N_D(H)\ne\mathcal N_D(H'),
\]

then

\[
\boxed{
(E(H)\triangle E(H'))\setminus D
\ne\varnothing.
}
\]

Thus every nontrivial transition between normalized hosts changes at least one
labelled physical edge outside the complete private union.

### Proof

Normalization makes the two hosts identical on `D` by deleting it from both. If
the normalized edge sets differ, their difference must lie outside `D`. ∎

This edge is a new context witness, not another citation of a reopened private
batch.

## 5. Finite normalized context stock or exact recurrence

Consider `J` nontrivial transitions between consecutive normalized hosts on one
fixed labelled board. Choose the first nonprivate edge in each symmetric
difference as the canonical context witness.

### Theorem CMR811 -- PROVED

For every integer `lambda>=2`, at least one of the following holds.

1. One exact labelled nonprivate edge is a context witness in at least `lambda`
   normalized transitions.
2.
   \[
   \boxed{J\le(\lambda-1)2N^2.}
   \]

### Proof

CMR810 supplies one witness per nontrivial normalized transition. The absolute
labelled edge universe has size at most `2N^2`; deleting `D` only lowers the
available witness stock. Apply the pigeonhole principle. ∎

A recurrent witness enters the selected-state, routing, loss-time ancestry, or
physical restoration ledger according to the transition which changed it.

## 6. Normalized state change or paid restoration

### Theorem CMR812 -- PROVED

Every reset followed by private-batch normalization reaches at least one of:

1. the identical normalized host and anchor state, so the segment is erasable by
   CMR809;
2. a nonprivate context-edge change supplied by CMR810;
3. loss of one stored anchor edge, supplied by CMR801;
4. contraction or owner/envelope change;
5. genuine restoration of private edges, carrying the CMR797 token payment even
   when the normalized segment is erased.

### Proof

If the anchor survives, apply the projection. Equal normalized hosts give branch
1 and unequal hosts give branch 2. If the anchor fails use CMR801. Structural
exits give branch 4. Every reopened private edge is still a physical restoration
and is charged before normalization. ∎

Normalization removes duplicate structural credit, not genuine edge incidence.

## 7. Private-normalization endpoint

### Corollary CMR813 -- PROVED

After one anchor pass, repeated owner resets cannot obtain unbounded progress by
restoring and re-deleting the same private batches. Every continuation reaches
at least one of:

1. exact cycle erasure after canonical normalization;
2. one new or recurrent nonprivate context edge;
3. one missing anchor edge and forward deletion ancestry;
4. genuine private-edge restoration with exact token payment;
5. permanent private deletion, pair contraction, strict owner descent, or
   envelope expansion;
6. strict target-potential improvement.

Thus the remaining return frontier is supported on context changes outside the
already-normalized private deletion union.

### Proof

Combine CMR807--CMR812 with CMR793--CMR806 and the global return forest
CMR777--CMR784. ∎

No all-`n` theorem is claimed. Projection identities, pure-reopening erasure,
nonprivate witness extraction, and recurrence arithmetic are checked in
[`scripts/verify_prime_power_private_batch_normalization.py`](../scripts/verify_prime_power_private_batch_normalization.py).
