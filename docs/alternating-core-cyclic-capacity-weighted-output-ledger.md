# Weighted output accounting inside cyclic capacity-source cores

**Branch:** `research/alternating-core-chain`

AC3qp--AC3qt close every acyclic capacity-source hierarchy and reduce the remaining
source graph to positive cyclic strongly connected components.  A cyclic component may
preserve its internal source stock while repeatedly emitting lower-ranked sources or
physical capacity.  Counting only the internal stock therefore misses the actual growth.

This note attaches the already constructed downstream terminal-yield weights to every
realized exit from the cyclic component.  Internal branching, downstream emission and
terminal physical-capacity creation then have one exact weighted surplus.  Under finite
occurrence capacities, positive surplus is bounded by physical headroom plus exact paid
loss/destruction.  The only zero-surplus residual is genuinely phase-sensitive circulation.

## Cyclic component and downstream yield

Fix one positive cyclic capacity-source component `S`.  Contract the rest of the finite
capacity-source graph into the acyclic downstream region `R` and terminal physical-capacity
sink `beta`.  Give every downstream source type `v in R` its terminal-yield weight `y_v`
from AC3qp, and put `y_beta=1`.

At time `t`, source type `a in S` has stock `s_a(t)`, downstream type `v` has stock
`u_v(t)`, and terminal physical capacity is `B(t)`.  Define

`P(t)=sum_(a in S)s_a(t)+sum_(v in R)y_v*u_v(t)+B(t)`.

For one realized transition whose debit lies in `S`, record gross component debits `d_a`,
gross component creations `r_a`, downstream creations `e_v`, and terminal creation `G`.
Put

`D_S=sum_a d_a`,

`R_S=sum_a r_a`,

`E_down=sum_v y_v*e_v+G`,

and define the **realized weighted output surplus**

`z=R_S+E_down-D_S`.

All gross quantities are occurrence-faithful.  An unrealized declared slot contributes zero.
A transition wholly inside the downstream acyclic region obeys the AC3qp network contract.

## AC3qu -- exact cyclic-output potential change -- PROVED

For every transition debiting only sources in `S`,

`P(t+1)-P(t)=z`.

For every downstream-network transition, including terminal physical-capacity creation and
destruction,

`P(t+1)-P(t)<=-D_beta`,

where `D_beta>=0` is its gross terminal physical-capacity destruction.

### Proof

For an `S`-transition, component stock changes by `R_S-D_S`, downstream yield stock changes
by `sum_v y_v e_v`, and terminal capacity changes by `G`; summing gives `z` exactly.

For a downstream transition, the `S`-stock is unchanged.  AC3qp gives
`Delta(sum_v y_v u_v)<=-G`, while terminal capacity changes by `G-D_beta`.  Adding cancels
`G` and leaves at most `-D_beta`. QED.

Thus an exit source is counted by the amount of terminal capacity it can still generate,
not merely by one symbolic source name.

## AC3qv -- finite occurrence capacities give a weighted ceiling -- PROVED

Assume every component source type `a`, every downstream source type `v`, and terminal
physical capacity have fixed finite additive occurrence ceilings

`b_a`, `c_v`, `B_max`.

Every physically feasible state satisfies

`P(t)<=H_out`,

where

`H_out=sum_(a in S)b_a+sum_(v in R)y_v*c_v+B_max`.

If a transition leaves this feasible region, the least overloaded decorated occurrence
coordinate is a canonical weighted-output crossing certificate.

### Proof

Sum the component coordinate ceilings with coefficient one, the downstream ceilings with
coefficient `y_v`, and the terminal ceiling with coefficient one.  A state violating one of
the coordinate ceilings has a nonempty finite overloaded set, whose least member is
canonical. QED.

The ceiling is physical.  Fresh source aliases do not enlarge it unless they introduce a new
occurrence coordinate, which is an outer reset.

## AC3qw -- weighted surplus/loss identity and bound -- PROVED

Consider a finite history consisting of `S`-transitions and downstream transitions.  For the
`S`-transitions put

`A_out=sum_t (z_t)_+`,

`L_out=sum_t (-z_t)_+`.

Let

