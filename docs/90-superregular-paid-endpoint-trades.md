# Superregular paid endpoint trades

The endpoint-derangement theorem PP3ih samples from the complete off-diagonal
endpoint rectangle. Consequently every unary-invalid cell must be charged in the
first moment. This chapter removes that loss: delete all unary-invalid cells from
the host first, then sample a spread perfect matching from the remaining
superregular graph.

The result applies to both structured alternatives from PP3hy. A resource bank
supplies linear removal credit through endpoint-disjoint blocker pairs, while a
blocker star supplies concentrated removal credit through its centre.

## 1. The source-safe endpoint host

Let

\[
R_0=\{(x_i,y_i):i\in[q]\}
\]

be points from one permutation layer of a saturated no-three source `S`. Put

\[
S_0=S\setminus R_0.
\]

Make a balanced bipartite graph `G_safe` with left vertices `x_1,...,x_q` and
right vertices `y_1,...,y_q`. Join `x_i` to `y_j` when all of the following hold.

1. `i != j`, so the selected endpoint moves.
2. The cell `(x_i,y_j)` is not already occupied by `S_0`.
3. The cell `(x_i,y_j)` lies on no secant through two points of `S_0`.

For an edge `a=(x_i,y_j)` of `G_safe`, write `cell(a)=(x_i,y_j)`.

### Proposition PP3in -- PROVED

Every perfect matching `M` of `G_safe` gives a saturated configuration

\[
S_M=S_0\cup\{\operatorname{cell}(a):a\in M\}
\]

with the following properties.

1. Every point of `R_0` moves.
2. No inserted cell collides with `S_0`.
3. No triple consists of one inserted cell and two points of `S_0`.

Every remaining possible new triple contains two or three inserted cells.

#### Proof

A perfect matching uses every selected old column and every selected old row
once, so deleting `R_0` and inserting its matching cells preserves every row and
column count. Conditions 1 and 2 give movement and disjointness. Condition 3
removes every one-inserted-cell triple. Since `S_0` is no-three, every remaining
new violation contains two or three inserted cells. ∎

## 2. Pair, triple, and shadow pattern counts

Let `P_G` be the number of unordered pairs of compatible edges of `G_safe`
whose two cells lie on a line through at least one point of `S_0`. Count each edge
pair once, regardless of anchor multiplicity.

Let `Q_G` be the number of three-edge matchings in `G_safe` whose three cells
are collinear.

Fix the controller-entry universe `V` and its pair weight `w_V` from PP3ij. Define

\[
A_G
=
\sum_{a\in E(G_{\rm safe})}
\sum_{p\in S_0}w_V(\operatorname{cell}(a),p)
\]

and

\[
B_G
=
\sum_{\substack{\{a,b\}\subseteq E(G_{\rm safe})\\
                 a,b\text{ compatible}}}
w_V(\operatorname{cell}(a),\operatorname{cell}(b)).
\]

Finally, let

\[
\mathcal C(R_0)
\]

be the exact removal credit from PP3ib.

## 3. Superregular paid-trade theorem

### Theorem PP3io -- PROVED FROM SR1

Fix constants `delta>0` and sufficiently small `epsilon>0`. There are constants
`K=K(delta)` and `q_0` such that the following holds for `q>=q_0`.

Assume `G_safe` is `(epsilon,delta)`-superregular. If

\[
\boxed{
K^2\dfrac{P_G}{q^2}
+
K^3\dfrac{Q_G}{q^3}
+
\dfrac{1}{\mathcal C(R_0)}
\left(
K\dfrac{A_G}{q}
+
K^2\dfrac{B_G}{q^2}
\right)
<1,
}
\]

then some perfect matching `M` of `G_safe` is source-admissible and strictly
decreases the controller-shadow potential `Psi_V`.

#### Proof

Choose a uniformly random perfect matching of `G_safe`. By SR1, after increasing
`K` if necessary, every prescribed matching of rank `r<=3` has probability at
most

\[
\left(\dfrac Kq\right)^r.
\]

Let `X_M` count the anchored pair patterns and collinear triple patterns selected
by `M`. Then

