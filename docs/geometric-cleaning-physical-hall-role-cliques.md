# Physical destruction roles inside weighted Hall cores

**Branch:** `research/geometric-cleaning`

GC2al--GC2ap localize weighted Hall failure to one exact shared current resource and
one geometric role.  For rectangle corrections, current-resource eligibility has a
much sharper physical meaning: a current factor is destroyed only because the target
or the partner cell is deleted.  Once the exact destroyed support cell and its side
are fixed, every event in that role fibre deletes the same physical cell.

Therefore a same-resource, same-destruction-role fibre is a conflict clique, not a
broad compatible fan.  Weighted deficiency consequently localizes to either a
same-cell conflict overload or one heavy exact event--resource incidence.

## Rectangle destruction eligibility

An event `j` is one rectangle correction with target cell `b_j` and partner cell
`u_j`.  It deletes `b_j,u_j` and inserts the two cross-cells.

Let `p` be one exact current factor resource with physical support `Q_p` of rank at
most `r`.  Occurrence-faithful eligibility means

`p in A_j  =>  Q_p intersect {b_j,u_j} != empty`.

Fix a total order on support cells.  The canonical physical destruction role of
incidence `(j,p)` is the least pair

`(side,q)`

such that `q in Q_p` and either `side=target,q=b_j` or
`side=partner,q=u_j`.

There are at most `2r` roles for one resource.

## GC2aq -- finite physical destruction-role dictionary -- PROVED

Every occurrence-faithful event--resource incidence has one canonical role from an
alphabet of size at most `2r`.

The role records the exact deleted support cell and whether it is the target or the
partner.  Inserted cross-cells are not valid destruction roles for a current factor.

### Proof

Eligibility supplies at least one support cell among the two deleted cells.  Choose
the least eligible `(side,q)` in the fixed order.  Each of the at most `r` support
cells has two possible sides.  A current factor survives insertion and can be
destroyed only by deletion, so no cross-cell role is needed. QED.

## GC2ar -- every fixed physical role fibre is a clique -- PROVED

Fix one exact resource `p` and one canonical role `(target,q)`.  Every event in that
fibre has `b_j=q`.  Hence any two distinct events delete the same target cell and
cannot be installed simultaneously.

Likewise, every event in a fixed role `(partner,q)` has `u_j=q`, so the fibre is again
a clique in the full installation-conflict graph.

### Proof

The role definition fixes the corresponding deleted rectangle cell.  Two distinct
rectangle corrections using the same deleted target or partner compete for that
physical permutation-layer cell, so simultaneous installation is impossible. QED.

This uses the standard GC conflict relation, which includes shared deleted cells.

## GC2as -- weighted physical-role localization in a minimal Hall core -- PROVED

Let `X` be the canonical nonsingleton weighted Hall core from GC2al, with deficiency
`delta>0`, shared-resource set `P_sh` of size `M`, and uncovered-incidence total `U`.
Assume every shared eligible resource has physical support rank at most `r` and use
the equal-split weights `w_(j,p)` from GC2an.

Then one exact resource `p*` and one physical destruction role carry total incidence
weight at least

`U/(2*r*M) >= |X|*delta/(2*r*M)`.

All events in the selected fibre form a clique.

### Proof

GC2an gives one shared resource carrying weight at least `U/M`.  Partition that
resource's incidences among at most `2r` canonical roles from GC2aq and choose a
heaviest role.  GC2ar makes the selected fibre a clique. QED.

The selected weight is uncovered Hall-deficiency incidence, not capacity already
available for payment.

## GC2at -- clique-or-heavy-event dichotomy -- PROVED

Give the selected physical role fibre total incidence weight `V`.  For every integer
`Gamma>=0`, exactly one of the following structural alternatives is available:

1. the fibre has more than `Gamma+1` events, and every event conflicts with more than
   `Gamma` other events in the same exact resource--role fibre;
2. the fibre has at most `Gamma+1` events, and one exact event--resource incidence has
   weight at least

   `V/(Gamma+1)`.

Consequently the heavy-event alternative has weight at least

`|X|*delta/[2*r*M*(Gamma+1)]`.

For `Gamma=0`, the output is simply either two distinct corrections deleting the same
exact cell or one exact heavy event incidence.

### Proof

A clique on `k` vertices has degree `k-1` at every vertex.  If `k>Gamma+1`, use the
first alternative.  Otherwise weighted pigeonhole among at most `Gamma+1` events
gives the second.  Substitute GC2as's lower bound for `V`. QED.

## GC2au -- physical completion of the weighted Hall continuation -- PROVED UNDER THE RECTANGLE-DESTRUCTION CONTRACT

Whenever the normalized overload branch returns a weighted Hall failure whose events
are occurrence-faithful rectangle corrections and whose current resources have rank
at most `r`, there is one exact continuation:

1. a singleton Hall core, hence one atomic demand/capacity overload;
2. two or more same-resource corrections deleting one common exact target or partner
   cell, quantitatively refined by the `Gamma` conflict alternative in GC2at;
3. or one exact event--resource incidence carrying at least

   `|X|*delta/[2*r*M*(Gamma+1)]`

   of the uncovered-deficiency scale.

### Proof

Use GC2ap for a singleton core.  For a nonsingleton core apply GC2as and GC2at. QED.

Thus the generic compatible Hall-deficiency fan disappears under the physical
rectangle-destruction role contract.  It is replaced by a same-deleted-cell conflict
clique or one heavy exact event incidence.

## Corrected GC frontier

The weighted Hall branch is now reduced to atomic or one-cell physical structure.
The remaining work is to:

- turn a heavy event incidence into normalized current payment or a higher exact
  excess ratio;
- classify repeated corrections deleting the same target or partner cell;
- exploit high-ratio current factors from the other GC2ak branch;
- and combine these routes with isolated-cell prospective stars, pool depletion,
  global context causes and local superregular resampling.

## Finite check

`scripts/verify_geometric_physical_hall_role_cliques.py` exhausts small rectangle
event systems and random weighted Hall cores.  It checks canonical support-cell/side
roles, the `2r` role stock, clique structure, weighted resource/role localization and
the clique-or-heavy-event bound.
