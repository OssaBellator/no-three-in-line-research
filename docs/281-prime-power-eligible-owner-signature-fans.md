# Cross-line collateral is one exact edge-assignment cost

The authoritative range begins at CMR1422.  Fix an old saturated state

\[
S=O\cup M,
\]

a target edge `e in M`, and the extension-free response bank

\[
\mathcal B_e=\operatorname{PM}(H_e),
\qquad
H_e=K_{n,n}\setminus(O\cup\{e\}).
\]

For a response `R`, let `E^+(R)=R\setminus M` and use the absolute edge order
from CMR1215.

## Exact owner load

For `a in E^+(R)` and a nonaxis real line `L` through `a`, put

\[
z_{a,L}(R)=
\left|
\left[
O\cup(R\cap M)\cup\{b\in R\setminus M:a\prec b\}
\right]\cap L
\right|.
\]

### Theorem CMR1422 -- PROVED

The number of new triples owned by `a` is

\[
\boxed{
\gamma_e(a,R)=\sum_{L\ni a}\binom{z_{a,L}(R)}2.
}
\]

### Proof

A triple containing entering edge `a` is owned by `a` exactly when neither of
its other selected cells is an earlier entering edge.  On each line the
eligible other cells are precisely those counted by `z_{a,L}`.  Distinct pairs
with `a` determine distinct supporting lines. ∎

### Theorem CMR1423 -- PROVED

\[
\boxed{
N(R)=\sum_{a\in R}\gamma_e(a,R),
}
\]

where `gamma_e(a,R)=0` for nonentering edges.

### Proof

Apply the canonical owner partition CMR1215 and CMR1422. ∎

## Conditional edge weights

For uniform `R in B_e`, define

\[
p_e(a)=\Pr(a\in R),
\qquad
g_e(a)=\mathbb E[\gamma_e(a,R)\mid a\in R].
\]

### Theorem CMR1424 -- PROVED

\[
\boxed{
\mathbb E N(R)=\sum_{a\in E(H_e)}p_e(a)g_e(a).
}
\]

### Proof

Take expectation in CMR1423 and condition each summand on `a in R`. ∎

### Theorem CMR1425 -- PROVED

The marginal matrix `p_e(x,y)`, with zeros on forbidden edges, is doubly
stochastic:

\[
\sum_y p_e(x,y)=1,
\qquad
\sum_x p_e(x,y)=1.
\]

### Proof

Every response matching contains exactly one edge in each source row and each
target column.  Take expectations. ∎

## Assignment dual

Define

\[
\mathcal A_e(g)=
\max_{Q\in\operatorname{PM}(H_e)}\sum_{a\in Q}g_e(a).
\]

### Theorem CMR1426 -- PROVED

\[
\boxed{
\mathbb E N(R)\le\mathcal A_e(g)
}
\]

and

\[
\boxed{
\mathcal A_e(g)=
\min\left\{
\sum_x\alpha_x+\sum_y\beta_y:
\alpha_x+\beta_y\ge g_e(x,y)
\text{ on }E(H_e)
\right\}.
}
\]

### Proof

CMR1425 places the marginal matrix in the bipartite perfect-matching polytope.
Its weighted value is at most the maximum integral matching value.  The second
identity is bipartite assignment duality. ∎

### Theorem CMR1427 -- PROVED

If rational potentials satisfy the dual edge inequalities and

\[
\boxed{
\sum_x\alpha_x+\sum_y\beta_y<D_S(e),
}
\]

then some extension-free response has potential strictly below `Phi(S)`.

### Proof

CMR1424--CMR1426 bound expected new collateral by the dual sum, while every
response omits `e` and destroys at least `D_S(e)` old targets. ∎

### Theorem CMR1428 -- PROVED

All quantities in CMR1427 are rational.  Clearing denominators produces a
finite strict integer certificate

\[
A_x+B_y\ge G_e(x,y)
\]

on allowed edges and

\[
\sum_xA_x+\sum_yB_y<D\,D_S(e).
\]

### Proof

Multiply the rational inequalities by one common positive denominator. ∎

## Cross-line endpoint

### Corollary CMR1429 -- PROVED

Canonical collateral is now one shared-edge assignment problem rather than an
independent sum over lines.  Every new triple is counted once, all lines
through one response edge share the same edge weight, and rational row/column
potentials give an independently checkable improvement certificate.  Product
and fixed-interface descendants remain off the diagonal by CMR1318--CMR1325.
The remaining task is quantitative control of `g_e(a)` by exact rook,
primitive-height, prefix and carry classes.  No all-`n` theorem is claimed.

Checked by
[`scripts/verify_prime_power_cross_line_owner_assignment.py`](../scripts/verify_prime_power_cross_line_owner_assignment.py).
