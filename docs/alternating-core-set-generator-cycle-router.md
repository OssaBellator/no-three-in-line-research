# Reverse-atom gates for recurrent set-generator macro cycles

**Branch:** `research/alternating-core-chain`

The outer-alphabet audit leaves arbitrary selected subbanks, transition-state
families and support generators as genuine set-valued data.  Their full state
spaces can have size `2^U`, so a polynomial atom dictionary does not by itself
make the exact outer-profile graph polynomial.  Nevertheless an exact return
cycle cannot change a set-valued field without later reversing the membership
of at least one atom changed on the departure edge.

This note localizes every such cycle to one reverse-atom gate.  It does not
claim that the reverse gate is paid merely because it exists.  The remaining
obligation is attached to that exact atom and gate kind rather than to an
arbitrary full selected subset or complete cycle word.

## Set-valued outer fields

Let the outer profile contain ordered set fields

\[
S_j\subseteq \mathcal U_j,
\qquad 1\le j\le q,
\]

where every atom universe `U_j` is finite and totally ordered.  Put

\[
U_j=|\mathcal U_j|.
\]

A directed outer edge may change several fields and several atoms at once.  No
atomic physical interpolation is assumed.

Fix one directed edge

\[
e:\alpha\longrightarrow\beta
\]

which changes at least one set field.  Choose the least changed set-field index
`j(e)` and then the least atom

\[
u(e)\in S_{j(e)}(\alpha)\triangle S_{j(e)}(\beta).
\]

Its departure direction is `+` when the atom is absent in `alpha` and present
in `beta`, and `-` in the opposite case.

## AC3nn -- every exact return contains an opposite atom gate -- PROVED

Let a chronological return path start at `beta` and end at `alpha`.  Then some
edge on that return path changes the membership of `u(e)` in the direction
opposite to its change on `e`.

Choose the first such edge.  It is the **canonical reverse gate** of the return
episode.  Before that edge, the membership of `u(e)` remains equal to its
post-departure value in `beta`; immediately after it, the membership equals its
value in `alpha`.

The statement remains true when `e` or the reverse gate changes an arbitrary
batch of other atoms.  It does not require the intermediate subsets obtained by
single-atom toggles to be legal transition states.

### Proof

The chosen atom has different membership in `alpha` and `beta`.  Along the
finite membership word on the return path, the initial bit is therefore the
opposite of the final bit.  Hence the bit changes at least once.  At its first
change it moves from the `beta` value to the `alpha` value, which is exactly the
opposite direction from the departure edge.  All preceding return vertices
retain the `beta` value. QED.

## Gate kinds and address stock

For field `j`, suppose every reverse edge has one canonical gate kind from a
finite dictionary `K_j`.  A gate kind may record the least physical cause,
owner-status route, protection-context change, generator operation, phase
change or another already proved finite reset witness.  It need not identify
the full source and target subsets.

Give a reverse gate the address

\[
\boxed{(j,u,\varepsilon,\kappa)},
\]

where `epsilon` is the departure direction and `kappa in K_j` is the kind of
the opposite return edge.

## AC3no -- polynomial reverse-gate localization -- PROVED

The ambient reverse-gate address stock is at most

\[
\boxed{
R_{\rm gate}
\le
2\sum_{j=1}^q U_jK_j.
}
\]

For one fixed repeated decorated edge `e`, the field, atom and departure
direction are fixed.  Therefore its return episodes use at most `K_{j(e)}`
reverse-gate addresses.  If those episodes have total weight `W`, one exact
reverse-gate address carries weight at least

\[
\boxed{W/K_{j(e)}}.
\]

Thus a set field may have exponentially many complete states while every
recurrent edge return is localized to a polynomial address whenever the atom
and gate-kind dictionaries are polynomial.

### Proof

There are `U_j` atom choices, two departure directions and `K_j` gate kinds in
field `j`; summing gives the first bound.  For a fixed edge, AC3nn fixes the
field, atom and direction, leaving only the gate kind.  Weighted pigeonhole
gives the second display. QED.

Equality of a reverse-gate address does not identify the complete intervening
history and is not itself payment.

## AC3np -- monotone set-generator epochs contain no return cycle -- PROVED

