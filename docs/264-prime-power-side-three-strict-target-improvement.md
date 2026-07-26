# Every dirty side-three joint state has an exact clean target response

CMR1174--CMR1176 construct the unique side-three response matching for one target
edge.  The earlier theorem used only the executable-or-blocked split.  The complete
physical classification is stronger: every dirty saturated side-three state has
exactly one collinear triple, and every labelled response through any cell of that
triple produces a clean saturated state.

This gives an exact zero-offspring base row for the collateral reproduction matrix.

Let `K=K_{3,3}`.  A saturated physical side-three state is the union of two disjoint
perfect matchings.

## 1. Six physical saturated states

### Theorem CMR1278 -- PROVED

Every saturated physical side-three state is the complement in `K` of one perfect
matching.  Conversely the complement of every perfect matching is the union of the
other two matchings in one of the two 1-factorisations containing it.

There are exactly six physical saturated states.

### Proof

Two disjoint perfect matchings use six of the nine cells.  Every row and column has
one unused cell, so the three unused cells form a perfect matching `F`.  Thus the
state is `K\setminus F`.  Distinct omitted matchings give distinct complements, and
`K_{3,3}` has `3!=6` perfect matchings. ∎

Layer order gives several labelled representations of one physical complement but
does not change its physical triple potential.

## 2. Exact potential classification

Write an omitted matching as the permutation tuple

\[
(f(0),f(1),f(2)).
\]

### Theorem CMR1279 -- PROVED BY COMPLETE SIX-STATE CLASSIFICATION

The six complements have the following physical triple potentials.

\[
\begin{array}{c|c|c}
\text{omitted matching}&\Phi(K\setminus F)&\text{unique target if dirty}\\
\hline
(0,1,2)&0&-\\
(2,1,0)&0&-\\
(0,2,1)&1&\{(0,2),(1,1),(2,0)\}\\
(1,0,2)&1&\{(0,2),(1,1),(2,0)\}\\
(1,2,0)&1&\{(0,0),(1,1),(2,2)\}\\
(2,0,1)&1&\{(0,0),(1,1),(2,2)\}
\end{array}
\]

Hence exactly two physical states are clean and every dirty state has exactly one
collinear triple.

### Proof

For each of the six omitted permutations, list the remaining six cells and test
the `binom(6,3)=20` triples by the integer determinant.  The table is the complete
list.  Equivalently, row/column reflection pairs the first two clean complements,
the next two anti-diagonal dirty complements, and the last two diagonal dirty
complements. ∎

This is a finite theorem, not an asymptotic claim.

## 3. The unique response changes the omitted matching

Let a labelled dirty state be `S=O\cup M`, where `O,M` are disjoint perfect
matchings, and let `F=K\setminus S` be the omitted matching.  Choose a target cell
`e` in layer `M`.

### Theorem CMR1280 -- PROVED

The CMR1175 forbidden matching through `e` is exactly `M`, and the unique response
matching is exactly `F`.  Thus the response state is

\[
\boxed{Q=O\cup F=K\setminus M.}
\]

The same statement holds with the two layers interchanged.

### Proof

Relative to the fixed opposite matching `O`, there are exactly two disjoint
side-three completions.  One is the current layer `M`; since it contains `e`, it is
the unique forbidden extension through `e`.  The other is the unused matching
`F`, which is the response of CMR1175. ∎

Thus a response replaces the omitted matching by the old targeted layer matching.

## 4. Every target-cell response is clean

### Theorem CMR1281 -- PROVED

Let `S` be any dirty saturated side-three state and `T` its unique physical target.
For either layer and every target cell `e` belonging to that layer, the unique
response state `Q` of CMR1280 satisfies

\[
\boxed{\Phi(Q)=0.}
\]

There are exactly twenty-four labelled target-cell response instances, and all are
strict improvements from one to zero.

### Proof

Use the six-state table CMR1279 and the response rule CMR1280.  For each of the four
dirty omitted matchings, the target has three cells.  Each cell has one selected
layer label, and exchanging the ordered layer representation gives the second
labelled realization.  Direct substitution shows that the old targeted matching
`M`, which becomes the new omitted matching, is either `(0,1,2)` or `(2,1,0)`, the
two clean rows of the table.

Equivalently, enumerate the twelve ordered disjoint layer pairs.  The eight dirty
ordered pairs carry three target cells each, giving twenty-four responses, all with
zero new potential. ∎

No collateral triple is created in any side-three target response.

## 5. Restricted side-three hosts

### Theorem CMR1282 -- PROVED

At a restricted side-three owner containing a dirty selected minimum, choose any
cell of its unique target and form the singleton response matching.

1. If the singleton is feasible, it is a strict improvement to potential zero.
2. If it is infeasible, one missing response edge is an inclusion-minimal blocker;
   restoring it gives the deficiency-one unit-wall product with child-side sum two.

### Proof

The first branch is CMR1281.  The second is CMR1176 and CMR1150--CMR1156. ∎

Thus restricted availability cannot turn the side-three dirty state into a terminal
positive minimum.

## 6. Exact side-three offspring matrix

Take the four dirty physical target classes of CMR1279 as parent credit classes and
use any of the CMR1281 target responses.

### Theorem CMR1283 -- PROVED

Every chosen response creates zero new physical triple credits.  Hence the exact
offspring matrix is

\[
\boxed{A_3=0_{4\times4},}
\]

and

\[
\boxed{\rho(A_3)=0.}
\]

The all-ones weight vector is an exact integer certificate with unit slack.

### Proof

Every response state is clean by CMR1281.  Therefore every offspring count is zero.
The remaining statements are immediate. ∎

Any coarser dirty-target grouping has the same zero row.

## 7. Gluing the side-three base

### Theorem CMR1284 -- PROVED UNDER THE BLOCK-TRIANGULAR OWNER HYPOTHESIS

If a product, unit-wall or lifted-interface offspring matrix places the side-three
base as a diagonal terminal block and all incoming collateral lies in upper
off-diagonal blocks, then any subcritical earlier blocks glue with `A_3` by
CMR1273.

### Proof

The diagonal side-three block has the positive certificate `A_3\mathbf1=0<\mathbf1`.
Apply constructive block gluing upward. ∎

The remaining issue is proving the required owner ordering for cross-factor
collateral, not the side-three response itself.

## 8. Side-three endpoint

### Corollary CMR1285 -- PROVED

The side-three joint factor is completely resolved for target-versus-collateral
purposes.

1. Two of its six physical saturated states are clean.
2. Each dirty state has one target.
3. Every labelled target-cell response is clean.
4. Restricted blockage gives strict unit-wall descent to sides summing to two.
5. Its exact credit-reproduction block has spectral radius zero.

Together with the clean root side-two base and rigid residual side-two contraction,
the small matching base contributes no positive offspring obstruction.  The open
spectral work begins at side four and in cross-factor/fixed-interface coupling.

No all-`n` theorem is claimed.  Six-state classification, twenty-four target
responses, restricted singleton blockage and the zero offspring matrix are checked
in
[`scripts/verify_prime_power_side_three_strict_improvement.py`](../scripts/verify_prime_power_side_three_strict_improvement.py).
