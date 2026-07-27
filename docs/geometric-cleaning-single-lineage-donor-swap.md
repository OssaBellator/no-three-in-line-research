# Single-lineage balanced-donor feedback router

**Branch:** `research/geometric-cleaning`

GC2ff--GC2fj route a paid already-current star either to a direct AN descent, a new exact
matching-dependent certificate, or one quantitatively heavy exact current lineage. The last output
may contain fewer than seven lineages, so the AN block theorem cannot be reapplied directly.

This note neutralizes one heavy current lineage by averaging over a complete menu of legal balanced
donor swaps in its permutation layer. Every donor swap destroys the named lineage, fixed-only
collateral is impossible, and all new exact collateral has matching rank one or two. A failed average
therefore collapses to one exact operation-addressed certificate with no loss depending on the number
of legal donors.

## Heavy-current-lineage donor menu

Fix one current exact certificate lineage

`Q={z,x,y}`

of weight `h>0` in a two-permutation-layer current host. Choose `x` as the movable endpoint in one
permutation layer. Let `D` be a nonempty finite set of donor rows. For each `s in D`, let `tau_s` be
the balanced transposition which swaps the two layer assignments in the row of `x` and donor row `s`.

Assume the **single-lineage donor-swap contract**:

1. every `tau_s` is legal from the current state and preserves the two-layer permutation, hard-context,
   row and column constraints;
2. `tau_s` removes the physical cell `x`, and therefore destroys the exact lineage `Q`;
3. the complete exact post-swap ledger contains every newly present certificate and every additionally
   destroyed current certificate;
4. exact aliases are aggregated inside each operation address;
5. every new certificate receives its donor-swap address, moved-cell rank and exact physical
   completion;
6. if additional lineage, label or context data multiply one physical completion, the least such field
   is returned rather than hidden inside the completion stocks;
7. failure returns the least donor, legality, row, column, layer, occurrence, alias, inventory or
   context field.

Let `d=|D|`. For `s in D`, write `E_s` for the total weight of exact certificates absent before
`tau_s` and present afterwards. Additional destroyed current certificates are allowed and only
improve the potential estimate.

Define the safe one-operation completion stocks

`K_1=2*binom(N^2,2)`,

`K_2=N^2`,

`K_swap=K_1+K_2`.

## GC2fk -- exact destruction and zero rank-zero collateral -- PROVED

Every donor swap `tau_s` destroys the full weight `h` of `Q`. Every genuinely new exact certificate
uses at least one of the two moved post-swap cells. Hence its matching rank is one or two, and the
fixed-only collateral is exactly zero.

### Proof

The transposition removes `x` from the current layer, so the named physical triple `Q` is absent after
the swap. All cells outside the two exchanged layer positions are unchanged. A certificate using no
moved post-swap cell would therefore have exactly the same physical cells and labels before and after
the operation, contradicting that it is newly present. There are only two moved post-swap cells, so
the matching rank is one or two. QED.

## GC2fl -- donor-average descent -- PROVED UNDER THE DONOR-SWAP CONTRACT

For every donor `s`, the potential change satisfies

`Delta_s<=E_s-h`.

Put

`E_bar=(1/d)sum_(s in D)E_s`.

For every `epsilon in (0,1)`, if

`E_bar<=(1-epsilon)h`,

then one legal donor swap decreases the potential by at least

`epsilon*h`.

### Proof

The named current lineage contributes destruction weight `h`. Every newly present exact certificate
is counted in `E_s`; any other destroyed current certificate only lowers the actual change. Thus
`Delta_s<=E_s-h`. Averaging over the complete donor menu gives

`(1/d)sum_s Delta_s<=E_bar-h<=-epsilon*h`.

One donor is no larger than the average. QED.

## GC2fm -- failed donor average gives one exact certificate -- PROVED

If the hypothesis of GC2fl fails, then one donor operation creates one exact prospective certificate
`P` of rank one or two and weight

`h_P>(1-epsilon)h/K_swap`.

The output retains its exact donor-swap address, moved-cell rank and physical completion.

### Proof

Failure gives

`sum_s E_s>d(1-epsilon)h`.

For one donor operation, a rank-one new certificate chooses one of the two moved post-swap cells and
at most two fixed cells, so the safe stock is `K_1`. A rank-two certificate uses both moved cells and
at most one fixed cell, so the safe stock is `K_2`. Thus the complete operation-addressed ledger over
all `d` donors contains at most `d K_swap` exact slots. Weighted pigeonhole gives one slot heavier
than

`d(1-epsilon)h/(dK_swap)=(1-epsilon)h/K_swap`.

GC2fk excludes rank zero. QED.

The cancellation of `d` is the point of using the complete operation-addressed ledger: a large donor
menu improves averaging without weakening the exact feedback certificate.

## GC2fn -- installed-bank heavy-lineage continuation -- PROVED

Use

`Delta_cap=L_cert*(N^2-2)`.

Suppose GC2fi returns a heavy current lineage from an installed birth-weight bank `W_B`, so

`h>W_B/[8q_ch N^2(2Delta_cap-1)]`.

For every `epsilon in (0,1)`, this lineage has one continuation:

1. one donor swap decreases `Phi` by more than

   `epsilon*W_B/[8q_ch N^2(2Delta_cap-1)]`;

2. one exact rank-one or rank-two prospective certificate has weight greater than

   `(1-epsilon)W_B/[8q_ch N^2(2Delta_cap-1)K_swap]`;

3. the legal donor menu is empty;

4. or one donor-swap, complete-ledger, occurrence, alias, matching, context or outer-reset field fails.

### Proof

If the donor menu is empty, use alternative 3. Otherwise apply GC2fl--GC2fm and substitute the strict
heavy-lineage lower bound. All excluded hypotheses are the named failures. QED.

## GC2fo -- single-lineage feedback router -- PROVED UNDER THE DECLARED CONTRACTS

Every heavy exact current lineage produced by the direct current-anchor router now gives direct
balanced-swap descent, one quantitatively heavy exact rank-one/rank-two feedback certificate, an empty
donor reservoir, or a named physical failure. Once a matching-dependent feedback certificate is
installed as a current lineage, the same router applies again with its new occurrence identity.

Tagged-only repetitions still use the finite signature quotient. A non-tagged recurrence must
therefore spend descent, create a new exact lineage, exhaust a donor reservoir, enter a finite ticket,
or leave the fixed context.

### Proof

Use GC2fn for a heavy current lineage and GC2eg--GC2ek for installation of the exact feedback output.
GC2cs--GC2cw handle tagged-only signature recurrence. QED.

## Corrected GC frontier

A heavy current certificate no longer remains a terminal atom merely because fewer than seven
lineages share its endpoint type. A complete balanced-donor menu either destroys it with quantified
descent or returns one exact rank-one/rank-two feedback certificate at a donor-count-free scale.

The remaining geometry is payment or neutralization of repeated non-tagged feedback certificates,
proof of a sufficiently large legal donor reservoir in roles outside the direct two-layer host,
block-tuple overload recursion, unbounded contexts, pool depletion, global-context causes and local
superregular resampling.

## Finite check

`scripts/verify_geometric_single_lineage_donor_swap.py` samples two-layer permutation hosts, legal
balanced donor swaps and exact rank-one/rank-two collateral ledgers. It checks destruction of the
named current lineage, absence of fixed-only new certificates, the donor-average descent inequality,
the donor-count cancellation in the exact feedback bound and the integrated installed-bank constants.
