# Rank-three barrier for fixed-partition cyclotomic mappings

The protected-spread reduction PX96 suggests importing structured families of
strong complete mappings from finite-field theory.  First-order cyclotomic
mappings are a natural candidate: on each multiplicative coset they are linear,
and many existence theorems are known.

This chapter shows that the same local linearity is fatal for the rank-three
spread needed by PX97.  The obstruction is independent of how many admissible
cyclotomic mappings exist or how they are weighted.

Let \(p\) be prime and let \(d\mid p-1\).  Let \(C\le\mathbb F_p^\ast\) be the
unique subgroup of index \(d\), with

\[
m=|C|=\frac{p-1}{d}.
\]

Its cosets are

\[
C_1,\ldots,C_d.
\]

A first-order cyclotomic mapping of this fixed partition has the form

\[
f(0)=0,
\qquad
f(x)=a_jx
\quad(x\in C_j),
\]

for coefficients \(a_j\in\mathbb F_p\).  We may restrict to any subfamily, such
as the strong complete members, and put any probability distribution on it.

## Theorem PX111 -- PROVED

Suppose

\[
m\ge3.
\]

For every probability distribution on first-order cyclotomic mappings of the
fixed index-\(d\) partition, some three-edge matching cylinder \(E\) satisfies

\[
\boxed{
\Pr(E\subseteq\operatorname{graph}(f))
\ge
\frac1{p-1}.
}
\]

Consequently its normalized rank-three spread constant is at least

\[
\boxed{
K_3
\ge
\frac{(p)_3}{p-1}
=p(p-2).
}
\]

In particular, no such family has rank-three spread with an absolute constant.
The conclusion holds a fortiori for every fixed-index family as \(p\to\infty\).

### Proof

For a coset \(C_j\), a three-element subset \(X\subset C_j\), and a nonzero
multiplier \(a\in\mathbb F_p^\ast\), define the cylinder

\[
E(j,X,a)
=
\{(x,ax):x\in X\}.
\]

These cylinders are all distinct.  The row set recovers \(j\) and \(X\), while
one row-image edge recovers \(a\).

The complete labelled family has size

\[
d\binom m3(p-1).
\]

Every realized cyclotomic map contains exactly

\[
d\binom m3
\]

members of this family: on each coset, every three rows use the one local
multiplier \(a_j\).  Therefore

\[
\sum_{j,X,a}
\Pr\bigl(E(j,X,a)\subseteq\operatorname{graph}(f)\bigr)
=
d\binom m3.
\]

Averaging over the \(d\binom m3(p-1)\) cylinders gives one with probability at
least \(1/(p-1)\).  Multiplying by \((p)_3\) gives the normalized bound.
\(\square\)

No permutation, complete-mapping, or strong-complete hypothesis was used.  The
barrier is caused solely by three rows sharing one deterministic local slope.

## Corollary PX111a -- PROVED

A first-order cyclotomic route can avoid PX111 only if every multiplicative
coset has size at most two, equivalently

\[
\boxed{
d\ge\frac{p-1}{2}.}
\]

Thus bounded-index and even moderately growing-index cyclotomic constructions
cannot prove PX97.  Any viable cyclotomic spread theorem would need an index
linear in \(p\), random movement of the coset partition, or additional
nonlinear mixing inside every coset.

## 2. Piecewise-affine variant

The same argument remains an obstruction if one allows a separate intercept on
each fixed coset,

\[
f(x)=a_jx+b_j.
\]

There are at most \(p(p-1)\) nonconstant affine rules on one coset.  Averaging
over the corresponding labelled cylinders gives some three-edge cylinder of
probability at least

\[
\frac1{p(p-1)},
\]

and therefore normalized constant at least

\[
\frac{(p)_3}{p(p-1)}=p-2.
\]

So fixed-coset piecewise-affine families still miss constant rank-three spread
by a linear factor whenever a coset contains three rows.

## 3. Consequence for the switching program

PX111 explains why the quartic sign cubes and bounded-index cyclotomic mapping
families cannot replace global switching expansion.  Both retain deterministic
three-row affine packets.

The PX98--PX110 dynamics move in the necessary direction: overlapping bridge
trades destroy the fixed local slope packages and the finite-defect design
provides many exits.  The remaining task is to show that repeated bridges erase
all persistent three-row affine packets while maintaining bounded reverse
congestion.

## 4. Verification

Run

```bash
python scripts/verify_product_cyclotomic_rank_three_barrier.py
```

The verifier enumerates all coefficient vectors for the small cases
\((p,d)=(7,2),(13,3),(13,4)\), reproduces every labelled-cylinder population,
and checks the exact averaging identity.  It also verifies the symbolic bounds
for every divisor \(d\) of \(p-1\) through prime order 101.
