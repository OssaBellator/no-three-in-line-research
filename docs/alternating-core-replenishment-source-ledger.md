# Source-ledger closure for replenishable multiplicity

**Branch:** `research/alternating-core-chain`

AC3pe--AC3pi separate threshold-capped structural multiplicity from uncapped
additive supply.  The remaining gap is replenishment: a raw coordinate may increase
inside a larger construction because another finite resource was consumed.
Replenishment is harmless only when every created unit is occurrence-faithfully
charged to a bounded source ledger.

This note gives a one-level source theorem.  It does not allow sources to replenish
for free.  Recursive source creation requires a lower-rank source theorem or a higher
outer reset.

## Multiplicity and source counters

Let

`m=(m_1,...,m_q) in Z_(>=0)^q`

be the uncapped additive multiplicity vector from AC3ph, and put

`M(m)=sum_i m_i`.

Let `A` be a finite set of exact replenishment-source addresses.  Source `a` has an
integer residual counter

`s_a in Z_(>=0)`

and an integer conversion rate `rho_a>=1`.

For one transition `m->m'`, define total created and consumed multiplicity

`R=sum_i (m_i'-m_i)_+`,

`C=sum_i (m_i-m_i')_+`.

For the source transition `s->s'`, put

`d_a=s_a-s_a'`.

## AC3pj -- source-faithful replenishment inequality -- PROVED UNDER THE SOURCE-LEDGER CONTRACT

A multiplicity transition is source-faithfully replenished when:

1. `d_a>=0` for every source;
2. every positive multiplicity creation is assigned to exact source debits; and
3. the aggregate creation satisfies

   `R <= sum_(a in A) rho_a*d_a`.

If `R>0`, at least one source debit is positive.  A transition with `R>0` and no
source debit leaves the source-ledger epoch.

### Proof

The inequality is the declared conversion contract.  If `R>0` while every `d_a=0`,
the right side is zero, contradicting the inequality. QED.

The source address must include every datum affecting its conversion rate or payment
status.  Equality of physical support alone does not authorize a debit.

## AC3pk -- total replenishment is bounded by initial source stock -- PROVED

Along any source-faithful history with coordinatewise nonincreasing source counters,

`sum_t R_t <= sum_(a in A) rho_a*s_a^(0)`.

Moreover the number of transitions with positive replenishment is at most

`sum_(a in A) s_a^(0)`.

### Proof

Sum AC3pj over the history.  The total debit of source `a` telescopes and is at most
its initial counter.  Every positive-replenishment transition has at least one
positive integer source debit, so their number is at most the total initial source
stock. QED.

## AC3pl -- exact transition-count bound with consumption and replenishment -- PROVED

Assume every accepted multiplicity-changing transition has either `C>=1` or a
positive source debit.  Then the total number of accepted multiplicity-changing
transitions is at most

`M(m^(0)) + sum_(a in A)(rho_a+1)*s_a^(0)`.

### Proof

Nonnegativity of the final multiplicity gives

`sum_t C_t <= M(m^(0)) + sum_t R_t`.

By AC3pk,

`sum_t C_t <= M(m^(0)) + sum_a rho_a*s_a^(0)`.

Every accepted transition is counted by at least one consumed multiplicity unit or
one source debit.  Hence the number of transitions is at most

`sum_t C_t + sum_(t,a)d_(t,a)`

and the second term is at most `sum_a s_a^(0)`.  Combine the two bounds. QED.

The estimate permits one transition to both consume and replenish coordinates; such
a transition is merely overcounted.

## AC3pm -- lexicographic source potential -- PROVED

Define

`Phi=M(m)+sum_a rho_a*s_a`,

`S=sum_a s_a`.

On a source-faithful transition:

- a transition with `C>=1` and no multiplicity creation strictly decreases `Phi`;
- a positive-replenishment transition does not increase `Phi` and strictly decreases
  `S`.

Thus the ordered pair `(Phi,S)`, in lexicographic order, strictly decreases on every
accepted transition after splitting a mixed transition into its declared consumption
and replenishment ledger atoms.

### Proof

For a replenishment atom, `Delta M=R` and

`Delta Phi=R-sum_a rho_a*d_a<=0`,

while positive replenishment forces `sum_a d_a>=1`, so `S` decreases.  A consumption
atom reduces `M` by at least one and does not increase any source counter, so `Phi`
strictly decreases. QED.

The atom split is accounting only; AC3pl already gives the transition bound without
physically splitting the move.

## AC3pn -- closure with a finite replenishment source ledger -- PROVED UNDER THE CAPPED-SOURCE CONTRACT

Inside one reconstructed source epoch assume:

1. structural multiplicity semantics factor through the finite capped signature of
   AC3pe--AC3pg;
2. uncapped multiplicity is additive supply;
3. every multiplicity creation satisfies AC3pj for a finite exact source set `A`;
4. source counters are coordinatewise nonincreasing and their conversion rates are
   fixed inside the epoch;
5. every accepted multiplicity-changing transition consumes a multiplicity unit or a
   source unit;
6. capped recreation gates close by the AC3pi routes; and
7. any source replenishment, rate change, new source address or nonfactoring semantic
   change is a higher outer reset.

Then replenishable multiplicity cannot sustain an infinite nonterminal history inside
the source epoch.  The number of multiplicity-changing transitions is bounded by
AC3pl, while structural returns use the finite capped gate stock.

### Proof

AC3pl bounds all multiplicity-changing transitions.  AC3pg and AC3pi bound structural
false-to-true returns.  Recreation-free common-owner segments are bounded by AC3nz.
Every forbidden source change exits the epoch. QED.

## Corrected AC4 owner frontier

One-level replenishable additive multiplicity is no longer open when every created
unit is paid from a finite nonreplenishing source ledger.  The remaining multiplicity
cases are:

- sources which themselves replenish without a lower-rank or outer-reset theorem;
- cyclic source dependencies;
- conversion rates or structural semantics depending on unbounded raw values;
- nonadditive/shared resources outside an exact capacity model;
- and the unresolved availability, conflict, reverse and arithmetic macro-cycle
  interfaces.

## Finite check

`scripts/verify_ac_replenishment_source_ledger.py` exhausts small multiplicity/source
histories and random larger ledgers.  It checks the source-faithful inequality,
telescoping replenishment bound, transition-count bound, lexicographic potential and
closure accounting with mixed consume/replenish moves.
