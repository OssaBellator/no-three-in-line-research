# Endpoint-host regularization and support-rank thinning

The paid theorem PP3io needs a superregular source-safe endpoint host. This
chapter shows that sparse unary obstruction already gives such a host after a
small deterministic pruning. It also records the exact random-thinning law for
the remaining pair, triple, and shadow patterns.

## 1. Tied endpoint indices

Let

\[
R_0=\{(x_i,y_i):i\in[Q]\}
\]

lie in one permutation layer. The old column `x_i` and old row `y_i` are tied:
removing endpoint `i` removes both resources. For `I subseteq [Q]`, put

\[
R_I=\{(x_i,y_i):i\in I\}
\]

and let `G_safe[I]` be the endpoint host induced by the left columns and right
rows indexed by `I`.

Write `F` for the bipartite complement of `G_safe` on the full `Q by Q`
endpoint rectangle. Let

\[
\theta=\dfrac{|E(F)|}{Q^2}.
\]

## 2. Deterministic high-degree pruning

### Theorem PP3is -- PROVED

Assume `theta<1/16`. There is a set `I subseteq [Q]` of size

\[
\boxed{
|I|\ge(1-2\sqrt\theta)Q
}
\]

such that every left and right vertex of the forbidden graph induced by `I` has
degree at most

\[
\sqrt\theta Q.
\]

Consequently `G_safe[I]` is

\[
\left(
\sqrt{\dfrac{\sqrt\theta}{1-2\sqrt\theta}},
1-\dfrac{\sqrt\theta}{1-2\sqrt\theta}
\right)
\]

-superregular.

#### Proof

Let `L_bad` be the left indices whose forbidden degree exceeds
`sqrt(theta)Q`. Since the sum of left forbidden degrees is `theta Q^2`,

\[
|L_{\rm bad}|\le\sqrt\theta Q.
\]

The same bound holds for the corresponding set `R_bad` of right indices. Delete
an endpoint index whenever either its left or right copy is bad. Thus

\[
I=[Q]\setminus(L_{\rm bad}\cup R_{\rm bad})
\]

has the displayed size. Restricting the opposite part cannot increase a
forbidden degree, so every remaining forbidden degree is at most
`sqrt(theta)Q`.

Put `q=|I|` and

\[
\eta=\dfrac{\sqrt\theta Q}{q}
\le
\dfrac{\sqrt\theta}{1-2\sqrt\theta}.
\]

Apply PP3ip to the induced host. ∎

### Corollary PP3it -- PROVED

If `theta=o(1)`, then the endpoint bank contains a subbank of size

\[
(1-o(1))Q
\]

whose source-safe host has density `1-o(1)` and is `o(1)`-superregular.

For a resource matching, every retained endpoint still carries its own distinct
blocker-credit unit. Hence the pruned bank has removal credit at least `|I|`.

If the conclusion cannot be applied with `theta=o(1)`, then the endpoint
rectangle itself contains `Omega(Q^2)` unary-invalid cells. If `theta=o(1)` but
one insists on retaining every endpoint, the only obstruction removed by the
pruning is a set of at most `2sqrt(theta)Q` endpoint indices with unusually high
forbidden degree.

## 3. Endpoint-index support rank

A cell `(x_i,y_j)` uses the endpoint-index support `{i,j}`. A finite cell pattern
`Z` uses

\[
\operatorname{supp}(Z)
=
\bigcup_{(x_i,y_j)\in Z}\{i,j\}.
\]

For a family `mathcal Z_h` of weighted or unweighted patterns having support
size exactly `h`, let `N_h` denote its total weight.

### Proposition PP3iu -- PROVED

Choose a uniform `q`-subset `I` of `[Q]`. The expected total weight of patterns
from `mathcal Z_h` whose support is contained in `I` is exactly

\[
\boxed{
\mathbb E N_h(I)
=
\dfrac{(q)_h}{(Q)_h}N_h.
}
\]

#### Proof

A fixed `h`-element support is contained in a uniform `q`-subset with probability

\[
\dfrac{\binom{Q-h}{q-h}}{\binom Qq}
=
\dfrac{(q)_h}{(Q)_h}.
\]

Sum the pattern weights by linearity. ∎

This law applies to:

- unary forbidden cells, with support rank one or two;
- anchored inserted-cell pairs, with support rank two through four;
- inserted collinear triples, with support rank three through six;
- unary insertion-shadow weights, with support rank one or two;
- pair insertion-shadow weights, with support rank two through four.

## 4. Simultaneous thinning endpoint

For a resource bank, let `P_h,Q_h,A_h,B_h` be the support-rank decompositions of
the PP3io counts on the full `Q`-endpoint rectangle. Thus

\[
P_G=\sum_{h=2}^4P_h,
\qquad
Q_G=\sum_{h=3}^6Q_h,
\]

and analogously for `A` and `B` over their possible support ranks.

### Theorem PP3iv -- PROVED

Fix `q<=Q`. There is a `q`-endpoint subbank for which the non-unary part of the
PP3io expression, using the resource-credit bound `mathcal C>=q`, is at most

\[
\boxed{
K^2\sum_{h=2}^4
\dfrac{(q)_h}{(Q)_h}\dfrac{P_h}{q^2}
+
K^3\sum_{h=3}^6
\dfrac{(q)_h}{(Q)_h}\dfrac{Q_h}{q^3}
+
K\sum_{h=1}^2
\dfrac{(q)_h}{(Q)_h}\dfrac{A_h}{q^2}
+
K^2\sum_{h=2}^4
\dfrac{(q)_h}{(Q)_h}\dfrac{B_h}{q^3}.
}
\]

More generally, the same conclusion holds jointly with any finite collection of
nonnegative support-ranked diagnostics by adding them to the random objective.

#### Proof

Choose `I` uniformly among the `q`-subsets. Apply PP3iu to every pattern family
and substitute the resulting expected counts into the PP3io expression. Some
choice of `I` is no larger than the expectation. The retained resource endpoints
still supply at least `q` removal-credit units. ∎

The theorem is most useful for patterns whose support rank exceeds the number of
selected matching edges in the corresponding bad event. For example, a
four-index anchored pair receives an additional thinning factor of order
`(q/Q)^2` after normalization by `q^2`. Low-support patterns do not dilute and
are the genuine structured cores.

## 5. Combined regularization alternative

### Corollary PP3iw -- PROVED

A resource endpoint bank converts successfully whenever one can choose
`q->infinity` so that:

1. its induced unary forbidden density tends to zero;
2. after the PP3is pruning, the retained size is `(1-o(1))q`;
3. the support-ranked PP3iv expression tends to zero.

Then the pruned host is superregular by PP3is and the paid trade exists by
PP3io.

Failure has one of the following localized forms.

1. **Dense unary rectangle:** `Omega(q^2)` unary-invalid cells.
2. **High endpoint row or column:** one endpoint index has `Omega(q)` unary
   forbidden degree.
3. **Low-support pair core:** rank-two or rank-three anchored/shadow patterns
   carry positive normalized mass.
4. **Low-support triple core:** rank-three inserted or shadow patterns carry
   positive normalized mass.

High-support diffuse patterns can be diluted by endpoint thinning; only these
low-support cores survive every such reduction.

## 6. Revised remaining theorem

The controller-shadow conversion problem has now been reduced twice.

- Unary-invalid cells are absorbed into a superregular host after high-degree
  pruning.
- High endpoint-index support is diluted by random subbank selection.

The unresolved statement is therefore a low-support conversion theorem for the
four explicit obstruction classes in PP3iw, together with the existing
blocker-star branch.