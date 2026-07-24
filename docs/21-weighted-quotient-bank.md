# Weighted quotient-bank extraction from syndrome degrees

This chapter closes the "paid bank" gap left by the common-ratio conversion theorem. Arbitrary pair weights do not admit a constant-fraction single-ratio extraction. The weights arising from the no-three-in-line syndrome are more structured: they are induced by vertex triple degrees, with a uniformly bounded pair-overlap correction.

Throughout, let

\[
P_x=(x,a/x)\in H_a,
\qquad x\in X\subseteq\mathbb F_p^*,
\qquad |X|=k.
\]

The points \(P_x\) belong to one current permutation layer. The other current layer is a permutation \(Q\), so every column and every row contains exactly one point of \(Q\).

Let \(\mathcal T\) be any chosen family of current collinear-triple certificates. For \(x\in X\), define

\[
h(x)=|\{T\in\mathcal T:P_x\in T\}|,
\qquad
H=\sum_{x\in X}h(x).
\]

For distinct \(x,y\in X\), put

\[
c(x,y)=|\{T\in\mathcal T:P_x,P_y\in T\}|.
\]

Removing \(P_x,P_y\) destroys exactly

\[
d(x,y)=h(x)+h(y)-c(x,y)
\]

certificates from \(\mathcal T\).

## 1. Admissibility graph

The rectangle switch on \(P_x,P_y\) replaces

\[
(x,a/x),(y,a/y)
\]

by

\[
(x,a/y),(y,a/x).
\]

Call \(\{x,y\}\) inadmissible if one of the inserted cells is already occupied by the opposite layer \(Q\).

### Lemma WQ1 — PROVED

The graph of inadmissible pairs on \(X\) has maximum degree at most two.

### Proof

Write the opposite layer as a permutation \(\pi_Q\) from columns to rows. For fixed \(x\), a collision at the first inserted cell requires

\[
\pi_Q(x)=a/y,
\]

which determines at most one \(y\). A collision at the second inserted cell requires

\[
\pi_Q(y)=a/x,
\]

which also determines at most one \(y\), because \(\pi_Q\) is a bijection. Thus every \(x\) has at most two inadmissible partners. \(\square\)

This is the exact place where saturation is used in the weighted inverse theorem.

## 2. Weighted quotient averaging

Assume

\[
|X/X|\le Kk.
\]

For \(g\ne1\), let \(E_g\) be the set of admissible unordered pairs

\[
\{x,gx\}\subseteq X.
\]

The graph \((X,E_g)\) has maximum degree at most two.

For a represented ratio \(g\), define its directed vertex-weight mass

\[
B_g=
\sum_{\substack{x\in X:\ gx\in X\\ \{x,gx\}\text{ admissible}}}
\bigl(h(x)+h(gx)\bigr).
\]

### Theorem WQ2 — PROVED

Suppose \(k\ge6\). There is a nonidentity ratio \(g\) and a matching \(M\subseteq E_g\) such that

\[
\boxed{
\sum_{\{x,y\}\in M}\bigl(h(x)+h(y)\bigr)
\ge
\frac{k-3}{3(Kk-1)}H
\ge
\frac{H}{6K}.
}
\]

### Proof

Before deleting inadmissible pairs, summing over all nonidentity ratios gives

\[
\sum_{g\ne1}
\sum_{x:gx\in X}
\bigl(h(x)+h(gx)\bigr)
=2(k-1)H.
\]

Indeed, every vertex weight \(h(x)\) appears \(k-1\) times as the first endpoint and \(k-1\) times as the second endpoint.

Let \(F\) be the inadmissibility graph. Every inadmissible unordered pair is counted in the two orientations corresponding to \(g\) and \(g^{-1}\). Therefore the directed weight removed by excluding inadmissible pairs is at most

\[
2\sum_{\{x,y\}\in E(F)}(h(x)+h(y))
=2\sum_x \deg_F(x)h(x)
\le4H,
\]

using Lemma WQ1. Hence

\[
\sum_{g\ne1}B_g\ge2(k-3)H.
\]

At most \(|X/X|-1\le Kk-1\) nonidentity ratios are represented, so some \(g\) satisfies

\[
B_g\ge\frac{2(k-3)}{Kk-1}H.
\]

Let

\[
w(\{x,gx\})=h(x)+h(gx).
\]

The sum of these undirected edge weights is at least \(B_g/2\); equality can fail only because an order-two ratio counts each undirected edge twice in \(B_g\). Since \((X,E_g)\) has maximum degree two, its edges can be partitioned into at most three matchings. One matching therefore has weight at least

