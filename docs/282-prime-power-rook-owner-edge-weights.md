# Exact rook classes give cross-line owner weights

Fix `S=O union M`, target `e in M`, and

\[
H_e=K_{n,n}\setminus(O\cup\{e\}).
\]

Relabel `O` to the identity only for rook counting; real collinearity remains
in the original parent coordinates.

## Candidate characterization

Let `V_e` be the physical collinear triples `U` contained in
`O union E(H_e)` for which

\[
P_U=U\setminus O
\]

is nonempty, matching-compatible and not contained in `M`.

### Theorem CMR1430 -- PROVED

For every response `R in PM(H_e)`,

\[
\boxed{
U\in\mathcal T(O\cup R)\setminus\mathcal T(O\cup M)
\iff U\in\mathcal V_e\text{ and }P_U\subseteq R.
}
\]

### Proof

A newly selected triple has a nonempty compatible response prescription and at
least one response edge absent from `M`.  Conversely, containment of such a
prescription selects the triple and the edge outside `M` makes it new. ∎

## Owner fixed before sampling

Put

\[
A_U=P_U\setminus M,
\qquad
a(U)=\min_\prec A_U.
\]

### Theorem CMR1431 -- PROVED

Whenever candidate `U` occurs, its CMR1215 owner is exactly `a(U)`.  The owner
is independent of the rest of the sampled response.

### Proof

The response edges of `U` in `M` are old.  Its entering edges are exactly
`A_U`, and CMR1215 chooses their least member. ∎

## Owner-local rook classes

Let `(r,q,d,epsilon)` be the CMR1414--CMR1416 rook class of `P_U`.  Define

\[
C_e(a;r,q,d,\varepsilon)
=
|\{U\in\mathcal V_e:a(U)=a,
(r(U),q(U),d(U),\varepsilon(U))=(r,q,d,\varepsilon)\}|.
\]

Write `pi_n(r,q,d,epsilon)` for the exact class probability.

### Theorem CMR1432 -- PROVED

The unconditional expected collateral owned by `a` is

\[
\boxed{
c_e(a):=\mathbb E\gamma_e(a,R)
=
\sum_{r,q,d,\varepsilon}
C_e(a;r,q,d,\varepsilon)\pi_n(r,q,d,\varepsilon).
}
\]

### Proof

CMR1431 fixes the owner of every candidate.  CMR1430 says it occurs exactly
when its prescription occurs; CMR1416 gives that probability. ∎

### Theorem CMR1433 -- PROVED

Every allowed edge has positive marginal and

\[
\boxed{
g_e(a)=\frac{c_e(a)}{p_e(a)}.}
\]

Consequently

\[
\boxed{
\mathbb E N(R)=\sum_ac_e(a)=\sum_ap_e(a)g_e(a).
}
\]

### Proof

Every allowed edge extends to a bank matching.  Divide the unconditional owner
load by its marginal and sum the owner partition. ∎

## Geometric refinements

Refine each candidate by any finite inherited-coordinate signature `eta`, such
as primitive height, line population, prefix, quotient or carry class.

### Theorem CMR1434 -- PROVED

\[
\boxed{
c_e(a)=
\sum_{r,q,d,\varepsilon,\eta}
C_e(a;r,q,d,\varepsilon,\eta)\pi_n(r,q,d,\varepsilon).}
\]

Every coarsening gives an exact CMR1328 row, and fibre maxima give an honest
CMR1329 upper quotient.

### Proof

The extra signature partitions each owner/rook class without changing its
prescription probability. ∎

## Closed assignment and host certificates

### Theorem CMR1435 -- PROVED

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

If the dual sum is below `D_S(e)`, a strict improvement exists.

### Proof

The displayed value is exactly `g_e(x,y)` by CMR1432--CMR1433.  Apply
CMR1426--CMR1427. ∎

### Theorem CMR1436 -- PROVED

For unavailable allowed edges `U_H`, a sufficient host-feasible condition is

\[
\sum_x\alpha_x+\sum_y\beta_y
+(\Phi(S)+1)\sum_{a\in U_H}p_e(a)<D_S(e).
\]

### Proof

Combine CMR1435 with the exact unavailable-edge expectation CMR1420. ∎

### Corollary CMR1437 -- PROVED

Cross-line owner weights are exact finite dot products of inherited geometric
class counts with rook probabilities.  No perfect-matching enumeration is
needed, and rational assignment/host certificates are integer-checkable.  The
remaining problem is to bound the geometric owner-class counts strongly
enough for a subcritical same-owner row.  No all-`n` theorem is claimed.

Checked by
[`scripts/verify_prime_power_rook_owner_edge_weights.py`](../scripts/verify_prime_power_rook_owner_edge_weights.py).
