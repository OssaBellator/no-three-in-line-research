# Every dirty full side-four grid state has an ambient strict target response

This chapter concerns the complete standard coordinate grid

\[
\{0,1,2,3\}\times\{0,1,2,3\},
\]

and affine images obtained by translation and one common nonzero scale.  It does
not apply automatically to a scattered residual factor with four arbitrarily
labelled source and target coordinates; arbitrary relabelling does not preserve
real collinearity.

## 1. Complete full-grid state stock

### Theorem CMR1286 -- PROVED BY COMPLETE FINITE ENUMERATION

On the standard full grid there are 216 ordered pairs of disjoint perfect matchings
and 90 physical saturated states.  Their ordered-state potential distribution is

\[
\begin{array}{c|rrrrrrr}
\Phi&0&1&2&4&5&6&8\\
\hline
\#&40&48&84&24&8&8&4,
\end{array}
\]

and the physical-state distribution is

\[
\begin{array}{c|rrrrrrr}
\Phi&0&1&2&4&5&6&8\\
\hline
\#&11&24&38&10&4&2&1.
\end{array}
\]

### Proof

Enumerate the 24 perfect matchings, the nine derangements relative to each fixed
matching, and every three-cell integer determinant.  Common affine translation and
scaling preserve determinant zero. ∎

## 2. Complete target-response search

Fix a dirty full-grid state `S=O union M`, a physical target cell `e`, a disjoint
forbidden extension `F` through `e`, and

\[
R\in\operatorname{PM}(K_{4,4}\setminus(O\cup F)).
\]

### Theorem CMR1287 -- PROVED

The response `Q=O union R` is saturated, layer-disjoint, omits `e`, and destroys
every old target containing `e`.

### Proof

The response matching avoids `O` and the extension containing `e`. ∎

This combinatorial response statement remains valid for arbitrary labelled
side-four factors; the numerical potential claims below require the full-grid
coordinates.

## 3. Every dirty full-grid state has a lower response

### Theorem CMR1288 -- PROVED BY COMPLETE FINITE ENUMERATION

Each of the 176 dirty ordered full-grid states has a target response `Q` with

\[
\boxed{\Phi(Q)<\Phi(S).}
\]

The best-change distribution is

\[
\begin{array}{c|rrrrrr}
\min_Q(\Phi(Q)-\Phi(S))&-1&-2&-4&-5&-6&-8\\
\hline
\#&56&76&34&4&4&2.
\end{array}
\]

### Proof

Enumerate every target, labelled target cell, disjoint forbidden extension and
response matching.  The 10,368 response instances give the displayed exhaustive
distribution. ∎

## 4. Canonical full-grid policy

### Theorem CMR1289 -- PROVED

Fixed-order tie breaking selects one improving response for every dirty ordered
full-grid state.  Repeated accepted responses reach a clean state after at most

\[
\boxed{\Phi(S)\le8}
\]

steps.

### Proof

Every accepted response lowers the nonnegative integer potential by at least one.
∎

## 5. Restricted hosts on the same full coordinate sets

Let `H` be a restricted host on the same full-grid vertices, with selected minimum
`S`, and let `Q` be its canonical ambient improving response.  Put
`A=Q\setminus E(H)`.

### Theorem CMR1290 -- PROVED UNDER THE FULL-GRID COORDINATE HYPOTHESIS

If `A` is empty, `Q` is a feasible strict improvement.  If `A` is nonempty, adding
it creates a lowering expansion:

\[
\min_{R\in\mathcal F(H\cup A)}\Phi(R)
\le\Phi(Q)<\Phi(S).
\]

Canonical expansion normalization accepts a lower minimum or contracts an added
minimum-core edge.

### Proof

The expansion retains `S` and makes `Q` feasible.  Apply CMR942--CMR952. ∎

For scattered residual coordinates, an ambient state found by the standard-grid
enumeration need not have the same potential and cannot be imported by relabelling.

## 6. Finite full-grid budget

### Theorem CMR1291 -- PROVED

On the full-grid owner there are at most eight accepted decreases before
cleanliness and at most eight labelled-edge contractions before residual state
cardinality is exhausted.

### Proof

Use CMR1289 and the eight labelled edges of a saturated side-four state. ∎

## 7. Credit interpretation

### Theorem CMR1292 -- PROVED FOR THE FULL STANDARD/AFFINE GRID

Every accepted response strictly decreases the all-ones live-credit potential:

\[
\#\text{new credits}<\#\text{retired credits}.
\]

The same holds for the ambient response before normalization of a lowering
expansion.

### Proof

Live-credit count equals physical triple potential by CMR1256, and CMR1288 gives
strict decrease. ∎

## 8. Scoped endpoint

### Corollary CMR1293 -- PROVED

The complete standard side-four root grid, and verified affine copies, have a
finite deterministic strict-improvement policy.  Restricted hosts on those same
coordinate sets improve or contract through a lowering expansion.

This is a finite root/affine base theorem.  Arbitrary residual side-four factors
still require inherited-coordinate collateral analysis through CMR1158--CMR1269.

No all-`n` theorem is claimed.  The standard-grid 216-state stock and 10,368
responses are checked in
[`scripts/verify_prime_power_side_four_finite_improvement.py`](../scripts/verify_prime_power_side_four_finite_improvement.py).
