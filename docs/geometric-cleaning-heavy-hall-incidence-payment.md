# Heavy physical Hall incidences: menu size, payment and excess ratio

**Branch:** `research/geometric-cleaning`

GC2aq--GC2au show that a nonsingleton weighted Hall failure has one exact current
resource and one physical destruction role whose events all delete the same target or
partner cell.  Such a role fibre is a conflict clique.  For rectangle corrections it
is also a finite alternative menu: once the common deleted cell is fixed, a distinct
event is determined by its other deleted cell.

This note collapses the clique to one heavy exact event incidence and then compares
that incidence directly with the capacity of its current resource.  The Hall branch
therefore ends in real normalized payment, a zero-capacity obstruction or one exact
high excess/capacity ratio.

## Exact rectangle-event convention

Work on an `N x N` permutation layer.  An exact rectangle event is determined by an
ordered pair `(b,u)` of distinct current layer cells, its target and partner.  If
several identical records have the same ordered pair and resource role, aggregate
them into one event with their total weight.

Fix a current resource `p` and one physical role from GC2aq.  Give its role fibre
nonnegative incidence weights `v_j` and total

`V=sum_j v_j`.

## GC2av -- a fixed physical role has at most `N-1` rectangle alternatives -- PROVED

A fixed target role `(target,q)` contains at most `N-1` distinct events.  A fixed
partner role `(partner,q)` also contains at most `N-1` distinct events.

### Proof

In the target role every event has target `q`; distinct exact events have distinct
partners.  A permutation layer has one cell in each row and column, and the partner
must differ from `q`, leaving at most `N-1` choices.  The partner-role argument is the
same with target and partner interchanged. QED.

The conclusion is a menu-size statement, not simultaneous compatibility.

## GC2aw -- one heavy exact event incidence -- PROVED

Every nonempty physical role fibre contains one exact event--resource incidence of
weight at least

`V/(N-1)`

for `N>=2`.

For the fibre supplied by GC2as from a nonsingleton canonical Hall core `X`, one exact
incidence has weight

`v_* >= |X|*delta/[2*r*M*(N-1)]`,

where `delta` is the core deficiency, `r` the resource-rank bound and `M` the number
of shared resources.

### Proof

GC2av bounds the number of aggregated events by `N-1`; weighted pigeonhole gives the
first inequality.  Substitute the lower bound `V>=|X|delta/(2rM)` from GC2as. QED.

Thus a large same-cell clique cannot remain quantitatively diffuse over more than a
linear number of exact rectangle alternatives.

## GC2ax -- exact-incidence pay-or-ratio split -- PROVED

Let the selected exact event incidence have deficiency weight `v_*>0`, and let its
exact current resource have capacity `c_p>=0`.  Fix `theta>=1`.

Exactly one of the following top-level cases holds:

1. `c_p=0`, giving an exact zero-capacity event--resource obstruction;
2. `c_p>0` and `v_*<=theta*c_p`, in which case

   `x_(j*,p)=v_*/theta`

   is factor-conservative paid mass attached to that exact event and resource;
3. `c_p>0` and `v_*>theta*c_p`, giving the exact incidence ratio

   `v_*/c_p>theta`.

In the payment case the paid amount is at least

`|X|*delta/[2*r*M*(N-1)*theta]`.

### Proof

The zero-capacity case is separate.  In the moderate case division by `theta` gives
`0<x_(j*,p)<=c_p`, so the allocation is feasible on the exact resource.  The remaining
positive-capacity case is precisely the displayed ratio inequality.  Substitute
GC2aw's lower bound in the payment branch. QED.

The payment is a quantitative portion of the event's uncovered Hall demand.  It does
not assert that the full event demand is paid.

## GC2ay -- physical Hall failure now routes to payment or one exact ratio -- PROVED UNDER THE RECTANGLE-DESTRUCTION CONTRACT

Whenever GC2ak returns a weighted Hall failure for occurrence-faithful rectangle
events with current resource rank at most `r`, fix `theta>=1`.  There is one exact
continuation:

1. a singleton Hall core, hence one atomic demand/neighbourhood-capacity overload;
2. a zero-capacity exact event--resource incidence;
3. factor-conservative current payment at least

   `|X|*delta/[2*r*M*(N-1)*theta]`;
4. or one exact event--resource incidence with deficiency-weight/capacity ratio greater
   than `theta`.

### Proof

Use GC2ap for a singleton core.  For a nonsingleton core, apply GC2as, GC2av and
GC2aw to select the heavy event incidence, then apply GC2ax. QED.

The same-deleted-cell clique is an intermediate localization device; it is no longer a
terminal GC output.

## GC2az -- unified normalized-overload continuation -- PROVED

Combining GC2ah and GC2ay, fixed-target overload demand at threshold `theta` has one
of the following exact structural outputs:

1. direct factor-conservative payment from the moderate overload factors;
2. a factor family carrying more than half the excess with factor ratio above
   `theta`;
3. an atomic or zero-capacity weighted event overload;
4. factor-conservative payment on one exact heavy Hall incidence;
5. or one exact heavy Hall incidence whose deficiency-weight/capacity ratio exceeds
   `theta`.

Thus both the direct overload branch and the Hall-failure branch now terminate in the
same payment-or-high-ratio language.

## Corrected GC frontier

The remaining geometric work is to exploit one exact high-ratio factor or event
incidence, rather than to localize a diffuse Hall fan.  Other open interfaces remain
the isolated-cell prospective star, pool depletion, global context causes and local
superregular resampling.

## Finite check

`scripts/verify_geometric_heavy_hall_incidence_payment.py` exhausts small permutation
layers, fixed target/partner role fibres and weight/capacity assignments.  It checks
the `N-1` menu bound, heavy-event localization, the quantitative Hall import and the
exact pay/zero-capacity/high-ratio split.