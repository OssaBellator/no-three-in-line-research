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

### Recursive geometry and inherited closure

- Completed-reciprocal channels and the stated balanced recursive prime-power
  banks are proved.
- Prefix, quotient, carry, Hall-wall, line-clean, joint-parent, and harmonic
  packet calculations are closed at their indexed scales.
- Closure envelopes form a nested chain of at most `h+1` epochs with at most `h`
  strict expansions.
- Positive target load contracts to the four-endpoint one-target core under the
  global-baseline closure.

### Matching, restoration, and product structure

- Entering and leaving matching churn have equal cardinality; recreated selected
  conflicts contain entering edges.
- Every physical edge occurrence has exact labelled nonroot full-token incidence
  `(p+1)(h-1)`.
- Exact selected-state cycles are erasable under monotone masks.
- Canonical selectors, unavailable-edge absorption, rollback, packet loss,
  returned-edge ancestry, and forced certificates have finite stock,
  deletion/essentiality responses, or explicit physical restoration payment.
- Protected/free, child-routing, essential-core, and unit-wall products are exact.
  A nonfixed selected edge belongs to one unique strict child factor.
- One physical edge has at most
  \[
  (h+1)\left(1+\sum_{m=1}^{N}(2m^2+m+1)\right)
  \]
  structural owner slots, so branch-wide recurrence concentrates at one owner.

### Returned targets, Hall walls, and protected lines

- A recurrent target edge deletes while nonessential. On return, its stored
  avoiding matching either survives or exposes a missing old matching edge.
- Essential return creates Hall deficiency exactly one and an exact lower-side
  unit-wall product. The full factor tree has at most `d` splits and cubic
  owner-edge stock.
- A recurrent physical target has at most six labelled same-layer pair types.
  A recurrent type deletes one nonessential pair edge or contracts two essential
  pair edges, lowering side by two.
- A full-envelope layer rematching avoids `r` protected nonaxis lines whenever
  `q>=2r+4`. Saturation produces a historical target-pair bank or a cell wall/star.
- Historical targets are never treated as simultaneous. Ordered two-layer
  rematching neutralises stored pair signatures, and temporal reuse is counted by
  physical cell--absence-run slots.

### Global restoration ancestry

- Physical restoration is defined in absolute parent coordinates and is not
  duplicated by envelope, routing, factor, wall, or certificate relabelling.
- Structural deletion generations form a forward acyclic out-degree-one ancestry
  forest. Long paths force many genuine restoration runs of one labelled edge.
- Fresh unpaid structural roots have an explicit branch-wide polynomial stock.
- A surviving stored anchor can re-delete every restored private edge in one
  simultaneous operation. Anchor failure exposes one of only `2n` anchor edges.
- Private-batch normalization is idempotent. Reopening only private edges
  normalizes to the identical state and is cycle-erasable.
- A newly enabled nonimproving state uses a newly added edge, which is immediately
  absorbed into the aggressive branch's private deletion union.

## Critical completeness correction

CMR785--CMR821 describe a rigorous **aggressive normalization subbranch**. Deleting
one candidate's complete anchor-entering batch preserves the anchor and gives
strong private-edge accounting, but it may also remove other untested states,
including an improving state. Branch-local forcing and contraction are not
statements about the original full family.

CMR830--CMR837 give the exact completeness-preserving response. For an
equal-cardinality feasible state family,

\[
\mathcal F\setminus\{Q\}
=
\bigcup_{f\in Q,\,\mathcal F-f\ne\varnothing}(\mathcal F-f).
\]

Every state other than `Q`, including every improving state, survives in at least
one viable single-edge child. Every root-to-leaf path has at most `2n^2-2n`
deletions. The aggressive batch branch is contained in the viable child branches
but is not their union.

CMR838--CMR845 identify the viable children exactly. With

\[
E_*(\mathcal F)=\bigcap_{R\in\mathcal F}R,
\]

one has

\[
\mathcal F-f\ne\varnothing
\iff
f\notin E_*(\mathcal F).
\]

After contracting the full compatible core, the residual family has empty core,
and at every node

\[
\boxed{
\text{contracted core rank}+\text{viable child count}=2n.
}
\]

The zero-child case is a singleton and the one-child case is deterministic.
Total contracted core rank along a branch is at most `2n`.

## Other corrections retained

- Naive sequential two-layer rematching may reoccupy an old first-layer cell.
- One edge return may serve several neutralisations in one continuous absence run;
  the ledger counts cell--run slots rather than raw episode-return pairs.
- Removing one essential edge produces deficiency one, not a large Hall batch.
- Routing compensation and essentiality escape may be distributed across several
  alternating components.
- Owner relabelling does not itself create physical restoration.

## Current open frontier

1. **Core-free branch-width control.** Compress or bound the width of the viable
   single-edge state-exclusion tree after full essential-core contraction, or
   prove that a canonical aggressive branch retains an improving witness.
2. **Fixed-owner, fixed-edge closure.** Inside a retained branch, show that an edge
   restored often enough to survive normalization, bulk redeletion, anchor-loss
   ancestry, and deletion/contraction responses forces target-load decrease,
   reserve exhaustion, or strict potential improvement.
3. **Prime-field and low-height transfer.** Rebuild the owner-labelled endpoint
   for prime fields and the remaining thin quotient/carry regimes.
4. **Arbitrary side lengths.** Extend the balanced prime families and control CRT
   assembly for every positive integer `n`.

## Bottom line

There is no complete proof. Through **CMR845**, the local geometric, matching,
restoration, product, and aggressive-normalization loops have exact finite-stock,
cycle-erasure, deletion/contraction, or payment normal forms. Completeness is now
represented by an exact polynomial-depth branching tree, whose unresolved part
is width in core-free equal-cardinality families.
