# Mixed collateral for arithmetic conic rematching

PX186 removes the internal logarithmic cost of a prime-length arithmetic
rematching block.  This chapter records the fixed-rank spread of the same conic
family and converts it into a complete one-/two-background-point collateral
criterion.

Let

\[
g(1)=1,
\qquad
g(x)=\frac{x}{x-1}\quad(x\ne1)
\]

and use its affine similarity orbit

\[
g_{\lambda,a,b}(x)
=
\lambda g\!\left(\lambda^{-1}(x-a)\right)+b.
\]

## 1. Exact secant and triangle bounds

## Theorem PX187 -- PROVED

The conic permutation satisfies

\[
\boxed{
\mu(g)\le p+3,
\qquad
\tau(g)\le8.
}
\]

Consequently its affine-orbit distribution has normalized cylinder constants

\[
\boxed{
K_1=1,
\qquad
K_2\le1+\frac3p<2,
\qquad
K_3\le8.
}
\]

### Proof: secants

For two rows \(u,v\ne1\), put

\[
U=u-1,
\qquad V=v-1.
\]

Since

\[
g(x)=1+\frac1{x-1},
\]

the secant slope is

\[
\frac{g(v)-g(u)}{v-u}
=-\frac1{UV}.
\]

Fixing a nonzero slope fixes the product \(UV\), and therefore gives at most
\(p-1\) ordered pairs.  A secant involving the exceptional row \(1\) has slope

\[
\frac1{(v-1)^2},
\]

so a fixed slope has at most two choices in each orientation.  Thus
\(\mu(g)\le p+3\).

### Proof: affine triangles

First assume none of \(u,v,w=u+t(v-u)\) equals \(1\).  With

\[
U=u-1,
\qquad V=v-1,
\qquad W=(1-t)U+tV,
\]

the image ratio is

\[
s
=
\frac{g(w)-g(u)}{g(v)-g(u)}
=
\frac{tV}{(1-t)U+tV}.
\]

For fixed \(t,s\notin\{0,1\}\), this determines \(V/U\).  The fixed secant slope
then determines \(UV\), hence \(U^2\), giving at most two ordered pairs.

There are three exceptional cases, according as \(u=1\), \(v=1\), or \(w=1\).
In each case the remaining ratio equation is quadratic and gives at most two
ordered pairs.  Thus the total multiplicity is at most

\[
2+3\cdot2=8.
\]

The orbit constants now follow from PX129. \(\square\)

The finite verifier shows that the bounds are nearly sharp: the exact secant
maximum is either \(p+1\) or \(p+3\) in the tested prime fields, while the
triangle maximum is at most eight.

## 2. Expected mixed collateral before forbidden repairs

Let \(R\times C\) be a normalized arithmetic block of prime order \(p\), and let
\(Z\) be the fixed background point set outside the replacement matching.

Define:

- \(C_1\): the number of certificates consisting of one candidate block cell and
  two points of \(Z\);
- \(C_2\): the number of certificates consisting of two compatible candidate
  block cells and one point of \(Z\).

All collinearities here are real scalar-grid collinearities.  Real certificates
remain valid modular certificates after the arithmetic normalization.

## Lemma PX187a -- PROVED

For a uniform conic-orbit matching \(M\),

\[
\boxed{
\mathbb E\Phi(Z\cup M)-\Phi(Z)
\le
\frac{C_1}{p}
+
\frac{2C_2}{(p)_2}
+
\frac{p-1}{2}.
}
\]

### Proof

A prescribed cell has orbit probability \(1/p\).  A prescribed compatible pair
has probability at most \(2/(p)_2\) by PX187.  Sum the corresponding one- and
two-background-point certificates.  Every orbit graph has exactly
\((p-1)/2\) modular internal triples by PX185, and real triples form a subset.
\(\square\)

This removes the normalized \(T_3/(p)_3\) certificate census entirely: the
internal cost is deterministically linear.

## 3. Combining collateral with forbidden hits

Let \(F\) be the union of the original-position and opposite-layer forbidden
partial matchings.  It has row and column degree at most two and therefore at
most \(2p\) cells.

