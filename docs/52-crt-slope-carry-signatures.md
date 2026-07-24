# CRT slope-carry signatures

CMCRT6--CMCRT7 show that saturated odd-prime local pairs necessarily contain
three-point local lines. A viable CRT assembly theorem must therefore retain
those local directions and their integer carries.

Let `m>1`, and let the global displacement vectors of a triple be

\[
U=P_1-P_0,
\qquad
V=P_2-P_0.
\]

Assume their local displacements admit one cyclic-line representation modulo
`m`: choose a direction vector `d` and scalar representatives `alpha,beta`
such that

\[
U\equiv\alpha d\pmod m,
\qquad
V\equiv\beta d\pmod m.
\]

This is automatic when `m` is prime and the projected triple is collinear over
\(\mathbb F_m\). Over a composite ring it is an explicit hypothesis;
determinant zero alone need not imply a cyclic representation. Collisions are
included by allowing one or both scalars to vanish. Write

\[
U=\alpha d+mA,
\qquad
V=\beta d+mB.
\]

## Exact local signature

### Theorem CMCRT8 — PROVED

The exact determinant is

\[
\det(U,V)=mL_m,
\]

where

\[
L_m
=
\alpha\det(d,B)
-
\beta\det(d,A)
+
m\det(A,B).
\]

### Proof

Bilinear expansion gives

\[
\begin{aligned}
\det(\alpha d+mA,\beta d+mB)
={}&\alpha\beta\det(d,d)
+\alpha m\det(d,B)\\
&+m\beta\det(A,d)
+m^2\det(A,B).
\end{aligned}
\]

The first term vanishes and
\(\det(A,d)=-\det(d,A)\). Factor `m`. ∎

The mixed-collision formula CMCRT3 is the special case where one local scalar
vanishes in each factor.

## Coprime-factor compatibility

Let `u,v` be coprime, put `N=uv`, and choose cyclic-line representations modulo
both factors. This is automatic when both factors are prime and the projected
triples are collinear in the two affine planes.

### Corollary CMCRT9 — PROVED

There is an integer quotient `q` satisfying

\[
L_u=vq,
\qquad
L_v=uq,
\qquad
\det(U,V)=Nq.
\]

The standard lifts are real collinear exactly when `q=0`, equivalently when
both local signatures vanish.

### Proof

CMCRT8 gives

\[
\det(U,V)=uL_u=vL_v.
\]

Coprimality makes the determinant divisible by `uv`; division gives the
identities. ∎

A positive saturated CRT theorem over prime factors must control collision
directions, distinct-point local directions and scalar positions, and the
carry vectors entering `L_m`. For composite local factors it must additionally
classify noncyclic zero-divisor incidences.

The checker is
[`scripts/verify_crt_slope_carry.py`](../scripts/verify_crt_slope_carry.py).
