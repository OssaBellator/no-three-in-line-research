# Realized amplification, stock loss and joint-ticket accounting

**Branch:** `research/alternating-core-chain`

AC3pu--AC3pz isolate a canonical multi-output address inside every nonconservative
cyclic source component.  Declared output slots are not created supply until a certified
transition realizes them.  This note adds the exact realized-stock ledger.  Repeated
binary realization either raises total source stock, is balanced by genuine stock loss
in the same epoch, or consumes a finite joint ticket.  It therefore cannot be hidden
inside the symbolic source graph.

## Address-pure realized transitions

Fix one cyclic source component `S` and its canonical multi-output address

`alpha=(a_*,o_1,o_2)`

from AC3py.  Inside one reconstructed epoch, call a transition **alpha-pure** when:

- it debits exactly one unit of source `a_*` inside `S`;
- it debits no other source in `S`;
- every source unit created inside `S` is a distinct certified realization of a declared
  output slot of `a_*`;
- all other resource changes are recorded outside this component ledger.

Let `h_t` be the number of realized component-output units in transition `t`.  Put

`S_tot(t)=sum_(a in S)s_a(t)`.

The transition may be lossy (`h_t=0`), conservative (`h_t=1`) or amplifying
(`h_t>=2`).

## AC3qa -- exact realized-stock increment -- PROVED

Every alpha-pure transition satisfies

`S_tot(t+1)-S_tot(t)=h_t-1`.

In particular, a certified realization of both canonical slots has `h_t>=2` and raises
component stock by at least one.  Declared but unrealized slots contribute zero.

### Proof

The transition removes one component source unit and creates exactly `h_t` component
source units.  No other component debit or creation is present by alpha-purity.  Hence
the total changes by `-1+h_t`. QED.

This is an execution statement, unlike AC3py's declared-capacity statement.

## AC3qb -- gain/loss stock identity -- PROVED

For a finite alpha-pure history define

`A=sum_t (h_t-1)_+`

and

`L=sum_t (1-h_t)_+`.

Then

`S_tot(T)=S_tot(0)+A-L`,

or equivalently

`A=L+S_tot(T)-S_tot(0)`.

Consequently, if `S_tot(t)<=H` throughout the history, then

`A<=L+H-S_tot(0)`.

For binary realizations `h_t in {0,1,2}`, `A` is exactly the number of fully realized
binary amplifications and `L` is exactly the number of zero-output losses.

### Proof

For every integer `h>=0`,

`h-1=(h-1)_+-(1-h)_+`.

Sum AC3qa over the history and telescope.  The cap gives
`S_tot(T)-S_tot(0)<=H-S_tot(0)`. QED.

Thus bounded stock forces every long amplification history to expose comparable genuine
stock loss somewhere in the same epoch.

## AC3qc -- canonical surplus-to-loss matching -- PROVED

Assume `S_tot(t)<=H`.  Expand every amplifying transition into `(h_t-1)` ordered surplus
units and every lossy transition into `(1-h_t)` ordered loss units.  Order both lists by
transition time and internal unit index.  Match the first surplus units to the ordered
loss units, and then match any remaining surplus units to the `H-S_tot(0)` ordered cap
slots.

This gives a canonical injection of all surplus units into

`{loss units} union {cap slots}`.

Hence at least

`(A-(H-S_tot(0)))_+`

surplus units are matched to genuine loss units.

If every loss unit has one of `K_loss` exact finite loss-address types, one exact loss
address receives at least

`(A-(H-S_tot(0)))_+/K_loss`

matched surplus units.

### Proof

AC3qb gives `A<=L+H-S_tot(0)`, so the ordered target list has enough slots.  Matching by
list order is deterministic and injective.  Weighted pigeonhole over the `K_loss` loss
types gives the final bound. QED.

The matching is a whole-history accounting device; a matched loss may occur before or
after its surplus.  The theorem does not identify loss with progress automatically.  It
localizes the exact consumption gate that must pay for bounded amplification.

## AC3qd -- finite joint tickets bound full realization -- PROVED

Suppose every transition realizing both canonical slots consumes one unit from a
persistent nonreplenishing joint-ticket counter `J_alpha>=0`.  Then the number of such
full realizations is at most `J_alpha(0)`.

More generally, if slot `o_i` has a persistent ticket stock `J_i` and every full
realization consumes one ticket from both stocks, then the number of full realizations is
at most

`min(J_1(0),J_2(0))`.

### Proof

Each full realization strictly decreases the declared nonnegative counter or both slot
counters.  No transition replenishes them inside the epoch. QED.

A ticket certifies realized use; it is not consumed merely because the graph declares a
slot.

## AC3qe -- realized-amplification epoch router -- PROVED UNDER THE REALIZED-SLOT CONTRACT

Inside one fixed cyclic-source epoch, assume:

1. every use of the canonical multi-output address is alpha-pure or exits by an outer
   reset;
2. every conservative `h_t=1` transition is quotient-stuttering, finitely ticketed or
   separately descending;
3. total component stock is capped by `H`, or crossing `H` is a terminal/outer output;
4. every loss unit is impossible, terminal, descending or consumes one unit from a finite
   exact loss-ticket stock;
5. full realization either consumes a finite joint ticket or enters the gain/loss ledger
   AC3qb--AC3qc.

Then the canonical multi-output address cannot sustain an infinite nonterminal history.
Full realizations are bounded by joint tickets plus the finite stock headroom and the
finite paid loss stock.  Conservative steps close by assumption, and every forbidden
change exits the epoch.

### Proof

Joint-ticketed full realizations are bounded by AC3qd.  For all remaining full
realizations, AC3qb and AC3qc charge every surplus unit either to one of the finite cap
slots or to a genuine loss unit.  The cap stock is finite, and assumption 4 gives a
finite loss-unit budget.  Conservative transitions close by assumption 2. QED.

## Corrected AC4 owner frontier

A multi-output cyclic source address is now unresolved only when:

- realized amplification can cross every available stock cap without becoming a terminal
  or outer output;
- loss units can recur without payment, descent or finite tickets;
- conservative phase circulation is payment-relevant and unticketed;
- or the conversion is nonadditive/shared and cannot be represented by distinct realized
  output units.

The remaining non-source AC4 interfaces are unchanged: genuinely unbounded structural
semantics, nonfactoring continuations, recreatable gate capacities, unresolved
availability/conflict/reverse gates, nonadditive owners and scalar/arithmetic macro
cycles.

## Finite check

`scripts/verify_ac_realized_amplification_accounting.py` exhausts small realized-output
histories and randomly samples longer mixed histories.  It checks the exact stock
identity, cap inequality, canonical whole-history surplus-to-loss matching,
loss-type localization and joint-ticket bounds.