# Status and honesty ledger

**Last updated:** 26 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open. This repository does **not** contain a complete proof.

The collision-free theorem ledger is split between

- `proofs/composite-modulus-theorem-index-live.md` through CMR747; and
- `proofs/composite-modulus-theorem-index-live-continuation.md` from CMR748 onward.

## Closed prime-power components

### Geometry, closure, and matching products

- The indexed completed-reciprocal, prefix, quotient, carry, Hall-wall,
  line-clean, joint-parent, and harmonic-packet results remain proved at their
  stated scales.
- Closure envelopes form at most `h+1` nested epochs with at most `h` strict
  expansions.
- Protected/free, child-routing, essential-core, exchange-SCC, and unit-wall
  matching products are exact.
- Every matching-relevant edge has unique ownership in those products; a nonfixed
  edge follows one strict side-descending factor lineage.

### Physical restoration and target recurrence

- Physical restoration is defined in absolute parent coordinates and is not
  duplicated by envelope, routing, factor, wall, or certificate relabelling.
- Structural deletion generations form a forward acyclic out-degree-one ancestry
  forest. Long paths force repeated genuine absence runs of one labelled edge.
- A recurrent target edge deletes while nonessential. Essential return produces
  a deficiency-one Hall wall and an exact lower-side product.
- A recurrent physical target has at most six labelled same-layer pair types. A
  recurrent type deletes one nonessential pair edge or contracts two essential
  pair edges.
- Historical protected-line targets are neutralised through stored labelled pairs,
  and reuse is counted by cell--absence-run slots rather than raw episodes.

### Aggressive anchor normalization

- At one fixed owner, an anchor-preserving aggressive branch rejects a
  nonimproving state by deleting its complete anchor-entering set.
- Every such batch has at least two labelled edges; batches are pairwise disjoint
  and total at most `n(n-1)` on that branch.
- Reopened private batches restore distinct physical edges and carry exact token
  payment. A surviving stored anchor re-closes all restored private edges at once.
- Private normalization is idempotent. Pure reopening normalizes to the identical
  state and is cycle-erasable.
- A newly enabled nonimproving state uses a newly added edge, which is immediately
  absorbed into the private union.

These statements are rigorous **on the surviving aggressive branch**.

## Critical completeness correction

Deleting a complete entering batch may remove other untested states, including an
improving state. Therefore the aggressive branch is not by itself a complete
existence search.

For an equal-cardinality state family and rejected state `Q`, CMR830--CMR837 give

\[
\mathcal F\setminus\{Q\}
=
\bigcup_{f\in Q,\,\mathcal F-f\ne\varnothing}(\mathcal F-f).
\]

Every alternative state survives in at least one viable single-edge child, and
every root-to-leaf path has at most `2n^2-2n` deletions. Branch-local forcedness
is never promoted to the original family without this union.

With

\[
E_*(\mathcal F)=\bigcap_{R\in\mathcal F}R,
\]

CMR838--CMR845 prove

\[
\mathcal F-f\ne\varnothing
\iff
f\notin E_*(\mathcal F).
\]

After complete-core contraction the residual family has empty core, and

\[
\boxed{
\text{contracted core rank}+\text{viable child count}=2n.
}
\]

The zero-child case is a singleton, the one-child case is deterministic, and
total contracted core rank along a branch is at most `2n`.

## Distinguishing rank and exchange SCCs

For a rejected state `Q`, define its distinguishing rank as the minimum number of
its labelled edges which no alternative state contains simultaneously.

- This rank is the transversal number of the difference-support hypergraph and
  equals the minimum number of single-edge children needed to exclude only `Q`.
- It is additive in exact Cartesian products.
- For a full one-layer perfect-matching family, it equals the directed feedback-
  vertex number of the exchange graph relative to `Q`.
- Usable matching edges are exactly the exchange edges inside SCCs. The matching
  family factors exactly over SCC blocks, and distinguishing rank adds over the
  cyclic blocks.
- Large local rank means every low-rank prescription of the base matching occurs
  in another local matching.

This localizes one-layer width exactly but does not yet bound the coupled
layer-disjoint joint-state width.

## Constant-arity geometric completeness

Every nonimproving state which destroys positive designated target load creates a
genuinely new physical collinear triple. Retain its exact three labelled edges
`C`. Then

\[
\mathcal F
=
\left(\bigcup_{f\in C}(\mathcal F-f)\right)
\cup
\mathcal F_C.
\]

Thus the complete scheduler response has at most four branches:

1. up to three single-edge deletion children covering every state which omits one
   edge of `C`;
2. one conditioned branch where `C` occurs in every surviving state and enters
   forced-certificate handoff or exact contraction.

Every state of the original family survives in at least one branch. Conditioning
on `C` lowers state cardinality by three under contraction and decreases
possible distinguishing rank by at most three.

## Corrections retained

- Naive sequential two-layer rematching may reoccupy an old first-layer cell.
- Historical target lines are not simultaneous target families.
- One edge return may serve several neutralisations in one continuous absence run.
- Removing one essential edge produces Hall deficiency exactly one.
- Routing compensation and essentiality escape may be distributed across several
  alternating components.
- One physical restoration is counted once globally even when several nested
  owners observe it.
- Aggressive batch deletion is branch-local; completeness uses viable single-edge
  unions or the rank-three prescription split.

## Current open frontier

1. **Constant-arity tree compression.** Bound or compress the polynomial-depth
   tree generated by the three deletion children plus one forced-triple branch,
   or establish target-load/potential monotonicity across its side branches.
2. **Forced-triple and fixed-edge closure.** Convert repeated conditioned
   forced-triple branches and fixed-owner physical-edge restoration into target-
   load decrease, reserve exhaustion, or strict global potential improvement.
3. **Prime-field and low-height transfer.** Rebuild the owner-labelled endpoint
   for prime fields and remaining thin quotient/carry regimes.
4. **Arbitrary side lengths.** Extend balanced prime families and control CRT
   assembly for every positive integer `n`.

## Bottom line

There is no complete proof. Through **CMR869**, local geometry, matching products,
restoration ancestry, aggressive normalization, exact completeness branching,
core contraction, distinguishing width, exchange-SCC factorization, and the
rank-three geometric split have rigorous normal forms. The unresolved
prime-power problem is global compression or potential descent across the
remaining constant-arity completeness tree.
