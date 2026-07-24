# Controller-shadow endpoint-permutation trades

The resource matching PP3hy produces many bad candidate entries with disjoint
controller points and endpoint-disjoint blocker pairs.  After the layer
refinement PP3hz, one may choose one blocker endpoint from each pair inside a
common perfect-matching layer.  Those endpoints can be removed simultaneously
by a permutation trade that preserves every old row and column degree.

This chapter records the exact controller-shadow potential change.  The only
remaining issue is collateral from the inserted permutation points.

## 1. Matching-layer endpoint permutations

Let

\[
 R_0=\{r_i=(x_i,y_i):i\in[q]\}
\]

be a subset of one source permutation layer.  Thus all `x_i` and all `y_i` are
distinct.  For a permutation `sigma in S_q`, put

\[
 r_i^\sigma=(x_i,y_{\sigma(i)}),
 \qquad
 R_\sigma=\{r_i^\sigma:i\in[q]\}.
\]

Assume `R_sigma` is disjoint from the unchanged source points outside `R_0`.

### Proposition PP3ia -- PROVED

Replacing `R_0` by `R_sigma` preserves exactly two source points in every old
row and every old column.

If `sigma` is a derangement, every point of `R_0` is removed.

#### Proof

The replacement keeps the same set of old columns `{x_i}` and the same set of
old rows `{y_i}`.  Each affected row and column therefore loses one point and
gains one point.  A fixed point of `sigma` reproduces `r_i`; a derangement has
none. ∎

This is a simultaneous version of disjoint alternating rectangle switches.
Every permutation decomposes into cycles, and each nontrivial cycle is a
row-column-preserving cyclic trade.

## 2. Controller-shadow incidence potential

Fix the complete movement/refill candidate-entry universe used by the
controller-aware graphs.  For two possible source points `p,q`, define

\[
 w(p,q)
\]

as the number of candidate entries whose candidate cell is collinear with
`p,q` and whose controller is neither `p` nor `q`.  Put `w(p,q)=w(q,p)` and
`w(p,p)=0`.

For a source set `S`, define the multiplicity potential

\[
 \boxed{
 \Psi(S)=\sum_{\{p,q\}\subseteq S}w(p,q).
 }
\]

Every controller-aware bad cell entry contributes at least one unit to
`Psi(S)`.  Multiple blocker witnesses for one entry are deliberately counted
with multiplicity.

### Proposition PP3ib -- PROVED

Let

\[
 S_0=S\setminus R_0,
 \qquad
 S_\sigma=S_0\cup R_\sigma.
\]

Then

\[
 \boxed{
 \begin{aligned}
 \Psi(S_\sigma)-\Psi(S)
 ={}&
 \sum_{a\in R_\sigma}\sum_{p\in S_0}w(a,p)
 +
 \sum_{\{a,b\}\subseteq R_\sigma}w(a,b)
 \\
 &-
 \sum_{r\in R_0}\sum_{p\in S_0}w(r,p)
 -
 \sum_{\{r,s\}\subseteq R_0}w(r,s).
 \end{aligned}
 }
\]

#### Proof

Pairs contained wholly in `S_0` occur in both potentials and cancel.  The
remaining old pairs are exactly those with at least one endpoint in `R_0`, and
the remaining new pairs are exactly those with at least one endpoint in
`R_sigma`.  Expand the two sums. ∎

Define the **removal credit**

\[
 \mathcal C(R_0)
 =
 \sum_{r\in R_0}\sum_{p\in S_0}w(r,p)
 +
 \sum_{\{r,s\}\subseteq R_0}w(r,s)
\]

and the **insertion cost**

\[
 \mathcal I(\sigma)
 =
 \sum_{a\in R_\sigma}\sum_{p\in S_0}w(a,p)
 +
 \sum_{\{a,b\}\subseteq R_\sigma}w(a,b).
\]

Then PP3ib is simply

\[
 \Psi(S_\sigma)-\Psi(S)
 =
 \mathcal I(\sigma)-\mathcal C(R_0).
\]

## 3. Credit supplied by a resource matching

Suppose the selected resource matching contains bad entries

\[
 (\lambda_i,e_i,\{p_i,q_i\}),
 \qquad i\in[q],
\]

and the chosen common-layer blocker endpoint is `r_i in {p_i,q_i}`.  Put
`R_0={r_i}`.

### Proposition PP3ic -- PROVED

The removal credit satisfies

\[
 \boxed{
 \mathcal C(R_0)\ge q.
 }
\]

#### Proof

For every selected entry, its candidate cell is counted in
`w(p_i,q_i)`.  The blocker pairs are endpoint-disjoint, and one endpoint of
each pair belongs to `R_0`.  Therefore the corresponding `q` incidence units
all occur among the old-pair terms defining `mathcal C(R_0)`. ∎

The credit can be much larger because one removed endpoint may destroy many
unselected blocker incidences as well.

## 4. Exact improvement endpoint

Call a permutation `sigma` **source-admissible** when

1. `R_sigma` is disjoint from `S_0`;
2. `S_0 union R_sigma` is no-three-in-line.

### Theorem PP3id -- PROVED

Let `R_0` come from a resource matching of size `q`.  If there is a
source-admissible derangement `sigma` satisfying

\[
 \boxed{
 \mathcal I(\sigma)<\mathcal C(R_0),
 }
\]

then the endpoint-permutation trade preserves saturation and strictly reduces
the controller-shadow incidence potential.

It is sufficient to have

\[
 \mathcal I(\sigma)<q.
\]

#### Proof

Saturation is PP3ia and source admissibility preserves the no-three property.
PP3ib gives the exact potential change.  The second statement uses PP3ic. ∎

Thus a positive-density controller-shadow failure is converted into a paid
permutation bank: PP3hy supplies `q=Omega(m^{21/40})` units of guaranteed
removal credit, and a successful trade only has to keep its total inserted
shadow below that credit.

## 5. SAT and local-lemma formulation

The choice of `sigma` may be encoded as a perfect matching between the selected
old columns and old rows.  The following forbidden events are exact.

- an inserted point already belongs to `S_0`;
- three inserted points are collinear;
- two inserted points and one point of `S_0` are collinear;
- one inserted point and two points of `S_0` are collinear;
- the weighted insertion shadow exceeds the available credit.

The first four are fixed-rank geometric conflicts of the same type as the
clone-space and product-state endpoints already proved on the branch.  The last
is an additive cost constraint and may be handled by first moment, alteration,
or a weighted matching measure.

## 6. Remaining conversion theorem

The controller-aware density bottleneck is now reduced to one explicit
statement.

> Given the `Omega(m^{21/40})` endpoint set from PP3hy, find a source-admissible
> derangement whose insertion cost is below its removal credit.

Failure means that every spread endpoint permutation either creates a source
triple or has large weighted boundary shadow.  This is precisely the kind of
star/collateral concentration targeted by the alternating neutralization and
protected tomographic trade machinery.
