# Conservative cycles and amplification addresses in cyclic source cores

**Branch:** `research/alternating-core-chain`

AC3po--AC3pt close every finite acyclic replenishment network and reduce an arbitrary
source graph to its nontrivial strongly connected components.  This note gives the
first exact classification inside one such component.  Positive integer conversion
rates make a strict separable linear potential impossible on a directed cycle.  The
component is therefore either one conservative unit cycle or it contains a canonical
branching/rate address with at least two declared output slots.

The second outcome is an amplification-capable address, not a claim that every allowed
output is simultaneously realized.  A realization theorem, capacity ticket, or outer
reset is still required before it becomes an executable amplification certificate.

## Positive cyclic source component

Let `S` be a finite nonempty source-type set.  For `a,v in S`, let

`rho_(a,v) in Z_(>=0)`

be the declared conversion rate.  Keep the directed edge `a->v` exactly when
`rho_(a,v)>0`, and assume this positive dependency digraph is strongly connected and
contains a directed cycle.  Equivalently, when `|S|=1`, require a positive self-loop.
Self-loops are allowed.  The edge-free singleton SCC is acyclic and was already closed
by AC3po--AC3pt.

Put

`g_a=sum_v rho_(a,v)`.

For bookkeeping, source `a` has the canonical output-slot set

`O_a={(v,k):rho_(a,v)>0, 1<=k<=rho_(a,v)}`,

so `|O_a|=g_a`.

## AC3pu -- no strict separable source potential on a positive cycle -- PROVED

There is no positive real vector `(w_a)_(a in S)` satisfying

`w_a > sum_v rho_(a,v)*w_v`

for every `a in S`.

### Proof

Choose any directed cycle

`a_0->a_1->...->a_(m-1)->a_0`.

Every rate on the cycle is a positive integer and hence at least one.  The proposed
inequality at `a_i` gives

`w_(a_i) > rho_(a_i,a_(i+1))*w_(a_(i+1)) >= w_(a_(i+1))`.

Chaining around the cycle gives `w_(a_0)>w_(a_0)`, a contradiction. QED.

Thus the path-product potential from AC3po cannot be extended through a genuinely
cyclic positive component by merely changing scalar source weights.

## AC3pv -- unit-cycle or multi-output address -- PROVED

Exactly one of the following structural alternatives holds:

1. `g_a=1` for every `a in S`;
2. one canonical source type `a_*` has `g_(a_*)>=2`, and hence at least two exact
   output slots in `O_(a_*)`.

The canonical source in the second case is the least source, in a fixed total order,
with `g_a>=2`; its first two ordered output slots form the canonical amplification
address.

### Proof

Every source has at least one positive outgoing edge: this follows from strong
connectivity for `|S|>1`, and from the required self-loop for `|S|=1`.  Therefore every
`g_a>=1`.  If they are all one, use the first alternative.  Otherwise the least source
with value at least two and its first two slots are well defined. QED.

A rate at least two and two distinct positive outgoing edges are treated uniformly:
both create two declared output slots.

## AC3pw -- the all-unit component is one directed simple cycle -- PROVED

Assume `g_a=1` for every source.  Then each source has exactly one positive outgoing
edge, that edge has rate one, and the positive dependency digraph is one directed
simple cycle containing every source in `S`.

### Proof

The equality `g_a=1` is a sum of nonnegative integers.  Hence exactly one outgoing rate
is positive and it equals one.  A finite functional digraph consists of directed cycles
with directed trees feeding them.  Strong connectivity forbids feeding trees and more
than one cycle, so all vertices lie on one directed cycle. QED.

Call this the **conservative unit-cycle case**.  A unit debit merely moves one source
unit to the next phase when the declared conversion is realized exactly.

## AC3px -- phase-insensitive conservative cycles close by stutter erasure or tickets -- PROVED UNDER THE CONSERVATIVE-CYCLE CONTRACT

Let the component be the unit cycle

`a_0->a_1->...->a_(m-1)->a_0`.

Assume inside one reconstructed epoch:

1. every realized internal conversion debits one unit at `a_i` and creates at most one
   unit at `a_(i+1)`;
2. owner currentness, payment status, continuation and all capped structural semantics
   depend on the component only through the total stock
   `S_tot=sum_i s_(a_i)`;
3. a conversion preserving `S_tot` is either erased as a quotient-stuttering transition
   or consumes one ticket from a finite exact edge-ticket stock;
4. any change of the cycle, rate, source address or phase-sensitive semantics is an
   outer reset.

Then the conservative component cannot sustain an infinite accepted internal history.

### Proof

A lossy conversion strictly decreases the nonnegative integer `S_tot`.  A stock-
preserving conversion is semantically stuttering by the quotient contract and is either
erased or consumes a finite edge ticket.  Thus only finitely many accepted internal
conversions remain.  Capped structural returns are handled by AC3pi. QED.

Without phase insensitivity or finite circulation tickets, a token may rotate forever;
this note does not identify such free rotation with progress.

## AC3py -- canonical amplification-capable source address -- PROVED

Assume the second alternative of AC3pv.  The triple

`(a_*,o_1,o_2)`,

where `o_1,o_2` are the first two slots of `O_(a_*)`, is a finite canonical address at
which one source debit has declared aggregate output capacity at least two.

If a certified transition realizes both slots as distinct additive output units, then
that transition creates at least two source units from one debit.  If only one or zero
slots are realized, the unused slot must not be counted as created supply.

### Proof

The slot stock is finite and ordered, so the address is canonical.  Its two slots are
distinct by construction.  The final statements distinguish declared capacity from
realized creation. QED.

This is the exact wall between graph structure and execution: the graph supplies an
amplification address, while the transition oracle must certify which slots actually
materialize.

## AC3pz -- cyclic-source SCC router -- PROVED

Every finite positive cyclic strongly connected source component has one exact
continuation:

1. a conservative unit cycle, closed under AC3px when phase is quotient-stuttering or
   finitely ticketed;
2. a canonical multi-output source address from AC3py;
3. or an outer reset caused by a change of rates, addresses or payment-relevant
   semantics.

Consequently a generic cyclic SCC is no longer an undifferentiated AC4 obstruction.
The remaining cyclic cases are:

- conservative circulation with payment-relevant phase and no finite ticket;
- a multi-output address whose simultaneous realization and collateral are unresolved;
- or a nonadditive/shared conversion not represented by exact output slots.

## Corrected AC4 owner frontier

Acyclic source networks and phase-insensitive conservative unit cycles now close.
The live source frontier is executable amplification or uncharged phase-sensitive
circulation inside a cyclic SCC.  Other remaining AC4 interfaces are genuinely
unbounded structural semantics, nonfactoring continuations, recreatable gate
capacities, unresolved availability/conflict/reverse gates, nonadditive owners and
scalar/arithmetic macro cycles.

## Finite check

`scripts/verify_ac_cyclic_source_scc_router.py` exhausts small positive cyclic strongly
connected integer-rate graphs and random larger components.  It checks the impossibility
of strict separable weights, the unit-cycle/multi-output dichotomy, canonical output
slots, conservative-cycle quotient histories and finite ticket closure.