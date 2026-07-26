# Lineage survival and chargeback for created-collateral stars

**Branch:** `research/geometric-cleaning`

GC2cb--GC2cg convert a multiplicative destroyed-factor overload into a prospective
created-factor fibre through one inserted rectangle cell.  The output is geometric but
initially prospective: its factors become current only after the corresponding hard-legal
rectangle event is executed.

This note supplies the missing temporal ledger.  Every newly created exact factor receives
one occurrence-faithful lineage tag.  A tagged cohort then has an exact survival-or-first-
destruction identity.  Its endpoint-disjoint star either remains as current structure or is
paid, without double counting, by later correction rows.  A global tagged-energy potential
also identifies the only zero-drift residual: corrections which destroy nothing except
previously tagged collateral.

## Exact factor lineages

Work in one correction history with a fixed exact factor universe and fixed factor weights.
An exact factor **lineage** is born when a factor occurrence changes from absent to present.
If the same geometric-label signature disappears and is later recreated, the recreated
occurrence is a new lineage.

When a correction event `j` is executed, let

`D_j`

be its total destroyed current-factor weight and

`N_j`

its total newly created factor weight.  Every newly created lineage receives one active
collateral tag recording its birth event and its exact physical signature.  A tag is removed
at the first later event which destroys that lineage.  Tags never duplicate one lineage and
never survive its destruction.

Let `T(t)` be the total current factor weight, let `U(t)` be the total weight of active tagged
lineages, and put

`Phi_tag(t)=T(t)-U(t)`.

Since every active tag belongs to one current factor lineage,

`0<=U(t)<=T(t)`

and `Phi_tag(t)>=0`.

## GC2ch -- exact cohort survival/first-destruction identity -- PROVED

Fix one birth event `j_0` and one selected cohort `C` of exact lineages created by that event.
Give the cohort total initial weight

`W_C=sum_(p in C)w_p`.

At any later time `t`, partition the original cohort into lineages still current and lineages
already destroyed for the first time.  Let their weights be `S_C(t)` and `P_C(t)`.  Then

`W_C=S_C(t)+P_C(t)`.

The paid part `P_C(t)` is assigned injectively to exact later event--factor destruction
incidences: every lineage is charged only to its first destroying event.

### Proof

Every original lineage is in exactly one of two states at time `t`: it has never yet been
destroyed and remains the same current occurrence, or it has a unique first destruction time.
The alternatives are disjoint and exhaustive.  Summing their fixed lineage weights gives the
identity.  Uniqueness of the first destruction time makes the event--factor assignment
injective. QED.

Recreation of the same symbolic signature does not alter the identity because it creates a
new lineage rather than reviving the old occurrence.

## GC2ci -- half-survival or half-chargeback for a created star -- PROVED

Assume the cohort `C` is an endpoint-disjoint rank-two or rank-three created-collateral star
through one inserted cell `q`, as supplied by GC2cf, and has weight `W_C>0`.  At every later
time, at least one of the following quantitative alternatives holds:

1. `P_C(t)>=W_C/2`; later correction rows have already destroyed and paid at least half of the
   original star weight;
2. `S_C(t)>=W_C/2`; at least half of the original exact star remains current.

For a canonical disjoint router, assign the equality case `P_C(t)=S_C(t)=W_C/2` to the first
alternative.  In the second alternative, the surviving factors are still pairwise disjoint
outside `q` and all still contain the same exact current anchor `q`.

### Proof

Apply GC2ch and compare the two nonnegative summands with `W_C/2`.  A surviving lineage has
not changed its exact support.  Taking a subset of an endpoint-disjoint star preserves
endpoint disjointness and the common anchor. QED.

Thus prospective collateral cannot evaporate silently.  It becomes either current geometric
structure or exact future destruction payment.

## GC2cj -- exact global tagged-energy drift -- PROVED

Consider one correction event `j`.  Let `C_j` be the total destroyed weight whose lineages
carry active tags immediately before the event.  Tag every newly created lineage of total
weight `N_j`.  Then

`T'=T-D_j+N_j`,

`U'=U-C_j+N_j`,

and therefore

