# Mixed-collision factorization for ordered-box CRT assembly

The naive CRT obstruction from CMCRT1 can be sharpened into an exact geometric
classification.

Let \(u,v>1\) be coprime and put

\[
N=uv.
\]

All coordinates below are standard representatives in \([N]\).

## 1. Synchronized two-layer CRT saturation

Let

\[
f_{u,0},f_{u,1}:\mathbb Z_u\to\mathbb Z_u,
\qquad
f_{v,0},f_{v,1}:\mathbb Z_v\to\mathbb Z_v
\]

be permutation pairs with

\[
f_{m,0}(x)\ne f_{m,1}(x)
\qquad(m\in\{u,v\}).
\]

For \(arepsilon\in\{0,1\}\), define \(f_{N,\varepsilon}\) coordinatewise by

\[
f_{N,\varepsilon}(x)\equiv f_{u,\varepsilon}(x\bmod u)\pmod u,
\]

\[
f_{N,\varepsilon}(x)\equiv f_{v,\varepsilon}(x\bmod v)\pmod v.
\]

### Theorem CMCRT2 — PROVED

The graphs of \(f_{N,0}\) and \(f_{N,1}\) are disjoint permutations. Their
union contains exactly two points in every row and column.

### Proof

A coordinatewise CRT combination of permutations is a permutation of
\(\mathbb Z_N\). At a fixed column, equality of the two global rows would imply
equality modulo both `u` and `v`, contradicting either local pointwise
disjointness condition. Two disjoint permutation layers give exact
saturation. ∎

This completes the algebraic saturation part of synchronized CRT assembly.

## 2. Exact mixed-collision determinant

Consider three distinct global grid points \(P_0,P_1,P_2\). Suppose

\[
P_1\equiv P_0\pmod u
\]

coordinatewise, while

\[
P_2\equiv P_0\pmod v.
\]

Define the integer scaled collision vectors

\[
A=\frac{P_1-P_0}{u},
\qquad
B=\frac{P_2-P_0}{v}.
\]

### Theorem CMCRT3 — PROVED

The exact integer determinant factors as

\[
\Delta(P_0,P_1,P_2)
=uv\det(A,B)
=N\det(A,B).
\]

Consequently the three standard lifts are real collinear if and only if the
two scaled collision vectors \(A,B\) are parallel.

### Proof

The two displacement vectors from \(P_0\) are \(uA\) and \(vB\). Bilinearity
of the two-dimensional determinant gives

\[
\det(uA,vB)=uv\det(A,B).
\]

The integer determinant vanishes exactly when \(A\) and \(B\) are linearly
dependent over neither \(\mathbb Q\) nor \(\mathbb R\), equivalently when they
are parallel. ∎

Thus CMCRT1's divisibility by `N` is not an uncontrolled carry: its quotient
is an explicit determinant of scaled collision directions.

## 3. Classification under local modular arc hypotheses

Let \(S_N\) be any synchronized CRT lift whose projections \(S_u,S_v\) have
the following property:

> no three distinct projected points are collinear modulo the local modulus.

### Theorem CMCRT4 — PROVED UNDER HYPOTHESES

Every real collinear triple in \(S_N\) has, after relabelling, the mixed form

\[
P_1\equiv P_0\pmod u,
\qquad
P_2\equiv P_0\pmod v,
\]

and therefore satisfies

\[
\det\left(rac{P_1-P_0}{u},
          rac{P_2-P_0}{v}ight)=0.
\]

### Proof

A real triple has determinant zero modulo each local factor. In one factor,
if all three projected points were distinct, they would violate the local
modular arc hypothesis. Hence some projected pair coincides in that factor.

The same collision pair cannot coincide in both factors, because CRT would
then make the corresponding global points equal. The collision pairs in the
two factors are therefore different. Two different edges of a three-vertex
set share a vertex, so relabel the common vertex as \(P_0\). CMCRT3 completes
the proof. ∎

## 4. Direction-separation assembly criterion

For a global candidate set \(S_N\), define

\[
\mathcal D_u
=
\left\{
\operatorname{prim}\left(\frac{P'-P}{u}\right):
P\ne P',\ P\equiv P'\pmod u
\right\},
\]

and define \(\mathcal D_v\) analogously. Directions are unoriented primitive
integer vectors.

### Corollary CMCRT5 — PROVED UNDER HYPOTHESES

Under the local modular arc hypotheses of CMCRT4, if

\[
\mathcal D_u\cap\mathcal D_v=\varnothing,
\]

then the synchronized CRT lift contains no real collinear triple.

### Proof

A real triple would yield parallel nonzero scaled collision vectors by
CMCRT4, so their primitive directions would lie in both direction sets. ∎

This is a positive ordered-box CRT criterion. It replaces the insufficient
statement “one factor sees three distinct points” by the exact requirement
that the two local collision channels use disjoint scaled directions.

## 5. Remaining CRT target

The next construction problem is concrete:

1. choose synchronized local permutation pairs with modular line caps;
2. compute or control their global scaled collision-direction sets;
3. separate the `u`- and `v`-collision directions, perhaps by affine shears,
   digit placement, or one factor reserved solely as a direction breaker.

The identities are checked in
[`scripts/verify_crt_mixed_collision.py`](../scripts/verify_crt_mixed_collision.py).
