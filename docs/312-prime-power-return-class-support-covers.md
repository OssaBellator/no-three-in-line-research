# Geometric class supports compile return superlevels into vertex covers

CMR1630--CMR1637 reduce the combined return-selector block to matching numbers
or vertex covers in score superlevel graphs.  The remaining geometric estimates
usually arrive classwise: an owner, height, token, prefix, carry or interface
class has a proved score cap and is supported on a small set of source rows or
target columns.  This chapter compiles those local support statements into one
shared assignment certificate.

The construction never optimizes return and selector offspring separately.  It
uses the combined score

\[
h_T=g_{\rm ret}+Tg_{\rm sel}
\]

throughout.

Let `G=(L,R,E)` be a finite bipartite response host.  Give every edge a finite
class

\[
\sigma(a)\in\mathcal S
\]

and suppose a nonnegative rational class cap `H_s` satisfies

\[
h_T(a)\le H_{\sigma(a)}.
\]

For every class `s`, let

\[
C_s\subseteq L\cup R
\]

be an explicit vertex cover of all class-`s` edges.

## 1. Threshold class unions have explicit covers

Let the distinct positive class caps be

\[
0<\tau_1<\cdots<\tau_m,
\qquad \tau_0=0.
\]

For each level define

\[
\mathcal S_j=\{s:H_s\ge\tau_j\},
\qquad
C_j=\bigcup_{s\in\mathcal S_j}C_s.
\]

### Theorem CMR1670 -- PROVED

`C_j` is a vertex cover of the exact score superlevel graph

\[
E_j=\{a:h_T(a)\ge\tau_j\}.
\]

Hence

\[
\boxed{\nu(E_j)\le |C_j|.}
\]

### Proof

If `h_T(a)>=tau_j`, then the class cap of `a` is at least `tau_j`, so
`sigma(a) in S_j`.  The edge is covered by `C_{sigma(a)}` and therefore by the
union `C_j`.  A vertex cover bounds the matching number. ∎

The union size counts shared support vertices only once.

## 2. Class-supported assignment certificate

### Theorem CMR1671 -- PROVED

The combined return-selector assignment satisfies

\[
\boxed{
\max_{Q\in\operatorname{PM}(G)}
\sum_{a\in Q}h_T(a)
\le
\sum_{j=1}^m(\tau_j-\tau_{j-1})|C_j|.
}
\]

If the right side is below one, the coupled return-selector block is
subcritical.

### Proof

Apply CMR1670 in the superlevel matching-number bound CMR1631.  The spectral
conclusion is CMR1633. ∎

Thus geometric support bounds may be inserted without solving the full
assignment problem.

## 3. Source-star and target-star specialization

Suppose every class cover is written as

\[
C_s=X_s\cup Y_s,
\qquad X_s\subseteq L,
\quad Y_s\subseteq R.
\]

### Theorem CMR1672 -- PROVED

At threshold `tau_j`, one may use

\[
\boxed{
|C_j|
=
\left|\bigcup_{s\in\mathcal S_j}X_s\right|
+
\left|\bigcup_{s\in\mathcal S_j}Y_s\right|.
}
\]

In particular, if all high-score edges lie in `r_j` source stars and `c_j`
target stars, then

\[
\boxed{\nu(E_j)\le r_j+c_j.}
\]

### Proof

The source and target vertex sets are disjoint, so the size of their union is the
sum of the two displayed union sizes.  Apply CMR1670. ∎

Owner-row, target-column, token and prefix supports fit this form directly.

## 4. Alternative class covers may be optimized jointly

A class may have several proved covers, for example a small source-row cover and
a different small target-column cover.  Let

\[
\mathcal C_s=\{C_{s,1},\ldots,C_{s,k_s}\}
\]

be a finite nonempty family of valid covers.

### Theorem CMR1673 -- PROVED

For every threshold, the finite optimization

\[
\boxed{
\kappa_j
=
\min_{q_s\in\{1,\ldots,k_s\}}
\left|
\bigcup_{s\in\mathcal S_j}C_{s,q_s}
\right|
}
\]

produces a valid superlevel-cover size.  Consequently

\[
\max_Q\sum_{a\in Q}h_T(a)
\le
\sum_j(\tau_j-\tau_{j-1})\kappa_j.
\]

### Proof

Every selected `C_{s,q_s}` covers its class.  Their union covers the threshold
union, regardless of the choices.  Minimize over the finite choice set and apply
CMR1671. ∎

This optimization is a finite set-cover problem, not an independence
assumption between classes.

## 5. Nested cumulative covers

Choose one class cover `C_s` once and use it at every threshold.  The resulting
unions satisfy

\[
C_1\supseteq C_2\supseteq\cdots\supseteq C_m.
\]

### Theorem CMR1674 -- PROVED

The nested cover sum has the equivalent vertex-weight form

\[
\boxed{
\sum_{j=1}^m(\tau_j-\tau_{j-1})|C_j|
=
\sum_{z\in L\cup R}w(z),
}
\]

where

\[
w(z)=\max\{H_s:z\in C_s\}
\]

with maximum zero when no selected class cover contains `z`.

### Proof

A vertex `z` belongs to `C_j` exactly for the levels not exceeding the largest
class cap among selected covers containing `z`.  Its layer increments telescope
to that maximum.  Sum over vertices. ∎

Hence one may publish either nested covers or one nonnegative weight per support
vertex.

## 6. Direct rational dual from class covers

### Theorem CMR1675 -- PROVED

The vertex weights from CMR1674 form a feasible assignment dual:

\[
\boxed{u_x+v_y\ge h_T(x,y)}
\]

for every allowed edge, by assigning `u_x=w(x)` on sources and `v_y=w(y)` on
targets.  Its objective is exactly the nested cover sum.

### Proof

An edge of class `s` is incident to at least one vertex of `C_s`.  That endpoint
has weight at least `H_s`, which is at least the exact edge score.  The other
endpoint has nonnegative weight.  CMR1674 gives the objective identity. ∎

The cover compiler therefore produces an ordinary rational assignment dual as
well as a combinatorial certificate.

## 7. Strict integer form

Assume all class caps have common denominator `D>0`.  Write

\[
L_s=DH_s\in\mathbb Z_{\ge0}
\]

and give every support vertex integer weight

\[
W(z)=\max\{L_s:z\in C_s\}.
\]

### Theorem CMR1676 -- PROVED

The finite strict integer condition

\[
\boxed{
\sum_{z\in L\cup R}W(z)<D
}
\]

certifies the complete return-selector block subcritical.

### Proof

Divide by `D` to obtain the rational dual of CMR1675 with objective below one,
then apply CMR1586. ∎

This is compatible with the labelled SCC and CRT integer-certificate protocol.

## 8. Class-support endpoint

### Corollary CMR1677 -- PROVED

The superlevel return frontier now has a geometric compiler.

1. Assign one combined score cap to every exact owner/height/token/prefix/carry/
   interface class.
2. Prove one or more source/target vertex covers for each class.
3. Optimize the finite cover choices if useful.
4. Form nested threshold unions or the equivalent vertex weights.
5. Check one rational objective below one, or its strict integer form.

The remaining host-uniform task is to supply small class supports and score caps
from the inherited geometry.  No all-`n` theorem is claimed.

Class-union covers, nested layer sums, alternative-cover optimization and exact
integer duals are checked in
[`scripts/verify_prime_power_return_class_support_covers.py`](../scripts/verify_prime_power_return_class_support_covers.py).
