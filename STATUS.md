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

- Nonlinear completed-reciprocal channels and balanced recursive banks are proved
  for the stated prime-power families.
- Prefix, quotient, carry, Hall-wall, line-clean, and joint-parent collateral
  calculations are closed at their recorded scales.
- Closure envelopes have invariant inherited row sets and form a nested chain of
  at most `h+1` epochs, with at most `h` strict expansions.
- Positive target load contracts to the four-endpoint one-target core under the
  global-baseline closure.

### Dynamic matching and token accounting

- Entering and leaving matching churn have equal cardinality; every recreated
  selected conflict contains an entering edge.
- Every physical edge occurrence has exact labelled nonroot full-token incidence
  `(p+1)(h-1)`.
- Exact selected-state cycles are erasable under monotone masks.
- Packet losses, unavailable edges, rollback, and restored-edge recreation have
  owner-labelled finite stock, deletion ancestry, or explicit reintroduction
  payment.
- Static token consumption is not assumed monotone; current statements use
  absence runs, entering-edge incidence, private deletion stock, or exact owner
  transitions.

### Protected selectors and sparse products

- Canonical selectors have fixed forbidden matchings, fixed collateral profiles,
  and finite owned edge, line, token, and certificate universes.
- Heavy lines and secant stars execute by simultaneous absorption outside a
  protected matching core.
- Large protected cores have sparse interfaces and exact protected/free product
  factorisations.
- Mixed product conflicts are Cartesian rectangles of low factor rank.
- Nonessential prescriptions delete; essential prescriptions contract and
  transfer to strict factors.
- Strict child routing changes pay at least two entering and two leaving support
  edges, while nonforced mixed atoms disappear after at most `d^2` deletions.

### Target handoff, returned edges, and unit Hall walls

- A nonimproving transition destroying `D` targets creates at least `D` new
  triples, and one entering cell inherits at least `ceil(D/c)` when the churn size
  is `c`.
- Four-endpoint handoff banks destroy the inherited cell-star target family;
  target-load loss is multiplicatively paid by entering-edge churn.
- A recurrent entering target cell is nonessential in its current host and can be
  deleted while preserving matchability.
- If that cell later returns, a stored avoiding matching either survives and
  permits redeletion, or exposes an exact missing old matching edge.
- An essential returned edge creates a canonical Hall wall of deficiency exactly
  one. After contraction, its matching family factors into strict factors whose
  side sum is one less.
- The complete unit-wall factor tree has at most `d` splits and total owner-edge
  stock at most
  \[
  \frac{d(d+1)(2d+1)}6.
  \]

### Protected target lines and historical-pair neutralisation

- A full-envelope layer rematching can avoid any `r` protected nonaxis lines when
  \[
  q\ge2r+4,
  \]
  giving guaranteed capacity
  \[
  R(q)=\left\lfloor\frac{q-4}{2}\right\rfloor.
  \]
- Reuse of an already protected target line pays an entering edge on that line.
- Saturation at `R(q)+1` lines is dyadically localised by primitive height.
- Historical target triples are not treated as simultaneous; one same-layer pair
  is retained from each line and a majority layer supplies at least half the
  signatures.
- For `q>=8`, an ordered two-layer rematching can destroy the live target while
  globally omitting a compatible historical pair bank.
- Temporal reuse is counted by physical cell--absence-run slots, not raw episode
  multiplicity.
- A recurrent physical target has at most six labelled same-layer pair types.
  Once one type recurs, one pair cell deletes matching-preservingly or both
  essential pair cells contract, decreasing factor side by two.

### Global return ancestry and anchor normalization

- Physical restoration is defined in absolute parent coordinates and is not
  duplicated by envelope, routing, factor, wall, or certificate relabelling.
- Returned structural deletions form a forward acyclic ancestry graph of
  out-degree at most one. A path longer than `(mu-1)2N^2` forces `mu` deletion
  generations of one labelled physical edge.
- Fresh unpaid structural roots have an explicit branch-wide polynomial stock;
  selected-state and routing losses are paid endpoints rather than new roots.
- At a fixed owner, every nonimproving target-destroying state contributes its
  complete anchor-entering set. The anchor survives, at least two new labelled
  edges are deleted, and at most `n(n-1)` such batches occur.
- If target-destroying states are exhausted, one exact labelled same-layer target
  pair is forced and contracts, leaving a rank-one residual trigger.
- Rejected entering batches are pairwise disjoint private deletion codes. A later
  reset reopening `k` batches restores at least `k` distinct labelled edges and
  pays at least `k(p+1)(h-1)` token incidences.
- A surviving stored anchor re-closes all restored private edges simultaneously.
  Anchor failure exposes one of only `2n` missing anchor edges.
- Private-batch normalization is idempotent. Pure reopening normalizes to the same
  state and is cycle-erasable; every nonerasable change uses a nonprivate edge.
- A newly enabled state uses a newly added edge. If the state is nonimproving,
  that enabling edge is immediately absorbed into the private union.

### Physical-edge structural lineage

- Exact skeleton, child-routing, essential-core, and unit-wall products give
  unique ownership of every matching-relevant edge.
- A nonfixed edge follows one strict child factor; factor-tree branching does not
  duplicate its lineage.
- With `H_m=2m^2+m+1`, one physical edge has at most
  \[
  (h+1)\left(1+\sum_{m=1}^{N}H_m\right)
  \]
  structural owner slots.
- Many branch-wide restorations of one edge therefore concentrate at one fixed
  owner, where bulk redeletion, private absorption, anchor-loss ancestry,
  matching-preserving deletion, or essential contraction applies.

## Important corrections retained

- Naive sequential two-layer rematching may reoccupy old first-layer cells. The
  CMR758--CMR759 construction explicitly forbids the live target in both ordered
  layer rematchings.
- A historical family of target lines is not a simultaneous target family.
- One edge return may serve several neutralisations in one absence run; CMR766--
  CMR769 count cell--run slots.
- Removing one essential edge produces Hall deficiency exactly one, not a large
  deficiency batch.
- Routing compensation and essentiality escape may be distributed across several
  alternating components.
- One physical restoration is counted once globally even when several nested
  owners or private certificates observe it.

## Current open frontier

1. **Final fixed-owner, fixed-edge loop.** Show that an edge genuinely restored
   often enough to survive private normalization, bulk redeletion, anchor-loss
   ancestry, and deletion/contraction responses forces inherited target-load
   decrease, protected-reserve exhaustion, or strict global potential
   improvement.
2. **Prime-field and low-height transfer.** Rebuild the owner-labelled endpoint
   for prime fields and the remaining thin quotient/carry regimes.
3. **Arbitrary side lengths.** Extend the balanced prime families and control CRT
   assembly for every positive integer `n`.

## Bottom line

There is no complete proof. Through **CMR829**, the local factor, routing,
forced-certificate, target-handoff, recurrent-target, returned-edge, unit-wall,
protected-line, historical-pair, absence-run, labelled-pair, anchor-batch,
normalization, and physical-edge-lineage loops have exact finite-stock,
cycle-erasure, deletion/contraction, or entering-edge payment normal forms.

The principal remaining prime-power theorem is now fixed-owner and fixed-edge,
not owner proliferation or repeated private-batch reopening. Arbitrary
side-length coverage remains necessary afterward.
