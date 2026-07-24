# Primitive-slope factorization of relative denominator addresses

BDA3f removes absolute coarse translations but leaves four unbounded
relative quotient variables.  On an actual collinear matching triple,
those variables are not independent: the two displacement vectors share
one primitive integer direction.

Let

\[
P_i=(x_i,y_i)\in\mathbb Z^2,\qquad i=1,2,3,
\]

use three distinct rows and three distinct columns, and put

\[
U=x_2-x_1,\quad V=x_3-x_1,\quad
S=y_2-y_1,\quad T=y_3-y_1.
\]

All four differences are nonzero.

## BDA3g -- primitive-slope factorization

### Lemma BDA3g -- PROVED

The three cells are collinear if and only if there is a unique primitive
spatial direction \((a,b)\) and unique nonzero integer point scales
\(m,n\), normalized by

\[
a>0,\qquad \gcd(a,|b|)=1,
\]

such that

\[
\boxed{
(U,S)=m(a,b),
\qquad
(V,T)=n(a,b).
}
\]

Equivalently, every compatible collinear triple has one primitive
rational slope \(b/a\) and two signed positions \(m,n\) on that line
relative to \(P_1\).

If

\[
x_i=qX_i+r_i,\qquad y_i=qY_i+s_i,
\qquad 0\le r_i,s_i<q,
\]

then these parameters obey the four exact residue constraints

\[
\boxed{
\begin{aligned}
ma&\equiv r_2-r_1\pmod q,&
na&\equiv r_3-r_1\pmod q,\\
mb&\equiv s_2-s_1\pmod q,&
nb&\equiv s_3-s_1\pmod q.
\end{aligned}
}
\]

### Proof

Collinearity is the determinant equation

\[
UT=VS.
\]

Let \(\delta=\gcd(|U|,|S|)\).  Divide \((U,S)\) by \(\delta\), reverse
both signs if necessary to make the first coordinate positive, and call
the resulting primitive vector \((a,b)\).  The same sign choice gives a
unique nonzero \(m\) with \((U,S)=m(a,b)\).

The determinant equation becomes \(aT=bV\).  Since \(a\) and \(b\) are
coprime, \(a\mid V\).  Put \(n=V/a\); then \(T=nb\).  Distinct rows and
columns make \(a,b,m,n\) nonzero.  Conversely, the displayed
factorization makes \(UT-VS=0\).  The normalization of \((a,b)\) and
the two displacement vectors force all four parameters, proving
uniqueness.

Reducing \(U=ma\), \(V=na\), \(S=mb\), and \(T=nb\) modulo \(q\) gives
the four congruences. \(\square\)

## Interface to BDA4

The unbounded part of a BDA3f relative address is now an arithmetic
slope chain rather than an arbitrary four-dimensional walk.  For each
fixed residue word, admissible triples are exactly the primitive
directions \((a,b)\) and point scales \((m,n)\) satisfying the four
displayed congruences.  Thus a heavy unbounded profile must concentrate
on primitive slopes, on scale classes, or on their interaction.

This does not make the alphabet finite: primitive slopes and scales can
still escape.  It gives the next exact BDA4 classification interface.
Repeated primitive directions are the common-ratio geometry to be
tested against the existing CR/WQ absorber, while dispersed directions
must pay for genuinely new slope classes.

`scripts/verify_bda_primitive_slope.py` exhaustively factors all
compatible collinear triples in a small integer box and checks uniqueness
and the four denominator residue constraints.
