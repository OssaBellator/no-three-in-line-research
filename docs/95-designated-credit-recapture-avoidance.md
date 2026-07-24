# Designated-credit recapture avoidance

A PP3hy resource matching of size `q` supplies at least `q` units of removal
credit, one from each selected bad controller entry. The weighted first moment
PP3ja treats possible reappearance of those same incidences as generic insertion
cost. This chapter instead forbids their direct recapture at the unary level.

Each designated blocker line meets the endpoint rectangle in a partial matching.
When the union of those partial matchings has small row and column degree, it can
be added to the PP3ix low-support event family at negligible cost.

## 1. Designated blocker data

Let the selected resource entries be

\[
(z_i,e_i,\{r_i,s_i\}),
\qquad i\in[q],
\]

where:

- `z_i` is the bad macro candidate cell;
- `e_i` is its controller edge;
- `{r_i,s_i}` is the selected noncontroller blocker pair;
- the endpoints `r_i` lie in one common permutation layer and form the removed
  endpoint set `R_0`;
- `s_i` remains in the source.

The resource-disjoint conclusion PP3hy ensures that the `r_i,s_i` and
controllers are all mutually disjoint in the required sense.

For every `i`, let `L_i` be the set of off-diagonal endpoint cells `a` satisfying

\[
z_i,\ s_i,\ a
\quad\text{collinear}.
\]

### Proposition PP3jo -- PROVED

Each `L_i` is a partial matching in the endpoint rectangle: it contains at most
one cell in every selected old column and at most one cell in every selected old
row.

#### Proof

The chosen blocker line `z_i s_i` is neither vertical nor horizontal. Indeed, an
axis blocker through a movement or refill candidate contains its controller edge,
whereas the selected pair is noncontroller. A nonaxis line meets each old column
and each old row in at most one cell. ∎

Let

\[
F_{\rm rec}
=
\bigcup_{i=1}^q L_i
\]

be the simple recapture-forbidden graph.

## 2. Exact preservation of designated credit

### Proposition PP3jp -- PROVED

Suppose an endpoint permutation avoids every cell of `F_rec`. Then none of the
`q` designated controller-shadow incidences is reinserted through its unchanged
endpoint `s_i`.

Equivalently, for every `i`, the pair consisting of `s_i` and the new endpoint
cell in the selected old column of `r_i` does not block `z_i`.

#### Proof

A replacement cell `a` and `s_i` block `z_i` exactly when `a` lies on the line
`z_i s_i`, which is the definition of `L_i`. ∎

Other inserted pairs may still block `z_i`, and replacement cells may create
shadow at unrelated controller entries. Those contributions remain in the
residual insertion cost.

## 3. Recapture degree and the permutation local lemma

Let

\[
d_{\rm rec}
=
\max\{\Delta_L(F_{\rm rec}),\Delta_R(F_{\rm rec})\}.
\]

### Proposition PP3jq -- PROVED

Adding all recapture cells as unary canonical bad events increases the PP3ix
resource mass by at most

\[
\boxed{
\dfrac{d_{\rm rec}}q.
}
\]

Thus recapture avoidance is asymptotically free whenever

\[
d_{\rm rec}=o(q).
\]

#### Proof

A prescribed permutation cell has probability `1/q`. At one left or right
resource there are at most `d_rec` recapture cells. ∎

Since every `L_i` is a partial matching, the crude multiset incidence is `q^2`.
The useful quantity is the degree of the simple union: many designated lines may
pass through the same forbidden cell, and one unary exclusion then protects all
of those credit units simultaneously.

## 4. Residual shadow weights

For an endpoint cell `a` and unchanged source point `p`, define

\[
w_{\rm des}(a,p)
=
|\{i:p=s_i,\ a\in L_i\}|.
\]

Put

\[
w_{\rm res}(a,p)
=
w_V(a,p)-w_{\rm des}(a,p).
\]

This is nonnegative because every counted designated incidence is one of the
controller entries included in `w_V(a,p)`.

Define

\[
A_{\rm res}
=
\sum_{a}
\sum_{p\in S_0}w_{\rm res}(a,p),
\]

where the first sum is over allowed endpoint cells after all unary restrictions.
Keep the binary insertion-shadow weight

\[
B_G
\]

from PP3io; it includes the possibility that two inserted cells jointly reblock
a designated entry.

### Theorem PP3jr -- PROVED

Assume the combined source-validity and recapture low-event family has PP3ix
resource mass at most `1/24`. If

\[
\boxed{
9\dfrac{P_4}{q^2}
+
27\dfrac{Q_{\ge4}}{q^3}
+
3\dfrac{A_{\rm res}}{q^2}
+
9\dfrac{B_G}{q^3}
<1,
}
\]

then some endpoint permutation is source-admissible and strictly decreases the
controller-shadow potential.

#### Proof

Condition on avoiding the combined low-event family. PP3iy gives `(3/q)^r`
spread up to rank three. The first two terms bound the remaining source-invalid
pair and triple events.

The expected residual unary and binary insertion cost is at most

\[
3\dfrac{A_{\rm res}}q
+
9\dfrac{B_G}{q^2}.
\]

Recapture avoidance protects all `q` designated credit units by PP3jp, so the
removal credit available against residual insertion cost is at least `q`.
Divide the expected cost by `q` and apply the integer-plus-normalized-cost
argument from PP3ja. ∎

This theorem can be strictly stronger than PP3ja even when the total unary
shadow weight `A_G` is large, because all direct recapture multiplicity has been
removed before averaging.

## 5. Rich recapture alternative

### Corollary PP3js -- PROVED

For every fixed `rho>0`, either

\[
d_{\rm rec}<\rho q
\]

and recapture avoidance costs less than `rho` of the PP3ix mass budget, or one
selected endpoint row or column contains at least `rho q` distinct cells lying on
designated blocker lines.

The latter is a **rich recapture fibre**. It consists of many distinct designated
lines whose intersections with one endpoint row or column land back in the
selected endpoint coordinate set.

#### Proof

This is the definition of maximum degree in the simple union `F_rec`. ∎

A rich recapture fibre is more structured than the original controller-shadow
star: all its lines are tied to resource-disjoint bad entries and all return to
one endpoint coordinate fibre. It is a natural target for a rectangle or
tomographic switch.

## 6. Remaining weighted conversion problem

Combine PP3jn with PP3jr. Under sparse unary endpoint shadow, source validity is
already available on a subbank of size `q=m^kappa`, `0<kappa<1/40`. The resource
trade improves the controller source whenever:

1. the recapture union has degree `o(q)`;
2. the residual unary shadow satisfies `A_res=o(q^2)`;
3. the binary insertion shadow satisfies `B_G=o(q^3)`.

Failure now has one of three explicit forms:

- a rich recapture fibre;
- a residual unary-shadow core;
- a residual binary-shadow core.

The guaranteed credit itself no longer needs to be averaged away.