Fix one set field `S_j` during an epoch.

1. If every strict change only adds atoms, no directed cycle can contain an
   edge changing `S_j`.
2. If every strict change only removes atoms, no directed cycle can contain an
   edge changing `S_j`.
3. In either direction, the field changes strictly at most `U_j` times.

More generally, every exact cycle which changes `S_j` contains both an
addition and a removal of at least one common atom.

### Proof

Cardinality strictly increases under a nonempty addition and strictly
decreases under a nonempty removal, so a one-direction history cannot return
to its starting set.  Each atom can enter at most once in an addition-only
epoch or leave at most once in a removal-only epoch.  The final statement is
AC3nn applied to any changed edge of the cycle. QED.

## Reverse-gate tickets

A reverse-gate realization is **gate-progressive** when every nonterminal use
consumes one previously unused ticket from a finite universe
`T_gate`, and no transition in the same closure attempt can restore that
ticket.  The ticket may name the exact selected protected atom, generator
support occurrence, owner-capacity unit, reopened exclusion, phase resource or
another proved capacity-one object.

The gate address alone is not a ticket.  In particular, a common owner whose
single payment covers several alternatives must remain in the common-owner
ledger rather than being duplicated into atom tickets.

## AC3nq -- conditional closure of set-generator macro cycles -- PROVED UNDER THE REVERSE-GATE CONTRACT

Assume every recurrent exact macro cycle which changes a set-valued outer field
has a canonical reverse gate satisfying at least one of:

1. the gate returns an improving state, accepted chamber, paid executable menu
   or terminal literal/resource profile;
2. the gate strictly advances a separately bounded integer potential;
3. the gate consumes a previously unused gate ticket;
4. the gate is physically impossible under its retained occurrence and
   coherence decorations.

Then no such set-generator cycle can recur indefinitely.  If the ticket
universe has size `Q_gate`, alternative 3 occurs at most `Q_gate` times.
Combining this gate counter with AC3kb's first-edge/internal-step potential and
AC3lc's remaining cycle routers gives finite closure for every recurrent cycle
covered by this contract.

### Proof

AC3nn assigns every set-generator return episode a reverse gate.  Alternatives
1 and 4 terminate that recurrence.  Alternative 2 strictly advances a bounded
counter.  Alternative 3 consumes an unrestorable finite ticket.  Therefore no
covered gate address, and hence no covered set-generator cycle, can recur
infinitely often.  AC3kb handles the history before edge repetition and the
internal work between resets. QED.

## AC3nr -- corrected generator and macro-cycle frontier -- PROVED

For selected subbanks, support registries and transition-state families whose
membership is represented in a finite physical atom universe:

1. a recurrent exact cycle need not be enumerated through all `2^U` full set
   states before localization;
2. every changed departure edge has AC3nn's opposite reverse atom;
3. the recurrence witness has AC3no's atom/gate address rather than an arbitrary
   complete subset name;
4. compatible monotone epochs terminate by AC3np;
5. a reverse gate with payment, descent, impossibility or a capacity-one ticket
   closes through AC3nq.

The following remain live:

- reverse gates without any of those four discharges;
- cycles changing only scalar, arithmetic or common/nonadditive-owner fields;
- unbounded atom or gate-kind dictionaries;
- discretionary generators not represented by exact physical membership atoms;
- restoration of purported tickets across outer epochs.

### Proof

Items 1--4 are AC3nn--AC3np, and item 5 is AC3nq.  The excluded cases either do
not change a represented set field or lack the finite/progressive hypotheses
used by those theorems. QED.

## Consequence

The selected-subbank and nonmonotone state-generator portion of AC4 is now
cycle-localized to exact reverse-atom gates.  The next theorem need not classify
an exponential family of full subsets.  It must instead show that each
recurrent reverse gate is paid, strictly descending, impossible or consumes an
unrestorable physical ticket.

## Finite check

`scripts/verify_ac_set_generator_cycle_router.py` exhausts all simple cycles of
subsets of a three-atom universe through length five.  For every changed first
edge it checks the canonical least atom, the first opposite return gate,
monotone-cycle impossibility and the finite gate-address count.  It also checks
batch edges which change more than one atom at once.
