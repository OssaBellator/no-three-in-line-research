# Cross-line collateral is one exact edge-assignment cost

CMR1372 shows that summing independent linewise upper bounds is too coarse.
The correction is to keep the shared response edge which simultaneously lies
on all of its incident lines.  Canonical last-entering ownership then turns the
complete collateral expectation into one doubly-stochastic edge-assignment
cost.

Fix an old saturated state

\[
S=O\cup M,
\]

a target edge `e in M`, and the extension-free bank

\[
\mathcal B_e=\operatorname{PM}(H_e),
\qquad
H_e=K_{n,n}\setminus(O\cup\{e\}).
\]

Fix the absolute total order on labelled physical edges from CMR1215.  For a
response `R in B_e`, put

\[
E^+(R)=R\setminus M.
\]

Every new physical triple receives its least edge in `E^+(R)` as owner.

## Exact owner load on one response edge

For `a in E^+(R)` and a nonaxis real line `L` through `a`, define

\[
z_{a,L}(R)=
\left|
\left[
O\cup(R\cap M)\cup
\{b\in R\setminus M:a\prec b\}
\right]
\cap L
\right|.
\]

### Theorem CMR1382 -- PROVED

The number of new triples owned by `a` is

\[
\boxed{
\gamma_e(a,R)
=
\sum_{L\ni a}\binom{z_{a,L}(R)}2.
}
\]

For `a notin E^+(R)`, put `gamma_e(a,R)=0`.

### Proof

Because `a` is entering, its physical cell was absent from the old state, so
every current collinear triple containing `a` is new.  Such a triple is owned
by `a` exactly when neither of its other two selected cells is an entering edge
preceding `a`.  The allowed other cells on `L` are therefore exactly those
counted by `z_{a,L}(R)`.  Choose their unordered pair.  Every pair with `a`
determines one unique real line, so the line sums are disjoint. ∎

This is the exact cross-line correction: all lines through `a` are paid by the
same matching edge.

## Exact owner partition

### Theorem CMR1383 -- PROVED

For every response `R`,

\[
\boxed{
N(R)=\sum_{a\in R}\gamma_e(a,R).
}
\]

### Proof

This is CMR1215 with the owner-fibre cardinality evaluated by CMR1382. ∎

No rank-one, rank-two or rank-three triple is counted more than once.

## Conditional owner weights

Let `R` be uniform on `B_e`.  For every allowed edge `a`, put

\[
p_e(a)=\Pr(a\in R).
\]

When `p_e(a)>0`, define

\[
\boxed{
g_e(a)=
\mathbb E[\gamma_e(a,R)\mid a\in R].
}
\]

Set `g_e(a)=0` when `p_e(a)=0`.

### Theorem CMR1384 -- PROVED

\[
\boxed{
\mathbb E N(R)
=
\sum_{a\in E(H_e)}p_e(a)g_e(a).
}
\]

Every number in this identity is rational and exactly computable from the
finite bank.  The edge marginal `p_e(a)` also has the exact rank-one rook
formula of CMR1376.

### Proof

Apply CMR1383, take expectation, and condition each summand on the event
`a in R`.  Finite uniform averages are rational. ∎

## The marginal matrix is doubly stochastic

View `p_e(a)` as an `n by n` matrix, putting zero on forbidden edges.

### Theorem CMR1385 -- PROVED

\[
\boxed{
\sum_y p_e(x,y)=1
\quad\text{for every source }x,
}
\]

and

\[
\boxed{
\sum_x p_e(x,y)=1
\quad\text{for every target }y.
}
\]

Thus `p_e` is a doubly stochastic matrix supported on `H_e`.

### Proof

Every response matching contains exactly one edge in each source row and one
edge in each target column.  Take expectations of these deterministic
identities. ∎

## Assignment and dual certificates

Define the maximum owner-assignment value

\[
\mathcal A_e(g)=
\max_{Q\in\operatorname{PM}(H_e)}
\sum_{a\in Q}g_e(a).
\]

### Theorem CMR1386 -- PROVED

\[
\boxed{
\mathbb E N(R)\le\mathcal A_e(g).
}
\]

Moreover

\[
\boxed{
\mathcal A_e(g)
=
\min
\left\{
\sum_x\alpha_x+\sum_y\beta_y:
\alpha_x+\beta_y\ge g_e(x,y)
\text{ for every }(x,y)\in E(H_e)
\right\}.
}
\]

### Proof

By CMR1385, `p_e` belongs to the bipartite perfect-matching polytope.  Its
weighted value is therefore at most the maximum integral perfect-matching
value.  The second identity is the standard primal--dual theorem for the
finite bipartite assignment problem; integrality follows from the bipartite
matching polytope. ∎

The dual variables couple all lines incident with the same source or target
vertex.  This coupling is absent from the independent-line kernel of CMR1370.

## Strict-improvement certificate

### Theorem CMR1387 -- PROVED

If there are rational row and column potentials satisfying

\[
\alpha_x+\beta_y\ge g_e(x,y)
\]

on every allowed edge and

\[
\boxed{
\sum_x\alpha_x+\sum_y\beta_y<D_S(e),
}
\]

then some extension-free response has potential strictly below `Phi(S)`.

### Proof

CMR1384 and CMR1386 bound expected new collateral by the displayed dual sum.
Every response omits `e`, hence destroys at least `D_S(e)` old targets.  The
expected new-minus-destroyed value is negative, so one response is a strict
improvement. ∎

For a restricted host, add the exact unavailable-edge penalty from CMR1380.

## Exact integer verification

### Theorem CMR1388 -- PROVED

All data in CMR1387 can be certified without floating point.  Multiply the
conditional owner weights and dual potentials by a common positive
denominator.  The certificate becomes the finite integer system

\[
A_x+B_y\ge G_e(x,y)
\]

on allowed edges and

\[
\boxed{
\sum_xA_x+\sum_yB_y<D\,D_S(e),
}
\]

where `D` is the common denominator.

### Proof

The bank, owner loads, edge marginals and conditional expectations are finite
rational quantities.  Clearing denominators preserves all weak and strict
inequalities because the multiplier is positive. ∎

## Cross-line assignment endpoint

### Corollary CMR1389 -- PROVED

The same-owner target-bank problem has the following exact normal form.

1. Canonical owner loads have the line formula of CMR1382.
2. Every new triple is counted once at one entering response edge.
3. Uniform expected collateral is one doubly-stochastic edge cost.
4. The strongest linear edge-only upper certificate is the bipartite
   assignment dual.
5. Rational row/column potentials give an independently checkable integer
   strict-improvement certificate.
6. Product and fixed-interface descendants remain off the diagonal by
   CMR1318--CMR1325.

The remaining quantitative task is to dominate the conditional edge loads
`g_e(a)` by primitive-height, prefix, quotient and carry potentials strongly
enough that the assignment dual sum is below the target load, or to include
the corresponding edge-profile classes in a subcritical upper quotient.
No all-`n` theorem is claimed.

The identities and finite assignment bounds are checked in
[`scripts/verify_prime_power_cross_line_owner_assignment.py`](../scripts/verify_prime_power_cross_line_owner_assignment.py).
