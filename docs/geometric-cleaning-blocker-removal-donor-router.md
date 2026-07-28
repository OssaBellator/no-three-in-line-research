# One-removal many-donor neutralization for concentrated blockers

**Branch:** `research/geometric-cleaning`

GC2fu--GC2fy turn an empty or capacity-deficient donor reservoir into one exact blocker atom carrying
large donor-incidence demand.  This note handles the physical-blocker branch when that atom has one
legal removal or neutralization operation.  The blocker is paid once, after which the complete donor
fan is averaged without a loss in its size.

## Removable blocker fan model

Fix one heavy current lineage `Q` of weight `h>0` and one exact physical blocker atom `p`.  Let `S` be
a nonempty set of `n` donor rows whose least blocker address is `p`.

Assume the **one-removal donor-fan contract**:

1. one legal operation `eta` removes or neutralizes `p` while preserving the exact lineage `Q`;
2. after `eta`, every donor swap `tau_s`, `s in S`, is legal and destroys `Q`;
3. the complete two-stage ledger contains all new and additionally destroyed certificates;
4. exact aliases are aggregated inside every operation address;
5. removal-only new collateral has total weight `F_p`, counted once for the entire donor menu;
6. donor-dependent new collateral after `eta tau_s` has total weight `E_s`, excluding the already
   counted removal-only bank;
7. the removal-only exact output stock is at most `K_rem`, and each donor-dependent operation has at
   most `K_swap` exact output slots;
8. extra lineage, label or context multiplicities are returned as named fields rather than hidden in
   either stock;
9. failure returns the least removal, donor, legality, persistence, ledger, alias, completion, context
   or boundary field.

Any current factors additionally destroyed by `eta` or `tau_s` only improve the potential estimate.

## GC2fz -- exact two-stage potential bound -- PROVED

For every donor `s in S`,

`Delta_(eta,s)<=F_p+E_s-h`.

### Proof

The donor stage destroys the full current lineage weight `h`.  The complete created collateral is the
disjoint union of the removal-only bank of weight `F_p` and the donor-dependent bank of weight `E_s`.
Any other destroyed current factor lowers the true potential change. QED.

## GC2ga -- common-removal donor average -- PROVED

Put

`E_bar=(1/n)sum_(s in S)E_s`.

For every `epsilon in (0,1)`, if

`F_p+E_bar<=(1-epsilon)h`,

one legal two-stage operation `eta tau_s` decreases the potential by at least `epsilon h`.

### Proof

Average GC2fz over the complete donor fan.  One donor has potential change no larger than the average,
which is at most `-epsilon h`. QED.

The common removal cost is counted once, not once for every donor.

## GC2gb -- failed margin gives one exact output -- PROVED

If the hypothesis of GC2ga fails, at least one of the following holds:

1. one exact removal-only certificate has weight greater than
   `(1-epsilon)h/(2K_rem)`;
2. one exact donor-dependent certificate has weight greater than
   `(1-epsilon)h/(2K_swap)`.

### Proof

Failure gives `F_p+E_bar>(1-epsilon)h`.  Hence either
`F_p>(1-epsilon)h/2` or `E_bar>(1-epsilon)h/2`.

In the first branch, weighted pigeonhole over at most `K_rem` exact removal-only outputs gives
alternative 1.  In the second,

`sum_s E_s>n(1-epsilon)h/2`.

The complete operation-addressed donor ledger has at most `nK_swap` slots, so one slot has weight
greater than `(1-epsilon)h/(2K_swap)`. QED.

The donor count cancels exactly.

## GC2gc -- installed-bank quantitative continuation -- PROVED

Suppose

`h>W_B/[8q_ch N^2(2Delta_cap-1)]`.

Then the removable-blocker fan gives one of:

1. two-stage descent greater than
   `epsilon W_B/[8q_ch N^2(2Delta_cap-1)]`;
2. one exact removal-only certificate heavier than
   `(1-epsilon)W_B/[16K_rem q_ch N^2(2Delta_cap-1)]`;
3. one exact donor-dependent certificate heavier than
   `(1-epsilon)W_B/[16K_swap q_ch N^2(2Delta_cap-1)]`;
4. or a named contract failure.

### Proof

Apply GC2ga--GC2gb and substitute the strict heavy-lineage lower bound. QED.

## GC2gd -- concentrated physical-blocker router -- PROVED UNDER THE DECLARED CONTRACTS

A capacity-overloaded exact blocker atom from GC2fw--GC2fy now has one continuation:

1. one legal blocker removal unlocks its donor fan and yields quantified descent;
2. the failed margin produces one heavy exact removal-only certificate;
3. the failed margin produces one heavy exact donor-dependent feedback certificate;
4. no occurrence-faithful removal exists, returning the exact blocker atom to GC3/GC4, pool or global
   context routing;
5. or one removal, persistence, donor, output-stock, lineage, context or boundary field fails.

Every exact output enters the existing lineage installation and finite-signature feedback routers.

### Proof

If the one-removal contract holds, use GC2gc.  Otherwise retain the exact concentrated blocker address
and its declared type.  Existing current-incidence, Hall, GC4, pool and context routers handle those
explicit branches. QED.

## Corrected GC frontier

A concentrated physical donor blocker no longer needs to be charged separately to every blocked
alternative.  One removal is shared across the entire donor fan, and failed average descent returns a
heavy exact output with no donor-count loss.

The remaining geometry is construction or payment of blocker-removal operations for every physical
role, capacity-overloaded target-common/global atoms with no removal, repeated non-tagged feedback
cycles, bounded-budget-dominated small reservoirs, roles outside the singleton-rectangle host,
block-tuple recursion, genuine pool depletion and local superregular resampling.

## Finite check

`scripts/verify_geometric_blocker_removal_donor_router.py` samples shared-removal donor fans and exact
collateral ledgers.  It checks the two-stage potential inequality, common-cost averaging, the two
pigeonhole branches, donor-count cancellation and the installed-bank constants.
