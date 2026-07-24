# The strong-complete exact-cover hypergraph

The affine-orbit route asks for one strong-complete seed with small secant and
affine-triangle multiplicities. This chapter records the exact sparse
perfect-matching host in which those seeds live.

Let \(p>3\) be prime. Take four vertex classes

\[
R=C=D=S=\mathbb F_p.
\]

For every ordered pair \((x,y)\in\mathbb F_p^2\), define the four-edge

\[
e(x,y)=\bigl(x,\ y,\ x-y,\ x+y\bigr)
\in R\times C\times D\times S.
\]

Write \(\mathcal H_p\) for the resulting four-partite four-uniform hypergraph.

## Theorem PX138 -- PROVED

Perfect matchings of \(\mathcal H_p\) are in bijection with strong-complete
mappings

\[
f:\mathbb F_p\to\mathbb F_p.
\]

Under the correspondence, the matching is

\[
M_f=\{e(x,f(x)):x\in\mathbb F_p\}.
\]

### Proof

A perfect matching uses every row vertex exactly once, so it selects one edge
\(e(x,f(x))\) for each \(x\). Covering the column class says that \(f\) is a
permutation. Covering the difference and sum classes says respectively that

\[
x\mapsto x-f(x)
\quad\hbox{and}\quad
x\mapsto x+f(x)
\]

are permutations. These are exactly the strong-complete conditions. The
converse is immediate. \(\square\)

## Theorem PX139 -- PROVED

The hypergraph \(\mathcal H_p\) has the following exact properties.

1. Every vertex has degree \(p\).
2. Any two vertices in distinct classes lie in at most one common edge.
3. Consequently \(\mathcal H_p\) is linear.
4. Let \(F\) be any matching of size \(k\), and delete all vertices covered by
   \(F\). Every remaining vertex in the residual hypergraph has degree at least
   
   \[
   \boxed{p-3k.}
   \]

### Proof

Fixing any one coordinate of \(e(x,y)\) leaves one free field parameter, so the
degree is \(p\). Any two coordinates from distinct classes determine \(x,y\)
uniquely: for the pair \((D,S)\), use

\[
x=\frac{D+S}{2},
\qquad
y=\frac{S-D}{2},
\]

and all other pairs are simpler. Thus the codegree is at most one.

Fix a remaining vertex \(v\). One deleted matching edge contributes three
deleted vertices outside the class of \(v\). By linearity, each such vertex can
remove at most one edge through \(v\). Hence at most \(3k\) of the original
\(p\) incident edges disappear. \(\square\)

The residual estimate is uniform under every prescribed cylinder of bounded
rank. It identifies the missing probabilistic theorem precisely: construct a
perfect-matching measure in this sparse linear host whose extension ratios stay
of order \(1/p\) after deleting at most three matching edges.

## Theorem PX140 -- PROVED

The affine strong-complete mappings are

\[
f_{r,b}(x)=rx+b,
\qquad
r\notin\{0,1,-1\},
\qquad b\in\mathbb F_p.
\]

They have these exact extension counts.

1. There are \(p(p-3)\) affine strong-complete mappings.
2. Every one-edge cylinder of \(\mathcal H_p\) is contained in exactly \(p-3\)
   affine perfect matchings.
3. Every compatible two-edge cylinder is contained in exactly one affine
   perfect matching.
4. A compatible three-edge cylinder is contained in an affine perfect matching
   exactly when its input and output affine ratios satisfy
   
   \[
   t=s.
   \]
   
   In that case the affine extension is unique.

### Proof

The three maps \(f_{r,b}\), \(x-f_{r,b}(x)\), and \(x+f_{r,b}(x)\) are affine
permutations exactly when \(r,1-r,1+r\) are nonzero. This gives the total count.

For one edge \((x,y)\), every allowed slope \(r\) determines the unique intercept
\(b=y-rx\). For two compatible edges, their unique secant slope is nonzero,
not one, and not minus one: the three exclusions follow respectively from the
column, difference, and sum vertices being distinct. Thus the secant line gives
one affine extension.

For three edges, the same affine line contains the third graph point exactly
when the row ratio and image ratio agree, namely \(t=s\). \(\square\)

## Consequence: exact rank-two spread and affine rank-three freezing

The uniform affine measure has ideal rank-one and constant-factor rank-two
cylinders:

\[
\Pr(e\in M)=\frac1p,
\qquad
\Pr(e_1,e_2\in M)=\frac1{p(p-3)}.
\]

But an affine three-edge cylinder has the same probability as its two-edge
subcylinder. Its normalized rank-three constant is therefore

\[
\frac{(p)_3}{p(p-3)}
=\frac{(p-1)(p-2)}{p-3}
=\Theta(p).
\]

This is the exact-cover version of the near-affine barrier PX101. Nonlinear
perfect matchings are needed only to flatten the third-order extension counts;
the first two ranks are already solved by elementary affine matchings.

## Verification

Run

```bash
python scripts/verify_product_strong_complete_exact_cover.py
```

The verifier checks the matching correspondence, regularity, linearity,
residual degree bound, and all affine extension counts on small prime fields.
