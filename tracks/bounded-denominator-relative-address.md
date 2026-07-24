# Relative coarse addresses for denominator-\(q\) collateral

BDA3e isolates a finite intrinsic residue word but leaves absolute block
identities, anchors, and coarse carries in the geometric address. For
the collinearity part of a collateral triple, absolute coarse positions
can be removed exactly: only four relative quotient coordinates remain.

Fix canonical representatives \(0\le r_i,s_i<q\) and write three cells
as

\[
P_i=(x_i,y_i)
=
(qX_i+r_i,\ qY_i+s_i),
\qquad i=1,2,3.
\]

Put

\[
\Delta X_i=X_i-X_1,
\qquad
\Delta Y_i=Y_i-Y_1
\quad(i=2,3).
\]

## BDA3f -- relative-address determinant

### Lemma BDA3f -- PROVED

The oriented collinearity determinant is exactly

\[
\boxed{
\begin{aligned}
D(P_1,P_2,P_3)
={}&
\bigl(q\Delta X_2+r_2-r_1\bigr)
\bigl(q\Delta Y_3+s_3-s_1\bigr)\\
&-
\bigl(q\Delta X_3+r_3-r_1\bigr)
\bigl(q\Delta Y_2+s_2-s_1\bigr).
\end{aligned}
}
\]

Consequently:

1. collinearity depends on the coordinate residues and only the four
   relative coarse quotients
   \[
   (\Delta X_2,\Delta X_3,\Delta Y_2,\Delta Y_3);
   \]
2. simultaneous translation of all three coarse addresses does not
   change the profile;
3. if all four relative quotients lie in \([-W,W]\), then a fixed
   residue word has at most
   \[
   \boxed{(2W+1)^4}
   \]
   collinearity-address types.

Thus any residue-complete finite BDA3 alphabet acquires at most a
\((2W+1)^4\) multiplicative refinement on a relative carry window of
width \(W\). In particular, for a rank-three prescription whose three
cells all carry the BDA3e decoration, the combined intrinsic and
relative-address count is at most

\[
\boxed{
6\bigl(q^2\varphi(q)\bigr)^3(2W+1)^4.
}
\]

### Proof

Use

\[
D(P_1,P_2,P_3)
=(x_2-x_1)(y_3-y_1)-(x_3-x_1)(y_2-y_1)
\]

and substitute the quotient--residue decompositions. This gives the
displayed identity. The absolute values \(X_1,Y_1\) cancel, proving the
translation assertion. Four integer coordinates, each with \(2W+1\)
choices, give the counting bound. Multiplication by the BDA3e intrinsic
word bound proves the final display. \(\square\)

For prescriptions containing unchanged anchors, their finitely many
coordinate residues must also be added to the base alphabet. BDA3f
still removes their absolute common translate, but it does not assert
that the relative quotient window is bounded.

## Residue-only obstruction

### Proposition BDA3-residue-wall -- PROVED

For every \(q\ge2\), coordinate residues alone do not determine
collinearity, even for a compatible three-cell matching.

### Proof

The triples

\[
\{(0,0),(1,1),(q,q)\}
\quad\text{and}\quad
\{(0,0),(1,1),(2q,q)\}
\]

have the same corresponding coordinate residues modulo \(q\), and both
use three distinct rows and columns. The first is collinear, while the
second has determinant

\[
q-2q=-q\ne0.
\]

Hence some relative coarse-address information is indispensable.
\(\square\)

## Interface to BDA4

BDA3 no longer needs absolute block identities for the determinant
test. It needs one of the following:

- a proof that paid collateral remains in a bounded relative quotient
  window \(W_q\);
- a finite quotient of the four relative variables preserving allowed
  transitions; or
- a classification showing that escape to unbounded relative quotients
  is itself a paid or absorbable BDA4 template.

The residue-only wall rules out declaring the intrinsic BDA3e word to be
the complete profile without one of these additional inputs.

`scripts/verify_bda_relative_address.py` checks the determinant identity,
coarse-translation invariance, bounded-window count, and the residue wall
for small denominators.