`Phi_tag'-Phi_tag=-(D_j-C_j)<=0`.

The decrease is exactly the destroyed weight not already represented by active collateral
tags.

### Proof

The ordinary factor ledger gives the update for `T`.  Destroyed tagged lineages remove tag
weight `C_j`; every new lineage receives a tag, adding `N_j`, which gives the update for `U`.
Subtract the two equations.  Since tagged destroyed weight is a subweight of total destroyed
weight, `C_j<=D_j`. QED.

This potential does not require the correction gain to be large.  It records the more basic
fact that newly created collateral is never counted as fresh current obstruction twice.

## GC2ck -- exact zero-drift recycling classification -- PROVED

For one tagged correction event,

`Phi_tag'=Phi_tag`

if and only if

`C_j=D_j`;

that is, every destroyed factor unit was already an active tagged lineage.  Otherwise the
event strictly decreases `Phi_tag` by the positive untagged destroyed weight `D_j-C_j`.

A zero-drift event may replace tagged collateral by new tagged collateral, but it cannot
consume any previously uncharged current factor.  Consequently an infinite tagged history
requires either infinitely much strict untagged destruction, or recurrent tagged-only
lineage recycling.

### Proof

The equivalence is immediate from GC2cj and `C_j<=D_j`.  The final statement partitions all
events by strict or zero drift. QED.

The tagged-only branch is a finite lineage/signature-cycle problem under a fixed physical
universe; it is not a new gain-provenance problem.

## GC2cl -- complete created-collateral chargeback router -- PROVED UNDER THE LINEAGE-CYCLE CONTRACT

Suppose GC2cf supplies a created-collateral star `C` of weight

`W_C >= (1-1/R_*)*Dsum_j/[2*r*(2Delta-1)]`

for a hard-legal event `j`, with the rank-three specialization

`W_C >= (1-1/R_*)*Dsum_j/[6*(2Delta-1)]`.

Execute `j`, tag every newly created exact lineage, and follow the resulting fixed-universe
history.  The router is nested:

1. for the distinguished cohort, exact later correction rows have paid at least `W_C/2`, or a
   current endpoint-disjoint star through the same inserted cell survives with weight at least
   `W_C/2`;
2. independently for the intervening history, the global potential `Phi_tag` has strictly
   decreased by accumulated untagged destroyed weight, or every intervening event is a
   tagged-only recycling step.

Assume every tagged-only recycling cycle in the fixed exact lineage/signature state graph is
quotient-stuttering, strictly descending, or consumes a finite exact cycle ticket, and every
change of the physical universe, factor weights, lineage signature alphabet or payment
semantics is an outer reset.  Then no created-collateral branch can sustain an infinite
nonterminal history without cohort payment, a surviving current star, strict tagged-potential
descent or an outer reset.

### Proof

GC2ci gives the first nested pair for the distinguished star cohort at every checkpoint.
GC2cj sums all strict untagged destruction into the nonnegative potential `Phi_tag`.  If no
strict decrease occurs, GC2ck says every event destroys tagged weight only.  Under the stated
finite-state lineage-cycle contract, recurrent tagged-only segments erase, descend or spend
finite tickets.  A forbidden data change exits the epoch. QED.

## Corrected GC frontier

The multiplicative-overload branch no longer ends at merely prospective collateral.  After
execution, its star has an exact temporal continuation: half survives as current anchored
structure or half is charged to later destruction rows, while the global tagged-energy
potential pays every destruction of previously untagged factors.

The next live geometry is therefore current surviving created stars, high created-pair
multiplicity, or tagged-only recycling cycles.  These may be fed into GC4 installation and
conflict overload, finite lineage-cycle tickets, or exact current-factor chargeback.  Other
open interfaces remain isolated-cell prospective stars not yet tied to an executable event,
pool depletion, global context causes and local superregular resampling.

## Finite check

`scripts/verify_geometric_created_collateral_lineage_chargeback.py` exhausts small weighted
lineage cohorts and event updates and samples longer histories.  It checks the exact cohort
partition, first-destruction injectivity, half-survival/half-payment dichotomy, endpoint-
disjoint survivor inheritance, tagged-energy drift and zero-drift recycling classification.