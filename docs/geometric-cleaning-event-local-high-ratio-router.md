# Event-local high-ratio demand and deleted-cell factor stars

**Branch:** `research/geometric-cleaning`

GC2av--GC2az reduce a physical weighted Hall failure to current payment, an atomic or
zero-capacity overload, or one exact event--resource incidence with high deficiency
weight relative to capacity.  The exact event contains more structure than one selected
incidence: its uncovered demand was split equally over every shared eligible current
resource.

This note reassembles those equal pieces.  Either at least half of them normalize to
real payment, or more than half lie on high-ratio resources.  Occurrence-faithful
rectangle destruction then places a quarter of the event demand on current factors
through one exact deleted cell.  A rank split and the weighted anchor-link lemma turn
the rank-three branch into pair concentration or an endpoint-disjoint high-ratio star.

## One exact Hall-core event

Let `j` be an event in a canonical nonsingleton minimal Hall core.  Write

`u_j>0`

for its uncovered demand after removing capacity private to `j`.  Let `P_j` be its
nonempty set of shared eligible current resources and put

`d_j=|P_j|`,

`v_j=u_j/d_j`.

Thus every incidence `(j,p)`, `p in P_j`, carries equal uncovered-demand weight `v_j`.
Resource `p` has nonnegative capacity `c_p`, physical support `Q_p`, and rank between
one and `r`.  The event is one rectangle correction deleting exact current cells
`b_j,u_j^cell`.  Occurrence-faithful eligibility means

`Q_p intersect {b_j,u_j^cell} != empty`.

Fix `theta>=1`.

## GC2ba -- event-local payment or high-ratio majority -- PROVED

Define the moderate and high-ratio resource sets

`P_mod={p in P_j:c_p>=v_j/theta}`,

`P_hi=P_j\P_mod`.

Exactly one of the following holds:

1. `|P_mod|>=d_j/2`, and assigning `v_j/theta` to every moderate resource gives
   factor-conservative current payment at least

   `u_j/(2*theta)`;
2. `|P_hi|>d_j/2`, so the high-ratio incidences carry total weight greater than

   `u_j/2`,

   and every positive-capacity member satisfies `v_j/c_p>theta`; zero-capacity members
   are exact atomic capacity obstructions.

### Proof

The two sets partition `P_j`.  In the first case every assigned amount is at most the
corresponding capacity, and

`|P_mod|*v_j/theta >= d_j*v_j/(2*theta)=u_j/(2*theta)`.

If the first case fails, `|P_hi|>d_j/2`; multiplying by the common incidence weight
`v_j` gives the second weight bound.  The ratio statement is the definition of
`P_hi` when `c_p>0`. QED.

This is stronger than selecting one heavy incidence: the whole exact event is now paid
or more than half of its uncovered demand remains on high-ratio current resources.

## GC2bb -- one deleted cell carries a high-ratio factor family -- PROVED

Assume the high-ratio alternative of GC2ba and discard any zero-capacity resource as an
immediate atomic output.  Assign every remaining `p in P_hi` canonically to the first
cell, in the ordered pair `(b_j,u_j^cell)`, that lies in `Q_p`.

One exact deleted cell `q` receives a resource family `H_q` of total incidence weight
strictly greater than

`u_j/4`.

Every resource in `H_q` contains `q` and satisfies `v_j/c_p>theta`.

### Proof

The two deleted-cell classes partition `P_hi`.  Their weights sum to more than
`u_j/2`, so one has weight greater than `u_j/4`.  The support and ratio statements are
preserved by restriction. QED.

## GC2bc -- rank localization through the deleted cell -- PROVED

Partition `H_q` by exact support rank `s in {1,...,r}`.  One rank class `H_(q,s)` has
incidence weight

`W_(q,s)>u_j/(4*r)`.

Every member contains `q` and has capacity strictly less than `v_j/theta`.

### Proof

