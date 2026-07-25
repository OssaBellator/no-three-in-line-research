# Exact protected spread for every fixed family of linear directions

PX170 gives exact subpower spread for the two diagonal colourings.  The same
exact-cover and completion argument works for any fixed finite family of
pairwise nonproportional linear colourings.  This chapter records the uniform
host and the resulting fixed-direction protected theorem.

Let

\[
\mathcal L=(L_1,\ldots,L_s)
\]

be a fixed family of nonzero linear forms

\[
L_j(x,y)=a_jx+b_jy
\]

over \(\mathbb F_p\).  Assume that no two coefficient vectors
\((a_j,b_j)\) are proportional.  Include the row and column forms

\[
L_1(x,y)=x,
\qquad
L_2(x,y)=y.
\]

Define the \(s\)-partite \(s\)-uniform host

\[
e(x,y)=\bigl(L_1(x,y),\ldots,L_s(x,y)\bigr).
\]

## Theorem PX171 -- PROVED

For every fixed family \(\mathcal L\) and all sufficiently large primes for
which its coefficient vectors remain pairwise nonproportional, the host has the
following exact properties.

1. It has \(p^2\) edges.
2. Every vertex has degree \(p\).
3. Every pair of vertices in distinct parts has codegree at most one.
4. Perfect matchings are exactly permutations

   \[
   f:\mathbb F_p\to\mathbb F_p
   \]

   for which every map

   \[
   x\longmapsto L_j(x,f(x))
   \]

   is a permutation.
5. After deleting a matching of size \(k\), every remaining vertex has residual
   degree at least

   \[
   \boxed{p-(s-1)k.}
   \]

### Proof

Fixing one nonzero linear form leaves one free field parameter, so every vertex
has degree \(p\).  Two nonproportional forms give an invertible two-by-two
linear system and therefore determine \((x,y)\) uniquely.  This proves
codegree one and also injectivity of the edge parametrisation.

Covering the row and column parts gives a permutation graph.  Covering every
other part is exactly the simultaneous-rainbow condition for its linear form.

A deleted matching edge contributes one deleted vertex in each of the other
\(s-1\) parts.  By linearity, each such vertex removes at most one edge through
a fixed remaining vertex.  The residual estimate follows. \(\square\)

## 2. Fixed-family exact pseudorandom completion

## Theorem PX172 -- PROVED USING EXTERNAL MATCHING THEOREMS

Fix \(s\), a family \(\mathcal L\) as above, and \(\gamma>0\).  For every
sufficiently large prime there is a simultaneous-rainbow permutation \(f\) for
\(\mathcal L\) satisfying

\[
\boxed{
\mu(f)\le p^{1+\gamma},
\qquad
\tau(f)\le p^\gamma.
}
\]

### Proof

Repeat the exact-cover construction PX141 and PX158--PX169 in the host from
PX171.  The external matching theorems are stated for every fixed uniformity,
so the replacement of four parts by the fixed number \(s\) changes only their
constants.

All structural estimates retain the required powers of \(p\):

- the host is \(p\)-regular and linear by PX171;
- the pseudorandom tuple weights for secants and affine triangles are still
  parametrised by the same scalar graph points;
- requiring compatibility in the additional linear-form parts can only delete
  tuples and reduce concentration norms;
- in the duplicated reservoir, a completion edge has at most
  \((s-1)p+O_s(1)\) old projection-collision partners, and a fixed old edge has
  at most \(s-1\) partners in one completion row;
- the five-star and high-arity bucket counts depend on the three scalar graph
  parameters, not on the number of extra labelled parts, so their exponents are
  unchanged.

Append the padded secant, triangle, and anchored tests to the polynomial-sized
test family in the first-stage theorem, then use the projection, star, and
bucket conflicts in the covering theorem exactly as in PX167 and PX169.  The
result is a perfect matching of the \(s\)-partite host whose graph has the
displayed multiplicities. \(\square\)

## 3. Protected direction families

Fix a finite set \(D\) of nonaxis primitive directions and a nonzero local
scalar \(m\).  For

\[
q=(a,b)\in D
\]

put

\[
\chi_q(x,y)=bx-amy.
\]

When the direction slopes are distinct modulo \(p\), the coefficient vectors
of

\[
x,
\qquad y,
\qquad \{\chi_q:q\in D\}
\]

are pairwise nonproportional.  Thus PX171--PX172 apply.

## Theorem PX173 -- PROVED

Fix a finite direction set \(D\) and \(\gamma>0\).  For every sufficiently
large prime there are first- and conditional second-stage distributions for
the simultaneous-rainbow problem PX96 such that every rank-\(k\) cylinder,
\(k\le3\), has probability at most

\[
\frac{p^\gamma}{(p)_k}.
\]

Consequently there is a protected distribution on pairs \((P,\Phi)\) with
joint cylinders

\[
\boxed{
\Pr\bigl(
\Phi(x_i)=y_i,
P(x_i)=w_i
\text{ for }i\in[k]
\bigr)
\le
\frac{p^{2\gamma}}{(p)_k^2}.
}
\]

### Proof

Use PX172 to choose one simultaneous-rainbow seed for the forms
\(x,y,\chi_q\).  Its affine similarity orbit preserves every linear-form
permutation condition, because

\[
L_j\bigl(\lambda u+a,\lambda f(u)+b\bigr)
=
\lambda L_j(u,f(u))+a_ja+b_jb.
\]

The cylinder calculation PX129 depends only on the graph coordinates and gives
the one-stage bound from \(\mu\) and \(\tau\).

For the conditional second stage, relabel the input by

\[
u=\Phi(x).
\]

The colourings become the same fixed linear forms

\[
bw-amu
\]

on \((u,w)\).  Choose an independent affine-orbit mapping \(h\) and put

\[
P(x)=h(\Phi(x)).
\]

The conditional cylinder bound is therefore identical.  Multiply the two
bounds as in PX97. \(\square\)

## 4. Exact remaining boundary

PX173 resolves the protected simultaneous-rainbow spread problem for every
**fixed** finite direction family, with an arbitrarily small power loss.  It
does not yet permit

\[
|D|\longrightarrow\infty
\]

with \(p\).  The external matching theorems used in PX172 keep the host
uniformity fixed, while protecting every primitive direction through height
\(H\) requires

\[
|D|=\Theta(H^2).
\]

A polynomial high-direction codegree saving needs \(H=p^\delta\), so the next
bottleneck is a growing-uniformity version of PX172, or a direction-selection
argument showing that only a much smaller subfamily of low directions must be
protected.

## Verification

Run

```bash
python scripts/verify_product_multi_direction_exact_cover.py
```

The verifier checks regularity, pair codegree, residual degree, and affine-orbit
covariance for five simultaneous linear forms at prime orders seven and eleven.
