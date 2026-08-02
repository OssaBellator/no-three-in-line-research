# Arithmetic rematching blocks have linear internal collateral

PX184 proves that the uniform degree-two-forbidden rematching bank can have
\(\Omega(t\log t)\) expected internal collateral.  This chapter gives a structured
replacement when the movable row and column sets are arithmetic progressions of
prime length.

The construction is the extremal finite-field permutation

\[
g(1)=1,
\qquad
g(x)=\frac{x}{x-1}\quad(x\ne1).
\]

Its graph is one affine conic plus one exceptional point.  It has exactly
\((p-1)/2\) modular collinear triples, and an affine-orbit averaging argument
allows it to avoid an arbitrary degree-two forbidden-position system after at
most two local swaps.

The result closes the **internal** rank-three collateral term for arithmetic
neutralization blocks.  Mixed triples with one or two background points remain
to be controlled separately.

## 1. The conic permutation

Let \(p\) be an odd prime and define

\[
g:\mathbb F_p\to\mathbb F_p
\]

by the displayed formula.  For \(x\ne1\),

\[
(g(x)-1)(x-1)=1.
\]

Thus all graph points except

\[
P=(1,1)
\]

lie on the nondegenerate affine conic

\[
(x-1)(y-1)=1.
\]

## Theorem PX185 -- PROVED

The map \(g\) is a permutation and its graph satisfies:

1. every affine line contains at most three graph points;
2. every collinear triple contains \(P\);
3. the exact number of modular collinear triples is

   \[
   \boxed{\frac{p-1}{2}.}
   \]

### Proof

The Möbius map \(x\mapsto x/(x-1)\) is a bijection from
\(\mathbb F_p\setminus\{1\}\) to itself, and no value in its image is \(1\).
Adding \(g(1)=1\) gives a permutation.

A line meets a nondegenerate conic in at most two points, so any graph line has
at most two conic points and possibly \(P\).  Hence every triple contains \(P\).

A nonvertical line through \(P\) has form

\[
y-1=m(x-1).
\]

On the conic this becomes

\[
m(x-1)^2=1.
\]

It has two conic intersections exactly when \(m\) is a nonzero square.  Every
such slope gives one triple with \(P\), and different slopes give different
triples.  There are \((p-1)/2\) nonzero square slopes. \(\square\)

This is the classical permutation attaining the minimum possible number of
finite-field collinear triples.

## 2. Avoiding two forbidden partial matchings

Let \(F\subseteq\mathbb F_p^2\) have row and column degree at most two.  Consider
the affine similarity orbit

\[
g_{\lambda,a,b}(x)
=
\lambda g\!\left(\lambda^{-1}(x-a)\right)+b,
\]

where

\[
\lambda\in\mathbb F_p^*,
\qquad a,b\in\mathbb F_p.
\]

Every orbit map is a permutation, retains exactly \((p-1)/2\) modular triples,
and has maximum line occupancy three.

For every prescribed cell \((x,y)\), exactly \(p(p-1)\) of the
\(p^2(p-1)\) parameter triples use that cell.  Hence a uniform orbit map hits
one prescribed cell with probability \(1/p\).

## Theorem PX186 -- PROVED

For every prime \(p\ge11\) and every forbidden set \(F\) of row and column
degree at most two, there is a permutation

\[
\pi:\mathbb F_p\to\mathbb F_p
\]

such that

1. \((x,\pi(x))\notin F\) for every row \(x\);
2. \(\pi\) differs from one affine-orbit copy of \(g\) on at most four rows;
3. its number of modular collinear triples is at most

   \[
   \boxed{16p.}
   \]

### Proof

Since \(|F|\le2p\), a uniform orbit map has expected number of forbidden hits at
most two.  Choose one, say \(\sigma\), with at most two bad rows.

Fix one bad row \(x\).  Swap its image with the image in a helper row \(u\).
The swap is allowed provided

\[
(x,\sigma(u))\notin F,
\qquad
(u,\sigma(x))\notin F.
\]

The first condition excludes at most two helper rows because row \(x\) has at
most two forbidden columns.  The second excludes at most two because column
\(\sigma(x)\) has at most two forbidden rows.  Avoid \(x\), the other bad row,
and previously used helpers.  For \(p\ge11\), an allowed helper remains.

The swap repairs \(x\) without creating a new forbidden hit.  Repeating once if
necessary gives an \(F\)-avoiding permutation and changes at most four rows.

Let \(k\le4\) be the number of changed graph points.  The unchanged part lies on
a conic plus one point, so every line contains at most three unchanged points.
For one new point, the number of pairs of unchanged points collinear with it is
at most

\[
3(p+1),
\]

because there are \(p+1\) projective directions and at most three pairs on one
line.  Pairs involving another new point contribute only \(O(kp+k^2)\) in
total.  Adding the original \((p-1)/2\) triples gives the convenient bound
\(16p\). \(\square\)

The constant is deliberately loose.  In the finite verifier, random forbidden
systems through \(p=19\) always admitted an orbit map with no forbidden hits at
all.

## 3. Transport to a real arithmetic block

Let the movable row and column sets be

\[
R=\{r_0+A x:x\in\mathbb F_p\},
\qquad
C=\{c_0+B y:y\in\mathbb F_p\},
\]

represented by \(p\) distinct integers in the scalar grid, with \(A,B\ne0\).
Normalize every forbidden position in \(R\times C\) to a cell of
\(\mathbb F_p^2\), apply PX186, and select

\[
(r_0+Ax,\ c_0+B\pi(x)).
\]

Any real collinearity among three selected points has determinant zero over the
integers.  After removing the nonzero factor \(AB\) and reducing modulo \(p\),
the corresponding normalized graph triple is modularly collinear.

## Corollary PX186a -- PROVED

Every prime-length arithmetic rematching block with forbidden row and column
degree at most two has a perfect matching which avoids all forbidden positions
and contains at most

\[
\boxed{16p}
\]

real collinear triples internally.

Thus the internal rank-three cost is linear rather than the
\(\Theta(p\log p)\) cost of the uniform bank from PX184.

## 4. Consequence for rectangle repair

PX186a supplies an exact structured alternative to the uniform banks in
PX73, PX76, and PX79 whenever their movable endpoint rows and columns contain a
common prime-length arithmetic block.

It does not yet finish the neutralization inequality:

- triples containing one replacement point and two fixed background points;
- triples containing two replacement points and one fixed background point

must still be controlled.  However, the previously intrinsic-looking
rank-three logarithm is gone.

The next repair theorem can therefore be stated as an inverse-additive
alternative:

1. either the movable row/column endpoint pairs contain a large coupled
   arithmetic block, where PX186a gives linear internal collateral;
2. or the row and column sets have additive expansion, which should disperse
   the \(T_1,T_2,T_3\) certificate masses directly.

This links the rectangle decoder to the repository's existing inverse-additive
and quotient-structure machinery rather than to polynomial direction
protection.

## Verification

Run

```bash
python scripts/verify_product_arithmetic_rematching.py
```

The verifier checks the exact conic triple count and line cap, searches every
affine-orbit parameter against random unions of two forbidden permutations,
performs the local repairs, and verifies the \(16p\) bound through prime order
nineteen.  It also checks real-to-modular transport on arithmetic row and column
progressions.
