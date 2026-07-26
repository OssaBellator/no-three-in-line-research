# Exact rook classes give the cross-line owner weights

CMR1382--CMR1389 express uniform extension-free collateral as the assignment
cost

\[
\mathbb E N(R)=\sum_a p_e(a)g_e(a).
\]

The conditional owner weight `g_e(a)` appears to require averaging over all
perfect matchings containing `a`.  It does not.  For a fixed old state, every
candidate triple has a fixed residual prescription and a fixed genuinely
entering subset.  Its canonical owner is therefore known before the response
matching is sampled.  CMR1374--CMR1381 then give its exact occurrence
probability.

Retain

\[
S=O\cup M,
\qquad
H_e=K_{n,n}\setminus(O\cup\{e\}),
\qquad e\in M.
\]

For matching-count calculations, relabel target columns so that `O` becomes
the identity.  This relabeling is used only for the rook parameters; real
collinearity and all physical lines remain in the original parent-grid
coordinates.

## Candidate triples and residual prescriptions

Let `V_e` be the set of physical collinear triples `U` contained in

\[
O\cup E(H_e)
\]

such that

\[
P_U:=U\setminus O
\]

is nonempty, matching-compatible and not contained in `M`.

### Theorem CMR1398 -- PROVED

For every response `R in PM(H_e)`,

\[
\boxed{
U\in\mathcal T(O\cup R)\setminus\mathcal T(O\cup M)
\iff
U\in\mathcal V_e\text{ and }P_U\subseteq R.
}
\]

### Proof

If `U` is newly selected, its response-layer cells form a nonempty compatible
prescription contained in `R`; at least one of those cells was not in `M`, so
`P_U` is not contained in `M`.  Conversely, if `P_U subseteq R`, all three cells
of `U` are selected in `O union R`.  Since `P_U` is not contained in `M`, at
least one cell was absent from the old state, so the triple is new. ∎

## The owner is fixed before sampling

Define the genuinely entering subset of a candidate by

\[
A_U=P_U\setminus M.
\]

It is nonempty.  Put

\[
a(U)=\min_\prec A_U.
\]

### Theorem CMR1399 -- PROVED

Whenever `U` occurs in a response, its CMR1215 owner is exactly `a(U)`.
In particular, the owner does not depend on which other bank edges occur.

### Proof

For a realized candidate, the response-layer edges of `U` lying in `M` were
already present and are not entering.  The remaining response-layer edges are
exactly `A_U`, all of which enter.  CMR1215 chooses their least edge. ∎

This is stronger than the response-by-response description of CMR1382.

## Owner-local rook classes

After relabeling `O` to the identity, let

\[
(r(U),q(U),d(U),\varepsilon(U))
\]

be the exact rook parameters of `P_U` from CMR1374--CMR1376.  For an allowed
edge `a`, define

\[
C_e(a;r,q,d,\varepsilon)
=
|\{U\in\mathcal V_e:
 a(U)=a,
 (r(U),q(U),d(U),\varepsilon(U))=(r,q,d,\varepsilon)\}|.
\]

Let

\[
\pi_n(r,q,d,\varepsilon)
=
\frac{B_n(r,q,d,\varepsilon)}{D_n(n-2)/(n-1)}
\]

be the exact prescription probability from CMR1376.

### Theorem CMR1400 -- PROVED

The unconditional expected collateral owned by `a` is

\[
\boxed{
c_e(a)
:=\mathbb E\gamma_e(a,R)
=
\sum_{r,q,d,\varepsilon}
C_e(a;r,q,d,\varepsilon)
\pi_n(r,q,d,\varepsilon).
}
\]

### Proof

By CMR1399, a candidate is assigned to `a` independently of the sampled
response.  By CMR1398 it occurs exactly when `P_U subseteq R`, whose probability
is the rook-class value `pi_n`.  Sum the indicators over the candidates owned
by `a`. ∎

Every physical triple appears in exactly one owner-local class sum.

## Closed conditional owner weight

The exact edge marginal is

\[
p_e(a)=\pi_n(1,q(a),d(a),\varepsilon(a)).
\]

Every allowed edge has positive marginal because it belongs to a perfect
matching of `H_e`.

