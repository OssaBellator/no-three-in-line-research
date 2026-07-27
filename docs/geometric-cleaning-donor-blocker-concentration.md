# Exact blocker concentration for balanced-donor reservoirs

**Branch:** `research/geometric-cleaning`

GC2fp--GC2ft already split donor scarcity into explicit collision, line, target-disjoint support,
target-common and global cause classes.  This note adds a capacity-and-weight refinement to that physical
partition: every unavailable donor row still has one least exact blocker address, but each address now
comes with an optional certified blocking capacity and carries the full heavy-lineage donor demand.  A
small or empty legal menu therefore exposes one blocker atom with large donor-incidence demand, or
violates its declared capacity.

## Candidate donor reservoir

Fix one heavy current lineage `Q={z,x,y}` of weight `h>0`.  Let `U` be a complete finite candidate donor
reservoir with

`d_0=|U|>=1`.

For every candidate row `s in U`, either the balanced donor transposition `tau_s` is legal, or the
complete legality audit returns one least exact blocker address `p(s)` from a finite dictionary `P`.
Write

`K_blk=|P|>=1`,

`D={s in U:tau_s is legal}`,

`d=|D|`,

and

`n_p=|{s in U\D:p(s)=p}|`.

A blocker address includes its field type and every physical row, column, layer, occupied cell, hard
literal, context atom, pool token or boundary label needed to make the cause exact.  Aliases are
aggregated before counting.  If a further field is needed, that least field is returned rather than
hidden in `K_blk`.

Optionally give each address a declared integer blocking capacity `b_p>=0` inside one fixed context and
put

`B_blk=sum_(p in P)b_p`.

A capacity change, new blocker address, pool replenishment or context change is an outer reset.

## GC2fu -- exact legal/blocker partition -- PROVED

The candidate reservoir satisfies

`d_0=d+sum_(p in P)n_p`.

For every threshold `Gamma>=0`, either

`d>=d_0-K_blk*Gamma`

or one exact blocker address satisfies

`n_p>Gamma`.

### Proof

Every candidate is legal or has one least blocker address, and these classes are disjoint.  This gives
the identity.  If every `n_p<=Gamma`, the illegal stock is at most `K_blk Gamma`, proving the legal-menu
bound. QED.

## GC2fv -- empty-menu blocker concentration -- PROVED

If `d=0`, one exact blocker address has

`n_p>=ceil(d_0/K_blk)`

and donor-incidence demand

`L_p=n_p h>=d_0 h/K_blk`.

This is operation-incidence demand through one physical blocker, not `n_p` distinct copies of the
lineage `Q`.

### Proof

With no legal donors, the counts `n_p` sum to `d_0`.  Pigeonhole gives the count bound; multiply by the
common lineage demand `h`. QED.

## GC2fw -- capacity-certified donor existence or overload -- PROVED

At least one of the following occurs:

1. some blocker address exceeds capacity, `n_p>b_p`;
2. the legal donor stock satisfies

   `d>=d_0-B_blk`.

In particular, if `d_0>B_blk` and no capacity overload occurs, the legal donor menu is nonempty.

### Proof

If no address exceeds capacity, then

`sum_p n_p<=sum_p b_p=B_blk`.

Use GC2fu's partition identity.  The final statement is integrality. QED.

A capacity overload retains the exact blocker address, excess `n_p-b_p`, field type and complete physical
cause.  It enters the existing cause-load, raw-gain, Hall-deficiency, GC4 or pool-depletion routers
according to that field type.

## GC2fx -- heavy-lineage donor/blocker router -- PROVED UNDER THE DECLARED CONTRACTS

Fix `epsilon in (0,1)`.  One heavy exact current lineage of weight `h` has one continuation:

1. one legal donor swap decreases the potential by at least `epsilon h`;
2. one exact rank-one/rank-two feedback certificate has weight greater than

   `(1-epsilon)h/K_swap`;

3. one exact blocker address has incidence demand at least `d_0 h/K_blk` when the legal menu is empty;
4. one blocker address exceeds its declared capacity, while otherwise

   `d>=d_0-B_blk`;

5. or one candidate-completeness, least-blocker, donor-swap, capacity, alias, context or boundary field
   fails.

### Proof

If `d>0`, apply GC2fl--GC2fm to the complete legal donor menu.  If `d=0`, apply GC2fv.  Independently,
GC2fw gives the capacity-certified lower bound or overload.  Failed hypotheses are retained explicitly.
QED.

## GC2fy -- installed-bank blocker-localized continuation -- PROVED

Suppose the heavy lineage comes from an installed bank of birth weight `W_B`, so

`h>W_B/[8q_ch N^2(2Delta_cap-1)]`.

Then the empty-menu blocker branch of GC2fx gives one exact blocker address with incidence demand greater
than

`d_0 W_B/[8K_blk q_ch N^2(2Delta_cap-1)]`.

The descent and exact-feedback alternatives retain the bounds of GC2fn.  Thus donor-reservoir failure is
no longer an unstructured endpoint: it is one quantitative exact physical blocker overload.

### Proof

Substitute the strict heavy-lineage bound into GC2fv.  The other alternatives are GC2fn and GC2fx. QED.

## Corrected GC frontier

Beyond the physical cause budgets of GC2fp--GC2ft, a missing balanced-donor menu now localizes to one
least blocker atom or a declared capacity overload.  For direct two-layer hosts, any candidate reservoir
larger than the total blocker capacity automatically contains a legal donor.

The remaining geometry is payment or removal of the concentrated blocker atom, construction of complete
candidate reservoirs outside direct two-layer hosts, repeated non-tagged feedback lineage growth,
block-tuple overload recursion, pool depletion, global contexts and local superregular resampling.

## Finite check

`scripts/verify_geometric_donor_blocker_concentration.py` samples complete candidate reservoirs, least
blocker partitions and declared capacities.  It checks the exact legal/blocker identity, threshold and
empty-menu concentration, capacity-certified donor existence, blocker-incidence constants and the
integrated installed-bank scale.