`K_down=-sum_(t downstream)(P(t+1)-P(t))>=0`

be the exact observed downstream potential drop.  Then

`P(T)=P(0)+A_out-L_out-K_down`.

If every state is physically feasible, then

`A_out<=L_out+K_down+H_out-P(0)`.

### Proof

AC3qu gives the exact change `z_t` on every component transition.  Split each `z_t` into its
positive and negative parts.  By definition, the downstream changes sum to `-K_down`.
Telescope to obtain the identity, then use `P(T)<=H_out`. QED.

This is the cyclic analogue of AC3qb and AC3qm.  It charges weighted emission and internal
branching to initial physical headroom, exact component loss or exact downstream
destruction.

## AC3qx -- unit-cycle leakage and internal branching are both positive surplus -- PROVED

Two important special cases are exact.

1. **Unit internal circulation with exits.**  If a component transition debits one source
   unit and realizes exactly one internal successor, then

   `z=E_down`.

   Every realized downstream or terminal exit is therefore positive weighted surplus.
2. **Pure internal branching.**  If a transition has no downstream or terminal output, then

   `z=R_S-D_S`.

   Every realized internal creation beyond the gross debit count is positive weighted
   surplus.

In particular, an internal unit cycle accompanied by a realized terminal or lower-component
slot is not conservative circulation.  It increases `P` by the exact downstream yield of
that slot.

### Proof

Substitute `R_S=D_S` in the first case and `E_down=0` in the second into the definition of
`z`. QED.

This separates declared multi-output structure from its three execution outcomes: positive
weighted surplus, negative weighted loss, or exact zero-surplus phase movement.

## AC3qy -- cyclic weighted-output router -- PROVED UNDER THE WEIGHTED-CAPACITY CONTRACT

Inside one reconstructed cyclic capacity-source epoch assume:

1. all component, downstream and terminal units have occurrence-faithful coordinates with
   the finite ceilings of AC3qv;
2. every realized component output is recorded in `R_S`, `e_v` or `G` before acceptance;
3. positive feasibility crossings are impossible, terminal, descending or consume a finite
   exact crossing ticket and end the current feasible segment;
4. negative weighted-surplus units and downstream potential drops are impossible, terminal,
   descending or paid from finite exact loss/destruction ticket stocks;
5. every zero-surplus component transition is quotient-stuttering, descending or consumes a
   finite exact phase/circulation ticket;
6. changes of the component, downstream graph, yield weights, occurrence ceilings, rates or
   payment-relevant decorations are outer resets.

Then the cyclic capacity-source component cannot sustain an infinite nonterminal internal
history.

### Proof

On each maximal feasible segment, AC3qw bounds total positive weighted surplus by finite
headroom plus the finite paid loss/destruction stocks.  AC3qx includes both realized exits
and internal branching in that surplus.  Negative-surplus and downstream-drop transitions
close by assumption 4.  Zero-surplus transitions close by assumption 5.  A feasibility
crossing ends the segment under assumption 3, and only finitely many ticketed crossings can
occur.  Every forbidden data change exits the epoch. QED.

## Corrected AC4 source frontier

A cyclic capacity-source core with finite weighted physical output capacity is now closed
whenever positive output, negative loss and zero-surplus phase movement obey the declared
crossing/payment/ticket contracts.  The remaining cyclic source cases are:

- phase-sensitive zero-surplus circulation without a finite ticket or quotient;
- fresh or recreatable weighted occurrence capacity outside the fixed ceiling;
- realized outputs without occurrence-faithful downstream or terminal addresses;
- nonadditive/shared outputs not represented by the weighted coordinate sum;
- unpaid weighted loss or downstream destruction.

The other AC4 interfaces remain genuinely unbounded structural semantics, nonfactoring
continuations, recreatable non-source tickets, unresolved availability/conflict/reverse
gates, nonadditive owners and scalar/arithmetic macro cycles.

## Finite check

`scripts/verify_ac_cyclic_weighted_output_ledger.py` exhausts small cyclic stock/output
steps and samples mixed component/downstream histories.  It checks the exact potential
change, weighted ceiling, surplus/loss identity, unit-cycle leakage, internal branching and
the finite-headroom bound.