There are at most `r` nonempty rank classes and their weights sum to more than
`u_j/4`.  Weighted pigeonhole gives the bound.  The capacity inequality is the
high-ratio condition. QED.

Ranks one and two are lower-dimensional exact current-factor concentrations.  The
rank-three class has a graph link at `q`.

## GC2bd -- high-ratio rank-three anchor-link router -- PROVED

Assume the selected rank is three.  Regard each exact factor occurrence

`Q_p={q,x_p,y_p}`

as one edge `{x_p,y_p}` in the link multigraph at `q`, carrying weight `v_j` and
capacity `c_p`.  Parallel edges are retained as distinct factor occurrences.

For every integer `Delta>=1`, either:

1. one pair `{q,x}` belongs to more than `Delta` selected factor occurrences; or
2. there is a family `S_q` of factor occurrences pairwise disjoint outside `q` with
   incidence weight

   `W(S_q)>u_j/[4*r*(2*Delta-1)]`.

In the second case their total current capacity satisfies

`sum_(p in S_q)c_p < W(S_q)/theta`.

### Proof

If a link vertex has degree greater than `Delta`, use the first alternative.  Otherwise
the link multigraph has maximum degree at most `Delta`.  Greedily edge-colour its line
graph with at most `2*Delta-1` colours: each edge meets at most `2*Delta-2` other edge
occurrences, including parallel occurrences.  A heaviest colour class is a matching
and retains at least `W_(q,3)/(2*Delta-1)`, which is strictly larger than the displayed
bound by GC2bc.

Every selected occurrence has `c_p<v_j/theta`.  Summing over the matching gives the
capacity inequality because its incidence weight is `v_j` times its number of
occurrences. QED.

Thus the endpoint-disjoint star is not merely demand weighted: its total available
current capacity is less than a `1/theta` fraction of its retained demand incidence.

## GC2be -- lower-rank and rank-three high-ratio outputs -- PROVED

The high-ratio event branch has one exact structural continuation:

1. a zero-capacity current resource;
2. a rank-one or rank-two current-factor family through one deleted cell, carrying
   weight greater than `u_j/(4r)` and satisfying the same ratio threshold;
3. a rank-three pair-codegree greater than `Delta`;
4. or an endpoint-disjoint rank-three factor star of weight greater than
   `u_j/[4r(2Delta-1)]` and total capacity less than its weight divided by `theta`.

### Proof

Apply GC2bb and GC2bc.  Ranks one and two give the second outcome; rank three enters
GC2bd. QED.

## GC2bf -- unified event-local Hall continuation -- PROVED UNDER THE RECTANGLE-DESTRUCTION CONTRACT

For every exact nonsingleton Hall-core event and every `theta>=1`, `Delta>=1`, there is
one of:

1. factor-conservative current payment at least `u_j/(2theta)`;
2. a zero-capacity resource;
3. a lower-rank high-ratio factor concentration through one deleted cell;
4. a high pair-codegree through that deleted cell;
5. or an endpoint-disjoint rank-three high-ratio factor star with the quantitative
   demand/capacity gap from GC2bd.

Consequently the high-ratio Hall output is no longer one isolated scalar ratio.  It
enters the same lower-rank, pair-concentration and anchor-link geometry used elsewhere
in GC2.

## Corrected GC frontier

The live high-ratio branch is now a lower-rank current concentration, high pair
codegree, or endpoint-disjoint factor star with an explicit aggregate capacity deficit.
The remaining work is to use those structures in an executable correction, chargeback
or terminal overload theorem.  Other open interfaces remain isolated-cell prospective
stars, pool depletion, global context causes and local superregular resampling.

## Finite check

`scripts/verify_geometric_event_local_high_ratio.py` exhausts and randomly samples
finite event-resource systems.  It checks the moderate-payment/high-ratio split,
deleted-cell and rank localization, multigraph pair codegrees, weighted matching
extraction and the aggregate star capacity deficit.