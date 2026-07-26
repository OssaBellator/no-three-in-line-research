# Additive memory drift on zero-surplus phase cycles

**Branch:** `research/alternating-core-chain`

AC3qz--AC3re reduce a fixed-stock zero-surplus cyclic source core to a finite decorated
phase graph when every payment-relevant decoration already has finite range.  The remaining
source-side question is whether an apparently unbounded phase memory can be reconstructed
from additive counters carried by the cycle edges.

For additive memory the answer is exact.  Every return to the same phase occupancy traverses
all cycle edges equally often, so the memory change is an integer multiple of one complete-
cycle drift vector.  Zero cycle drift makes the additive memory invisible on every occupancy
return.  Nonzero bounded drift gives a finite return budget, while nonzero unbounded drift is
an explicit monotone counter gate rather than hidden circulation.  Finite modular memory adds
only its group order.

## Additive phase-memory model

Fix the conservative directed unit cycle

`a_0 -> a_1 -> ... -> a_(m-1) -> a_0`

from AC3qz, with fixed total stock `B`.  A legal zero-surplus transition on edge `i` moves one
source unit from `a_i` to `a_(i+1 mod m)`.

In addition to the phase occupancy `s`, carry:

- an integer memory vector `h in Z^r`;
- a finite abelian-group memory value `g in G`;
- one finite static context `chi in X`.

Traversing edge `i` changes memory by fixed edge increments

`h' = h + delta_i`,

`g' = g + gamma_i`,

where `delta_i in Z^r` and `gamma_i in G`.  The increments, cycle, group and static context
remain fixed inside the epoch.  Put

`Delta=sum_(i=0)^(m-1)delta_i in Z^r`,

`Gamma=sum_(i=0)^(m-1)gamma_i in G`.

All additions in `G` use its group law.

## AC3rf -- exact additive-memory drift on every occupancy return -- PROVED

Consider a nonempty transition segment starting and ending at the same phase occupancy.  Let
`k>=1` be the common edge-traversal count supplied by AC3ra.  Then

`h_end-h_start=k*Delta`,

`g_end-g_start=k*Gamma`.

### Proof

AC3ra says every directed cycle edge is traversed exactly `k` times.  Summing the fixed
integer increment `delta_i` over all traversals gives `k sum_i delta_i=k Delta`.  The same
calculation in the finite abelian group gives `k Gamma`. QED.

Thus no detailed transition ordering survives in the return memory.  Only the number of
complete circulations matters.

## AC3rg -- finite modular return period -- PROVED

Let `o=ord_G(Gamma)` be the additive order of `Gamma`, with `o=1` when `Gamma=0`.  On an
occupancy-return segment with circulation count `k`, the modular memory returns exactly when

`o divides k`.

Moreover

`1<=o<=exp(G)<=|G|`,

where `exp(G)` is the exponent of the finite abelian group.

### Proof

By AC3rf, modular memory returns precisely when `k Gamma=0`.  The positive integers with this
property are exactly the multiples of the order of `Gamma`.  The order of any element divides
the group exponent and is at most the group size. QED.

Consequently modular phase memory can multiply a primitive occupancy-cycle period by at most
`|G|`; it cannot create an unbounded recurrence alphabet.

## AC3rh -- bounded nonzero additive drift gives a finite return budget -- PROVED

Suppose some integer coordinate `j` has `Delta_j!=0` and is physically confined throughout
the epoch to

`L_j<=h_j<=U_j`.

Then every occupancy-return segment changes `h_j` in the same strict direction by at least
`|Delta_j|`.  Along one linear history, the number of pairwise consecutive nonempty occupancy-
return blocks is at most

`floor((U_j-L_j)/|Delta_j|)`.

More generally, if every return block has circulation count at least `k_0`, the bound improves
to

`floor((U_j-L_j)/(k_0*|Delta_j|))`.

### Proof

