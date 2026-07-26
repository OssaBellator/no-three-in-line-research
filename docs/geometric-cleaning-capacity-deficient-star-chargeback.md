# Capacity-deficient factor stars and gain-certified external chargeback

**Branch:** `research/geometric-cleaning`

GC2ba--GC2bf reduce one high-ratio Hall event to a lower-rank concentration, high pair
codegree or an endpoint-disjoint rank-three factor star.  In the star branch the retained
demand incidence exceeds `theta` times the total current factor capacity.  This note
makes the resulting unpaid residual exact.

The star factors all meet the same rectangle event and are all destroyed by that event,
but Hall capacity is not automatically the event's potential gain.  Executable descent
follows only when an external payment is certified by the current correction--factor
gain ledger of GC2g.  The distinction is retained explicitly.

## Capacity-deficient event star

Fix one exact rectangle event `j` and an endpoint-disjoint current-factor star `S_j`
returned by GC2bd.  Give factor occurrence `p in S_j` demand-incidence weight `e_p>0`
and residual current capacity `c_p>=0`.  Put

`W=sum_(p in S_j)e_p`,

`C=sum_(p in S_j)c_p`.

Assume

`C<W/theta`

for some `theta>=1`.  The complete payment demand represented by the selected star is
`W`.

Let `P_ext` be any further exact current-resource set eligible to pay event `j`, disjoint
from the selected star as resource occurrences.  A complete allocation consists of
nonnegative amounts `x_p`, `p in S_j union P_ext`, satisfying

`x_p<=c_p`

on the star, the declared external capacity bounds on `P_ext`, and

`sum_p x_p=W`.

## GC2bg -- exact internal payment ceiling and residual -- PROVED

The selected star can contribute at most `C` to any factor-conservative payment of its
own demand.  Therefore its unpaid residual

`R_star=W-C`

satisfies

`R_star>(1-1/theta)W`.

### Proof

Factor conservativity gives `x_p<=c_p` for each selected occurrence, so the total
internal contribution is at most `sum c_p=C`.  Subtract from `W` and use `C<W/theta`.
QED.

The residual is demand weight, not newly created factor weight and not potential gain.

## GC2bh -- every complete payment needs external mass -- PROVED

Every complete factor-conservative payment of demand `W` uses external payment at least

`R_star=W-C>(1-1/theta)W`.

Consequently, if the total declared external capacity is smaller than `R_star`, complete
payment is impossible and the event has an exact event-local Hall deficit.

### Proof

The star contributes at most `C` by GC2bg.  The remaining contribution must be supplied
by `P_ext`.  If its capacity is smaller than the remaining demand, no complete allocation
exists. QED.

This converts the aggregate star deficit into one exact external-source obligation.

## GC2bi -- finite external-role localization -- PROVED

Suppose every external payment incidence `(j,p)` has one of at most `T_ext` exact physical
source roles.  Any complete payment contains one role class carrying external payment at
least

`R_star/T_ext>(1-1/theta)W/T_ext`.

If every exact role fibre contains at most `B_ext` resource occurrences, one exact
external resource incidence carries payment at least

`R_star/(T_ext*B_ext)`.

### Proof

Partition the external payment from GC2bh by role and apply weighted pigeonhole.  In the
bounded-fibre refinement, partition the selected role once more by exact resource
occurrence. QED.

The role must identify the physical source and occurrence; equal lines or labels do not
merge distinct current resources.

## Gain-certified external allocations

Call an external allocation **gain-certified** when every amount `x_(j,p)` is an exact
current correction--factor charge for event `j` and resource `p`, and the event row obeys

`sum_p x_(j,p)<=g_j`,

where `g_j>0` is the current hard-legal correction gain.  This is precisely the row
condition supplied by a GC2g charge matrix.  A generic Hall allocation need not satisfy
it.

## GC2bj -- gain-certified chargeback is executable -- PROVED

If a complete payment of the star demand is gain-certified, then

`g_j>=W`.

If only the forced external part is gain-certified, then

`g_j>=R_star>(1-1/theta)W`.

In either case executing the exact rectangle event decreases the current potential by at
least the displayed amount.

### Proof

The gain-certified row inequality says that the sum of certified charges assigned to
`j` is at most `g_j`.  A complete certified row has total `W`; a certified external
subrow has total at least `R_star` by GC2bh.  The event was declared current, hard-legal
and row--column preserving, so its certified gain is executable. QED.

This is the promised chargeback interface: payment becomes descent only after provenance
to the current gain row is installed.

## GC2bk -- Hall capacity alone does not imply gain -- PROVED AS A WALL

From a factor-conservative Hall allocation satisfying only resource-capacity inequalities,
one cannot infer a positive lower bound on `g_j`.

### Proof

Take any positive capacities and a complete allocation, and independently set the event's
created collateral equal to or larger than its destroyed current weight, giving
`g_j<=0`.  The capacity inequalities remain unchanged.  Therefore a gain conclusion
requires the additional row-provenance contract used in GC2bj. QED.

The wall prevents current capacity from being silently counted as correction gain.

## GC2bl -- capacity-deficient star continuation -- PROVED UNDER THE EXTERNAL-SOURCE CONTRACT

For every endpoint-disjoint high-ratio star from GC2bd, one top-level alternative holds:

1. complete payment is impossible because external capacity is below `R_star`;
2. complete payment exists, uses external mass at least `R_star`, and localizes that mass
   to one exact physical source role, and optionally one exact resource incidence under a
   fibre cap.

Inside the second alternative, exactly one provenance branch applies:

- the forced external allocation is gain-certified, in which case the rectangle event
  gives executable descent greater than `(1-1/theta)W`;
- or it is only Hall-capacity payment and remains explicitly non-gain-certified.

Thus the star is no longer an unquantified capacity shortage.  Its missing payment is an
exact external-source mass.  The remaining GC obligation is to install gain provenance
for that source role, or to classify the resulting event-local Hall deficit.

## Corrected GC frontier

The endpoint-disjoint high-ratio star now has a sharp residual and provenance wall.
The live branch is either an exact external-source Hall deficit or one heavy external
physical role whose allocation still needs a GC2g gain certificate.  Other open
interfaces remain lower-rank and high-pair execution, isolated-cell prospective stars,
pool depletion, global context causes and local superregular resampling.

## Finite check

`scripts/verify_geometric_capacity_deficient_star_chargeback.py` exhausts and randomly
samples star capacities, demand weights, external capacities and role partitions.  It
checks the residual inequality, external-capacity Hall obstruction, role localization,
gain-certified row bound and the non-gain wall.