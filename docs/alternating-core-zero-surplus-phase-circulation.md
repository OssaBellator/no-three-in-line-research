# Exact phase-state circulation inside zero-surplus cyclic source cores

**Branch:** `research/alternating-core-chain`

AC3qu--AC3qy charge every realized cyclic-source exit and every internal branch to one
downstream-yield-weighted surplus.  The only internal source motion not seen by that
potential is exact zero-surplus movement around a conservative directed unit cycle.
This note classifies that residual without assuming phase insensitivity.

For fixed total stock, the phase distribution has a finite exact state space.  More
strongly, every return to the same distribution traverses every directed cycle edge the
same number of times.  A finite payment decoration therefore turns every recurrent
phase-sensitive history into one canonical finite cycle word.  Such a word must be
quotient-erased, descending, ticketed, or declared an outer reset; no other hidden
circulation remains.

## Conservative phase model

Fix the directed unit cycle

`a_0 -> a_1 -> ... -> a_(m-1) -> a_0`,

with `m>=1`.  A zero-surplus internal transition chooses one index `i`, debits one
unit at `a_i`, and realizes exactly one unit at `a_(i+1 mod m)`.  It has no downstream
output, terminal-capacity output, internal loss or internal branch.

Let

`s=(s_0,...,s_(m-1)) in Z_(>=0)^m`

be the phase occupancy and put `B=sum_i s_i`.  The transition on edge `i` changes

`s_i' = s_i-1`,

`s_(i+1)' = s_(i+1)+1`,

with all other coordinates fixed.  Let `xi` be one value in a finite payment-relevant
decoration set `Q` of size `q`.  The decoration contains every finite field on which
acceptance, continuation, terminal status or phase payment depends.

## AC3qz -- finite exact phase-state stock -- PROVED

For fixed total stock `B`, the number of phase occupancies is exactly

`N_occ=binom(B+m-1,m-1)`.

The number of decorated phase states `(s,xi)` is at most

`N_phase=q*binom(B+m-1,m-1)`.

### Proof

A phase occupancy is a weak composition of `B` into `m` parts, so stars and bars gives
the first count.  Multiply by the `q` possible decorations. QED.

This stock is physical.  Symbolic token names do not create new states unless token
identity is payment-relevant, in which case that finite identity data belongs in `xi`;
an unbounded identity field is an outer-state residual rather than phase circulation.

## AC3ra -- exact equal-flow law for every occupancy return -- PROVED

Consider a nonempty zero-surplus transition segment which starts and ends at the same
phase occupancy.  Let `n_i` be the number of traversals of edge

`a_i -> a_(i+1 mod m)`

inside the segment.  Then there is an integer `k>=1` such that

`n_0=n_1=...=n_(m-1)=k`.

Consequently the segment length is exactly `k*m`.

### Proof

The net change at phase `a_i` is

`n_(i-1 mod m)-n_i`.

Returning to the same occupancy makes every net change zero, so
`n_(i-1)=n_i` for every `i`.  All edge counts are therefore equal.  The segment is
nonempty, hence their common value `k` is positive, and the total number of transitions
is `sum_i n_i=k*m`. QED.

The transitions may be interleaved in many orders, but their aggregate flow is exactly
`k` complete circulations.  No proper subset of cycle edges can support a return.

## AC3rb -- modular phase clock -- PROVED

Define

`phi(s)=sum_(i=0)^(m-1) i*s_i mod m`.

Every zero-surplus unit-cycle transition satisfies

`phi(s')=phi(s)+1 mod m`.

Hence every occupancy-return segment has length divisible by `m`.

### Proof

For an edge `i->i+1` with `i<m-1`, the weighted sum increases by one.  For the wrap
edge `m-1->0`, it changes by `-(m-1)`, which is also one modulo `m`.  Iterate along a
return segment. QED.

This clock is an audit invariant; AC3ra is stronger because it identifies every edge
count, not only the total length modulo `m`.

## AC3rc -- canonical simple phase-cycle address -- PROVED

Order the finite decorated phase states and transition labels once and for all.  In any
history containing more than `N_phase` zero-surplus transitions, choose the earliest
ending repeated decorated state, and within that endpoint choose the latest previous
occurrence.  The intervening state word has no repeated internal decorated state and has
length at most `N_phase`.

