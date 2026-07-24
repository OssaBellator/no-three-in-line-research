# Projective lift separation and radial chains

BDA3i fixes the two projective residue classes of a content-reduced
address, and BDA3j gives its unique integer factorization

\[
M^\circ
=
h
\begin{pmatrix}a\\b\end{pmatrix}
\begin{pmatrix}u&v\end{pmatrix},
\qquad
h>0,
\]

where \(a>0\), both vectors are primitive, and
\(\gcd(h,q)=1\).  The only remaining ambiguity is how many integer
lifts of the two projective classes can occur.  This note gives an
exact separation law for those lifts and isolates the only
non-directional escape as a one-dimensional radial progression.

Write

\[
\|(x,y)\|_\infty=\max\{|x|,|y|\}.
\]

Every primitive integer vector is unimodular modulo \(q\).  Two such
vectors have the same class in
\(\mathbb P^1(\mathbb Z/q\mathbb Z)\) exactly when their reductions
differ by multiplication by a unit modulo \(q\).

## BDA3k -- \(q\)-Farey separation of projective lifts

### Theorem BDA3k -- PROVED

Let

\[
d=(a,b),\qquad d'=(a',b')
\]

be distinct primitive integer vectors with \(a,a'>0\), and suppose
their reductions define the same class in
\(\mathbb P^1(\mathbb Z/q\mathbb Z)\).  Then

\[
\boxed{
q\mid ab'-ba'
}
\]

and hence

\[
\boxed{
\left|\frac ba-\frac{b'}{a'}\right|
=
\frac{|ab'-ba'|}{aa'}
\geq
\frac{q}{\|d\|_\infty\|d'\|_\infty}.
}
\]

In particular, if both norms are at most \(A\), their slopes are
separated by at least \(q/A^2\).

Consequently, let \(\mathcal D\) be any collection of such normalized
primitive vectors, all in one projective residue class, all of norm at
most \(A\), whose slopes lie in an interval of length \(W\).  Then

\[
\boxed{
|\mathcal D|
\leq
\left\lfloor\frac{WA^2}{q}\right\rfloor+1.
}
\]

The same conclusion applies to an arbitrary primitive vector
\(c=(u,v)\) with \(u\ne0\) after replacing it by its projective
orientation

\[
c^+
=
\operatorname{sgn}(u)c
=
(|u|,\operatorname{sgn}(u)v).
\]

### Proof

Equality of the projective residue classes gives a unit
\(\lambda\in(\mathbb Z/q\mathbb Z)^\times\) such that

\[
(a',b')\equiv\lambda(a,b)\pmod q.
\]

Taking the determinant proves \(q\mid ab'-ba'\).  Distinct normalized
primitive vectors cannot have equal rational slope: equality would
make them positive rational multiples, and primitivity would force the
multiple to be one.  Thus the determinant is a nonzero multiple of
\(q\), so its absolute value is at least \(q\).  Dividing by \(aa'\)
proves the separation bound.

Order the slopes in \(\mathcal D\).  Every successive gap is at least
\(q/A^2\), so an interval of length \(W\) contains at most
\(\lfloor WA^2/q\rfloor+1\) of them.  Multiplication by \(-1\) is a
unit modulo \(q\), so projective orientation preserves the residue
class and the norm. \(\square\)

## BDA4c -- fixed-atlas lifts reduce to radial progressions

Consider a family of distinct content-reduced addresses

\[
M_i^\circ=h_i d_i c_i^{\mathsf T}
\]

which have one fixed complete BDA3i atlas profile.  Equivalently, their
normalized residue matrices are equal modulo \(q\).  Suppose

\[
\|d_i\|_\infty\leq A,\qquad
\|c_i\|_\infty\leq B,
\]

the slopes of the normalized \(d_i\) lie in an interval of length
\(W_d\), and the slopes of the projectively oriented \(c_i^+\) lie in
an interval of length \(W_c\).  Put

\[
P_d=\left\lfloor\frac{W_dA^2}{q}\right\rfloor+1,
\qquad
P_c=\left\lfloor\frac{W_cB^2}{q}\right\rfloor+1.
\]

### Corollary BDA4c -- PROVED

There are at most

\[
\boxed{2P_dP_c}
\]

different ordered factor pairs \((d_i,c_i)\).  Therefore a family of
\(K\) addresses contains a subfamily of at least

\[
\boxed{
\left\lceil\frac{K}{2P_dP_c}\right\rceil
}
\]

addresses with one fixed exact pair \((d,c)\).

On such a subfamily all radial parameters obey

\[
\boxed{
h_i\equiv h_j\pmod q.
}
\]

If its matrices have height at most \(N\), then

\[
1\leq h_i\leq
H=
\left\lfloor
\frac{N}{\|d\|_\infty\|c\|_\infty}
\right\rfloor,
\]

so there are at most

\[
\boxed{
\left\lceil\frac Hq\right\rceil
}
\]

distinct members of that radial chain.

### Proof

By BDA3i, one complete atlas profile fixes the projective residue class
of each factor.  Theorem BDA3k bounds the number of normalized
direction factors by \(P_d\) and the number of projectively oriented
scale factors by \(P_c\).  Each oriented scale vector has at most the
two lifts \(c^+\) and \(-c^+\), giving at most \(2P_dP_c\) exact factor
pairs.  Pigeonhole gives the displayed subfamily size.

Fix one exact pair \(d,c\).  Since both vectors are primitive, there
are integer vectors \(\alpha,\beta\) such that

\[
\alpha^{\mathsf T}d=1,
\qquad
c^{\mathsf T}\beta=1.
\]

If \(h_i dc^{\mathsf T}\equiv h_jdc^{\mathsf T}\pmod q\), multiply on
the left by \(\alpha^{\mathsf T}\) and on the right by \(\beta\).
This gives \(h_i\equiv h_j\pmod q\).  The BDA3j product-height identity
gives the bound \(h_i\leq H\), and one residue class modulo \(q\)
contains at most \(\lceil H/q\rceil\) integers in \([1,H]\).
\(\square\)

BDA3k and BDA4c replace the unbounded integer-lift problem by two
explicit alternatives:

1. genuinely different rational factor directions are
   \(q/A^2\)- or \(q/B^2\)-separated; or
2. repeated factor directions lie on one \(q\)-spaced radial chain.

Thus a heavy fixed profile cannot hide in an arbitrary four-coordinate
lift cloud.  The remaining BDA4 work is now to charge separated
directions through the carry/wrap-center interfaces and to classify a
single radial progression through the common-ratio or subgroup-coset
interfaces.

`scripts/verify_bda_lift_separation.py` exhaustively checks determinant
divisibility, the sharp slope identity, interval packing, projective
orientation, scalar faithfulness, and radial-chain spacing for small
denominators and primitive vectors.
