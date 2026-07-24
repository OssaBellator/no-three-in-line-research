# Low-support endpoint cores and a permutation local lemma

PP3iw isolates low endpoint-index support as the obstruction that does not dilute
under random endpoint thinning. These low-support patterns are not arbitrary.
They are exactly short cycles and short transitions in the permutation selected
on the endpoint rectangle. This chapter removes them by a canonical-event local
lemma and retains fixed-rank spread for the remaining high-support first moment.

## 1. Canonical events in a uniform permutation

Let `pi` be a uniformly random permutation of `[q]`. A rank-`r` canonical event
is specified by a matching

\[
F=\{(i_1,j_1),\ldots,(i_r,j_r)\}
\]

in `[q] by [q]` and is the event `F subseteq pi`. Its probability is

\[
\Pr(F\subseteq\pi)=\dfrac1{(q)_r}.
\]

Two canonical events conflict when their prescribed assignments cannot occur in
one permutation. The standard Lu--Szekely theorem says that this conflict graph
is a negative dependency graph.

For a family `mathcal L` of canonical bad events of rank at most three, define
for every left resource `i` and right resource `j`

\[
\lambda_i^L
=
\sum_{E\in\mathcal L:\,i\in L(E)}\Pr(E),
\qquad
\lambda_j^R
=
\sum_{E\in\mathcal L:\,j\in R(E)}\Pr(E),
\]

and put

\[
\lambda
=
\max\left\{
\max_i\lambda_i^L,
\max_j\lambda_j^R
\right\}.
\]

### Theorem PP3ix -- PROVED FROM THE STANDARD PERMUTATION LOPSIDED LOCAL LEMMA

Assume `q>=4` and

\[
\boxed{
\lambda\le\dfrac1{24}.
}
\]

Then some permutation avoids every event in `mathcal L`.

#### Proof

For each event `E`, put `x_E=2Pr(E)`. Every event has probability at most
`1/q<=1/4`, so `x_E<=1/2`.

An event of rank at most three uses at most three left and three right resources.
Every conflicting event uses at least one of these resources. Therefore

\[
\sum_{F\sim E}x_F
\le
2\cdot6\lambda
\le\dfrac12.
\]

Hence

\[
\prod_{F\sim E}(1-x_F)
\ge
1-\sum_{F\sim E}x_F
\ge\dfrac12.
\]

It follows that

\[
x_E\prod_{F\sim E}(1-x_F)
\ge
2\Pr(E)\cdot\dfrac12
=
\Pr(E).
\]

Apply the lopsided local lemma with the canonical-event negative dependency
graph. ∎

## 2. Conditional fixed-rank spread

### Theorem PP3iy -- PROVED FROM THE PUBLISHED LLL-DISTRIBUTION THEOREM

Under PP3ix, condition the uniform permutation on avoiding every event in
`mathcal L`. For every prescribed matching `F` of rank `r<=3`,

\[
\boxed{
\Pr(F\subseteq\pi\mid\text{avoid }\mathcal L)
\le
\dfrac{e^{r/3}}{(q)_r}
\le
\left(\dfrac3q\right)^r
}
\]

for all sufficiently large `q`.

#### Proof

Use the activities `x_E=2Pr(E)` from PP3ix. A rank-`r` cylinder uses `r` left
and `r` right resources, so the total probability mass of bad events conflicting
with it is at most `2r lambda`. Thus the total activity is at most

\[
4r\lambda\le\dfrac r6.
\]

The LLL-distribution theorem bounds the conditioned cylinder probability by its
unconditioned probability times

\[
\prod_{E\sim F}(1-x_E)^{-1}.
\]

For `0<=x<=1/2`, one has `-log(1-x)<=2x`. The product is therefore at most
`exp(r/3)`. Finally `(q)_r>=(q/2)^r` for fixed `r<=3` and large `q`, while
`2e^(1/3)<3`. ∎

## 3. Classification of low-support endpoint patterns

Represent an endpoint cell `(x_i,y_j)` by the directed arc `i->j`.

### Proposition PP3iz -- PROVED

The low-support source-validity patterns have the following exact forms.

1. A compatible two-cell pattern of support rank two is

   \[
   i\to j,
   \qquad
   j\to i.
   \]

   Thus it is a directed 2-cycle.

2. A compatible two-cell pattern of support rank three is a directed two-step
   transition, in one of the forms

   \[
   i\to j\to k
   \]

   or its reversal in the selected permutation cycle structure.

