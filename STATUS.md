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
- Every physical edge has exact labelled nonroot full-token incidence
  `(p+1)(h-1)` per occurrence.
- Exact selected-state cycles are erasable under monotone masks.
- Packet losses, unavailable edges, rollback, and restored-edge recreation have
  owner-labelled finite stock, deletion ancestry, or explicit reintroduction
  payment.
- Static token consumption is not assumed monotone; all current statements use
  absence runs, entering-edge incidence, or finite owner stock.

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
  triples, and one entering cell inherits at least `ceil(D/c)` of them when the
  churn size is `c`.
- Four-endpoint handoff banks destroy the inherited cell-star target family;
  target-load loss is multiplicatively paid by entering-edge churn.
- A recurrent entering target cell is nonessential in its current host and can be
  deleted while preserving matchability.
- If that cell later returns, a stored avoiding matching either survives and
  permits redeletion, or exposes an exact missing old matching edge.
- An essential returned edge creates a canonical Hall wall of deficiency exactly
  one. After contraction, its matching family factors exactly into two strict
  factors whose side sum is one less.
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
- Historical target triples are not treated as simultaneous. Instead, one
  same-layer pair is retained from each line, and a majority layer supplies at
  least half the signatures.
- The pair family either concentrates at one matching vertex or contains a large
  globally compatible partial matching.
- For `q>=8`, an ordered two-layer rematching can destroy the live target while
  globally omitting the entire compatible pair matching. The degree bound is
  four, so Hall applies.
- Fan signatures become many distinct absent wall cells or one globally forbidden
  repeated cell.
- At one envelope epoch, the neutralisation certificate-key stock is at most
  \[
  6\binom{2q^2}{3}.
  \]
- Temporal reuse is counted by physical cell--absence-run slots. Several
  neutralisations during one continuous absence are not charged as several edge
  returns.
- One cell--run slot carries at most the finite certificate-key stock. Unless one
  cell has many return runs, repeated reserve-saturation histories are finite.
- A recurrent physical target has at most six labelled same-layer pair types.
  Once one type recurs, either one pair cell is nonessential and deletes
  matching-preservingly, or both essential pair cells contract together,
  decreasing factor side by two and leaving a rank-one trigger.

## Important corrections retained

- Naive sequential two-layer rematching may reoccupy old first-layer cells. The
  CMR758--CMR759 construction explicitly forbids the live target in both ordered
  layer rematchings.
- A historical family of target lines is not a simultaneous target family.
  CMR755--CMR776 neutralise stored pair signatures and stabilise labelled
  recurrence instead.
- One edge return may serve several neutralisations in the same absence run.
  CMR766--CMR769 count cell--run slots, not raw episode-return incidences.
- Removing one essential edge produces Hall deficiency exactly one, not a large
  deficiency batch.
- Routing compensation and essentiality escape may be distributed across several
  alternating components; payment is component-supported rather than edgewise by
  assumption.

## Current open frontier

1. **Branch-wide owner-edge return budget.** Sum genuinely restored physical edges
   across envelope, routing, host, factor, and unit-wall owners after the
   deletion/double-contraction responses. Convert excess returns into permanent
   deletion ancestry, strict side descent, target-load decrease, or a global
   potential improvement.
2. **Full-token return closure.** Replace the remaining conditional one-pass token
   budgets by an unconditional bound compatible with owner changes and sparse
   rollback.
3. **Prime-field and low-height transfer.** Rebuild the owner-labelled endpoint
   for prime fields and the remaining thin quotient/carry regimes.
4. **Arbitrary side lengths.** Extend the balanced prime families and control CRT
   assembly for every positive integer `n`.

## Bottom line

There is no complete proof. Through **CMR776**, the local factor, routing,
forced-certificate, target-handoff, recurrent-target, returned-edge, unit-wall,
protected-line, historical-pair, absence-run, and labelled-pair loops have exact
finite-stock, deletion/contraction, or entering-edge payment normal forms.

The principal remaining prime-power theorem is a global, owner-consistent budget
for genuinely restored edges after those local responses. Arbitrary side-length
coverage remains necessary afterward.