Rotate this closed word to start at its least decorated state, breaking ties by the
lexicographically least transition word.  The result is a canonical **simple phase-cycle
address**.  Its underlying phase-edge counts are all equal to one integer `k`, and

`1<=k<=floor(N_phase/m)`.

All such addresses lie in a finite safe stock; for example their number is at most

`C_phase=sum_(ell=1)^N_phase N_phase^ell`.

### Proof

Among `N_phase+1` consecutive decorated states, two are equal.  The earliest-ending and
latest-starting convention removes every repeated internal decorated state, so the word
length is at most the number of states.  Canonical rotation is well defined on a finite
ordered word.  The occupancy also returns, so AC3ra gives equal edge counts and length
`k*m`; the length bound gives the displayed bound on `k`.  The crude stock bound counts
all state words of allowed lengths and therefore safely contains every canonical address.
QED.

The stock bound is intentionally loose.  Its role is to make phase-sensitive recurrence
a finite physical address rather than to optimize constants.

## AC3rd -- finite-state phase-circulation closure -- PROVED UNDER THE PHASE-CYCLE CONTRACT

Inside one reconstructed zero-surplus epoch assume:

1. total component stock `B`, cycle length `m` and the finite decoration set `Q` are fixed;
2. every accepted internal transition is the exact forward unit move above;
3. the decorated state contains every finite payment-relevant field, so future legality and
   terminal tests are Markovian in the current decorated state;
4. every canonical simple phase-cycle address from AC3rc is either quotient-stuttering,
   strictly descending in a declared well-founded potential, or consumes one ticket from a
   finite exact address stock;
5. any change of the cycle, total stock, transition rule, decoration alphabet or hidden
   payment-relevant memory is an outer reset.

Then the zero-surplus component cannot sustain an infinite nonterminal internal history.
More quantitatively, after quotient erasure, the number of non-descending cycle removals is
at most the total initial phase-cycle ticket stock, and every remaining acyclic run has at
most `N_phase-1` transitions.

### Proof

Take any finite prefix longer than `N_phase-1`.  AC3rc extracts one canonical simple
phase-cycle address.  If it is quotient-stuttering, erase it: by Markovianity the same
current decorated state remains and the suffix can be replayed.  Otherwise the cycle
strictly descends or spends its finite ticket.  Repeating this decomposition leaves an
acyclic decorated-state path of length at most `N_phase-1`.  An infinite internal history
would therefore require infinitely many descents or ticket expenditures, contradicting
well-foundedness or finite stock.  A data change exits the epoch by assumption 5. QED.

## AC3re -- zero-surplus cyclic-core router -- PROVED

After AC3qu--AC3qy and AC3qz--AC3rd, every finite additive cyclic capacity-source core has
one exact continuation:

1. positive realized weighted output, bounded by physical headroom or paid loss;
2. negative weighted output or downstream destruction, explicitly paid or descending;
3. zero-surplus circulation on a finite decorated phase graph, reduced to canonical equal-flow
   cycle words and closed by quotient, descent or finite tickets;
4. an outer reset introducing fresh/recreated weighted capacity, unbounded identity memory,
   changed rates or changed payment semantics;
5. or a genuinely nonadditive/shared output not represented by the coordinate ledger.

Thus phase sensitivity alone is no longer an unstructured AC4 obstruction.  The live case
is specifically unbounded payment-relevant memory or an unticketed recurrent simple phase
cycle.

## Corrected AC4 source frontier

Finite additive cyclic source cores now close whenever their weighted output coordinates are
bounded and their finite decorated zero-surplus cycles are quotient-erased, descending or
ticketed.  Remaining source-side interfaces are fresh or recreatable weighted capacity,
unbounded payment-relevant phase memory, unticketed recurrent simple phase cycles,
unaddressed outputs, nonadditive sharing and unpaid weighted loss/destruction.

The other AC4 interfaces remain genuinely unbounded structural semantics, nonfactoring
continuations, recreatable non-source tickets, unresolved availability/conflict/reverse
gates, nonadditive owners and scalar/arithmetic macro cycles.

## Finite check

`scripts/verify_ac_zero_surplus_phase_circulation.py` exhausts small phase distributions and
short legal words and samples larger histories.  It checks the weak-composition stock, exact
edge-flow equality on returns, the modular phase clock, canonical first-repeat cycle lengths
and finite-state cycle decomposition.