AC3rf gives change `k Delta_j` with `k>=1`.  Its sign is the fixed sign of `Delta_j` and its
magnitude is at least `|Delta_j|`, or at least `k_0|Delta_j|` under the stronger hypothesis.
A monotone sequence inside the interval `[L_j,U_j]` admits at most the displayed number of
such strict steps. QED.

A bounded additive counter therefore supplies its own finite circulation ticket stock.

## AC3ri -- zero cycle drift does not enlarge the recurrence state space -- PROVED

Assume `Delta=0`.  Along any one history, whenever the same phase occupancy occurs twice, the
integer memory vector `h` has the same value at both occurrences.

Hence, for fixed static context, integer additive memory with zero complete-cycle drift adds
no multiplicative factor to the number of recurrent occupancy states.  With finite modular
memory `G`, the number of recurrent `(occupancy,h,g,chi)` values encountered in one epoch is
at most

`|X|*|G|*binom(B+m-1,m-1)`.

### Proof

Two occurrences of the same occupancy delimit an occupancy-return segment.  AC3rf and
`Delta=0` show that the integer memory change on that segment is zero.  Thus one linear
history cannot visit one occupancy with two different `h` values.  There are
`binom(B+m-1,m-1)` occupancies, at most `|G|` modular values and `|X|` static contexts. QED.

The absolute initial value of `h` may be large, but it is fixed on all returns to a given
occupancy.  Changing that initial value or its interpretation is an outer-context change, not
new internal phase circulation.

## AC3rj -- additive phase-memory router -- PROVED UNDER THE ADDITIVE-MEMORY CONTRACT

Inside one reconstructed zero-surplus phase epoch, assume every payment-relevant unbounded
memory field is an integer additive register with fixed edge increments, every modular field
belongs to a fixed finite abelian group, and all remaining context is finite.  Then every
phase-memory coordinate has one exact continuation:

1. **zero complete-cycle drift:** it adds no recurrence multiplicity beyond the finite modular
   and occupancy stock of AC3ri;
2. **nonzero bounded drift:** it permits only the finite number of returns in AC3rh;
3. **nonzero unbounded drift:** it exposes one explicit monotone counter coordinate, which must
   be descending, capacity-bounded, ticketed, or declared an outer reset;
4. **changed increment law, group, bounds or memory interpretation:** an outer reset;
5. **nonadditive or path-dependent update:** the remaining genuine phase-memory obstruction.

Combining alternatives 1 and 2 with AC3rd closes every finite or bounded additive-memory
phase epoch under the existing quotient/descent/ticket contract.  Alternative 3 is no longer
hidden circulation: its least nonzero drift coordinate is a canonical monotone gate.

### Proof

Compute `Delta`.  If it is zero, use AC3ri and the finite-state phase-cycle closure AC3rd.  If
it is nonzero, choose the least coordinate with nonzero drift.  A declared physical interval
gives AC3rh; without one, AC3rf exhibits strict same-sign drift on every occupancy return.
Finite modular memory is controlled by AC3rg.  Any forbidden data change exits the epoch. QED.

## Corrected AC4 source frontier

Finite additive phase memory is now reconstructed completely.  The remaining source-side
phase obstruction is specifically:

- genuinely nonadditive or path-dependent hidden memory;
- an unbounded monotone additive counter with no cap, descent or ticket interpretation;
- unticketed recurrence in the finite zero-drift quotient;
- or a change of the memory law not recorded as an outer reset.

Fresh/recreated weighted capacity, unaddressed outputs, nonadditive sharing and unpaid weighted
loss/destruction remain separate source interfaces.  The other AC4 interfaces remain
unbounded structural semantics, nonfactoring continuations, recreatable non-source tickets,
unresolved availability/conflict/reverse gates, nonadditive owners and scalar/arithmetic
macro cycles.

## Finite check

`scripts/verify_ac_additive_phase_memory_drift.py` exhausts small legal phase words and samples
larger additive-memory histories.  It checks equal-flow return drift, modular orders, bounded
return budgets, zero-drift state collapse and the complete additive-memory router.