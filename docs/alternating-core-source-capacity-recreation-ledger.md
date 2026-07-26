# Source-paid activation and recreation of physical source capacity

**Branch:** `research/alternating-core-chain`

AC3qf--AC3qj derive a finite stock ceiling from a fixed physical source-atom universe
with fixed additive capacities.  The remaining growth mechanism is capacity creation:
an atom may be activated from zero capacity or an old capacity coordinate may be raised
again after destruction.  This note gives the exact ledger for those changes.

Capacity creation is harmless when every positive capacity increment is occurrence-
faithfully charged to a finite nonreplenishing source stock.  The theorem permits mixed
transitions which simultaneously create and destroy capacity coordinates.  Fresh atoms
outside the fixed candidate universe, free capacity creation and replenishing capacity
sources remain outer or higher-rank events.

## Variable physical capacity and capacity sources

Fix a finite totally ordered candidate atom universe `P`.  At time `t`, atom `p` has
integer capacity

`b_p(t)>=0`

and live occupancy `n_p(t)>=0`.  Put

`B(t)=sum_(p in P)b_p(t)`,

`S(t)=sum_(p in P)n_p(t)`.

A state is physically feasible when `n_p(t)<=b_p(t)` for every atom.  An atom with
`b_p(t)=0` is inactive; changing it to positive capacity is an activation and is counted
as capacity creation.

Let `A_cap` be a finite set of exact capacity-source addresses.  Source `a` has residual
counter `s_a(t)>=0` and integer conversion rate `rho_a>=1`.  For one transition define

`G_t=sum_p (b_p(t+1)-b_p(t))_+`,

`D_t=sum_p (b_p(t)-b_p(t+1))_+`,

`d_(t,a)=s_a(t)-s_a(t+1)`.

The transition is **source-faithful for capacity creation** when every `d_(t,a)>=0`,
every created capacity unit has an exact source assignment, and

`G_t <= sum_a rho_a*d_(t,a)`.

If `G_t>0`, at least one source debit is positive.  A new atom address outside `P`, a
rate change or an uncharged positive capacity increment leaves this ledger epoch.

## AC3qk -- exact total-capacity balance -- PROVED

For every finite capacity history,

`B(T)=B(0)+G-D`,

where

`G=sum_t G_t`,

`D=sum_t D_t`.

### Proof

For each coordinate,

`b_p(t+1)-b_p(t)
 =(b_p(t+1)-b_p(t))_+-(b_p(t)-b_p(t+1))_+`.

Sum first over atoms and then telescope over transitions. QED.

The identity records gross recreation, not merely the final net capacity change.
Destroying and later recreating one unit contributes once to both `D` and `G`.

## AC3ql -- finite source stock bounds all capacity creation -- PROVED

Along every source-faithful capacity history,

`G <= sum_(a in A_cap) rho_a*s_a(0)`.

Moreover the number of transitions with `G_t>0` is at most

`sum_a s_a(0)`.

### Proof

Sum the source-faithful creation inequality over transitions.  The debit of source `a`
telescopes and is at most its initial counter.  Every positive-capacity transition has
at least one positive integer debit. QED.

Thus repeated activation and recreation cannot manufacture new headroom without spending
one of the declared capacity sources.

## AC3qm -- combined realized-stock and capacity-recreation identity -- PROVED

Consider an alpha-pure source-unit history as in AC3qa.  Put

`A_amp=sum_t(h_t-1)_+`,

`L_amp=sum_t(1-h_t)_+`.

If the final state is physically feasible, then

`A_amp + D <= L_amp + (B(0)-S(0)) + G`.

Under the source-faithful capacity contract,

`A_amp + D
 <= L_amp + (B(0)-S(0)) + sum_a rho_a*s_a(0)`.

### Proof

AC3qb gives

`A_amp-L_amp=S(T)-S(0)`.

Final feasibility gives `S(T)<=B(T)`.  Substitute AC3qk:

`A_amp-L_amp <= B(0)+G-D-S(0)`.

Rearrange, then apply AC3ql. QED.

The gross destruction term is useful: capacity cannot be destroyed and recreated
cyclically for free.  Every such cycle either consumes capacity-source stock or appears
on the left side as unrecreated destruction.

## AC3qn -- exact creation-address localization -- PROVED

Assume every created capacity unit is assigned to one of at most `K_cap` exact decorated
creation addresses.  A decoration includes the target atom, source address, conversion
slot and every datum affecting payment or rate.

For a weighted family of created capacity units of total weight `W_cap`, one exact
creation address carries weight at least

`W_cap/K_cap`.

In particular, activation of an inactive atom is not a new address type merely because
its symbolic name is fresh: it must project to its fixed physical atom and decorated
creation address.  Failure to do so is a new-atom outer reset.

### Proof

The decorated address classes partition the created units.  Weighted pigeonhole gives
the bound.  The final statement is the physical occurrence contract. QED.

## AC3qo -- source-capacity recreation router -- PROVED UNDER THE CAPACITY-SOURCE CONTRACT

Inside one reconstructed source epoch assume:

1. all live units and all capacity coordinates use a fixed finite physical atom universe
   `P`;
2. every positive capacity increment satisfies the source-faithful contract for the
   fixed finite source set `A_cap`;
3. every state is physically feasible, or its least newly overloaded atom is impossible,
   terminal, descending or finitely ticketed as in AC3qh;
4. source-unit losses are impossible, terminal, descending or finitely ticketed;
5. conservative source transitions are quotient-stuttering, descending or finitely
   ticketed;
6. changes of `P`, source rates, source addresses, additive semantics or payment-relevant
   decorations are outer resets.

Then activation or recreation of physical source capacity cannot sustain an infinite
nonterminal internal history.

### Proof

AC3ql gives a finite gross capacity-creation budget.  AC3qm bounds realized amplification
and gross capacity destruction by initial headroom, the finite capacity-source budget and
the finite paid loss stock.  A feasibility crossing routes through AC3qh and assumption 3.
Conservative transitions close by assumption 5, and forbidden changes leave the epoch.
QED.

## Corrected AC4 source frontier

Fixed physical source capacities and one-level source-paid activation/recreation now close.
The remaining source-growth cases are:

- fresh physical atoms outside every fixed candidate universe;
- capacity sources which themselves replenish without a ranked-source theorem;
- cyclic capacity-source dependencies not covered by the existing cyclic SCC router;
- shared or nonadditive capacity which does not factor into atom coordinates;
- output units without occurrence-faithful atom addresses;
- unpaid source loss or payment-relevant unticketed conservative circulation.

The other AC4 interfaces remain genuinely unbounded structural semantics, nonfactoring
continuations, recreatable non-source tickets, unresolved availability/conflict/reverse
gates, nonadditive owners and scalar/arithmetic macro cycles.

## Finite check

`scripts/verify_ac_source_capacity_recreation.py` exhausts small capacity/source histories
and samples longer mixed histories.  It checks gross capacity balance, the source-paid
creation bound, the combined amplification/destruction inequality, activation accounting
and exact creation-address localization.