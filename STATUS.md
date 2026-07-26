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
- Returned structural deletions form a forward acyclic ancestry forest.
- A recurrent target edge deletes while nonessential; essential return produces a
  deficiency-one Hall wall and exact lower-side factorisation.
- Historical protected-line targets are neutralised through stored labelled pairs,
  with reuse counted by physical cell--absence-run slots.
- A recurrent physical target has at most six labelled same-layer pair types. A
  recurrent type deletes one nonessential pair edge or contracts two essential
  pair edges.

## Completeness and branch compression

The complete-entering-batch anchor deletion of CMR785--CMR821 is a rigorous
**aggressive subbranch**, but its forcing conclusions are branch-local. Complete
search uses exact viable-child unions or the rank-three prescription split.

The rank-three split can be made disjoint by assigning each state to its first
missing prescription edge. Every internal step fixes or deletes a previously
undecided edge, so the disjoint target-resolution tree has depth at most `2n^2`.
At one resolution stage, terminal leaves compress to at most

\[
8\binom{n^2}{3}
\]

fixed labelled-triple set-family classes. Unions with different inherited masks
are not silently identified with one matching host.

Along one stable-owner path, canonical new triples have support matching number at
most

\[
B_n=2n^2-2n+\left\lfloor\frac{2n}{3}\right\rfloor.
\]

A support cover has size at most `9B_n`. Long paths concentrate on one physical
cell or labelled matching vertex, and one exact labelled edge batches many
candidates through a binary delete/condition split with rank-two transfer.

## Minimum-anchor and minimum-face mode

If `S` is an actual minimum-potential state, every restriction preserving `S`
preserves one minimum. Forcing a chosen physical target and then a chosen labelled
anchor prescription uses at most

\[
2n^2-2n
\]

outside-anchor deletions. Exact contraction preserves minimum status for the
induced objective

\[
\Phi_P(R')=\Phi(P\cup R').
\]

For the complete minimum face at one host, every labelled edge is either omitted
by some minimum state and minimum-preservingly deletable, or belongs to the common
minimum core and contracts. Contracting the whole core leaves a residual minimum
family with empty common core.

One labelled physical edge has at most

\[
L_{\mathrm{edge}}(N,h)
=
(h+1)\left(1+\sum_{m=1}^{N}(2m^2+m+1)\right)
\]

structural owner slots. Each slot receives at most one uncharged first closure.
Every later active appearance is a genuine restoration unless the edge contracts.

## Complete same-vertex-set transition normalization

For restriction `H'\subseteq H`, the minimum can only rise. If an old minimum
survives, the new minimum face is exactly the surviving part of the old face.
For expansion `H\subseteq H'`, the minimum can only fall; every genuinely new
minimum state uses an added edge.

A same-value expansion is exactly rollbackable. If an expansion lowers the
minimum, added edges omitted by some new minimum peel away while preserving that
lower value; before the added batch is exhausted, one added edge enters the
minimum core and contracts. The same conclusion holds when the intersection/base
host has no feasible state.

Therefore every arbitrary same-vertex-set transition factors through its
intersection and normalizes to:

1. a monotone restriction preserving an old minimum;
2. a lost edge of the old canonical minimum;
3. exact contraction of an added minimum-core edge;
4. strict potential improvement.

Between contractions, normalized hosts form a nested decreasing chain. A coarse
saturated side-`N` bound is

\[
(2N+1)2N^2
\]

strict same-vertex-set restriction transitions before contraction, potential
improvement, or structural owner/vertex-set exit. Restoration-only activity no
longer needs an independent local capacity bound: at unchanged minimum value it
rolls back, and at lower value it contracts or improves.

## Corrections retained

- Naive sequential two-layer rematching may reoccupy an old first-layer cell.
- Historical target lines are not simultaneous target families.
- One edge return may serve several neutralisations in one absence run.
- Removing one essential edge produces Hall deficiency exactly one.
- Owner relabelling does not itself create physical restoration.
- Aggressive batch deletion is branch-local; completeness uses viable child unions
  or disjoint prescription partitions.
- A union of differently masked terminal leaves is a valid set family but is not
  silently treated as one matching host.
- An empty intersection host has no assigned minimum; it enters the lost-minimum
  or added-edge contraction branch directly.

## Current open frontier

1. **Structural vertex-set descent.** Transport the induced minimum objective,
   target load, and protected reserves through common-core contractions, unit-wall
   products, strict child products, and closure-envelope changes.
2. **Cross-factor potential.** The real-triple potential is not automatically
   additive across exact matching products; mixed triples must be transferred or
   charged using the product-rectangle machinery.
3. **Host representability.** Reconnect exact set-family contractions and merged
   terminal-leaf classes with geometric matching hosts when masks differ.
4. **Prime-field and arbitrary-length transfer.** Rebuild the endpoint for prime
   fields, thin quotient/carry regimes, and every positive integer side length.

## Bottom line

There is no complete proof. Through **CMR957**, local completeness has polynomial
certificate compression, minimum-anchor mode avoids branch width, fixed-owner
edges delete or contract, and all same-vertex-set host dynamics normalize to
finite restriction, rollback, contraction, or strict improvement. The remaining
prime-power problem is structural vertex-set descent and cross-factor potential
transport.
