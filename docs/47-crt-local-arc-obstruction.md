# The local-arc obstruction and a general CRT slope-carry signature

CMCRT4--CMCRT5 classify mixed collisions under a local modular-arc hypothesis.
For saturated prime-factor pairs, that hypothesis is impossible. The correct
replacement must retain local line directions and their integer carries.

## 1. A saturated prime pair cannot be a local arc

### Theorem CMCRT6 — PROVED

Let `p` be prime. Any subset of the affine plane
\(\mathbb F_p^2\) containing no three distinct collinear points has size at
most

\[
p+2.
\]

### Proof

Fix one point `P` of the set. There are exactly `p+1` affine line directions
through `P`: the `p` finite slopes and the vertical direction. If no three
points are collinear, every direction contains at most one further selected
point. Hence the set contains at most

\[
1+(p+1)=p+2
\]

points. ∎

### Corollary CMCRT7 — PROVED

For every odd prime `p`, no saturated pair of permutation layers in
\(\mathbb F_p^2\) satisfies the local modular-arc hypothesis of CMCRT4.

### Proof

A saturated pair has `2p` distinct points, while

\[
2p>p+2
\]

for every odd `p`. Apply CMCRT6. ∎

Thus CMCRT5 cannot be used by simply inserting saturated prime-factor pairs as
its local inputs. It remains valid as a conditional theorem for smaller
auxiliary projection sets, but it is not the direct all-composite assembly
endpoint.

## 2. General local slope-carry identity

Let `m>1`, and consider a global integer triple with displacement vectors

\[
U=P_1-P_0,
\qquad
V=P_2-P_0.
\]

Suppose its projection modulo `m` is collinear. Choose one modular direction
vector `d` and scalar representatives `alpha,beta` such that

\[
U\equiv\alpha d\pmod m,
\qquad
V\equiv\beta d\pmod m.
\]

This includes collisions by allowing one or both scalars to be zero. Write

\[
U=\alpha d+mA,
\qquad
V=\beta d+mB
\]

with integer carry vectors `A,B`.

### Theorem CMCRT8 — PROVED

The exact global determinant is

\[
\det(U,V)=mL_m,
\]

where the **local slope-carry signature** is

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

Expand bilinearly:

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
\(\det(A,d)=-\det(d,A)\). Factoring `m` gives the formula. ∎

The mixed-collision factorization CMCRT3 is the special case where one local
scalar vanishes in each factor and the corresponding displacement is a full
multiple of that factor.

## 3. Two-factor compatibility

Let `u,v` be coprime, put `N=uv`, and suppose the triple is collinear modulo
both factors. Construct signatures `L_u,L_v` using CMCRT8.

### Corollary CMCRT9 — PROVED

There is an integer determinant quotient `q` such that

\[
L_u=vq,
\qquad
L_v=uq,
\qquad
\det(U,V)=Nq.
\]

The standard lifts are real collinear exactly when

\[
q=0,
\]

or equivalently when both local slope-carry signatures vanish.

### Proof

CMCRT8 gives

\[
\det(U,V)=uL_u=vL_v.
\]

Since `u` and `v` are coprime, the common determinant is divisible by `uv`.
Write it as `uvq`; division gives the two identities. The real determinant
vanishes exactly when `q=0`. ∎

## 4. Revised CRT target

A positive saturated CRT theorem must control three types of local data:

1. collision directions, covered by CMCRT3;
2. distinct-point local line directions `d` and scalar positions
   `alpha,beta`;
3. the carry vectors `A,B` entering `L_m`.

The new construction target is to force the two factor signatures to be
incompatible unless `q` is nonzero, or to absorb the population with
`L_u=L_v=0`. Merely separating collision directions is insufficient because
CMCRT7 guarantees many distinct-point local lines in every saturated odd-prime
factor.

The finite identity checker is
[`scripts/verify_crt_slope_carry.py`](../scripts/verify_crt_slope_carry.py).
