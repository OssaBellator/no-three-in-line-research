# Every created triple has one absolute last-entering-edge owner

CMR1202 and CMR1208 count new collateral in one response bank.  To combine banks
across fixed-core contraction, unit-wall products, child products and lifted
owners, the same physical triple must not be charged at several structural levels.
This chapter gives a canonical absolute owner.

Fix once and for all a total order `prec` on the labelled physical edge universe:
first by layer, then by absolute source coordinate, then by absolute target
coordinate.

For a transition between labelled saturated states `S` and `Q`, put

\[
E^+(S,Q)=Q\setminus S.
\]

All physical triples are interpreted in the original parent-grid coordinates.

## 1. Every new physical triple contains an entering edge

### Theorem CMR1214 -- PROVED

If

\[
U\in\mathcal T(Q)\setminus\mathcal T(S),
\]

then at least one labelled edge of `Q` whose physical cell lies in `U` belongs to
`E^+(S,Q)`.

### Proof

If every labelled edge of `Q` supporting the three physical cells of `U` already
belonged to `S`, then all three physical cells would be selected in `S`, so
`U in mathcal T(S)`, contrary to the hypothesis.  Physical layer disjointness
ensures that each selected physical cell has one labelled representative. ∎

Thus created collateral always has a genuinely new physical support edge.

## 2. Canonical entering-edge owner

For every new triple `U`, define

\[
\omega_{S,Q}(U)
=
\min_{\prec}
\{e\in E^+(S,Q):\operatorname{cell}(e)\in U\}.
\]

### Theorem CMR1215 -- PROVED

The map `omega_{S,Q}` is well defined and partitions the new triples:

\[
\boxed{
\mathcal T(Q)\setminus\mathcal T(S)
=
\bigsqcup_{e\in E^+(S,Q)}
\mathcal N_e(S,Q),
}
\]

where

\[
\mathcal N_e(S,Q)
=
\{U:\omega_{S,Q}(U)=e\}.
\]

Consequently

\[
\boxed{
N(Q)
=
\sum_{e\in E^+(S,Q)}|\mathcal N_e(S,Q)|.
}
\]

### Proof

CMR1214 gives a nonempty finite owner set for every new triple, so the fixed total
order chooses one edge.  A function has disjoint fibres whose union is its domain.
∎

No geometric triple is charged once for each of its entering cells.

## 3. Expected collateral decomposes by absolute owners

Let `mu` be any probability distribution on a finite response bank.

### Theorem CMR1216 -- PROVED

\[
\boxed{
\mathbb E_{Q\sim\mu}N(Q)
=
\sum_e
\mathbb E_{Q\sim\mu}
\left[
\mathbf 1_{e\in E^+(S,Q)}
|\mathcal N_e(S,Q)|
\right].
}
\]

### Proof

Apply CMR1215 to every state and interchange two finite sums. ∎

This identity is independent of routing, factor or certificate labels.

## 4. Fixed-core cells do not duplicate collateral

Suppose a compatible prescription `P` has been conditioned and contracted, and a
residual response lifts from `R` to `P union R`.

### Theorem CMR1217 -- PROVED

Every triple created by the lifted response which uses cells of `P` is still owned
by one entering residual edge.  No edge of the unchanged fixed core is an owner.

### Proof

The fixed prescription belongs to both the old and new lifted states, so none of
its edges lies in `E^+(S,Q)`.  CMR1214 supplies an entering edge among the remaining
cells of every new triple.  The owner definition therefore chooses a residual
entering edge, even for rank-zero, rank-one or rank-two anchored collateral relative
to the residual factor. ∎

The fixed interface contributes geometry to the owner load but does not receive a
second charge.

## 5. Exact products preserve unique ownership

Consider any exact product used in the selected scheduler: protected/free,
fixed-routing child, unit-wall, essential-core or exchange-SCC factorisation.

### Theorem CMR1218 -- PROVED

Every entering labelled edge belongs either to one fixed interface or to exactly
one residual factor.  If it is not fixed in the transition, it belongs to one
unique varying factor.  Hence its owned collateral is assigned to that one factor
owner and not to all factors touched by the physical triple.

### Proof

CMR822 gives unique edge ownership in every listed exact product.  Fixed interface
edges are unchanged and cannot lie in the entering set.  Therefore every entering
owner edge lies in one unique residual factor.  The physical triple may touch
several factors, but CMR1215 assigns it by one edge rather than by every touched
factor. ∎

This is the required no-double-counting rule for low-rank Cartesian coupling atoms.

## 6. Ownership survives contraction and lifting

### Theorem CMR1219 -- PROVED

Let an entering edge `e` later become part of a contracted minimum core or fixed
unit-wall interface.  Every triple previously assigned to `e` remains assigned to
the same absolute labelled physical edge at its creation transition.  A later
lifted-owner representation does not create another collateral occurrence.

### Proof

The owner is defined from the absolute old and new states at the transition where
the triple first appears.  Later contraction changes representation, not that
historical physical transition.  Absolute source, target and layer labels are
unchanged. ∎

If the physical triple disappears and is later recreated, that later creation is a
new transition and is charged to the entering edge of the new absence run.

## 7. Bank scores split into edge-owner scores

In the fixed-target bank of CMR1198, order the allowed response edges by `prec`.
For `U in mathcal V_r`, let `a(U)` be the least edge of its residual prescription
`P_U`.  Define

\[
V_r(a)
=
|\{U\in\mathcal V_r:a(U)=a\}|,
\]

and

\[
\mathcal C_a
=
\frac{V_1(a)}n
+
\frac{V_2(a)}{(n)_2}
+
\frac{V_3(a)}{(n)_3}.
\]

### Theorem CMR1220 -- PROVED

\[
\boxed{
\mathcal C(S;O,F)
=
\sum_{a\in E(G)}\mathcal C_a.
}
\]

Moreover

\[
\boxed{
\mathbb E N(Q_R)
\le
\kappa_n
\sum_{a\in E(G)}\mathcal C_a.
}
\]

Each summand is attached to one absolute response edge and therefore to one unique
structural lineage.

### Proof

The least-edge rule partitions every `mathcal V_r`.  Summing the partition sizes
gives `V_r`, and CMR1202 supplies the expectation bound. ∎

The edge-local scores can now be compared with prefix cells, carry signatures,
Hall walls or full-token inventories without charging a triple at each ancestor.

## 8. Collateral-owner endpoint

### Corollary CMR1221 -- PROVED

The fixed-interface bookkeeping part of CMR1196 has the following exact normal
form.

1. Every new physical triple has one absolute entering-edge owner.
2. Owned loads partition total collateral exactly.
3. Fixed-core cells contribute anchored geometry but receive no duplicate owner
   charge.
4. Exact products assign every entering owner edge to one unique residual factor.
5. Later contraction or lifting preserves the historical owner.
6. Every fixed-target bank score is a sum of edge-local normalized scores.

Therefore the remaining target-versus-collateral problem may be stated as an
edge-owner inequality:

\[
\sum_{e\in E(S)}A_H(e)<3\Phi(S)
\]

or a stronger weighted variant, with every collateral term assigned once.  The
open task is now quantitative control of the owner scores by line, prefix, carry,
unit-wall and CRT structure, not ownership ambiguity.

No all-`n` theorem is claimed.  New-triple support, owner partitions, expectation
identities, fixed-core lifting, product uniqueness and score decomposition are
checked in
[`scripts/verify_prime_power_last_entering_collateral_owner.py`](../scripts/verify_prime_power_last_entering_collateral_owner.py).
