# Decomposing quotient secant incidence

CMR80 bounds aggregate rank-one repair collateral by the quotient secant energy
`J_s`. This chapter separates its universal endpoint contribution from genuine
quotient modular triples and repeated-projection carry stars.

Let

\[
N=p^k,
\qquad 1\le s<k,
\qquad m=p^s,
\qquad t=N/m,
\]

and let `S` be a recursive saturated two-layer state. Write

\[
\bar S_s
=
G(P_{0,s})\cup G(P_{1,s})
\subseteq[m]^2
\]

for its quotient state. It has exactly `2m` distinct points.

For a full selected point `P=(x,y)`, put

\[
\rho_s(P)=(x\bmod m,y\bmod m).
\]

For a full secant pair `e={P,Q}`, let `L_e` have primitive equation

\[
A_ex+B_ey=C_e.
\]

Define

\[
n_s(e)
=
\#\{R\in\bar S_s:A_eR_x+B_eR_y\equiv C_e\pmod m\}.
\]

By definition,

\[
n_s(e)=\sum_{\ell=0}^1 I_{s,\ell}(L_e).
\]

## 1. Distinct and repeated projections

Call `e` **distinct at scale s** when

\[
\rho_s(P)\ne\rho_s(Q),
\]

and a **collision pair** otherwise.

For a distinct pair, define

\[
q_s(e)=n_s(e)-2.
\]

The subtraction removes the two projected endpoints, both of which satisfy the
reduced line equation.

### Theorem CMR82 — PROVED

Let `E_s^dist` and `E_s^coll` be the full secant pairs of the two types. Then

\[
\mathcal J_s(S)
=
2|E_s^{dist}|
+
\sum_{e\in E_s^{dist}}q_s(e)
+
\sum_{e\in E_s^{coll}}n_s(e).
\]

Moreover,

\[
|E_s^{coll}|
=
2m\binom t2
=
N(t-1),
\]

and therefore

\[
|E_s^{dist}|
=
\binom{2N}{2}-N(t-1).
\]

### Proof

For a distinct pair, the two projected endpoints are two distinct selected
quotient points on the reduced line, so `n_s(e)=2+q_s(e)`.

A collision pair must have equal quotient column residues. It cannot use two
layers, because the saturated quotient state has

\[
P_{0,s}(a)\ne P_{1,s}(a)
\]

at every quotient column. Thus collision pairs are exactly the same-layer pairs
inside one quotient column fibre.

Each layer has `m` fibres containing `t` full points, so the number is

\[
2m\binom t2.
\]

Summing `n_s(e)` over the two pair classes proves the decomposition. ∎

The first term is a universal endpoint baseline. Every term beyond it is either
a genuine modular third-point incidence or a collision carry star.

## 2. Distinct-projection modular triples

### Theorem CMR83 — PROVED

For every distinct pair `e`, the quantity `q_s(e)` is exactly the number of
selected quotient points other than the two endpoints that form a
three-distinct-point modular collinear certificate on the specific reduced line
of `e`.

Consequently

\[
\mathcal M_s(S)
:=
\sum_{e\in E_s^{dist}}q_s(e)
\]

is a weighted quotient modular-syndrome energy. Its weight records how many
full real secants reduce to the same quotient line certificate.

### Proof

Every quotient point counted by `n_s(e)` satisfies the reduced primitive line
equation. For a distinct pair, the two endpoint projections are distinct and
account for exactly two counted points. Every remaining counted point is
distinct from both and supplies the claimed modular triple. Conversely every
such selected quotient point is counted by `n_s(e)`. ∎

Over the composite ring `Z/(p^s)`, one quotient point triple may satisfy more
than one primitive line equation. The definition deliberately retains the line
signature inherited from the full real secant; this is the carry information
needed for charging.

## 3. Collision pairs and primitive carry directions

Take a collision pair and orient it as `P,Q`. Since the projections agree,
write

\[
Q-P=m(u,v)
\]

with integers `u,v`, not both zero. Put

\[
g=\gcd(|u|,|v|),
\qquad
(u_0,v_0)=(u/g,v/g).
\]

### Theorem CMR84 — PROVED

The primitive real line of the collision pair reduces modulo `m` to

\[
-v_0(x-\bar x)+u_0(y-\bar y)
\equiv0\pmod m,
\]

where

\[
(\bar x,\bar y)=\rho_s(P)=\rho_s(Q).
\]

Hence `n_s(e)` is exactly the occupancy of the quotient saturated state on the
primitive carry-direction line through the collided quotient point.

### Proof

The exact displacement is `(mu,mv)`, whose coordinate gcd is `mg`. A primitive
normal vector to the real secant is therefore `(-v_0,u_0)`. The exact line
equation through `P` is

\[
-v_0(x-P_x)+u_0(y-P_y)=0.
\]

Reduce it modulo `m` and replace `P` by its common quotient residue. The selected
quotient solutions are precisely those counted by `n_s(e)`. ∎

Define the collision carry energy

\[
\mathcal C_s(S)
=
\sum_{e\in E_s^{coll}}n_s(e).
\]

CMR82 can now be written

\[
\boxed{
\mathcal J_s(S)
=
2\left(\binom{2N}{2}-N(t-1)\right)
+
\mathcal M_s(S)
+
\mathcal C_s(S).
}
\]

## 4. Revised charging target

The CMR81 rank-one obstruction is now explicit:

1. a deterministic endpoint baseline;
2. `M_s`, consisting of three-distinct-point modular quotient certificates with
   inherited real-line signatures;
3. `C_s`, consisting of same-layer repeated-projection pairs organized by
   primitive carry direction.

The next theorem should bound the excess energies `M_s` and `C_s` by the
quotient real syndrome, displacement multiplicities, and carry-cell energies.
For completed-reciprocal quotient states, CMR6, CMR9--CMR10, and
CMR58--CMR66 provide the required direction and valuation signatures.

A further sharpening of CMR80 should treat the universal endpoint baseline
separately, because the two forbidden matchings remove the original selected
cells from the actual rank-one candidate set. That is the remaining place where
the current `t I` line-lift bound is intentionally coarse.

The exact decomposition checks are in
[`scripts/verify_prime_power_quotient_incidence.py`](../scripts/verify_prime_power_quotient_incidence.py).