For the fixed background \(Z\), put

\[
\Lambda_1
=
\max_{z\in R\times C}
\#\{\{x,y\}\subset Z:x,y,z\text{ collinear}\},
\]

and

\[
\Lambda_2
=
\max_{\{z,z'\}\subset R\times C}
\#\{x\in Z:x,z,z'\text{ collinear}\},
\]

where the second maximum is over compatible pairs.

Set

\[
A
=
\frac{C_1}{p}
+
\frac{2C_2}{(p)_2}
+
\frac{p-1}{2}.
\]

A uniform orbit map has expected collateral at most \(A\) and expected number
of forbidden hits at most two.  Markov's inequality gives

\[
\Pr(\text{at least four hits})\le\frac12,
\]

and

\[
\Pr(\text{collateral}>3A)\le\frac13.
\]

Hence some orbit map has at most three forbidden hits and collateral at most
\(3A\).

Repair its bad rows by the image swaps from PX186.  At most three swaps are
needed, so at most six selected cells change.

## Theorem PX188 -- PROVED

For every prime \(p\ge11\), the arithmetic block has an \(F\)-avoiding perfect
matching \(M\) satisfying

\[
\boxed{
\Phi(Z\cup M)-\Phi(Z)
\le
3A
+6\Lambda_1
+6p\Lambda_2
+16p.
}
\]

### Proof

Choose the orbit map with at most three hits and collateral at most \(3A\).
PX186 repairs all hits using at most three helper swaps.  The final graph differs
from the orbit graph on at most six rows.

Every new changed point participates in at most \(\Lambda_1\) triples with two
background points, giving \(6\Lambda_1\).  Every replacement pair not already
present in the orbit graph contains at least one changed point.  There are at
most \(6p\) such pairs, and each has at most \(\Lambda_2\) background completions.
Finally PX186 bounds all internal triples after the swaps by \(16p\). \(\square\)

The constants are deliberately loose and double-count several sectors.

## 4. Structured neutralization criterion

In any clean-star, loaded-line, or radial-core endpoint whose movable rows and
columns form a prime-length arithmetic block, let \(D_*\) be the old mass
removed by the block.  If

\[
\boxed{
D_*
>
3\left(
\frac{C_1}{p}
+
\frac{2C_2}{(p)_2}
+
\frac{p-1}{2}
\right)
+6\Lambda_1
+6p\Lambda_2
+16p,
}
\]

then replacing the uniform AN1 bank by the conic rematching strictly lowers the
ordinary triple potential.

This is the first second-generation repair criterion in which the internal
rank-three term is linear with no logarithmic loss.

### Loaded-line simplification

If the current endpoint lies in the complementary regime where every selected
line has occupancy at most twelve, then

\[
\Lambda_2\le12.
\]

The repair penalty \(6p\Lambda_2+16p\) is then \(O(p)\).  Thus the only remaining
growing terms are the averaged one-point shadow \(C_1/p\), the averaged
pair shadow \(C_2/p^2\), and the maximum one-point shadow \(\Lambda_1\).

## 5. Remaining inverse-additive bridge

PX188 turns the general second-generation endpoint into a dichotomy.

1. **Arithmetic endpoint pairs.**  A coupled prime arithmetic block admits
   linear internal collateral and the explicit mixed-shadow criterion above.
2. **Additively expanding endpoint pairs.**  The absence of a large arithmetic
   block should force ratio and secant dispersion in \(C_1,C_2\), making the
   normalized mixed terms small.

The next theorem should extract one of these alternatives from the movable
endpoint pairs produced by PX72, PX75, or PX78.  This is an inverse-additive
problem on a single permutation layer, not a polynomial-direction protection
problem.

## Verification

Run

```bash
python scripts/verify_product_arithmetic_rematching.py
```

The verifier now additionally computes the exact secant and affine-triangle
multiplicities of the conic permutation through prime order nineteen and checks
\(\mu\le p+3\), \(	au\le8\), and the orbit forbidden-hit first moment.
