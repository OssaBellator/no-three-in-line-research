# Cross-line collateral is an exact edge-assignment problem

CMR1374--CMR1381 compute the uniform extension-free offspring row exactly.
Uniformity is not enough: a bank can have positive average new-minus-lost value
while still containing a strict or clean deterministic response.  The missing
operation is to let all geometric lines compete for the same response edges.

This chapter gives an exact normal form.  Assign every candidate triple to one
of the residual matching edges whose simultaneous selection would create it.
For a fixed assignment, collateral is bounded by an ordinary edge-weighted
perfect-matching cost.  Jointly optimizing the assignment and the matching is
exactly the original minimum-collateral problem.

The statements apply to any nonempty response host `G`, including a restricted
extension-free host.  If `G` has no perfect matching, the existing minimal
blocker/unit-wall theory applies instead.

## 1. Candidate prescriptions

Fix an old state `S`, a response host `G`, and a fixed part `O`.  Let `C` be any
finite family of possible new physical triple credits.  Each `T in C` has a
nonempty compatible residual prescription

\[
P_T=T\setminus O\subseteq E(G),
\qquad
1\le |P_T|\le3.
\]

Give `T` a nonnegative weight `v_T`.  For a response matching `R`, define

\[
N_v(R)=
\sum_{T\in\mathcal C}v_T\mathbf1_{P_T\subseteq R}.
\]

### Theorem CMR1382 -- PROVED

Every possible new triple in a one-layer response has one such nonempty
compatible residual prescription.  Its weighted contribution is exactly the
corresponding containment indicator in `N_v(R)`.

### Proof

The fixed cells of the triple are automatic.  Every nonfixed cell must be
selected by the response matching.  A triple which was absent before the move
contains at least one nonfixed entering cell, so the residual prescription is
nonempty.  Collinear nonaxis cells have distinct rows and columns, hence are
compatible. ∎

## 2. Edge selectors and loads

An **edge selector** is a map

\[
\sigma:\mathcal C\to E(G),
\qquad
\sigma(T)\in P_T.
\]

Define its edge load

\[
w_\sigma(a)
=
\sum_{T:\sigma(T)=a}v_T.
\]

### Theorem CMR1383 -- PROVED

For every selector and every response matching,

\[
\boxed{
N_v(R)
\le
\sum_{a\in R}w_\sigma(a).
}
\]

Thus

\[
\min_{R\in\operatorname{PM}(G)}N_v(R)
\le
\min_{R\in\operatorname{PM}(G)}
\sum_{a\in R}w_\sigma(a).
\]

### Proof

If `P_T subseteq R`, then its selected owner edge `sigma(T)` belongs to `R`, so
`v_T` appears on the right.  A nonoccurring candidate may also be charged, which
only increases the right side.  Sum over candidates. ∎

For fixed `sigma`, the right side is an ordinary minimum-cost bipartite perfect
matching problem.

## 3. Joint optimization is exact

### Theorem CMR1384 -- PROVED

\[
\boxed{
\min_{R\in\operatorname{PM}(G)}N_v(R)
=
\min_\sigma
\min_{R\in\operatorname{PM}(G)}
\sum_{a\in R}w_\sigma(a).
}
\]

### Proof

CMR1383 gives the left side at most the right side for every selector.  For the
reverse inequality, choose a response `R_*` minimizing `N_v`.  If
`P_T subseteq R_*`, select any edge of `P_T`.  Otherwise choose one edge in
`P_T setminus R_*`, which is nonempty.  Under this selector, exactly the
candidates occurring in `R_*` charge an edge of `R_*`.  Hence

\[
\sum_{a\in R_*}w_\sigma(a)=N_v(R_*).
\]

Every selector cost dominates true collateral by CMR1383, so its minimum
matching cost cannot fall below `N_v(R_*)`.  Equality follows. ∎

This equality is existential; constructing a useful selector uniformly is the
remaining geometric task.

## 4. Fractional matching form

Let `P(G)` be the bipartite perfect-matching polytope.  For `x in P(G)`, put

\[
F_v(x)=
\sum_{T\in\mathcal C}v_T
\min_{a\in P_T}x_a.
\]

### Theorem CMR1385 -- PROVED

\[
\boxed{
\min_{R\in\operatorname{PM}(G)}N_v(R)
=
\min_{x\in\mathcal P(G)}F_v(x).
}
\]