3. A compatible three-cell pattern of support rank three is one of the two
   orientations of a directed 3-cycle on three endpoint indices.

#### Proof

For a compatible pair `(i,j),(k,l)`, the left indices are distinct and the right
indices are distinct. Support rank two forces `{i,k}={j,l}`, and the off-diagonal
condition leaves exactly the transposition. Support rank three forces exactly one
cross equality, `j=k` or `l=i`, producing a directed two-step path.

For three compatible arcs with support size three, their three left indices and
three right indices are the same set. They define a fixed-point-free permutation
of three elements, hence a directed 3-cycle. ∎

## 4. The low-support bad-event family

On an endpoint rectangle, let `mathcal L` contain:

1. every unary-invalid arc excluded by `G_safe`;
2. every support-rank-two anchored pair pattern;
3. every support-rank-three anchored pair pattern;
4. every support-rank-three inserted collinear triple.

Each member is a canonical event of rank one, two, or three. Its local resource
mass is exactly computable from the unary forbidden degrees, transposition
counts, transition counts, and directed-triangle counts.

The transposition and directed-triangle contributions are automatically small in
the worst case:

- at one endpoint resource there are at most `q-1` transpositions, contributing
  `O(1/q)` probability mass;
- there are at most `O(q^2)` directed triangles through one resource,
  contributing `O(1/q)` mass.

The potentially non-negligible terms are therefore:

- unary forbidden degree divided by `q`;
- anchored two-step transition count divided by `q^2`.

## 5. Paid endpoint theorem after low-support cleaning

Let `P_4` be the number of anchored pair patterns of endpoint support rank four.
Let

\[
Q_{\ge4}=Q_4+Q_5+Q_6
\]

be the number of inserted collinear triples of support rank at least four. Keep
the full controller-shadow insertion weights `A_G,B_G` and removal credit
`mathcal C(R_0)` from PP3io.

### Theorem PP3ja -- PROVED

Assume the low-support family satisfies

\[
\lambda\le\dfrac1{24}.
\]

If

\[
\boxed{
9\dfrac{P_4}{q^2}
+
27\dfrac{Q_{\ge4}}{q^3}
+
\dfrac1{\mathcal C(R_0)}
\left(
3\dfrac{A_G}{q}
+
9\dfrac{B_G}{q^2}
\right)
<1,
}
\]

then an endpoint permutation is source-admissible and strictly decreases the
controller-shadow potential.

#### Proof

Condition the uniform permutation on avoiding `mathcal L`. By PP3iy, every
remaining rank-two or rank-three prescribed matching has probability at most
`(3/q)^r`.

Avoidance of `mathcal L` removes every unary source violation, every anchored
pair of support rank two or three, and every inserted triple of support rank
three. The only source-invalid events left are the `P_4` pair patterns and the
`Q_{>=4}` triple patterns. Their expected count is at most the first two terms of
the displayed expression.

The expected insertion cost is at most

\[
3\dfrac{A_G}{q}
+
9\dfrac{B_G}{q^2}.
\]

Apply the same integer-plus-normalized-cost argument as PP3io. ∎

## 6. Transition-bounded completion criterion

### Corollary PP3jb -- PROVED

Suppose every endpoint resource has:

- at most `eta q` unary-invalid incident arcs;
- at most `mu q^2` incident support-rank-three anchored transition events.

Then

\[
\lambda
\le
eta+
mu+
O\left(\dfrac1q\right).
\]

In particular, any fixed

\[
eta+\mu<\dfrac1{24}
\]

with positive slack satisfies PP3ix for all sufficiently large `q`.

#### Proof

Unary events have probability `1/q`. Transition events have probability
`1/(q)_2`. Add the worst-case transposition and directed-triangle masses from the
previous section. ∎

## 7. New exact residual obstruction

After PP3ja, the endpoint conversion can fail only through one of the following
quantities.

1. A unary forbidden endpoint degree of order `q`.
2. An anchored transition system with order `q^2` events through one endpoint
   resource.
3. Rank-four anchored pair density `P_4/q^2`.
4. High-support inserted-triple density `Q_{>=4}/q^3`.
5. Normalized unary or binary controller-shadow insertion cost.

The rank-two transposition and rank-three directed-cycle cores are no longer
open: they are absorbed by the permutation local lemma. The main new geometric
object is the anchored two-step transition system.