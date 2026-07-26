# Scalar-affine memory maps on zero-surplus phase cycles

**Branch:** `research/alternating-core-chain`

AC3rf--AC3rj classify additive memory on a conservative zero-surplus source cycle.  The next
path-dependent model allows every labelled phase transition to apply its own scalar-affine
integer map.  Different transition orders may then produce different memory values even when
the phase-edge multiset is fixed.

The order dependence is nevertheless finite at the cycle-address level.  Every canonical
simple phase-cycle word from AC3rc composes to one exact map

`h -> A_w*h+B_w`.

The integer multiplier gives a complete local classification: identity, idempotent reset,
involution, translation, or expansion about one rational fixed point.  Thus scalar-affine
memory is no longer an arbitrary hidden-history field.  The remaining global issue is only how
the finite collection of nontrivial cycle maps is ranked, bounded or ticketed when different
cycle words are interleaved.

## Scalar-affine phase-memory model

Work inside one fixed zero-surplus phase epoch from AC3qz--AC3re.  Its decorated phase-state
alphabet and transition-label alphabet are finite.  Carry one integer memory register

`h in Z`.

Every labelled transition `e` has fixed coefficients

`alpha_e,beta_e in Z`

and updates the memory by

`h' = alpha_e*h+beta_e`.

The coefficients, phase graph, legality rule and interpretation of `h` are fixed throughout
the epoch.  A change of any of these data is an outer reset.

For a transition word

`w=e_1 e_2 ... e_l`,

define recursively

`A_empty=1`, `B_empty=0`,

`A_(we)=alpha_e*A_w`,

`B_(we)=alpha_e*B_w+beta_e`.

## AC3rk -- exact affine composition of a phase word -- PROVED

For every word `w`, applying its transitions in order sends

`h -> A_w*h+B_w`.

For every integer `n>=0`, repeated application of the same closed word satisfies

- if `A_w=1`,

  `f_w^n(h)=h+n*B_w`;

- if `A_w!=1`,

  `f_w^n(h)=A_w^n*h+B_w*(A_w^n-1)/(A_w-1)`.

The second expression is integral.

### Proof

The one-word formula follows by induction using the displayed recursion.  Iterating one affine
map gives the geometric-sum formula.  Since `A_w^n-1` is divisible by `A_w-1`, the result is an
integer. QED.

This is where transition order is recorded: two cycle words with the same phase-edge counts may
have different pairs `(A_w,B_w)`, but each exact ordered word has only one pair.

## AC3rl -- finite-order scalar-affine cycle maps -- PROVED

Let `f(h)=A*h+B` be the map attached to one canonical simple phase-cycle word.

1. If `A=1` and `B=0`, then `f` is the identity.
2. If `A=0`, then `f` is idempotent:

   `f^2=f`.
3. If `A=-1`, then `f` is an involution:

   `f^2=id`.

Hence these three cases add respectively no memory state, at most one reset state, or at most a
two-cycle to the recurrence quotient.

### Proof

Substitute the three multiplier values into `f(h)=A h+B`.  When `A=0`, every value maps to `B`
and `B` maps to itself.  When `A=-1`,

`f(f(h))=-(-h+B)+B=h`. QED.

## AC3rm -- translation and expanding-defect gates -- PROVED

For the remaining multiplier cases:

1. **Translation.**  If `A=1` and `B!=0`, then

   `f^n(h)=h+nB`.

   Consecutive applications which remain inside a physical interval `L<=h<=U` number at most

   `floor((U-L)/|B|)`.

   Without a bound, every application is an explicit same-sign translation gate.

2. **Expansion.**  If `|A|>=2`, define the fixed-point defect

   `c=(A-1)h+B`.

   One application gives exactly

   `c'=A*c`.

   Thus `c=0` is a fixed point.  If `c!=0`, its absolute value grows by at least a factor two on
every repeated application of this cycle word.  If `1<=|c|<=C` is physically required, the
number of consecutive applications is at most

   `floor(log_(|A|)(C/|c_0|))`.

### Proof

The translation statement is AC3rk with `A=1`.  For expansion,

`(A-1)(Ah+B)+B=A((A-1)h+B)=Ac`.

The bounded repetition estimates follow from monotonic translation distance and geometric
growth of `|c|`. QED.

The defect coordinate avoids rational arithmetic: `c=0` is equivalent to the rational fixed
point equation `h=-B/(A-1)` whenever that value is integral.

## AC3rn -- finite affine cycle-address stock -- PROVED

Fix the finite decorated phase-state graph, its transition labels and all edge coefficients.
Every canonical simple phase-cycle address from AC3rc determines exactly one decorated affine
address

`(w,A_w,B_w)`.

Consequently the affine-address stock is no larger than the canonical simple cycle-word stock
`C_phase` from AC3rc.  Unbounded numerical values of `h` do not create new map addresses.

### Proof

The word `w` belongs to the finite AC3rc stock.  AC3rk reconstructs `(A_w,B_w)` deterministically
from the fixed edge coefficients, so no additional choice is introduced. QED.

## AC3ro -- scalar-affine phase-memory router -- PROVED UNDER THE AFFINE-CYCLE CONTRACT

Inside one fixed zero-surplus phase epoch, suppose every path-dependent unbounded memory field
is a scalar integer register with fixed affine edge updates.  Then every canonical simple phase
cycle has one exact continuation:

1. identity, reset or involution, absorbed into a finite quotient by AC3rl;
2. bounded translation, with the finite repetition budget of AC3rm;
3. bounded expanding defect, with the finite geometric repetition budget of AC3rm;
4. an unbounded translation or expansion gate carrying the finite address `(w,A_w,B_w)`;
5. a changed coefficient law, phase graph, memory interpretation or hidden state, which is an
   outer reset;
6. a genuinely nonlinear or non-affine path-dependent update, which remains outside this
   theorem.

Assume every live gate in alternative 4 either decreases a declared common well-founded rank,
consumes a finite ticket attached to its affine address, or exits the epoch.  Then the
scalar-affine phase epoch cannot contain an infinite nonterminal internal history.

### Proof

AC3rn gives finitely many cycle-map addresses.  AC3rl absorbs finite-order maps.  AC3rm bounds
every physically bounded translation or expansion.  Every remaining extracted phase cycle is
therefore a ranked, ticketed or exiting occurrence of one finite address.  AC3rd erases the
finite-state residue between such occurrences.  Infinite internal continuation would require
infinitely many rank decreases or ticket expenditures, or a forbidden data change. QED.

The common-rank requirement is necessary: unrelated translation or expansion maps may undo one
another when interleaved.  This note does not claim that arbitrary affine semigroups terminate.
It reduces the problem to a finite, explicitly labelled semigroup of cycle maps.

## Corrected AC4 phase-memory frontier

The phase-memory boundary now consists of:

- a finite family of unbounded affine cycle gates lacking a common rank or tickets;
- genuinely nonlinear or non-affine path-dependent memory;
- changes of the affine law not recorded as outer resets;
- and unticketed recurrence in the remaining finite quotient.

Additive memory, finite modular memory, finite-order affine maps, bounded translations and
bounded expanding defects are no longer live obstructions.  Fresh or recreated weighted
capacity, unaddressed outputs, nonadditive sharing and unpaid weighted loss remain separate
source interfaces.

## Finite check

`scripts/verify_ac_scalar_affine_phase_memory.py` exhausts short words over a small affine-map
alphabet and checks exact composition and iteration formulas.  It also verifies the identity,
reset and involution cases, bounded translation budgets, expanding-defect scaling and random
finite phase-cycle addresses.