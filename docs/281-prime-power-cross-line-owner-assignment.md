# Cross-line collateral is one exact edge-assignment cost

Fix an old state `S=O union M`, target `e in M`, and the extension-free bank

\[
\mathcal B_e=\operatorname{PM}(H_e),
\qquad H_e=K_{n,n}\setminus(O\cup\{e\}).
\]

For response `R`, put `E^+(R)=R\setminus M` and use the absolute edge order.
For `a in E^+(R)` and a nonaxis line `L` through `a`, define

\[
z_{a,L}(R)=
\left|[O\cup(R\cap M)\cup\{b\in R\setminus M:a\prec b\}]\cap L\right|.
\]

### Theorem CMR1422 -- PROVED

\[
\boxed{\gamma_e(a,R)=\sum_{L\ni a}\binom{z_{a,L}(R)}2.}
\]

### Proof

A new triple is owned by `a` exactly when its other two selected cells are not
earlier entering edges.  Their pair determines a unique line through `a`. ∎

### Theorem CMR1423 -- PROVED

\[
\boxed{N(R)=\sum_{a\in R}\gamma_e(a,R),}
\]

with zero load on nonentering edges.

Let

\[
p_e(a)=\Pr(a\in R),
\qquad
g_e(a)=\mathbb E[\gamma_e(a,R)\mid a\in R].
\]

### Theorem CMR1424 -- PROVED

\[
\boxed{\mathbb E N(R)=\sum_ap_e(a)g_e(a).}
\]

### Theorem CMR1425 -- PROVED

The matrix `p_e(x,y)`, zero on forbidden edges, is doubly stochastic:

\[
\sum_yp_e(x,y)=1,
\qquad
\sum_xp_e(x,y)=1.
\]

### Proof

Every response matching uses one edge in each row and column. ∎

Define

\[
\mathcal A_e(g)=
\max_{Q\in\operatorname{PM}(H_e)}\sum_{a\in Q}g_e(a).
\]

### Theorem CMR1426 -- PROVED

\[
\boxed{\mathbb E N(R)\le\mathcal A_e(g)}
\]

and

\[
\boxed{
\mathcal A_e(g)=
\min\left\{\sum_x\alpha_x+\sum_y\beta_y:
\alpha_x+\beta_y\ge g_e(x,y)\text{ on }E(H_e)\right\}.
}
\]

### Proof

The marginal matrix belongs to the bipartite perfect-matching polytope.  Apply
integrality and assignment duality. ∎

### Theorem CMR1427 -- PROVED

If rational dual potentials satisfy the edge inequalities and

\[
\boxed{\sum_x\alpha_x+\sum_y\beta_y<D_S(e),}
\]

some extension-free response has potential below `Phi(S)`.

### Theorem CMR1428 -- PROVED

After clearing denominators, CMR1427 becomes a finite strict integer system

\[
A_x+B_y\ge G_e(x,y),
\qquad
\sum_xA_x+\sum_yB_y<D\,D_S(e).
\]

### Corollary CMR1429 -- PROVED

Expected collateral is one shared-edge assignment cost, not an independent
sum over lines.  Every new triple is counted once and rational row/column
potentials give an independently checkable improvement certificate.  The
remaining task is quantitative control of the conditional owner weights by
rook, primitive-height, prefix and carry classes.  No all-`n` theorem is
claimed.

Checked by
[`scripts/verify_prime_power_cross_line_owner_assignment.py`](../scripts/verify_prime_power_cross_line_owner_assignment.py).
