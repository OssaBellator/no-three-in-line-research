# Finite auxiliary-state closure for chronological root-return gates

**Branch:** `research/alternating-core-chain`

AC3ti--AC3tm replace every primitive mixed-sign lift relation by a finite chronological word based at
one root.  First-level zero-defect macros and second-level transport-defect relations are genuine
returns to the same control root and the same primitive lift.  They may nevertheless change finite
payment, owner, phase or regular-history data.

This note quotients those remaining changes at root boundaries.  Under a finite root-boundary Markov
contract, individual exact root-return gates need no separate ticket: only a finite simple cycle in the
auxiliary state graph remains.

## Root-boundary gate model

Fix one normalized SCC, one root `r` and one primitive lift value at the root boundary.  Let:

- `Y` be a finite set of complete auxiliary boundary states, with `a=|Y|>=1`;
- `G` be the finite exact root-return gate dictionary, with `k=|G|>=1`;
- every gate `g in G` be one complete legal control word based at `r`, with zero total lift drift and
  edge length at most `L_gate`.

A safe dictionary imported from AC3tk--AC3tl is

`k<=K_rel+K_tr`

and

`L_gate=L_mac*max(1,P_tr+N_tr)`,

where first-level zero-defect words have length at most `L_mac` and second-level exact returns have
length at most `(P_tr+N_tr)L_mac`.

Assume the **root-boundary Markov contract**:

1. every payment, owner, capacity, regular-history and phase field affecting future gate legality is
   represented in `y in Y`;
2. for each `g in G` and `y in Y`, the gate is either illegal or has one deterministic successor
   `phi_g(y) in Y`;
3. every legal gate executes atomically to completion, returning to the same control root and lift;
4. after a legal gate sequence, terminal status and future legal gates depend only on the current
   auxiliary state;
5. a change of the SCC, root, lift normalization, gate words, auxiliary semantics or transition law is
   an outer reset.

Represent an illegal value by `bot`.  Thus every gate induces one partial transformation

`phi_g:Y -> Y union {bot}`.

## AC3tn -- exact root-boundary quotient -- PROVED

Two completed gate histories ending in the same auxiliary state `y` have identical legal next gates,
identical successor auxiliary states and identical terminal classification.

Consequently the complete live state at root boundaries is just `y`; the chronological list of earlier
root-return gates may be discarded.

### Proof

Items 1, 2 and 4 of the root-boundary Markov contract make every continuation query a function of the
current auxiliary state.  The control root and primitive lift are the same at every completed gate
boundary by item 3.  Hence equal values of `y` give equal complete boundary states and identical
continuations. QED.

No omitted payment balance is identified by this quotient.  Such an omission is a failure of item 1.

## AC3to -- finite partial-transformation monoid -- PROVED

Every gate word `v=g_1...g_j` induces one partial transformation

`phi_v=phi_(g_j) o ... o phi_(g_1)`.

There are at most

`(a+1)^a`

partial transformations of the `a`-element auxiliary state set, including the undefined value `bot`.

Thus arbitrarily long legal gate words have a finite transformation quotient.

### Proof

For each input state, a partial transformation has one of `a` defined outputs or the undefined value,
giving at most `(a+1)^a` tables.  Deterministic gate execution gives the composition identity by
induction on the word length. QED.

Illegal words only reduce the true transformation stock.

## AC3tp -- least-ending exact auxiliary cycle -- PROVED

Every legal root-boundary history containing at least `a` completed gates repeats an exact auxiliary
state.  Choosing the least ending time of a repeat gives a simple macro cycle containing at most `a`
gates.

The underlying control word:

- begins and ends at the same root;
- has zero net primitive-lift drift;
- returns to the same auxiliary state;
- and has edge length at most

`a*L_gate`.

### Proof

The history visits `a+1` auxiliary states, so two are equal.  At the least ending repeat, no state in the
intervening segment repeats internally; hence the segment has at most `a` gates.  Every constituent
gate returns to the root with zero lift drift, and the equal endpoint auxiliary states give an exact
full boundary-state return.  Summing the gate-length bounds proves the edge bound. QED.

The cycle is exact even when the individual gates change the auxiliary state.

## AC3tq -- finite exact macro-cycle stock -- PROVED

A safe address for a simple root-boundary cycle consists of its initial auxiliary state and its
nonempty gate word.  Therefore the exact cycle-address stock is at most

`C_aux=a*sum_(j=1)^a k^j`.

Every address has an underlying control word of length at most `a*L_gate`.

### Proof

There are `a` initial auxiliary states and at most `k^j` gate words of length `j`.  AC3tp bounds
`1<=j<=a`; summing gives the stock.  The control-word bound is AC3tp. QED.

Different gate words inducing the same partial transformation may be merged later, so the displayed
stock is deliberately safe.

## AC3tr -- auxiliary root-return epoch router -- PROVED UNDER THE ROOT-BOUNDARY CYCLE CONTRACT

Assume every canonical simple root-boundary cycle from AC3tp is one of:

1. quotient-stuttering and erasable;
2. strictly descending in a declared well-founded rank;
3. charged to a finite ticket of its exact auxiliary cycle address;
4. impossible under the physical gate contract;
5. or an outer reset.

Then no fixed root-boundary epoch contains infinitely many completed exact return gates.  After cycle
erasure, descent or ticket use, every residual cycle-free segment contains fewer than `a` completed
gates and fewer than `a*L_gate` underlying control edges.

In particular, individual first- or second-level root-return gates need not each consume a ticket.
Only repeated finite auxiliary-state cycles require a closure mechanism.

### Proof

Apply AC3tp at every least-ending repeated auxiliary state.  The extracted simple cycle erases,
descends, spends one finite exact ticket or leaves the epoch.  None can occur infinitely often under
the stated contract.  A segment with no repeated auxiliary state has fewer than `a` gates, and each
gate has at most `L_gate` edges. QED.

## Corrected AC4 numerical frontier

Exact chronological root returns no longer require an individual ticket when every future-relevant
boundary field has a fixed finite Markov quotient.  Their entire recurrence is one simple cycle in an
`a`-state gate graph, with explicit cycle and edge-length stocks.

The remaining numerical work is discharge of unticketed auxiliary macro cycles, unbounded or
identity-sensitive boundary state, unbounded zero-sum-free lift residuals, dynamic control graphs,
nonadditive updates, omitted guards or balances, and changes of law not declared as outer resets.

## Finite check

`scripts/verify_ac_root_return_auxiliary_state.py` samples finite partial gate transformations and
legal root-boundary histories.  It checks transformation composition, the `(a+1)^a` stock, least-ending
simple-cycle extraction, exact state return, the `a*L_gate` edge bound, cycle erasure and the
cycle-free residual bound.
