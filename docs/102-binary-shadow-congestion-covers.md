# Binary-shadow congestion covers

The endpoint theorem PP3jv removes a locally sparse binary shadow family by
placing every bad pair in the permutation local lemma.  The cubic-core endpoint
PP3kt shows what happens when the maximum binary resource degree is large.  This
chapter gives a different exact reduction: cover every binary conflict by deleting
one of its endpoint cells from the matching host.

The cost of such a cover is not its cardinality.  The relevant quantity is its
maximum old-row or old-column congestion, because that is what controls whether
the remaining endpoint host stays dense and matchable.

## 1. Binary conflicts and cover congestion

Let

\[
G_0=(L,R;E)
\]

be the zero-unary-shadow endpoint host of PP3jy, with

\[
|L|=|R|=q.
\]

Let

\[
\mathcal B\subseteq\binom E2
\]

be the simple binary insertion-shadow support.  Every member `{a,b}` of
`mathcal B` consists of two compatible endpoint cells, so `a` and `b` use
distinct left and right resources.

A set `C subseteq E` is a **binary cover** when

\[
C\cap B\ne\varnothing
\qquad
\text{for every }B\in\mathcal B.
\]

Define its resource congestion by

\[
\Delta(C)
=
\max_{v\in L\cup R}
|\{a\in C:v\in a\}|.
\]

### Proposition PP3la -- PROVED

Every perfect matching of

\[
G_C:=G_0\setminus C
\]

avoids every binary insertion-shadow pair.

#### Proof

If a perfect matching contained both cells of some `B in mathcal B`, then neither
cell of `B` would belong to `C`.  This contradicts the covering property. ∎

Thus binary shadow may be converted exactly into unary host deletion.

## 2. Fractional congestion and factor-two rounding

Define the fractional congestion number

\[
\tau^*(\mathcal B)
=
\min t
\]

subject to nonnegative variables `x_a`, `a in E`, satisfying

\[
x_a+x_b\ge1
\qquad
\text{for every }\{a,b\}\in\mathcal B,
\]

and

\[
\sum_{a\ni v}x_a\le t
\qquad
\text{for every }v\in L\cup R.
\]

The constant assignment `x_a=1/2` shows that

\[
\tau^*(\mathcal B)\le q/2.
\]

### Theorem PP3lb -- PROVED

There is a binary cover `C` satisfying

\[
\boxed{
\Delta(C)\le2\tau^*(\mathcal B).
}
\]

#### Proof

Take an optimal fractional solution and put

\[
C=\{a\in E:x_a\ge1/2\}.
\]

For every conflict `{a,b}`, the inequality `x_a+x_b>=1` puts at least one
endpoint in `C`, so `C` is a cover.  For every resource `v`,

\[
\frac12|\{a\in C:v\in a\}|
\le
\sum_{a\ni v}x_a
\le
\tau^*(\mathcal B).
\]

Multiply by two. ∎

No logarithmic rounding loss is needed because every conflict has exactly two
cells.

## 3. Zero-shadow endpoint after covering

Let `P_C` count compatible pairs of edges of `G_C` whose cells have a retained
source anchor, and let `Q_C` count three-edge matchings of `G_C` whose inserted
cells are collinear.  These are the remaining source-validity conflicts after the
unary and binary shadow supports have been removed.

### Theorem PP3lc -- PROVED FROM SR1

Fix `delta>0` and sufficiently small `epsilon>0`.  There is a constant
`K=K(delta)` such that the following holds for all sufficiently large `q`.
Assume `G_C` is `(epsilon,delta)`-superregular and

\[
\boxed{
K^2\frac{P_C}{q^2}
+
K^3\frac{Q_C}{q^3}
<1.
}
\]

Then `G_C` has a perfect matching whose endpoint trade is source-admissible and
has complete insertion shadow zero.  Every endpoint bank with positive removal
credit therefore gives a strict controller-shadow improvement.

#### Proof

Choose a uniform perfect matching of `G_C`.  By SR1, each prescribed compatible
pair or triple occurs with probability at most `(K/q)^2` or `(K/q)^3`.  The
displayed union bound gives positive probability of avoiding every remaining
source-invalid pair and triple.

