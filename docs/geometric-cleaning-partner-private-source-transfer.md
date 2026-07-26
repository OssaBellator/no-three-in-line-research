# Partner-private destroyed sources and bounded-congestion latent payment

**Branch:** `research/geometric-cleaning`

GC2k--GC2n show that a dangerous secant cannot pay through its own line and
that source-free latent witnesses exist.  A positive transfer is nevertheless
automatic when the rectangle correction destroys a current factor through its
partner cell rather than only through the common target.

The reason is rank.  Distinct partners are distinct current cells, so one
rank-`r` current factor can be partner-private for at most `r` corrections.
This note turns that observation into a bounded-congestion source map and
classifies every failure.

## Fixed-target rectangle family

Fix one current target cell `b` and a finite set `U` of distinct current partner
cells.  For every `u in U`, the rectangle correction `T_u` removes `b,u` and
inserts the two opposite corners.  Let its latent line-blocker witness have
weight `lambda_u>=0`.

Every current factor destroyed by `T_u` contains `b` or `u`, because those are
the only removed cells.

A destroyed current factor `Q` is **partner-private for `u`** when

- `u in Q`;
- `b notin Q`.

Let its current syndrome capacity be `omega_Q>0`, and assume all current factors
have rank at most `r`.

## GC2o -- partner-private source reuse is at most the factor rank -- PROVED

Suppose each partner `u` is assigned one partner-private destroyed factor
`Q_u`.  Then every exact current factor `Q` is assigned by at most `r` partners.

### Proof

If `Q_u=Q`, then `u` is one of the cells of `Q`.  The partners are distinct and
`Q` has at most `r` cells.  Hence at most `r` partners can assign to `Q`. QED.

No disjointness of the rectangle supports is needed; all corrections may share
the common target `b`.

## GC2p -- automatic bounded-congestion transfer -- PROVED

Fix `kappa>=1`.  Suppose every selected partner `u` has a partner-private source
`Q_u` satisfying

`lambda_u <= kappa * omega_(Q_u)`.

Then the assignment `u -> Q_u` is a cross-line source map of congestion at most

`M=r*kappa`.

Consequently the scaled charges

`p_u=lambda_u/(r*kappa)`

are factor-conservative current payment, with total paid mass

`sum_u p_u = (sum_u lambda_u)/(r*kappa)`.

### Proof

For one current factor `Q`, GC2o gives at most `r` assigned partners.  Each has
`lambda_u<=kappa*omega_Q`, so

`sum_(u:Q_u=Q) lambda_u <= r*kappa*omega_Q`.

This is exactly the congestion inequality from GC2n.  Scaling by `1/(r*kappa)`
preserves every factor capacity and the correction--factor provenance. QED.

For unweighted rank-three factors with `lambda_u<=omega_(Q_u)`, the loss is at
most the explicit factor `3`.

## Canonical eligibility and failure roles

Fix `kappa>=1`.  For each partner choose the least partner-private destroyed
factor satisfying `lambda_u<=kappa*omega_Q`, if one exists.  Call the partner
**eligible**.

Every ineligible partner has exactly one canonical failure role:

1. **source-free:** `T_u` destroys no current factor;
2. **target-common:** destroyed factors exist, but every one contains `b`;
3. **private-underweight:** a partner-private destroyed factor exists, but every
   such factor has `lambda_u>kappa*omega_Q`.

These roles are exhaustive because a destroyed factor contains `b` or `u`.

## GC2q -- paid private transfer or localized residual obstruction -- PROVED

Let the total latent weight be

`W=sum_(u in U) lambda_u`.

Then one of the following holds.

1. Eligible partners carry weight at least `W/2`.  They admit
   factor-conservative payment of at least

   `W/(2*r*kappa)`

   by GC2p.
2. One of the three ineligible failure roles carries latent weight at least

   `W/6`.

### Proof

If eligible weight is at least `W/2`, apply GC2p.  Otherwise ineligible weight
is greater than `W/2`.  The three canonical roles partition it, so one carries
at least one third of that mass, hence more than `W/6`. QED.

## GC2r -- target-common failure is an exact current-anchor obstruction -- PROVED

In the target-common role, every current factor destroyed by every retained
correction contains the same target cell `b`.

Thus this residual is not an arbitrary failure of source transfer: all available
current payment is concentrated in the current-factor link of one exact cell.
It must be handled by a paid target-anchor theorem, a capacity bound on reuse of
those factors, or an alternating-core delegation.  It cannot be charged
independently once per partner.

### Proof

This is the definition of the target-common role.  Reusing one such factor for
many partners would duplicate its current syndrome capacity, so no independent
partner charge is valid without an additional capacity theorem. QED.

## Corrected GC2 frontier

The line-blocker payment problem now has four explicit branches:

- partner-private sources give automatic rank-controlled payment;
- source-free witnesses remain genuinely unpaid;
- target-common witnesses concentrate on one current target-anchor link;
- private-underweight witnesses expose a quantitative mismatch between latent
  blocker weight and available current factor capacity.

The next geometric theorem should therefore bound the source-free and
underweight classes or turn the target-common class into a paid anchor bank.
The partner-private class is no longer open.

## Finite check

`scripts/verify_geometric_partner_private_source.py` exhausts small rank-bounded
factor systems.  It checks the rank reuse bound, the `r*kappa` congestion
inequality, the three-way failure partition and the `W/2` versus `W/6`
weighted router.