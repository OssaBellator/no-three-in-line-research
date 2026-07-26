# Gain-row overlap and exact provenance deficits for external star payment

**Branch:** `research/geometric-cleaning`

GC2bg--GC2bl show that a capacity-deficient event star needs external payment

`R_star=W-C>(1-1/theta)W`

and that Hall capacity alone is not correction gain.  This note compares the declared
external payment capacities directly with the exact GC2g charge row of the same rectangle
event.  Their coordinatewise overlap is the complete gain-certified capacity.  If it is
large enough, a canonical proportional allocation gives executable descent.  If it is too
small, the shortfall localizes to one physical source role as missing provenance.

## External capacity and exact gain row

Fix the rectangle event `j` and its forced external residual `R_star>0`.  Let `P_ext` be a
finite set of exact external current-resource occurrences.  Resource `p` has declared
factor-conservative payment capacity

`c_p>=0`.

Assume the current correction--factor ledger supplies an exact nonnegative GC2g charge-row
capacity

`a_p>=0`

for the same event and occurrence, with

`sum_(p in P_ext)a_p<=g_j`.

An amount paid by `p` is gain-certified only when it is bounded by both `c_p` and `a_p`.
Put

`z_p=min(c_p,a_p)`,

`Z_ext=sum_p z_p`,

`C_ext=sum_p c_p`.

## GC2bm -- exact gain-certified external capacity -- PROVED

The maximum total external allocation satisfying

`0<=x_p<=c_p`

and

`0<=x_p<=a_p`

for every occurrence is exactly

`Z_ext=sum_p min(c_p,a_p)`.

### Proof

Every feasible coordinate is at most `min(c_p,a_p)`, so the total is at most `Z_ext`.
Taking `x_p=min(c_p,a_p)` attains that total. QED.

Thus gain provenance is an intersection of two occurrence-level capacities, not a role- or
line-level identification.

## GC2bn -- canonical overlap allocation gives executable descent -- PROVED

If `Z_ext>=R_star`, define

`x_p=R_star*z_p/Z_ext`.

Then the allocation is factor-conservative and gain-certified, has total exactly
`R_star`, and satisfies

`g_j>=R_star>(1-1/theta)W`.

Executing the exact rectangle event therefore decreases the current potential by more
than `(1-1/theta)W`.

### Proof

The scalar `R_star/Z_ext` lies in `(0,1]`, so `x_p<=z_p<=c_p,a_p`.  Summing gives
`sum_p x_p=R_star`.  Since the complete row is dominated coordinatewise by the exact GC2g
charge row,

`R_star=sum_p x_p<=sum_p a_p<=g_j`.

Apply GC2bg for the strict comparison with `W`. QED.

This constructs the missing provenance rather than assuming that an arbitrary Hall
allocation already has it.

## GC2bo -- ordinary Hall deficit or pure provenance deficit -- PROVED

Assume `Z_ext<R_star` and put

`Delta_prov=R_star-Z_ext>0`.

Exactly one of the following top-level cases holds:

1. `C_ext<R_star`, giving an ordinary event-local Hall deficit of size at least
   `R_star-C_ext`;
2. `C_ext>=R_star`, so declared external capacity is sufficient but gain-certified
   capacity is not.  In this case

   `sum_p(c_p-a_p)_+ = C_ext-Z_ext >= Delta_prov`.

### Proof

The first alternative is the one-event Hall inequality.  In the second,

`c_p-min(c_p,a_p)=(c_p-a_p)_+`.

Summing gives `C_ext-Z_ext`, which is at least `R_star-Z_ext=Delta_prov`. QED.

The second outcome is a provenance deficit: enough payment capacity exists, but at least
`Delta_prov` of the required mass lies outside the event's exact gain row.

## GC2bp -- physical role localization of missing provenance -- PROVED

In the provenance-deficit case, suppose every external occurrence has one of at most
`T_prov` exact physical source roles.  One role class carries uncertified-capacity mass at
least

`Delta_prov/T_prov`.

If every role fibre contains at most `B_prov` resource occurrences, one exact occurrence
has

`(c_p-a_p)_+ >= Delta_prov/(T_prov*B_prov)`.

### Proof

Partition the nonnegative masses `(c_p-a_p)_+` by role and use GC2bo, then partition the
selected role by its at most `B_prov` occurrences. QED.

The selected occurrence is an exact place where Hall capacity exceeds installed gain
provenance.  It is not paid mass until an additional correction--factor incidence is
proved.

## GC2bq -- complete external gain-provenance router -- PROVED

For the forced external residual of every capacity-deficient star, exactly one of the
following holds:

1. `C_ext<R_star`: an ordinary external Hall deficit;
2. `C_ext>=R_star` and `Z_ext>=R_star`: the canonical overlap allocation GC2bn gives
   executable descent greater than `(1-1/theta)W`;
3. `C_ext>=R_star>Z_ext`: a pure provenance deficit `Delta_prov`, localized by GC2bp to
   one exact physical source role and, under a fibre cap, one exact resource occurrence.

### Proof

Compare `C_ext` and `Z_ext` with `R_star`, noting `Z_ext<=C_ext`.  The three cases are
mutually exclusive and exhaustive.  Apply GC2bn, GC2bo and GC2bp. QED.

## Corrected GC frontier

The endpoint-disjoint high-ratio star now has a complete one-event source router.  Its
external branch is either:

- a genuine Hall-capacity deficit;
- immediate gain-certified descent from the exact GC2g row overlap;
- or one physical source role where declared capacity exceeds installed gain provenance.

The next live obligation is to enlarge that exact gain row or classify the selected
provenance-deficit occurrence.  Other open interfaces remain lower-rank and high-pair
execution, isolated-cell prospective stars, pool depletion, global context causes and
local superregular resampling.

## Finite check

`scripts/verify_geometric_gain_row_overlap.py` exhausts small declared-capacity and
charge-row vectors and samples larger rational systems.  It checks the exact overlap
capacity, proportional certified allocation, Hall/provenance split and role/occurrence
localization.