### Theorem CMR1401 -- PROVED

\[
\boxed{
g_e(a)=\frac{c_e(a)}{p_e(a)}.
}
\]

Consequently

\[
\boxed{
\mathbb E N(R)=\sum_a c_e(a)=\sum_a p_e(a)g_e(a).
}
\]

### Proof

The first identity is the definition of conditional expectation together with
CMR1400.  Sum over owners and use the exact owner partition. ∎

Thus the complete cross-line assignment weights are obtained from geometric
candidate counts and a linear-size rook probability table, without enumerating
the bank states.

## Exact line/rook owner profile

For each candidate `U` owned by `a`, retain additionally the primitive height
and the old-layer populations of its real line.  Denote any resulting finite
geometric signature by `eta(U)` and refine the count to

\[
C_e(a;r,q,d,\varepsilon,\eta).
\]

### Theorem CMR1402 -- PROVED

The refined counts still partition `c_e(a)` exactly:

\[
\boxed{
c_e(a)
=
\sum_{r,q,d,\varepsilon,\eta}
C_e(a;r,q,d,\varepsilon,\eta)
\pi_n(r,q,d,\varepsilon).
}
\]

Any coarsening of `eta` gives an honest CMR1328 exact coarse row; replacing
its coefficients by fibre maxima gives a CMR1329 upper quotient.

### Proof

The new signature only partitions each owner/rook class into smaller disjoint
subclasses.  The occurrence probability depends on the residual prescription
rook class and is unchanged by the additional geometric label. ∎

This is the direct splice between exact matching probabilities and inherited
primitive-height, prefix and carry classes.

## Assignment dual using closed weights

### Theorem CMR1403 -- PROVED

Let `alpha_x,beta_y` be rational potentials satisfying

\[
\alpha_x+\beta_y
\ge
\frac1{p_e(x,y)}
\sum_{r,q,d,\varepsilon}
C_e((x,y);r,q,d,\varepsilon)
\pi_n(r,q,d,\varepsilon)
\]

on every allowed edge.  Then

\[
\mathbb E N(R)\le\sum_x\alpha_x+\sum_y\beta_y.
\]

If the right side is below `D_S(e)`, an extension-free strict improvement
exists.

### Proof

The displayed edge value is exactly `g_e(x,y)` by CMR1400--CMR1401.  Apply the
assignment dual and strict-improvement theorem CMR1386--CMR1387. ∎

No perfect-matching enumeration occurs in this certificate.

## Exact host penalty

Let `U_H` be the unavailable allowed edges in a restricted current host.

### Theorem CMR1404 -- PROVED

The unavailable-edge term is

\[
\boxed{
\sum_{a\in U_H}p_e(a),
}
\]

where every `p_e(a)` is the exact rank-one rook value.  Hence a sufficient
host-feasible improvement condition is

\[
\sum_x\alpha_x+\sum_y\beta_y
+(\Phi(S)+1)\sum_{a\in U_H}p_e(a)
<D_S(e).
\]

### Proof

Use CMR1380 for exact expected unavailable-edge use and CMR1403 for collateral.
The usual penalty argument then excludes every unavailable response. ∎

## Rook-owner assignment endpoint

### Corollary CMR1405 -- PROVED

For one extension-free target bank:

1. every candidate triple has a fixed owner before the response is sampled;
2. every owner load is an exact finite dot product of geometric class counts
   with rook probabilities;
3. conditional edge weights are obtained by one exact marginal division;
4. the full expectation is one doubly-stochastic assignment cost;
5. primitive-height, line-population, prefix and carry labels may refine the
   owner classes without losing exactness;
6. rational assignment potentials and host penalties are finite integer-checkable
   certificates.

The remaining open inequality is now precisely to bound the geometric
owner-class counts strongly enough that the assignment dual, or its
host-uniform upper quotient, is subcritical.  Independent line maxima are no
longer forced by the formalism.  No all-`n` theorem is claimed.

The exact owner weights are checked in
[`scripts/verify_prime_power_rook_owner_edge_weights.py`](../scripts/verify_prime_power_rook_owner_edge_weights.py).
