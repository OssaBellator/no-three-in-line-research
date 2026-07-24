# Two-scale thinning closes endpoint source validity

PP3jh leaves support-rank-four anchored pairs and support-rank-at-least-four
inserted triples. A resource bank from PP3hy has the much larger size

\[
Q=\Omega(m^{21/40}).
\]

It is not necessary to trade all `Q` endpoints simultaneously. This chapter
thins the bank to

\[
q=m^\kappa,
\qquad
0<\kappa<\dfrac1{40},
\]

and proves that every source-validity term then has vanishing normalized mass.
The remaining open issue is controller-shadow insertion cost, not preservation of
the no-three property.

## 1. Multiplicative energy of anchored rank-four pairs

Fix a retained anchor `p=(u,v)`. For endpoint indices define

\[
a_i=u-x_i,
\qquad
b_j=v-y_j.
\]

Two compatible endpoint cells

\[
(x_i,y_j),
\qquad
(x_k,y_l)
\]

are collinear with `p` if and only if

\[
\boxed{
a_i b_l=a_k b_j.
}
\]

This follows by expanding the determinant, exactly as in PP3jc.

Let

\[
r_p(n)=|\{(i,j):a_i b_j=n\}|.
\]

### Proposition PP3ji -- PROVED

For every anchor `p`,

\[
\boxed{
\sum_n r_p(n)^2
\le
(2D_m+4)Q^2,
}
\]

where `D_m=max_{n<=m^2}tau(n)=m^{o(1)}`.

#### Proof

For `n!=0`, every representation `a_i b_j=n` is a signed factorization of `n`.
Distinct endpoint columns and rows make `(i,j)` unique for a fixed factor pair,
so

\[
r_p(n)\le2\tau(|n|)\le2D_m.
\]

Therefore

\[
\sum_{n\ne0}r_p(n)^2
\le
2D_m\sum_{n\ne0}r_p(n)
\le
2D_mQ^2.
\]

For `n=0`, at most one `a_i` vanishes and at most one `b_j` vanishes. Hence
`r_p(0)<=2Q`, contributing at most `4Q^2`. ∎

### Corollary PP3jj -- PROVED

Let `P_4(Q)` be the number of distinct support-rank-four anchored pair patterns
on the complete `Q`-endpoint rectangle. Then

\[
\boxed{
P_4(Q)
=O(mD_mQ^2).
}
\]

#### Proof

For one anchor, PP3ji counts all ordered equal-product pairs, including the
rank-four compatible patterns. Sum over at most `2m` source anchors. Counting a
distinct cell pair once rather than once per anchor only decreases the result. ∎

## 2. Completion bounds for inserted triples

Let `Q_h(Q)` be the number of compatible inserted collinear triples whose
endpoint-index support has size `h`.

### Proposition PP3jk -- PROVED

One has

\[
\boxed{
Q_4(Q)=O(Q^3),
\qquad
Q_5(Q)=O(Q^4),
\qquad
Q_6(Q)=O(Q^5).
}
\]

#### Proof

A three-edge partial permutation decomposes into directed paths and directed
cycles on its endpoint-index support.

For support rank four, its structure is either a directed path of length three
or a directed 2-cycle together with one disjoint arc. Fix the structure and
three of its endpoint indices so that two cells and the old column of the third
cell are known. The line through the first two cells is nonvertical because the
matching edges have distinct left indices. It meets the prescribed old column
in at most one row, and the endpoint layer contains at most one index with that
row. Thus the fourth index is determined, giving `O(Q^3)` patterns.

For support rank five, the structure is a directed path of length two together
with one disjoint arc. Fix four indices; the fifth is determined by the same
line-column completion argument. This gives `O(Q^4)`.

For support rank six, the three arcs are index-disjoint. Fix the four indices of
two arcs and the left index of the third. Its right index is determined by the
intersection of their line with the prescribed old column. This gives
`O(Q^5)`. There are only constantly many orientations and choices of which arc
is completed. ∎

No candidate-only `Q^4 log Q` estimate is needed; endpoint-index support exposes
a unique-completion parameter in every high-support class.

## 3. Random subbank estimates

Choose a uniform `q`-subset of the `Q` tied endpoint indices. By PP3iu and the
preceding bounds,

\[
\mathbb E P_4(q)
=
O\left(
\dfrac{(q)_4}{(Q)_4}mD_mQ^2
\right)
=
O\left(
\dfrac{mD_mq^4}{Q^2}
\right),
\]

and

