# Finite-transducer quotient for regular path memory

**Branch:** `research/alternating-core-chain`

AC3sj--AC3sn treat path dependence determined by a fixed suffix window.  A finite window is only one
way to summarize history.  Many legality, payment and phase rules depend on whether the event history
belongs to one of finitely many regular classes, and such dependence is represented exactly by a
finite deterministic transducer.

This note replaces the literal suffix by an arbitrary finite automaton state.  The resulting quotient
can be exponentially smaller than the window stock and covers every fixed regular-language history
rule.  Only an unbounded automaton, an omitted counter or stack, or a changing transition law remains
outside the finite-state argument.

## Finite-transducer model

Fix one epoch.  Let:

- `X` be the finite decorated physical phase-state set;
- `L<=h<=U` be a bounded integer memory interval, with `R=U-L`;
- `Sigma` be a finite event alphabet of size `s>=1`;
- `Q` be a finite automaton-state set of size `q>=1`;
- `delta:Q x Sigma -> Q` be a deterministic transition map.

For a word `v=sigma_1...sigma_m`, write

`delta*(u,v)`

for the automaton state obtained by iterating `delta` from `u` along `v`.

Assume the **regular-history Markov contract**:

1. every event has one fixed signature in `Sigma`;
2. legality, the next physical state, the next numerical memory value and terminal classification
   depend only on `(x,h,u)` and the proposed event;
3. every ticket, payment, owner or capacity balance affecting future legality is represented in
   `(x,h,u)`;
4. the full event word is never inspected except through `u`;
5. changing `Q`, `delta`, `Sigma` or any physical transition law is an outer reset.

The numerical update may be affine or non-affine.  Only boundedness and finite-state history dependence
are used below.

## AC3so -- exact regular-history quotient -- PROVED

For every event word `v`, the live history summary is exactly

`u(v)=delta*(u_0,v)`.

Two histories ending at the same exact triple

`(x,h,u)`

have identical legal next events, identical successor triples and identical terminal classification.
Thus the full event words may be removed from the live state.

### Proof

The first statement is the definition of deterministic iteration.  The second is item 2 of the
regular-history Markov contract.  Equal triples answer every legal, successor and terminal query in the
same way. QED.

This does not identify histories carrying different omitted balances.  Any such balance violates item
3 and must be added to the decorated state.

## AC3sp -- exact finite state stock -- PROVED

The complete live-state stock is at most

`N_reg=|X|*(R+1)*q`.

It is independent of the total history length and of the number of words leading to one automaton
state.

### Proof

There are `|X|` physical decorations, `R+1` numerical memory values and `q` transducer states.  AC3so
removes the full word as an independent field. QED.

A suffix window of length `w` is the special case in which `Q` is the suffix automaton with at most

`sum_(j=0)^w |Sigma|^j`

states.  Minimizing the automaton can only reduce `q`.

## AC3sq -- canonical transducer return word -- PROVED

Every internal history containing at least `N_reg` transitions repeats one exact state `(x,h,u)`.
Choosing the least ending time at which a repeat occurs gives a simple directed cycle of length at most
`N_reg`.

If the cycle event word is `v`, then

`delta*(u,v)=u`.

### Proof

The history visits `N_reg+1` states, so AC3sp and pigeonhole give a repetition.  At the least ending
repeat there is no repeated interior state, hence the intervening path is a simple cycle and has length
at most the state stock.  Its event word carries the initial transducer state to the equal final state,
which gives the displayed return equation. QED.

The return equation is exact but does not assert that every automaton loop is physically legal.

## AC3sr -- finite transition-monoid and cycle-address stocks -- PROVED

Every event word `v` induces one transformation

`tau_v:Q -> Q`,

`tau_v(u)=delta*(u,v)`.

There are at most

`q^q`

such transformations, and concatenation satisfies

`tau_(vw)=tau_w o tau_v`.

Moreover, every canonical simple recurrence from AC3sq has an address consisting of its initial exact
state and a nonempty event word of length at most `N_reg`.  Hence a safe decorated cycle-ticket stock is

`N_reg*C_reg`,

where

`C_reg=sum_(ell=1)^(N_reg) s^ell`.

### Proof

A transformation of a `q`-element set has at most `q^q` possible tables.  Deterministic iteration gives
the composition identity.  For the cycle stock, there are at most `s^ell` words of length `ell`, and
AC3sq bounds the canonical length by `N_reg`; multiply by the possible initial exact states. QED.

The transition monoid records the effect of arbitrarily long words without retaining those words.
Illegal transformations and nonreturning words only reduce the true stocks.

## AC3ss -- regular-history epoch router -- PROVED UNDER THE TRANSDUCER-CYCLE CONTRACT

Assume every canonical simple exact-state return is one of:

1. quotient-stuttering and erasable;
2. strictly descending in a declared well-founded rank;
3. charged to a finite ticket of its exact state-cycle address;
4. impossible under the physical contract;
5. or an outer reset.

Then one fixed regular-history epoch has no infinite nonterminal internal history.  After completed
simple cycles are erased or paid, every residual cycle-free segment has fewer than `N_reg` transitions.

### Proof

The exact state graph is finite by AC3sp.  An infinite path repeats states infinitely often, and AC3sq
extracts a canonical simple cycle at each least-ending repeat.  Each extraction erases, descends, spends
a finite ticket or leaves the epoch.  None can happen infinitely often under the stated contract.  A
path without a repeated exact state has fewer than `N_reg` transitions. QED.

## Corrected AC4 history frontier

Every fixed regular-language dependence on the event history now belongs to a finite exact-state
quotient.  Fixed suffix windows are one explicit presentation, not the boundary of the method.

The remaining path-memory frontier is:

- an unbounded or dynamically growing automaton state set;
- pushdown, counter or other nonregular history memory not bounded elsewhere;
- a changing or physically unbounded event alphabet;
- payment-sensitive fields omitted from `(x,h,u)`;
- unticketed simple transducer-state cycles;
- unbounded numerical memory without a common rank;
- and changes of law not declared as outer resets.

Fresh or recreated weighted capacity, nonadditive outputs, unpaid loss and the other AC4 interfaces
remain unchanged.

## Finite check

`scripts/verify_ac_regular_history_transducer.py` exhausts small deterministic automata and continuation
words, enumerates their induced transformation monoids, and samples bounded decorated transducers.  It
checks exact continuation composition, the `q^q` monoid bound, the `|X|(R+1)q` state stock, least-ending
simple-cycle extraction, the transducer return equation and the cycle-free path bound.
