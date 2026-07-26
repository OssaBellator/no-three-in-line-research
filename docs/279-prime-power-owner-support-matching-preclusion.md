# Extension-free owner support has sharp matching preclusion

CMR1390--CMR1397 turn low collateral into a candidate-transversal problem.
CMR1398--CMR1405 give every candidate triple a fixed canonical owner edge and
compute its exact rook-class weight.  The remaining question is whether deleting
those owner edges can destroy every response matching.

For an extension-free target bank, that obstruction has a sharp size.  After
normalising the fixed opposite matching to the identity, write

\[
H_e=K_{n,n}\setminus(I\cup\{e\}),
\qquad
e=(u,v),
\qquad
u\ne v,
\qquad
n\ge4.
\]

The row of `e` and the column of `e` have degree `n-2`; every other vertex has
degree `n-1`.  The two degree-`n-2` stars are the only blocker walls of minimum
size.

Let `C` be a finite weighted candidate family.  Each `T in C` has a nonempty
matching-compatible residual prescription

\[
P_T\subseteq E(H_e),
\qquad
1\le |P_T|\le3,
\]

weight `v_T>=0`, and a fixed canonical owner

\[
a(T)\in P_T
\]

as in CMR1399.  For a response matching `R`, put

\[
N_v(R)=\sum_{T\in\mathcal C}v_T\mathbf1_{P_T\subseteq R}.
\]

## 1. Exact size of one minimal wall

Let `Q` be an inclusion-minimal perfect-matching blocker in `H_e`.  By
CMR1151--CMR1152 there are sets `X` of rows and `Z` of columns such that

\[
Q=E(H_e)\cap(X\times Z),
\qquad
|Z|=n-|X|+1.
\]

Put

\[
k=|X|,
\qquad
z=|Z|=n-k+1,
\qquad
s=|X\cap Z|,
\]

and

\[
\delta=\mathbf1_{u\in X,\ v\in Z}.
\]

### Theorem CMR1406 -- PROVED

The wall size is exactly

\[
\boxed{
|Q|=kz-s-\delta.
}
\]

### Proof

The rectangle `X times Z` has `kz` cells.  Exactly the `s` identity cells
`(i,i)` with `i in X cap Z` are absent from `H_e`.  The additional forbidden
edge `(u,v)` lies in the rectangle exactly when `delta=1`.  The identity edges
and `(u,v)` are distinct because `u ne v`.  Subtract them. ∎

## 2. Sharp matching-preclusion number

Define the two exceptional stars

\[
S_u=\{(u,y)\in E(H_e)\},
\qquad
S^v=\{(x,v)\in E(H_e)\}.
\]

Both have size `n-2`.

### Theorem CMR1407 -- PROVED

Every inclusion-minimal blocker `Q` in `H_e` satisfies

\[
\boxed{|Q|\ge n-2.}
\]

Equality holds if and only if

\[
\boxed{Q=S_u\quad\text{or}\quad Q=S^v.}
\]

### Proof

By CMR1406 and the bounds

\[
s\le\min(k,z),
\qquad
\delta\le1,
\]

we have

\[
|Q|\ge kz-\min(k,z)-1.
\]

If `2<=k<=n-1`, then also `2<=z<=n-1`.  When `k<=z`,

\[
|Q|\ge k(z-1)-1=k(n-k)-1\ge2n-5\ge n-1.
\]

The case `z<=k` is symmetric.  Thus equality with `n-2` can occur only when
`k=1` or `z=1`.

If `k=1`, then `Z` is the complete column side and `s=1`.  The value is `n-2`
exactly when the unique row is `u`, so `Q=S_u`.  If `z=1`, the symmetric
argument gives `Q=S^v`.  Both displayed stars are blockers because their
deletion isolates the corresponding exceptional vertex. ∎

Thus the matching-preclusion number of the extension-free graph is exactly
`n-2`, with exactly two minimum blockers.

## 3. Small deletion sets always survive

### Theorem CMR1408 -- PROVED

Let `F subseteq E(H_e)`.

1. If `|F|<=n-3`, then `H_e-F` has a perfect matching.
2. If `|F|=n-2`, then `H_e-F` has no perfect matching if and only if
   `F=S_u` or `F=S^v`.

### Proof

If `H_e-F` has no perfect matching, CMR1150 supplies an inclusion-minimal
blocker `Q subseteq F`.  CMR1407 gives `|Q|>=n-2`, proving the first statement.
For `|F|=n-2`, equality forces `F=Q`, and CMR1407 gives the two exceptional
stars.  Conversely, deleting either complete exceptional star isolates one
vertex. ∎

This is stronger than a generic minimum-degree estimate: it classifies every
minimum obstruction.

## 4. Small candidate transversals force a response

Let `B subseteq C` be an exempt family and let

\[
\sigma:\mathcal C\setminus B\to E(H_e),
\qquad
\sigma(T)\in P_T,
\]

be a `B`-transversal selector.  Put

\[
F_\sigma=\{\sigma(T):T\in\mathcal C\setminus B\}.
\]

### Theorem CMR1409 -- PROVED

If either

\[
|F_\sigma|\le n-3,
\]

or

\[
|F_\sigma|=n-2
\quad\text{and}\quad
F_\sigma\notin\{S_u,S^v\},
\]

then there is a response `R in PM(H_e)` satisfying

\[
\boxed{
N_v(R)\le\sum_{T\in B}v_T.
}
\]

Consequently, at a positive minimum with guaranteed destroyed load `L`, every
`B` with

\[
\sum_{T\in B}v_T<L
\]

has the following obstruction for every `B`-transversal selector:

\[
|F_\sigma|\ge n-1,
\]

