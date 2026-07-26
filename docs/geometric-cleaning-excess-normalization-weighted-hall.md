# Capacity normalization and weighted Hall deficits for overload-demand stars

**Branch:** `research/geometric-cleaning`

GC2ab--GC2af attach positive excess-demand weight to exact current factors and
localize rank-three excess to pair concentration or an endpoint-disjoint anchor
star.  The excess is not automatically paid: it may exceed current factor capacity.

This note gives the exact next interface.  Bounded excess/capacity ratio scales to a
factor-conservative payment.  Without such a bound, a threshold split returns either
a paid moderate part or a heavy-ratio factor family.  For downstream reopening
events, fractional payment is characterized exactly by weighted Hall inequalities;
failure returns a concrete weighted deficient event set.

## Excess-demand star

Fix one anchor `v` and a finite family `F_v` of distinct exact current factors
containing `v`.  Factor `Q` has current capacity `omega_Q>0` and excess-demand
weight `e_Q>0`.  Put

`E=sum_(Q in F_v)e_Q`.

The factors may be an endpoint-disjoint rank-three star from GC2ae, a lower-rank
concentration, or a high-pair fibre after fixing the corresponding exact role.

## GC2ag -- bounded ratio gives direct factor-conservative payment -- PROVED

Suppose

`e_Q <= R*omega_Q`

for every `Q in F_v`, where `R>=1`.  Define

`p_Q=e_Q/R`.

Then `0<p_Q<=omega_Q` for every factor and

`sum_Q p_Q=E/R`.

Thus a bounded excess/capacity ratio converts the complete overload-demand family
to factor-conservative paid mass with loss exactly `R`.

### Proof

Divide the displayed ratio inequality by `R`.  Summing `p_Q=e_Q/R` gives the total.
QED.

The payment is attached to the same exact factor occurrence and therefore needs no
cross-factor congestion theorem.

## GC2ah -- threshold pay-or-heavy split -- PROVED

Fix `theta>=1`.  Partition

`M_theta={Q:e_Q<=theta*omega_Q}`

and

`H_theta={Q:e_Q>theta*omega_Q}`.

Write `E_M` and `E_H` for their excess totals.  Then one of the following holds:

1. `E_M>=E/2`, and the moderate factors carry factor-conservative payment at least
   `E/(2*theta)` via `p_Q=e_Q/theta`;
2. `E_H>E/2`, and every retained heavy factor has exact ratio
   `e_Q/omega_Q>theta`.

### Proof

The two excess totals sum to `E`, so one is at least half.  On the moderate class,
`e_Q/theta<=omega_Q`, and the total normalized payment is `E_M/theta`.  The heavy
class has the defining ratio inequality. QED.

This theorem may be iterated over increasing thresholds.  Failure to normalize is
not diffuse: more than half of the current excess remains on factors whose overload
ratio exceeds the chosen threshold.

## Weighted reopening-payment system

Let `J` be a finite family of downstream star-reopening or installation events.
Event `j` requires nonnegative payment amount `a_j`.  Let `P` be a finite set of
exact current-factor resources with capacities `c_p>=0`.  Event `j` has an eligible
resource set `A_j subseteq P`.

A fractional payment is a family `x_(j,p)>=0` satisfying

`sum_(p in A_j)x_(j,p)=a_j`

for every event and

`sum_(j:p in A_j)x_(j,p)<=c_p`

for every resource.

## GC2ai -- weighted capacitated Hall theorem -- PROVED

A fractional payment exists if and only if every event subset `X subseteq J`
satisfies

`sum_(j in X)a_j <= sum_(p in union_(j in X)A_j)c_p`.

If payment fails, there is an exact weighted Hall-deficient subset `X` with strict
reverse inequality.

### Proof

Build a flow network with source-to-event capacity `a_j`, infinite event-to-eligible
resource edges and resource-to-sink capacity `c_p`.  A flow saturating every
source-to-event edge is exactly a fractional payment.  By max-flow/min-cut, such a
flow exists precisely when every cut determined by an event set `X` has eligible
resource capacity at least its total demand.  Failure gives a minimum cut and hence
the stated strict deficient subset. QED.

The theorem is the weighted analogue of GC4i.  It avoids integer tokenization and
preserves the rational weights naturally produced by overload normalization.

## GC2aj -- normalized excess factors satisfy weighted Hall automatically -- PROVED

Let `G subseteq F_v` be any factor class satisfying `e_Q<=R*omega_Q`.  Create one
event `j_Q` per factor with demand

`a_(j_Q)=e_Q/R`

and sole eligible resource `A_(j_Q)={Q}` of capacity `omega_Q`.

Then every weighted Hall inequality holds, and the events receive total payment

`sum_(Q in G)e_Q/R`.

### Proof

For any event subset, its eligible resources are the corresponding distinct factors.
The demand sum is at most the sum of their capacities term by term.  Apply GC2ai.
QED.

More general downstream events may use several factors.  In that setting GC2ai
returns either an actual fractional allocation or a weighted deficient cluster;
there is no remaining ambiguity about the payment obstruction.

## GC2ak -- complete excess normalization/Hall router -- PROVED

Fix `theta>=1` for an overload-demand anchor family of total excess `E`.  There is
one exact continuation:

1. factor-conservative normalized payment at least `E/(2*theta)`;
2. a heavy-ratio factor family carrying more than `E/2` excess with
   `e_Q/omega_Q>theta` on every retained factor;
3. after any downstream event/eligibility system is declared on a normalized
   factor class, a fractional payment satisfying every event demand;
4. or an exact weighted Hall-deficient event subset whose total demand exceeds the
   capacity of its complete eligible current-factor neighbourhood.

### Proof

Apply GC2ah.  The moderate route gives outcome 1 and its singleton eligibility
system satisfies GC2aj.  If a richer event system is used, apply GC2ai to obtain
outcome 3 or 4.  The heavy branch is outcome 2. QED.

## Corrected GC frontier

Capacity overload now has an exact normalization interface:

- bounded ratios produce real paid current-factor mass;
- failure at threshold `theta` concentrates more than half the excess above ratio
  `theta`;
- every declared weighted reopening system either pays fractionally or returns an
  exact weighted Hall deficit.

The remaining geometric work is to bound overload ratios from the fixed-target
geometry, exploit arbitrarily high-ratio factor families, or classify the weighted
Hall-deficient clusters through GC4k/GC4l and alternating-core delegation.

## Finite check

`scripts/verify_geometric_excess_normalization_weighted_hall.py` exhausts small
rational capacity/excess systems and event-resource graphs.  It checks bounded-ratio
normalization, the threshold split, singleton-factor Hall payment, direct fractional
max-flow feasibility and exact weighted deficiency witnesses.