\[
\frac{B_g}{6}
\ge
\frac{k-3}{3(Kk-1)}H.
\]

For \(k\ge6\), this is at least \(H/(6K)\). \(\square\)

## 3. Paid common-ratio bank

Let

\[
\beta=\max_{x\ne y}c(x,y).
\]

For the matching \(M\) supplied by WQ2, let

\[
D(M)=\sum_{\{x,y\}\in M}d(x,y).
\]

### Theorem WQ3 — PROVED

There is an admissible common-ratio bank with

\[
\boxed{
D(M)
\ge
\frac{k-3}{3(Kk-1)}H-rac{\beta k}{2}.
}
\]

In particular,

\[
\boxed{
D(M)\ge\frac{H}{6K}-\frac{\beta k}{2}.
}
\]

If

\[
H\ge6K\beta k,
\]

then

\[
\boxed{D(M)\ge\frac{H}{12K}.}
\]

### Proof

The matching pairs are vertex-disjoint, so

\[
D(M)
=
\sum_{\{x,y\}\in M}
\bigl(h(x)+h(y)-c(x,y)\bigr).
\]

Apply WQ2 and use \(c(x,y)\le\beta\) and \(|M|\le k/2\). \(\square\)

## 4. Hyperbola-channel specialization

Assume the current configuration is contained in a union of \(q\) modular hyperbola channels. A real line meets each channel in at most two points. For two points in the same channel, the number of current triple certificates containing both is therefore at most

\[
\boxed{\beta\le2q-2.}
\]

### Corollary WQ4 — PROVED

If \(|X/X|\le K|X|\), \(k\ge6\), and \(H\) is the total current triple incidence on the points \(P_x\), then there is an admissible common-ratio bank satisfying

\[
\boxed{
D(M)\ge\frac{H}{6K}-(q-1)k.
}
\]

If

\[
\boxed{H\ge12K(q-1)k,}
\]

then

\[
\boxed{D(M)\ge\frac{H}{12K}.}
\]

Thus a low-quotient-complexity core whose average point syndrome is sufficiently larger than the channel count always contains a genuinely paid common-ratio bank.

## 5. Integration with common-ratio conversion

For the extracted bank, let

\[
\Theta=
\max_{i,\ z\in W_i}A_{Y_i}(z)
\]

be the maximum switched-cell secant load, and let \(\Lambda\) be the maximum aligned-anchor multiplicity from the common-ratio conversion chapter.

Because \(|M|\le k/2\), Corollary CR4 gives the following.

### Theorem WQ5 — PROVED

If

\[
\boxed{
\frac{k-3}{3(Kk-1)}H-rac{\beta k}{2}
>
k\Theta+2q\Lambda,
}
\]

then one admissible common-ratio rectangle strictly lowers the triple potential.

In the \(q\)-channel universe, it is sufficient that

\[
\boxed{
\frac{H}{6K}-(q-1)k
>
k\Theta+2q\Lambda.
}
\]

If this inequality fails and no rectangle improves, the decoder-or-structure theorem still yields either:

1. a high-load secant star through one switched candidate cell; or
2. a large multiplicatively aligned opposite-colour anchor class.

Hence the weighted extraction and conversion theorems combine into the exact transition

\[
\boxed{
\text{low quotient complexity + high syndrome}
\Longrightarrow
\text{improvement or explicit alternating structure}.
}
\]

## 6. Why arbitrary pair weights are insufficient

A statement of the form "every weighting on the pairs of a small-doubling set has one ratio carrying a constant fraction of the total weight" is false. The weight may be placed on a matching whose edges all have different ratios.

The proof above succeeds because actual syndrome weights are induced by vertex degrees:

\[
w(x,y)=h(x)+h(y)-c(x,y),
\]

and saturation makes the inadmissibility graph sparse. These two features are essential.

## 7. Remaining bottleneck

WQ5 reduces the structured high-syndrome regime to controlling two quantities:

\[
\Theta
\quad\text{and}\quad
\Lambda.
\]

The next exact target is an alternating closure inequality:

> Starting from a high-load secant star or an aligned-anchor class, enlarge the active red/blue core and prove that either the total paid incidence grows faster than its collateral bounds, or the closure enters one of the explicitly classified subgroup-coset exceptions.

This is now narrower than weighted bank extraction: the paid bank exists automatically once the core has low quotient complexity and sufficiently high average syndrome.