\[
\mathbb E Q_4(q)=O\left(\dfrac{q^4}{Q}\right),
\quad
\mathbb E Q_5(q)=O\left(\dfrac{q^5}{Q}\right),
\quad
\mathbb E Q_6(q)=O\left(\dfrac{q^6}{Q}\right).
\]

### Proposition PP3jl -- PROVED

There is a `q`-endpoint subbank satisfying

\[
\boxed{
\dfrac{P_4(q)}{q^2}
+
\dfrac{Q_4(q)+Q_5(q)+Q_6(q)}{q^3}
=
O\left(
\dfrac{mD_mq^2}{Q^2}
+
\dfrac{q+q^2+q^3}{Q}
\right).
}
\]

The same subbank may be chosen jointly with the unary and transition diagnostics
below.

#### Proof

Add the normalized nonnegative quantities to one random objective and use their
expectations. Some subset is no larger than the expected objective. ∎

## 4. Low-support regularization after thinning

Let `F_Q` be the unary forbidden graph on the original resource rectangle and
assume

\[
|E(F_Q)|=o(Q^2).
\]

Let `N_tr(Q)` be its anchored transition population. PP3je gives

\[
N_{\rm tr}(Q)
=O(QmD_m+Q^2).
\]

For a uniform `q`-subset, PP3iu gives

\[
\mathbb E|E(F_q)|
=o(q^2)
\]

and

\[
\mathbb E N_{\rm tr}(q)
=
O\left(
\dfrac{q^3mD_m}{Q^2}
+
\dfrac{q^3}{Q}
\right)
=
o(q^3)
\]

at the scales below.

### Proposition PP3jm -- PROVED

One may choose the PP3jl subbank so that, after deleting `o(q)` additional
endpoint indices:

1. every unary forbidden degree is `o(q)`;
2. every transition degree is `o(q^2)`;
3. the PP3ix low-support mass is `o(1)`;
4. the PP3jl high-support normalized source term keeps the same asymptotic bound.

#### Proof

Include `|E(F_q)|/q^2` and `N_tr(q)/q^3` in the random objective of PP3jl. They
are `o(1)` in expectation. Choose one subbank on which the entire objective is
`o(1)` plus the displayed PP3jl bound.

Delete indices of unary degree above `sqrt(o(1))q`; the number deleted is
`o(q)`. Then delete indices of transition degree above `sqrt(o(1))q^2`; again
only `o(q)` are removed because the total transition incidence is `o(q^3)`.
All source pattern counts decrease under deletion. The remaining low-support
mass is `o(1)` by PP3jb. ∎

## 5. Prime-gap-scale source-valid endpoint trade

### Theorem PP3jn -- PROVED

Let a PP3hy resource bank have size

\[
Q=\Omega(m^{21/40})
\]

and unary forbidden endpoint density `o(1)`. Fix any constant

\[
0<\kappa<\dfrac1{40}
\]

and put `q=floor(m^kappa)`.

Then the bank contains a subbank of size `(1-o(1))q` supporting a permutation
that moves every retained endpoint and preserves saturation and the no-three
property.

Moreover, conditioned on source validity, prescribed matching cylinders of rank
at most three have probability `O(q^{-r})`.

#### Proof

Apply PP3jm. Since `D_m=m^{o(1)}` and `Q=m^(21/40+o(1))`,

\[
\dfrac{mD_mq^2}{Q^2}
=
m^{-1/20+2\kappa+o(1)}
=o(1)
\]

because `kappa<1/40`. Also

\[
\dfrac{q+q^2+q^3}{Q}=o(1).
\]

Thus the PP3ix low-support mass and the PP3ja high-support source term are both
`o(1)`. Apply PP3ix, PP3iy, and then the first-moment part of PP3ja with the
controller-shadow cost omitted. The selected permutation is source-admissible.
The conditional spread is PP3iy followed by another bounded first-moment
conditioning, which changes fixed-rank probabilities only by a `1+o(1)` factor.
∎

The exponent `1/40` comes from the rank-four anchored-pair term. It is not a
prime-gap width requirement: these endpoint trades prepare the source and may be
iterated by PP3il.

## 6. What remains after source validity

Under sparse unary endpoint shadow, the resource-bank branch now always contains
a source-admissible saturation-preserving endpoint trade. To make it an improving
trade, one still needs

\[
\boxed{
\mathcal I(M)<\mathcal C(R_0),
}
\]

or a probabilistic version of this inequality.

Thus the remaining resource-bank obstruction is purely weighted
controller-shadow collateral. Source collisions and all collinear-triple classes
have been removed.