unless `F_sigma` is one of the two exceptional `n-2` stars.

### Proof

CMR1408 gives a perfect matching after the selected deletions.  Apply CMR1391.
The minimum statement is the contrapositive. ∎

## 5. Canonical owner support is already a transversal

For `B subseteq C`, define its nonexempt owner support

\[
A(B)=\{a(T):T\in\mathcal C\setminus B\}.
\]

### Theorem CMR1410 -- PROVED

The map

\[
\sigma_B(T)=a(T)
\]

is a `B`-transversal selector with deletion set `A(B)`.  Hence CMR1409 applies
with `F_sigma=A(B)`.

In particular, a response of collateral at most `sum_{T in B}v_T` exists whenever

\[
|A(B)|\le n-3,
\]

or when `|A(B)|=n-2` and the owner support is not an exceptional star.

At a positive minimum, every subthreshold exempt family therefore leaves at
least `n-1` distinct canonical owner edges, except for the two explicitly
classified star supports.

### Proof

CMR1399 gives `a(T) in P_T` before the response is sampled.  Thus the canonical
owner map is a valid transversal.  Apply CMR1409. ∎

This is the direct bridge from rook-owner class counts to Hall-wall geometry.

## 6. A closed owner-tail certificate

Define the total canonical owner weight

\[
W(a)=\sum_{T:a(T)=a}v_T,
\qquad
W_{\rm tot}=\sum_aW(a).
\]

Call an edge set `A` **admissible** when

\[
|A|\le n-3,
\]

or when

\[
|A|=n-2
\quad\text{and}\quad
A\notin\{S_u,S^v\}.
\]

Put

\[
M_{n-2}(W)=\max_{A\text{ admissible}}\sum_{a\in A}W(a).
\]

### Theorem CMR1411 -- PROVED

For every admissible `A`, there is a response satisfying

\[
N_v(R)\le W_{\rm tot}-\sum_{a\in A}W(a).
\]

Therefore

\[
\boxed{
\min_{R\in\operatorname{PM}(H_e)}N_v(R)
\le
W_{\rm tot}-M_{n-2}(W).
}
\]

If the right side is below the destroyed old-credit load `L`, the target bank
contains a strict improving response.

### Proof

Exempt exactly the candidates whose canonical owner lies outside `A`.  Their
weight is

\[
W_{\rm tot}-\sum_{a\in A}W(a).
\]

Every nonexempt candidate is hit by its owner in `A`.  CMR1408 says `H_e-A` has
a perfect matching, so the smaller actual owner-deletion set also leaves a
perfect matching.  Apply CMR1391 and maximize over admissible `A`. ∎

The certificate is deterministic and finite.  It asks whether all but a small
owner-weight tail can be concentrated on at most `n-2` nonexceptional owner
edges.

## 7. Fractional rank-three cover criterion

For `B subseteq C`, let `tau_B^*` be the fractional transversal number of the
nonexempt prescription hypergraph:

\[
\tau_B^*
=
\min
\left\{
\sum_{a\in E(H_e)}y_a:
 y_a\ge0,
 \ \sum_{a\in P_T}y_a\ge1
 \text{ for every }T\notin B
\right\}.
\]

### Theorem CMR1412 -- PROVED

If

\[
\boxed{
3\tau_B^*<n-2,
}
\]

then there is a response `R` with

\[
N_v(R)\le\sum_{T\in B}v_T.
\]

Consequently, at a positive minimum with destroyed load `L`, every exempt family
of weight below `L` satisfies

\[
\boxed{
\tau_B^*\ge\frac{n-2}{3}.
}
\]

### Proof

Take a feasible fractional cover `y` and put

\[
A_y=\{a:y_a\ge1/3\}.
\]

Every prescription has size at most three and fractional sum at least one, so
it contains an edge of `A_y`.  Thus `A_y` is an integral transversal.  Also

\[
|A_y|\le3\sum_ay_a.
\]

If `3 sum_a y_a<n-2`, then the integer `|A_y|` is at most `n-3`.  CMR1409 gives
the response.  Minimize over `y` and take the contrapositive. ∎

This gives a polynomial linear-programming relaxation which is not constructed
from an already optimal response.

## 8. Dual dispersed-candidate packing

The finite LP dual of `tau_B^*` is

\[
\nu_B^*
=
\max
\left\{
\sum_{T\notin B}z_T:
 z_T\ge0,
 \ \sum_{T:a\in P_T}z_T\le1
 \text{ for every edge }a
\right\}.
\]

### Theorem CMR1413 -- PROVED

\[
\boxed{
\tau_B^*=\nu_B^*.
}
\]

Hence at a positive minimum, every exempt family of weight below the destroyed
load supports a fractional packing of nonexempt candidate prescriptions of total
mass at least

\[
\boxed{
\frac{n-2}{3},
}
\]

with edge load at most one.

### Proof

This is finite linear-programming duality applied to the incidence matrix of the
candidate prescriptions.  Combine it with CMR1412. ∎

The obstruction is now quantitative.  A closing theorem may either:

1. compress canonical owner support below the sharp matching-preclusion scale;
2. show that the only size-`n-2` support is not an exceptional star;
3. rule out the required fractional candidate packing using primitive height,
   prefix, quotient, carry or protected-reserve classes; or
4. charge an exceptional owner star to the existing loaded-line/secant-star
   mechanisms.

No all-`n` theorem is claimed.  The exact wall formula, sharp blocker
classification, small-deletion resilience, owner-tail policy and fractional
rounding are checked in
[`scripts/verify_prime_power_owner_support_matching_preclusion.py`](../scripts/verify_prime_power_owner_support_matching_preclusion.py).