All unary source and unary insertion-shadow terms were removed in `G_0`.
Proposition PP3la removes every binary insertion-shadow term.  Hence the selected
trade has zero insertion cost.  Positive removal credit and PP3id give strict
improvement. ∎

This theorem replaces the binary local-lemma term by a robust matching problem
in one explicitly pruned host.

## 4. Hall rectangles created by the cover

Suppose `G_C` has no perfect matching.  Let `X subseteq L` and `Y subseteq R` be
the Hall rectangle supplied by PP3jz for `G_C`:

\[
|X|+|Y|>q,
\qquad
X\times Y\subseteq E(\overline{G_C}).
\]

### Proposition PP3ld -- PROVED

The number of cover cells in the Hall rectangle satisfies

\[
\boxed{
|C\cap(X\times Y)|
\le
\Delta(C)\min\{|X|,|Y|\}.
}
\]

Consequently at least

\[
\boxed{
|X||Y|
-
2\tau^*(\mathcal B)\min\{|X|,|Y|\}
}
\]

cells of the rectangle were already absent from `G_0`.

#### Proof

Count cover cells by their left endpoints to get at most `Delta(C)|X|`, and by
their right endpoints to get at most `Delta(C)|Y|`.  Use PP3lb.  Every other cell
of the forbidden rectangle lies in the original complement of `G_0`. ∎

In particular, if `tau^*(mathcal B)=o(q)` and both sides of the Hall rectangle
have size at least `alpha q`, then the original unary support still occupies

\[
(\alpha^2-o(1))q^2
\]

cells.  A low-congestion binary cover cannot manufacture a new macroscopic Hall
obstruction from nothing.

## 5. Exact dual obstruction

The fractional congestion problem has the following dual.  Give every binary
conflict `B` a nonnegative weight `y_B` and every endpoint resource `v` a
nonnegative price `lambda_v`.

### Theorem PP3le -- PROVED

One has

\[
\boxed{
\tau^*(\mathcal B)
=
\max\sum_{B\in\mathcal B}y_B
}
\]

where the maximum is over weights satisfying

\[
\sum_{v\in L\cup R}\lambda_v\le1
\]

and, for every endpoint cell `a`,

\[
\boxed{
\sum_{B\ni a}y_B
\le
\lambda_{\ell(a)}+\lambda_{r(a)}.
}
\]

#### Proof

Use multipliers `y_B>=0` for the constraints

\[
1-x_a-x_b\le0
\]

and multipliers `lambda_v>=0` for

\[
\sum_{a\ni v}x_a-t\le0.
\]

The Lagrangian is

\[
\sum_B y_B
+t\left(1-\sum_v\lambda_v\right)
+
\sum_a x_a
\left(
\lambda_{\ell(a)}+\lambda_{r(a)}-
\sum_{B\ni a}y_B
\right).
\]

Its infimum over nonnegative `x_a,t` is finite exactly under the displayed dual
constraints.  Finite-dimensional linear-programming duality gives equality. ∎

A large congestion requirement therefore has an exact fractional conflict-packing
certificate supported by a unit total mass of endpoint-resource prices.

## 6. Revised binary endpoint

### Corollary PP3lf -- PROVED

The binary shadow branch has the following exact alternatives.

1. `tau^*(mathcal B)=o(q)`.  Then every binary conflict can be absorbed into a
   unary cover of resource degree `o(q)`.  A superregular residual host is closed
   by PP3lc; a matching failure returns an essentially original Hall rectangle by
   PP3ld.
2. `tau^*(mathcal B)>=rho q` along a subsequence for some `rho>0`.  Then PP3le
   supplies a fractional binary-conflict packing of total weight at least
   `rho q`, normalized by endpoint prices of total mass one.

Thus the cubic binary support count is no longer the terminal parameter.  The
correct quantity is the minimum endpoint-resource congestion needed to cover all
binary conflicts.  The remaining hard binary case is a linear-congestion dual
packing, not merely a large raw conflict family.
