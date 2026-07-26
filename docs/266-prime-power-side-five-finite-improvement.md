# Every dirty full side-five grid state has an ambient strict target response

This chapter concerns the complete standard grid

\[
\{0,1,2,3,4\}\times\{0,1,2,3,4\},
\]

and affine copies obtained by translation and one common nonzero scale.  Its
potential tables and lowering policy do not transfer by arbitrary relabelling to a
scattered residual factor.

## 1. Complete full-grid state stock

### Theorem CMR1294 -- PROVED BY COMPLETE FINITE ENUMERATION

The standard full grid has 5280 ordered disjoint permutation pairs and 2040
physical saturated states.  Their ordered potential distribution is

\[
\begin{array}{c|rrrrrrrrrrrrrrrr}
\Phi&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15\\
\hline
\#&64&192&960&1200&904&616&560&336&96&64&32&104&80&32&24&16,
\end{array}
\]

and their physical distribution is

\[
\begin{array}{c|rrrrrrrrrrrrrrrr}
\Phi&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15\\
\hline
\#&32&76&360&440&322&264&252&140&30&28&12&32&32&8&8&4.
\end{array}
\]

### Proof

Enumerate the 120 matchings, the 44 derangements relative to each fixed matching,
and the 152 collinear three-cell subsets of the standard `5 x 5` board.  Common
affine translation and scaling preserve the determinant-zero relation. ∎

## 2. Response-bank stock

### Theorem CMR1295 -- PROVED BY COMPLETE FINITE ENUMERATION

For disjoint perfect matchings `O,F`, the graph

\[
K_{5,5}\setminus(O\cup F)
\]

is 3-regular and has twelve or thirteen perfect matchings.  Among the 5280 ordered
pairs `(O,F)`, 2400 banks have size twelve and 2880 have size thirteen.

### Proof

Enumerate all 120 response matchings for every ordered pair. ∎

This bank-size statement is combinatorial and independent of coordinate geometry.

## 3. Full-grid target-response table

For a fixed matching `O` and a cell `e notin O`, let `mu_5(O,e)` be the minimum
standard-grid potential of `O union R` over every disjoint forbidden extension
through `e` and every response matching.

### Theorem CMR1296 -- PROVED FOR THE FULL STANDARD/AFFINE GRID

The table is defined for all

\[
\boxed{120\cdot20=2400}
\]

fixed-opposite/nonopposite-cell pairs.  Every minimizing response omits `e` and is
disjoint from `O`.

### Proof

Use CMR1198 and CMR1295 for existence.  The potential values are evaluated in the
standard full-grid coordinates. ∎

## 4. Every dirty full-grid state has a lower response

### Theorem CMR1297 -- PROVED BY COMPLETE FINITE ENUMERATION

Each of the 5216 dirty ordered standard-grid states has a target cell with

\[
\boxed{\mu_5(O_e,e)<\Phi(S).}
\]

The best-change distribution is

\[
\begin{array}{c|rrrrrrrrrrrrrr}
\min_Q(\Phi(Q)-\Phi(S))
&-1&-2&-3&-4&-5&-6&-7&-8&-9&-10&-11&-12&-13&-15\\
\hline
\#
&316&1268&1176&836&728&360&152&76&56&64&72&88&16&8.
\end{array}
\]

### Proof

Enumerate every standard-grid target cell and query the 2400-entry table. ∎

For scattered coordinates, the same combinatorial response exists but these
potential comparisons must be recomputed in the inherited parent geometry.

## 5. Canonical full-grid policy

### Theorem CMR1298 -- PROVED

Fixed-order tie breaking selects an improving response for every dirty full-grid
state.  Repeated accepted responses reach a clean state after at most

\[
\boxed{\Phi(S)\le15}
\]

steps.

### Proof

Each accepted move lowers the nonnegative integer potential by at least one. ∎

## 6. Restricted hosts on the same full coordinate sets

### Theorem CMR1299 -- PROVED UNDER THE FULL-GRID COORDINATE HYPOTHESIS

Let `Q` be the canonical ambient lower response and `A=Q\setminus E(H)`.  If `A` is
empty, `Q` is feasible.  Otherwise adding `A` gives

\[
\min_{R\in\mathcal F(H\cup A)}\Phi(R)
\le\Phi(Q)<\Phi(S),
\]

so canonical expansion normalization accepts a lower minimum or contracts an added
minimum-core edge.

### Proof

The expansion retains `S` and makes `Q` feasible.  Apply CMR942--CMR952. ∎

This argument cannot import a standard-grid response into an arbitrary scattered
factor without first verifying its actual potential.

## 7. Full-grid finite budget

### Theorem CMR1300 -- PROVED

On the standard/affine full-grid owner there are at most fifteen accepted potential
decreases and at most ten labelled-edge contractions.  Every accepted response
strictly decreases the all-ones live-credit potential.

### Proof

Use CMR1298, the ten labelled state edges, and CMR1256. ∎

## 8. Scoped endpoint

### Corollary CMR1301 -- PROVED

The complete standard side-five root grid, and verified affine copies, have a
finite deterministic strict-improvement policy.  Restricted hosts on those same
coordinates improve or contract by a lowering expansion.

This is a finite root/affine base theorem.  Arbitrary residual side-five factors
remain governed by inherited-coordinate response banks, local collateral
envelopes and the spectral framework CMR1198--CMR1277.

No all-`n` theorem is claimed.  The standard-grid 5280-state classification and
2400 response-table entries are checked in
[`scripts/verify_prime_power_side_five_finite_improvement.py`](../scripts/verify_prime_power_side_five_finite_improvement.py).
