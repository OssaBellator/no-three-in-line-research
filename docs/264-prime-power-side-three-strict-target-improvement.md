# Every dirty full side-three grid state has an exact clean target response

CMR1174--CMR1176 construct the unique side-three response matching for one target
edge on arbitrary labelled matching vertices.  The stronger geometric conclusion
in this chapter uses the complete standard coordinate sets

\[
\{0,1,2\}\times\{0,1,2\},
\]

or an affine image obtained by translating and applying one common nonzero scale to
both coordinate axes.  It does **not** apply merely by relabelling a scattered
residual side-three factor, because arbitrary coordinate relabelling does not
preserve real collinearity.

Let `K=K_{3,3}` with the standard grid coordinates.  A saturated physical state is
the union of two disjoint perfect matchings.

## 1. Six physical saturated states

### Theorem CMR1278 -- PROVED FOR THE FULL STANDARD/AFFINE GRID

Every saturated physical state is the complement in `K` of one perfect matching.
There are exactly six physical saturated states.

### Proof

Two disjoint perfect matchings use six of the nine cells.  Every row and column has
one unused cell, so the three unused cells form a perfect matching.  Distinct
omitted matchings give distinct complements, and `K_{3,3}` has `3!=6` perfect
matchings. ∎

## 2. Exact potential classification

Write an omitted matching as `(f(0),f(1),f(2))`.

### Theorem CMR1279 -- PROVED BY COMPLETE SIX-STATE CLASSIFICATION

On the full standard grid the six complements have potentials

\[
\begin{array}{c|c|c}
\text{omitted matching}&\Phi&\text{unique target if dirty}\\
\hline
(0,1,2)&0&-\\
(2,1,0)&0&-\\
(0,2,1)&1&\{(0,2),(1,1),(2,0)\}\\
(1,0,2)&1&\{(0,2),(1,1),(2,0)\}\\
(1,2,0)&1&\{(0,0),(1,1),(2,2)\}\\
(2,0,1)&1&\{(0,0),(1,1),(2,2)\}.
\end{array}
\]

Exactly two physical states are clean and every dirty state has one target.

### Proof

For each omitted permutation, test the `binom(6,3)=20` triples by the integer
determinant.  Translation and common scaling preserve the determinant-zero
condition, so the same table holds on affine copies of the full grid. ∎

No claim is made for arbitrary scattered source and target coordinates.

## 3. The unique response changes the omitted matching

Let a labelled dirty state be `S=O\cup M`, and let `F=K\setminus S` be the omitted
matching.  Choose a target cell `e` in layer `M`.

### Theorem CMR1280 -- PROVED COMBINATORIALLY

The CMR1175 forbidden matching through `e` is `M`, the unique response matching is
`F`, and

\[
\boxed{Q=O\cup F=K\setminus M.}
\]

The same holds with the layers interchanged.

### Proof

Relative to `O`, exactly two perfect matchings are disjoint from it.  One is the
current layer `M` and contains `e`; the other is the omitted matching `F`. ∎

This combinatorial statement remains valid on arbitrary labelled side-three
factors; only the cleanliness conclusion below needs the full-grid coordinates.

## 4. Every full-grid target response is clean

### Theorem CMR1281 -- PROVED FOR THE FULL STANDARD/AFFINE GRID

For every dirty full-grid state and every labelled cell of its unique target, the
CMR1280 response satisfies

\[
\boxed{\Phi(Q)=0.}
\]

There are twenty-four labelled target-cell response instances, all strict
improvements from one to zero.

### Proof

Apply the table CMR1279 and the response rule CMR1280.  Across the eight dirty
ordered layer pairs, each of the three target cells gives a response whose new
omitted matching is one of the two clean rows. ∎

## 5. Restricted hosts on the same full vertex sets

### Theorem CMR1282 -- PROVED UNDER THE FULL-GRID COORDINATE HYPOTHESIS

At a restricted host on the same complete standard/affine side-three vertex sets:

1. a feasible singleton response improves to zero;
2. an infeasible singleton has a one-edge minimal blocker and gives the
   deficiency-one unit-wall product with child-side sum two.

### Proof

Use CMR1281 in the feasible branch and CMR1176 with CMR1150--CMR1156 in the blocked
branch. ∎

A scattered residual factor retains only the executable-or-blocked statement of
CMR1176 unless its actual coordinates are verified to be an affine full grid.

## 6. Exact full-grid offspring block

### Theorem CMR1283 -- PROVED FOR THE FULL STANDARD/AFFINE GRID

For the four dirty full-grid state-target classes, every chosen response creates
zero new physical triple credits.  Hence

\[
\boxed{A_3=0_{4\times4},\qquad\rho(A_3)=0.}
\]

The all-ones vector is an exact integer certificate with unit slack.

### Proof

Every response is clean by CMR1281. ∎

## 7. Conditional gluing

### Theorem CMR1284 -- PROVED UNDER BOTH STATED HYPOTHESES

If a product or wall decomposition contains a diagonal terminal block whose actual
coordinate sets form an affine full side-three grid, and if the offspring matrix is
block upper triangular with that block last, then earlier subcritical blocks glue
with `A_3` by CMR1273.

### Proof

Use `A_3\mathbf1=0<\mathbf1` and constructive block gluing. ∎

Neither an arbitrary three-vertex factor nor an arbitrary coordinate relabelling
satisfies the geometric hypothesis automatically.

## 8. Scoped endpoint

### Corollary CMR1285 -- PROVED

The full standard side-three root grid, and every verified affine copy of it, is
resolved for target-versus-collateral purposes: two states are clean, each dirty
state has one target, every target response is clean, and blockage gives strict
wall descent.

For scattered residual side-three factors, the valid endpoint remains CMR1176:
the unique response is feasible or blocked, but its physical collateral must be
computed in the inherited parent coordinates.

No all-`n` theorem is claimed.  The standard-grid six-state classification and
twenty-four target responses are checked in
[`scripts/verify_prime_power_side_three_strict_improvement.py`](../scripts/verify_prime_power_side_three_strict_improvement.py).
