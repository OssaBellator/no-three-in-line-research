# Spread derangements and the endpoint-trade first moment

PP3id reduces controller-shadow improvement to a source-admissible derangement
whose insertion cost is below the removal credit. Uniform derangements already
supply the required fixed-rank spread. This chapter converts source validity
and weighted shadow collateral into one explicit normalized inequality.

## 1. Fixed-rank spread of uniform derangements

Let `q>=6`, and choose a uniform derangement

\[
\sigma\in S_q.
\]

A prescribed rank-`r` partial assignment consists of distinct indices
`i_1,...,i_r`, distinct values `j_1,...,j_r`, and requirements

\[
\sigma(i_k)=j_k,
\qquad i_k\ne j_k.
\]

### Proposition PP3ie -- PROVED

For `1<=r<=3`, every prescribed partial assignment has probability at most

\[
\boxed{
\dfrac{24}{q^r}.
}
\]

For `r=1`, the exact probability is `1/(q-1)`.

#### Proof

Uniform derangements are invariant under permutations fixing one index and
acting transitively on the other `q-1` values, proving the rank-one formula.

For general fixed `r`, the number of permutations extending the prescribed
partial assignment is at most `(q-r)!`. The number of derangements is at least
`q!/3` for `q>=2`. Hence the probability is at most

\[
\dfrac{3(q-r)!}{q!}
=
\dfrac3{(q)_r}.
\]

For `q>=6` and `r<=3`, every factor in `(q)_r` is at least `q/2`, so this is at
most `3\cdot2^r/q^r<=24/q^r`. ∎

Thus the inserted permutation cells form a rank-three `24/q`-spread family.

## 2. Source-validity pattern counts

Use the endpoint set

\[
R_0=\{(x_i,y_i):i\in[q]\}
\]

and unchanged source

\[
S_0=S\setminus R_0.
\]

For `i\ne j`, write

\[
c_{ij}=(x_i,y_j).
\]

Only off-diagonal cells can be selected by a derangement.

Define the following distinct forbidden patterns.

- `C`: off-diagonal cells that already belong to `S_0` or lie on a secant
  through two points of `S_0`.
- `P`: unordered compatible pairs of off-diagonal cells whose line contains a
  point of `S_0`. Compatible means their row and column indices are both
  distinct, so one permutation can select them together.
- `Q`: compatible triples of off-diagonal cells that are collinear.

Each cell, pair, or triple is counted once regardless of witness multiplicity.

### Proposition PP3if -- PROVED

Let `X_sigma` be the number of source-invalid pattern events selected by the
uniform derangement. Then

\[
\boxed{
\mathbb E X_\sigma
\le
24\left(
\dfrac Cq+
\dfrac P{q^2}+
\dfrac Q{q^3}
\right).
}
\]

If `X_sigma=0`, then `S_0 union R_sigma` is a set of distinct points with no
three collinear.

#### Proof

A forbidden cell, pair, or triple fixes respectively one, two, or three values
of the permutation. Apply PP3ie and sum.

The unchanged set `S_0` is no-three. Every new violation therefore uses one,
two, or three inserted cells and belongs to the corresponding pattern family.
The collision condition is included in `C`. ∎

## 3. Weighted insertion-shadow counts

Use the controller-shadow weights `w` from PP3ib. Define

\[
A
=
\sum_{i\ne j}
\sum_{p\in S_0}w(c_{ij},p)
\]

and

\[
B
=
\sum_{\substack{\{c_{ij},c_{k\ell}\}\text{ compatible}}}
w(c_{ij},c_{k\ell}).
\]

### Proposition PP3ig -- PROVED

The endpoint-trade insertion cost satisfies

\[
\boxed{
\mathbb E\mathcal I(\sigma)
\le
24\left(
\dfrac Aq+
\dfrac B{q^2}
\right).
}
\]

#### Proof

The unary part of `mathcal I` is the sum of the displayed cell weights over
selected cells. Each cell has selection probability at most `24/q`.
The binary part is the sum of pair weights over selected compatible pairs, and
each pair has probability at most `24/q^2`. Sum by linearity. ∎

The weights may be highly nonuniform; only their total normalized mass matters.

## 4. One-shot improvement theorem

### Theorem PP3ih -- PROVED

Suppose `R_0` comes from a resource matching of size `q`, so its removal credit
satisfies

\[
\mathcal C(R_0)\ge q.
\]

If

\[
\boxed{
24\left(
\dfrac Cq+
\dfrac P{q^2}+
\dfrac Q{q^3}
+
\dfrac A{q^2}+
\dfrac B{q^3}
\right)<1,
}
\]

then some endpoint derangement is source-admissible and strictly decreases the
controller-shadow incidence potential.

#### Proof

For a random derangement, consider

\[
Y_\sigma
=
X_\sigma+
\dfrac{\mathcal I(\sigma)}q.
\]

Propositions PP3if and PP3ig give `E Y_sigma<1`, so some derangement satisfies
`Y_sigma<1`. Since `X_sigma` is a nonnegative integer, this forces

\[
X_\sigma=0.
\]

It also gives

\[
\mathcal I(\sigma)<q\le\mathcal C(R_0).
\]

Apply PP3id. ∎

This is an exact paid-trade endpoint: source validity and controller-shadow
collateral share one unit budget.

## 5. Density form

### Corollary PP3ii -- PROVED

It is sufficient that

\[
C=o(q),
\qquad
P+A=o(q^2),
\qquad
Q+B=o(q^3).
\]

More generally, any fixed positive slack in the normalized PP3ih expression
produces a strict potential decrease.

#### Proof

Substitute into PP3ih. ∎

At the resource-bank scale

\[
q=\Omega(m^{21/40}),
\]

these are the natural rank-one, rank-two, and rank-three shadow thresholds.
They match the fixed-rank spread exponents of the endpoint permutation bank.

## 6. Failure concentration

If PP3ih fails, at least one of the following normalized quantities is bounded
below by an absolute constant:

\[
\dfrac Cq,
\qquad
\dfrac{P+A}{q^2},
\qquad
\dfrac{Q+B}{q^3}.
\]

Thus every failed resource-bank conversion exposes one of:

1. a dense forbidden-cell or source-secant shadow on the endpoint rectangle;
2. a quadratic anchored-pair or unary insertion-shadow core;
3. a cubic inserted-triple or pair-collateral core.

These are exact clone-space-style obstruction classes on the selected endpoint
rectangle. Protected rectangles, tomographic trades, or a second resampling
layer may be targeted at the specific rank carrying the failed mass.
