# Every dirty side-four joint state has an ambient strict target response

CMR1278--CMR1285 close side three exactly.  Side four is also finite enough for a
complete response-bank classification.  Unlike side three, one forbidden extension
can have several response matchings and not all of them improve.  Nevertheless,
every dirty ordered saturated state has at least one target cell, one disjoint
forbidden extension and one response matching of strictly smaller physical triple
potential.

If that response is unavailable in a restricted host, adding its missing edges is
a lowering expansion.  CMR942--CMR952 then accepts the lower minimum or contracts
an added minimum-core edge.  Thus the finite theorem remains useful inside the
selected scheduler.

## 1. Complete side-four state stock

### Theorem CMR1286 -- PROVED BY COMPLETE FINITE ENUMERATION

There are

\[
\boxed{216}
\]

ordered pairs `(O,M)` of physically disjoint perfect matchings of `K_{4,4}` and

\[
\boxed{90}
\]

distinct physical saturated states `O union M`.

The ordered-state potential distribution is

\[
\begin{array}{c|rrrrrrr}
\Phi&0&1&2&4&5&6&8\\
\hline
\#&40&48&84&24&8&8&4.
\end{array}
\]

Hence forty ordered states are clean and 176 are dirty.

The physical-state potential distribution is

\[
\begin{array}{c|rrrrrrr}
\Phi&0&1&2&4&5&6&8\\
\hline
\#&11&24&38&10&4&2&1.
\end{array}
\]

### Proof

Enumerate the `4!=24` perfect matchings.  For each ordered first matching, enumerate
the derangements relative to it; there are nine disjoint second matchings, giving
`24*9=216` ordered states.  Deduplicate their physical unions and evaluate every
three-cell integer determinant.  The displayed tables are the complete counts. ∎

## 2. Complete target-response search

Fix a dirty ordered state `S=O union M`, one physical target `T`, and a target cell
`e`.  Use the layer containing `e` as the rematched layer and the other layer as the
fixed opposite matching.  Enumerate every perfect matching `F` containing `e` and
disjoint from the opposite layer, and every response matching

\[
R\in\operatorname{PM}(K_{4,4}\setminus(O\cup F)).
\]

### Theorem CMR1287 -- PROVED

Every enumerated response state `Q=O union R` is saturated, physically layer-
disjoint, and omits `e`.  Therefore it destroys every old target containing `e`.

### Proof

The response matching avoids the fixed opposite matching and the forbidden
extension containing `e`.  Thus its union with the opposite layer is saturated and
omits the physical cell `e`. ∎

This is the exact side-four specialization of CMR1158.

## 3. Every dirty state has a lower response

### Theorem CMR1288 -- PROVED BY COMPLETE FINITE ENUMERATION

For every one of the 176 dirty ordered side-four states, the search of CMR1287
contains a response `Q` with

\[
\boxed{\Phi(Q)<\Phi(S).}
\]

The best potential changes over the 176 dirty ordered states have distribution

\[
\begin{array}{c|rrrrrr}
\min_Q(\Phi(Q)-\Phi(S))&-1&-2&-4&-5&-6&-8\\
\hline
\#&56&76&34&4&4&2.
\end{array}
\]

In particular the improvement is always at least one.

### Proof

For every dirty ordered pair, list all physical collinear triples, all three target
cells, all disjoint forbidden extensions through the corresponding labelled cell,
and all perfect matchings of the resulting degree-two response graph.  Evaluate the
integer determinant potential of each response.  There are 10,368 response
instances in the complete search, and the displayed best-change table covers all
176 dirty ordered states. ∎

No probabilistic estimate is used.

## 4. Canonical finite response choice

Fix total orders on targets, target cells, forbidden extensions and response
matchings.

### Theorem CMR1289 -- PROVED

Every dirty ordered side-four state has a unique canonical first response in the
CMR1288 search with smaller potential.  Repeated canonical response strictly
decreases the nonnegative integer `Phi` and therefore reaches a clean side-four
state after at most

\[
\boxed{\Phi(S)\le8}
\]

accepted responses.

### Proof

CMR1288 makes the improving response set nonempty, so fixed-order tie breaking
chooses one.  Every accepted move lowers `Phi` by at least one, and CMR1286 gives
maximum initial value eight. ∎

This is a finite deterministic policy, not merely existence of one clean state.

## 5. Restricted-host response

Let `H` be a restricted current host whose selected minimum is the dirty side-four
state `S`, and let `Q` be its canonical ambient improving response.  Put

\[
A=Q\setminus E(H).
\]

### Theorem CMR1290 -- PROVED

Exactly one of the following holds.

1. `A` is empty, so `Q` is feasible and gives strict potential improvement.
2. `A` is nonempty.  In the expanded host `H union A`,
   \[
   \min\Phi\le\Phi(Q)<\Phi(S),
   \]
   so the expansion is lowering.  Canonical expansion normalization therefore
   accepts a strict improvement or contracts one added minimum-core edge after
   minimum-preserving peels.

### Proof

The first branch is feasibility.  In the second branch, adding all missing response
edges makes `Q` feasible while retaining the old host and its minimum `S`.  Hence
the expanded minimum is strictly lower.  Apply CMR942--CMR949 and CMR952. ∎

Thus unavailability cannot turn the exact side-four improvement into a same-side
terminal obstruction.

## 6. Finite contraction/descent budget

### Theorem CMR1291 -- PROVED

Along a selected side-four owner, every canonical dirty response produces one of:

1. strict potential decrease;
2. contraction of an added core edge and strict residual-cardinality decrease;
3. unit-wall, child, fixed-core or envelope descent.

There are at most eight accepted potential decreases before cleanliness and at most
eight labelled-edge contractions before the two-layer state cardinality is
exhausted.

### Proof

CMR1289 bounds accepted decreases.  A saturated side-four joint state has eight
labelled edges, and every exact core contraction removes at least one residual
state edge.  Structural exits are the remaining CMR952 alternatives. ∎

The bounds are coarse but absolute.

## 7. Side-four credit interpretation

### Theorem CMR1292 -- PROVED

For every accepted CMR1289 response, the all-ones live-credit weight decreases:

\[
\boxed{
\#\text{new credits}<\#\text{retired credits}.
}
\]

For an unavailable canonical response, the same strict inequality holds in the
ambient expanded host before expansion normalization.

### Proof

The all-ones live-credit potential equals the physical triple potential by
CMR1256.  CMR1288 gives strict decrease.  The expanded host contains the same
ambient response state, so its physical transition has the same credit counts. ∎

This does not assert that the conservative one-parent offspring matrix has row sum
below one; extra destroyed credits are essential to the finite policy.

## 8. Side-four endpoint

### Corollary CMR1293 -- PROVED

The joint matching base through side four is closed for selected-execution target
improvement.

1. Side one contracts or is empty.
2. Root side two is clean and residual side two is rigid.
3. Every dirty side-three target response is clean.
4. Every dirty side-four state has an ambient strict target response.
5. Restricted unavailability gives lowering-expansion contraction or improvement.

The first unresolved finite matching side is therefore five.  For the general
prime-power proof, the remaining issue is not the side-three/four base but a
uniform spectral or target-collateral estimate stable under large sides, products,
fixed interfaces and CRT assembly.

No all-`n` theorem is claimed.  The complete 216-state stock, 10,368 response
instances, best-change distribution, canonical policy and restricted-host lowering
expansion are checked in
[`scripts/verify_prime_power_side_four_finite_improvement.py`](../scripts/verify_prime_power_side_four_finite_improvement.py).
