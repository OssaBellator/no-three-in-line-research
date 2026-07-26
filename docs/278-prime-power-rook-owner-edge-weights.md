# Exact rook classes give cross-line owner weights

Fix

\[
S=O\cup M,
\qquad H_e=K_{n,n}\setminus(O\cup\{e\}),
\qquad e\in M.
\]

Relabel `O` to the identity only for rook counting.  Real collinearity remains
in the original parent-grid coordinates.

Let `V_e` be the physical collinear triples `U` contained in
`O union E(H_e)` for which

\[
P_U=U\setminus O
\]

is nonempty, matching-compatible and not contained in `M`.

### Theorem CMR1398 -- PROVED

For every response `R in PM(H_e)`,

\[
\boxed{
U\in\mathcal T(O\cup R)\setminus\mathcal T(O\cup M)
\iff U\in\mathcal V_e\text{ and }P_U\subseteq R.
}
\]

### Proof

A new triple has a nonempty compatible response prescription and at least one
response edge absent from `M`.  Conversely, containment of such a prescription
selects the triple and makes it new. ∎

Put

\[
A_U=P_U\setminus M,
\qquad a(U)=\min_\prec A_U.
\]

### Theorem CMR1399 -- PROVED

Whenever `U` occurs, its CMR1215 owner is exactly `a(U)`, independently of the
other response edges.

### Proof

The edges of `P_U` in `M` are old; its entering edges are exactly `A_U`.
CMR1215 chooses their least member. ∎

Let `(r,q,d,epsilon)` be the exact CMR1374--CMR1376 rook class of `P_U`, and
define

\[
C_e(a;r,q,d,\varepsilon)
=
|\{U\in\mathcal V_e:a(U)=a,
(r(U),q(U),d(U),\varepsilon(U))=(r,q,d,\varepsilon)\}|.
\]

Write `pi_n(r,q,d,epsilon)` for the exact class probability.

### Theorem CMR1400 -- PROVED

\[
\boxed{
c_e(a):=\mathbb E\gamma_e(a,R)
=
\sum_{r,q,d,\varepsilon}
C_e(a;r,q,d,\varepsilon)\pi_n(r,q,d,\varepsilon).
}
\]

### Proof

CMR1399 fixes the owner, and CMR1398 makes occurrence equivalent to containing
the residual prescription.  Sum the candidate indicators. ∎

### Theorem CMR1401 -- PROVED

Every allowed edge has positive marginal and

\[
\boxed{g_e(a)=\frac{c_e(a)}{p_e(a)}.}
\]

Consequently

\[
\boxed{
\mathbb E N(R)=\sum_ac_e(a)=\sum_ap_e(a)g_e(a).
}
\]

Refine every owner/rook class by any inherited-coordinate signature `eta`, such
as primitive height, line population, prefix, quotient or carry class.

### Theorem CMR1402 -- PROVED

\[
\boxed{
c_e(a)=
\sum_{r,q,d,\varepsilon,\eta}
C_e(a;r,q,d,\varepsilon,\eta)\pi_n(r,q,d,\varepsilon).}
\]

Every coarsening gives an exact CMR1328 row; fibre maxima give a CMR1329 upper
quotient.

### Theorem CMR1403 -- PROVED

If rational potentials satisfy

\[
\alpha_x+\beta_y
\ge
\frac1{p_e(x,y)}
\sum_{r,q,d,\varepsilon}
C_e((x,y);r,q,d,\varepsilon)\pi_n(r,q,d,\varepsilon),
\]

then

\[
\mathbb E N(R)\le\sum_x\alpha_x+\sum_y\beta_y.
\]

A dual sum below `D_S(e)` forces strict improvement.

### Proof

The displayed edge value is exactly `g_e(x,y)` by CMR1400--CMR1401.  Apply the
assignment dual. ∎

### Theorem CMR1404 -- PROVED

For unavailable allowed edges `U_H`, a sufficient host-feasible condition is

\[
\sum_x\alpha_x+\sum_y\beta_y
+(\Phi(S)+1)\sum_{a\in U_H}p_e(a)<D_S(e).
\]

### Proof

Combine the exact unavailable-edge expectation with CMR1403. ∎

### Corollary CMR1405 -- PROVED

Every candidate has a fixed owner before sampling; owner loads are exact finite
rook/geometric dot products; conditional weights use one marginal division;
and rational assignment and host certificates are integer-checkable.  The
remaining issue is quantitative control of these owner classes, not ownership
or matching enumeration.  No all-`n` theorem is claimed.

Checked by
[`scripts/verify_prime_power_rook_owner_edge_weights.py`](../scripts/verify_prime_power_rook_owner_edge_weights.py).
