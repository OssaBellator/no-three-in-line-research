# Status and honesty ledger

**Last updated:** 26 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open. This repository does **not** contain a complete proof.

The collision-free theorem ledger is split across

- `proofs/composite-modulus-theorem-index-live.md` through CMR747;
- `proofs/composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `proofs/composite-modulus-theorem-index-live-continuation-2.md` from CMR870.

## Established prime-power structure

- Closure envelopes form at most `h+1` nested epochs with at most `h` strict
  expansions.
- Protected/free, child-routing, essential-core, exchange-SCC, and unit-wall
  matching products are exact.
- Physical restoration is defined in absolute parent coordinates and is not
  duplicated by owner relabelling.
- Returned structural deletions form a forward acyclic ancestry forest. A
  recurrent target edge deletes while nonessential; essential return produces a
  deficiency-one Hall wall and exact lower-side factorisation.
- Historical protected-line targets are neutralised through stored labelled
  pairs, and reuse is counted by physical cell--absence-run slots.
- A recurrent physical target has at most six labelled same-layer pair types. A
  recurrent type deletes one nonessential pair edge or contracts two essential
  pair edges.

## Critical completeness correction

The anchor-preserving complete-entering-batch deletion of CMR785--CMR821 is a
rigorous **aggressive subbranch**, but it may remove other untested states. Its
forcing and contraction conclusions are branch-local.

Completeness is restored by CMR830--CMR837:

\[
\mathcal F\setminus\{Q\}
=
\bigcup_{f\in Q,\,\mathcal F-f\ne\varnothing}(\mathcal F-f).
\]

Every alternative state, including every improving state, survives in at least
one viable single-edge child. Every root-to-leaf path has at most `2n^2-2n`
deletions.

The viable children are exactly the nonessential edges of `Q`. After contracting
the complete common core,

\[
\boxed{
\text{contracted core rank}+\text{viable child count}=2n.
}
\]

The zero-child case is a singleton, the one-child case is deterministic, and
total contracted core rank along a branch is at most `2n`.

## Distinguishing width and exchange factors

- The minimum number of children needed to exclude one state is the transversal
  number of its alternative-difference hypergraph.
- This distinguishing rank is additive in exact products.
- For a complete one-layer matching family, it equals the minimum directed
  feedback-vertex-set size of the exchange graph.
- Usable matching edges lie exactly inside exchange SCCs; the matching family
  factors over SCC blocks and the distinguishing ranks add.

These results localise one-layer completeness width exactly, but do not alone
control the coupled two-layer branch tree.

## Constant-arity geometric completeness

Every nonimproving state which destroys positive target load creates a canonical
new labelled collinear triple `C`. The exact family split is

\[
\mathcal F
=
\left(\bigcup_{f\in C}(\mathcal F-f)\right)
\cup
\mathcal F_C.
\]

Thus the scheduler has at most three deletion children plus one conditioned
forced-triple branch. Every original state survives in at least one branch.
Conditioning on `C` lowers state cardinality by three under contraction.

Encode each new triple by its three physical cells and six layer-labelled
matching endpoints. Along one stable-owner path, pairwise support-disjoint
triples consume distinct deletion or contraction resources. Hence their matching
number is at most

\[
B_n=2n^2-2n+\left\lfloor\frac{2n}{3}\right\rfloor
\]

unless there is structural exit or strict potential improvement. A maximal
packing gives a support cover of size at most `9B_n`, so every long path
concentrates on one physical cell or one labelled matching vertex.

If one support atom belongs to `d` distinct canonical triples, one exact labelled
edge belongs to at least

\[
\left\lceil\frac{d}{2n}\right\rceil
\]

of them. One binary edge split then batches those candidates: delete the edge, or
condition on and contract it, converting the triples to rank-two residual pairs.

## Corrections retained

- Naive sequential two-layer rematching may reoccupy an old first-layer cell.
- Historical target lines are not simultaneous target families.
- One edge return may serve several neutralisations in one absence run.
- Removing one essential edge produces Hall deficiency exactly one.
- Owner relabelling does not itself create physical restoration.
- Aggressive batch deletion is branch-local; completeness uses viable child
  unions or the new-triple prescription split.

## Current open frontier

1. **Global branch merging.** Merge or charge side branches which concentrate on
   the same labelled edge, rank-two residual pair, support atom, or forced
   certificate.
2. **Fixed-edge restoration closure.** Convert a repeatedly restored edge which
   survives deletion, normalization, and contraction responses into target-load
   decrease, reserve exhaustion, or strict global potential improvement.
3. **Prime-field and low-height transfer.** Rebuild the owner-labelled endpoint
   for prime fields and remaining thin quotient/carry regimes.
4. **Arbitrary side lengths.** Extend balanced prime families and control CRT
   assembly for every positive integer `n`.

## Bottom line

There is no complete proof. Through **CMR893**, completeness has a constant-arity
geometric split, polynomial root-to-leaf resource bounds, and a branch-batching
mechanism at recurrent support atoms. The remaining prime-power problem is global
merging or common-budget charging across those side branches.