For every explicit fractional perfect matching `x`,

\[
\min_RN_v(R)\le F_v(x).
\]

### Proof

At the incidence vector of a perfect matching `R`,

\[
\min_{a\in P_T}\mathbf1_R(a)
=
\mathbf1_{P_T\subseteq R},
\]

so `F_v(1_R)=N_v(R)`.  The function `F_v` is concave as a nonnegative sum of
minima of coordinates.  If `x` is a convex combination of perfect-matching
incidence vectors, concavity gives

\[
F_v(x)\ge
\sum_R\lambda_R F_v(\mathbf1_R)
\ge
\min_RN_v(R).
\]

Extreme points are themselves available in `P(G)`, proving equality. ∎

The formula is nonconvex but exact.  It identifies the object which primitive
height, prefix and carry estimates must upper-bound.

## 5. Selector/fractional duality

### Theorem CMR1386 -- PROVED

For fixed `x in P(G)`,

\[
\boxed{
F_v(x)
=
\min_\sigma
\sum_{a\in E(G)}x_aw_\sigma(a).
}
\]

An optimal selector assigns each candidate to an edge of `P_T` having minimum
`x`-coordinate.

### Proof

The selector objective separates over candidates:

\[
\sum_ax_aw_\sigma(a)
=
\sum_Tv_Tx_{\sigma(T)}.
\]

Minimize each term independently over `a in P_T`. ∎

Thus one fractional response profile pays each candidate line exactly once,
through its least-loaded residual edge.

## 6. Deterministic improvement criterion

Let `L_v` be any certified weighted old-credit loss guaranteed by every response
in the bank; for a target-cell bank this may be the weight of all old targets
containing the omitted cell.

### Theorem CMR1387 -- PROVED

If there is a fractional perfect matching `x in P(G)` with

\[
\boxed{F_v(x)<L_v,}
\]

then `G` contains a deterministic response `R` satisfying

\[
N_v(R)<L_v.
\]

Hence the weighted live-credit potential strictly decreases.

### Proof

CMR1385 gives `min_R N_v(R)<=F_v(x)`.  Choose a minimizing response and compare
with the guaranteed old-credit loss. ∎

This is a genuinely cross-line criterion.  The same response edge can be the
least-loaded owner for candidate triples on many different real lines, but it
is paid only through its single fractional coordinate.

## 7. Restricted hosts and blocker walls

### Theorem CMR1388 -- PROVED

For a restricted response graph `G` exactly one of the following holds.

1. `G` has a perfect matching, and CMR1383--CMR1387 apply without change.
2. `G` has no perfect matching.  An inclusion-minimal missing-edge cover is an
   exact deficiency-one Hall wall; restoring one blocker gives the strict
   unit-wall product of CMR1150--CMR1157.

### Proof

The first branch uses only the nonempty perfect-matching polytope.  The second
branch is the minimal-blocker theorem already proved. ∎

Thus edge-assignment failure caused solely by availability is structural
descent, not an uncontrolled error term.

## 8. The side-five uniform obstruction is resolved by policy choice

Use the standard side-five state

\[
M=(0,1,2,4,3),
\qquad
O=(1,3,4,0,2)
\]

from CMR1372, and target the cell `e=(0,0)` in `M` while fixing `O`.

### Theorem CMR1389 -- PROVED BY COMPLETE FINITE CHECK

The uniform extension-free law has positive expected new-minus-lost credit in
the aggregate example of CMR1381, but the target bank through `(0,0)` contains
the response

\[
R=(4,1,0,2,3)
\]

with

\[
N(R)=0,
\qquad
L(R)=2.
\]

For the selector constructed from this response in the proof of CMR1384, the
minimum edge-weighted matching cost is zero.

### Proof

The displayed permutation is disjoint from `O` and omits `(0,0)`.  Direct
integer-determinant enumeration shows that `O union R` creates no new physical
triple and destroys both old targets.  The selector construction then assigns
every candidate prescription an edge outside `R`, so `R` has selector cost
zero. ∎

This example confirms the logical role of the new normal form: exact uniform
cylinder rows are useful upper quotients, but deterministic row selection can
be strictly stronger.

No all-`n` theorem is claimed.  The selector inequalities, exact minimization
identities, fractional form and finite side-five witness are checked in
[`scripts/verify_prime_power_cross_line_edge_assignment.py`](../scripts/verify_prime_power_cross_line_edge_assignment.py).
