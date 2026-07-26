# Raw one-event gain rows and exact provenance repair

**Branch:** `research/geometric-cleaning`

GC2bm--GC2bq compare external Hall capacity with the globally normalized GC2g charge row.
That row is divided by the global congestion factor `K`, even when only one rectangle event
is under consideration.  For one event there is a larger canonical row: distribute the
complete event gain proportionally over the exact current factors destroyed by that event.

This note proves that the raw one-event row is already factor-conservative coordinatewise.
It repairs every provenance deficit caused only by global normalization.  If its overlap is
still too small, the residual splits exactly into source-free capacity and a destroyed-factor
ratio overload.

## Exact destroyed-factor row

Fix one current hard-legal rectangle event `j` with positive gain `g_j`.  Let `D_j` be its
finite set of exact current factor occurrences.  Factor `p in D_j` has current weight
`w_p>0`, and put

`Dsum_j=sum_(p in D_j)w_p`.

Assume the exact destroyed-minus-created ledger gives

`0<g_j<=Dsum_j`.

For every external resource occurrence `p`, define the raw one-event row

`q_p = g_j*w_p/Dsum_j` if `p in D_j`,

`q_p = 0` otherwise.

Let `c_p>=0` be the declared external Hall-payment capacity, and put

`C_ext=sum_p c_p`,

`Z_raw=sum_p min(c_p,q_p)`.

The forced residual demand from GC2bg is denoted `R_star>0`.

## GC2br -- the raw one-event row is exact and factor-conservative -- PROVED

The raw row satisfies

`sum_p q_p=g_j`

and, for every destroyed occurrence,

`0<q_p<=w_p`.

It is therefore an exact factor-conservative gain row for the single event `j`.

### Proof

Summing the definition over `D_j` gives

`sum_p q_p=(g_j/Dsum_j)*sum_(p in D_j)w_p=g_j`.

Since `g_j<=Dsum_j`, the common multiplier is at most one, so `q_p<=w_p`. QED.

This row may not be usable simultaneously for many events because one factor can then be
charged several times.  For the single event under analysis, no cross-event normalization
is needed.

## GC2bs -- raw-row overlap gives direct executable descent -- PROVED

The maximum total external allocation satisfying

`0<=x_p<=c_p`

and

`0<=x_p<=q_p`

for every occurrence is exactly `Z_raw`.

If `Z_raw>=R_star`, the proportional allocation

`x_p=R_star*min(c_p,q_p)/Z_raw`

is factor-conservative and gain-certified.  Consequently

`g_j>=R_star>(1-1/theta)W`,

and executing event `j` gives the displayed descent.

### Proof

Coordinatewise overlap gives the maximum exactly as in GC2bm.  When `Z_raw>=R_star`, the
proportional factor is at most one, so `x_p<=c_p,q_p`.  The allocation sums to `R_star`, and

`R_star=sum_p x_p<=sum_p q_p=g_j`.

Apply GC2bg for the strict comparison with `W`. QED.

If the normalized GC2g row has `a_p=q_p/K`, then `q_p>=a_p` and hence `Z_raw>=Z_ext`.
Thus GC2bs repairs every provenance deficit caused solely by the global factor `K`.

## GC2bt -- exact split of the residual raw-row deficit -- PROVED

Assume

`C_ext>=R_star>Z_raw`

and put

`Delta_raw=R_star-Z_raw>0`.

Define

`U_free=sum_(p notin D_j)c_p`,

`U_ratio=sum_(p in D_j)(c_p-q_p)_+`.

Then

`U_free+U_ratio=C_ext-Z_raw>=Delta_raw`.

### Proof

For every coordinate,

`c_p-min(c_p,q_p)=(c_p-q_p)_+`.

When `p notin D_j`, `q_p=0`, so this term is `c_p`.  When `p in D_j`, it is the summand in
`U_ratio`.  Summing gives `C_ext-Z_raw`, which is at least `R_star-Z_raw`. QED.

The two terms have different meanings.  `U_free` is Hall capacity on resources not destroyed
by the event at all.  `U_ratio` is capacity on destroyed factors that exceeds the event's
raw proportional gain row.

## GC2bu -- one exact source-free or ratio-overload role -- PROVED

In the raw-row deficit case, at least one of

`U_free>=Delta_raw/2`,

`U_ratio>=Delta_raw/2`

holds.

Suppose each occurrence has one of at most `T_raw` exact physical roles and every selected
role fibre contains at most `B_raw` occurrences.

- In the source-free branch, one exact occurrence outside `D_j` has capacity at least

  `Delta_raw/(2*T_raw*B_raw)`.

- In the ratio branch, one exact destroyed occurrence satisfies

  `(c_p-q_p)_+ >= Delta_raw/(2*T_raw*B_raw)`

  and

  `c_p/w_p > lambda_j`,

  where

  `lambda_j=g_j/Dsum_j`.

### Proof

The half split follows from GC2bt.  Partition the selected half by physical role and then by
occurrence.  In the ratio branch, positive excess means `c_p>q_p=lambda_j*w_p`. QED.

Thus failure of the raw row is not a generic provenance problem.  It is either payment
capacity on a resource that the event does not destroy, or an exact destroyed factor whose
Hall capacity is too large relative to the event's gain density.

## GC2bv -- complete raw-event provenance router -- PROVED

For the forced external residual of a capacity-deficient event star, exactly one of the
following holds:

1. `C_ext<R_star`: an ordinary external Hall deficit;
2. `C_ext>=R_star` and `Z_raw>=R_star`: the raw one-event overlap gives executable descent
   greater than `(1-1/theta)W`;
3. `C_ext>=R_star>Z_raw`: one exact physical role carries either source-free capacity or a
   destroyed-factor ratio overload as in GC2bu.

### Proof

Compare `C_ext` and `Z_raw` with `R_star`, noting `Z_raw<=C_ext`.  The cases are mutually
exclusive and exhaustive.  Apply GC2bs, GC2bt and GC2bu. QED.

## Corrected GC frontier

Global-normalization loss is no longer a reason for missing gain provenance at one event.
The remaining external-star outputs are now:

- a genuine Hall deficit;
- immediate descent from the raw event row;
- one physical source-free resource role;
- or one destroyed factor with capacity/gain-density ratio above `lambda_j`.

The next geometric obligation is to classify or repair those last two exact roles.  Other
open interfaces remain lower-rank and high-pair execution, isolated-cell prospective stars,
pool depletion, global context causes and local superregular resampling.

## Finite check

`scripts/verify_geometric_raw_event_gain_row.py` exhausts small destroyed-factor systems and
samples larger rational systems.  It checks the raw-row sum and factor conservativity,
coordinatewise overlap, proportional descent, the source-free/ratio split and exact role
localization.