\[
\mathbb E X_M
\le
K^2\dfrac{P_G}{q^2}
+
K^3\dfrac{Q_G}{q^3}.
\]

Proposition PP3in has already removed all unary source-invalid patterns.
Similarly, the expected controller-shadow insertion cost satisfies

\[
\mathbb E\mathcal I(M)
\le
K\dfrac{A_G}{q}
+
K^2\dfrac{B_G}{q^2}.
\]

Therefore

\[
\mathbb E\left(
X_M+
\dfrac{\mathcal I(M)}{\mathcal C(R_0)}
\right)<1.
\]

Some matching has the displayed random variable below one. Since `X_M` is a
nonnegative integer, it vanishes. Proposition PP3in then shows that `S_M` is
source-admissible, while

\[
\mathcal I(M)<\mathcal C(R_0).
\]

Apply PP3id. ∎

This theorem strictly strengthens PP3ih whenever unary-invalid cells are
numerous but the remaining host is still superregular.

## 4. Near-complete hosts are automatically superregular

Let `F` be the bipartite complement of `G_safe` inside the complete selected
endpoint rectangle. It includes the diagonal and every collision or fixed-secant
cell.

### Proposition PP3ip -- PROVED

Suppose `0<eta<1` and every vertex of `F` has degree at most `eta q`. Then
`G_safe` is

\[
(\sqrt\eta,1-\eta)
\]

-superregular.

#### Proof

Every vertex of `G_safe` has degree at least `(1-eta)q`. Let `X,Y` be subsets of
the two parts with

\[
|X|,|Y|\ge\sqrt\eta q.
\]

Using the forbidden degree bound from the left gives

\[
e_F(X,Y)\le eta q|X|,
\]

and hence

\[
\dfrac{e_F(X,Y)}{|X||Y|}
\le
\dfrac{eta q}{|Y|}
\le\sqrt\eta.
\]

Thus every such pair has allowed density at least `1-sqrt(eta)`. The global
allowed density lies between `1-eta` and `1`; consequently every large-pair
density differs from the global density by at most `sqrt(eta)`. ∎

### Corollary PP3iq -- PROVED

If the maximum unary-forbidden row or column degree is `o(q)`, then the endpoint
host is superregular with density `1-o(1)`. For every fixed positive `delta`, the
paid theorem PP3io therefore applies for all sufficiently large `q` once its
pair, triple, and normalized collateral expression is below one.

Conversely, failure of this automatic superregularity condition exposes one old
column or one old row having `Omega(q)` unary-invalid replacement cells. This is
a second-generation endpoint-shadow star, localized inside the endpoint
rectangle rather than across all macro candidates.

## 5. Credit in the two structural branches

### Proposition PP3ir -- PROVED

The removal credit in PP3io satisfies the following lower bounds.

1. If `R_0` comes from a resource matching of size `q`, then

   \[
   \mathcal C(R_0)\ge q.
   \]

2. If `R_0` contains a source point `r` that belongs to `D` blocker incidences in
   the fixed controller-entry universe, then

   \[
   \mathcal C(R_0)\ge D.
   \]

#### Proof

The first statement is PP3ic. For the second, every blocker incidence witnessed
by a pair `{r,p}` contributes at least one unit to `w_V(r,p)`. Since `r` is
removed, all those terms occur in the old-pair part of the removal credit. ∎

Thus the blocker-star centre can be paid directly; it does not first need to be
converted into endpoint-disjoint rays.

## 6. Revised conversion target

The open conversion theorem now has a sharper alternative.

- **Direct density:** the controller-aware global graphs satisfy PP3gl.
- **Paid superregular trade:** extract an endpoint rectangle for which the unary
  forbidden graph has maximum degree `o(q)` and the PP3io normalized expression
  is below one.
- **Localized failure:** a failed extraction yields either a high unary-forbidden
  endpoint row/column or one of the pair, triple, unary-shadow, or pair-shadow
  concentrations in PP3io.

The unary cell population is no longer itself an obstruction when its complement
is superregular. What remains is a regularization/conversion statement for the
localized endpoint cores.