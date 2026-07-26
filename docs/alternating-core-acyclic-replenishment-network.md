# Acyclic replenishment networks and path-product potentials

**Branch:** `research/alternating-core-chain`

AC3pj--AC3pn close one-level replenishment when every created multiplicity unit is
charged directly to a finite nonreplenishing source ledger.  The next natural case
allows one source type to create lower source types before those lower types create
terminal multiplicity.  Cycles are the only genuine new obstruction.  On a finite
directed acyclic conversion graph, reverse path-product weights give one exact
integer potential and an explicit transition bound.

## Ranked source network

Let `A` be a finite set of exact source types and let `mu` be a terminal multiplicity
sink.  Fix a directed acyclic graph on `A union {mu}` in which `mu` is a sink.  An
edge `a->v` has integer conversion rate

`rho_(a,v)>=0`.

Source type `a` has residual integer counter `s_a>=0`.  Terminal uncapped additive
multiplicity has total `M>=0`.

For one accepted transition declare gross source debits `d_a>=0`, gross source
creations `r_a>=0`, terminal multiplicity creation `R>=0`, and terminal consumption
`C>=0`, with

`s_a'=s_a-d_a+r_a`,

`M'=M-C+R`.

Gross debit and creation are recorded separately even if both occur at one source
type in the same transition.  The transition is network-faithful when

`r_v <= sum_(a:a->v) rho_(a,v)*d_a` for every `v in A`,

and

`R <= sum_(a:a->mu) rho_(a,mu)*d_a`.

Every created unit must therefore have a registered predecessor debit.  A source
address includes every datum affecting its rate, owner identity or payment status.

## AC3po -- canonical reverse path-product weights -- PROVED

Set `w_mu=1`.  In reverse topological order define

`w_a=1+sum_(v:a->v) rho_(a,v)*w_v`.

Then every `w_a` is a positive integer determined uniquely by the exact conversion
DAG and its rates.  Equivalently, `w_a` is the sum of rate products over all directed
paths beginning at `a`, with the length-zero path contributing one and a path ending
at `mu` using `w_mu=1`.

### Proof

A reverse topological order exists because the graph is finite and acyclic.  Every
successor weight is already defined when `w_a` is assigned, so the recurrence gives
one positive integer.  Repeated substitution expands it into the finite directed-path
sum. QED.

The weights may be large, but they are explicit finite integers.  Polynomial closure
requires a separate bound on depth, branching and conversion rates.

## AC3pp -- one network-faithful transition spends path-product potential -- PROVED

Define

`Psi=M+sum_(a in A) w_a*s_a`.

Every network-faithful transition satisfies

`Psi'-Psi <= -C-sum_a d_a`.

Thus any accepted transition with

`C+sum_a d_a>=1`

strictly decreases `Psi` by at least one.

### Proof

Using the update equations,

`Psi'-Psi=-C+R+sum_v w_v*r_v-sum_a w_a*d_a`.

Apply the creation inequalities and collect the coefficient of each debit `d_a`:

`R+sum_v w_v*r_v
 <= sum_a d_a*sum_(v:a->v)rho_(a,v)w_v
 = sum_a d_a*(w_a-1)`.

Substitution gives the displayed bound. QED.

The inequality permits one transition to debit several ranks, create several lower
ranks and consume terminal multiplicity simultaneously.

## AC3pq -- exact epoch transition bound -- PROVED

Inside one fixed acyclic source epoch, assume every accepted source-network
transition has `C+sum_a d_a>=1`.  Then the number of accepted transitions is at most

`Psi_0=M^(0)+sum_a w_a*s_a^(0)`.

The total gross terminal consumption plus total gross source debit also satisfies

`sum_t C_t+sum_(t,a)d_(t,a) <= Psi_0`.

### Proof

Sum AC3pp over the history.  The final potential is nonnegative, so the total decrease
is at most `Psi_0`.  Each transition decreases the potential by at least its declared
`C+sum d`, proving both statements. QED.

This bound already includes source-only debit steps and mixed debit/create steps.

## AC3pr -- capped owner recreation closes over an acyclic source network -- PROVED UNDER THE RANKED-SOURCE CONTRACT

Assume inside one reconstructed epoch:

1. structural owner semantics factor through the finite capped signature of
   AC3pe--AC3pg;
2. all uncapped multiplicity and every replenishment source are additive integer
   resources;
3. every source or multiplicity creation is network-faithful on one fixed finite DAG;
4. every accepted resource transition consumes terminal multiplicity or debits a
   source;
5. capped false-to-true recreation gates close by impossibility, terminal output,
   descent or finite unrestorable capacity;
6. changing the DAG, a rate, a source address or a payment-relevant semantic is a
   higher outer reset.

Then neither recursively replenished multiplicity nor recursively replenished source
stock can sustain an infinite nonterminal history inside the epoch.  Resource steps
are bounded by AC3pq and structural returns use the finite capped gate stock.

### Proof

AC3pq bounds every accepted source-network transition.  AC3pg and AC3pi bound the
structural false-to-true returns, and AC3nz bounds recreation-free common-owner
segments.  Every forbidden network change exits the epoch. QED.

## AC3ps -- arbitrary source graphs reduce to cyclic strongly connected cores -- PROVED

For any finite directed source-dependency graph, contract every strongly connected
component.  The condensation graph is acyclic.  AC3po--AC3pr therefore close every
component-to-component replenishment history once each nontrivial strongly connected
component has its own finite potential, ticket theorem or outer reset.

Consequently, after condensation, the only source-dependency obstruction is internal
to a nontrivial strongly connected component, including a self-loop.

### Proof

The condensation of a finite directed graph is a DAG.  Treat each component as one
macro source whose internal theorem supplies its declared output counters and rates.
Apply AC3pr to the condensation.  A component with no directed cycle is a singleton
without a self-loop and needs no further internal replenishment theorem. QED.

## AC3pt -- acyclic-source frontier router -- PROVED

Every finite replenishment dependency system now has one exact continuation:

1. an acyclic dependency network, closed by the path-product potential `Psi`;
2. a nontrivial source strongly connected component, which is the canonical residual
   cyclic source core;
3. a change of source graph, rate, address or structural semantics, which is an outer
   reset.

Thus ranked or acyclic source replenishment is no longer an AC4 obstruction.

## Corrected AC4 owner frontier

The remaining source cases are cyclic strongly connected source cores without an
internal decreasing potential, genuinely unbounded structural semantics, nonfactoring
continuations, recreatable gate capacities, nonadditive/shared resources outside an
exact capacity model, and the unresolved availability, conflict, reverse and
arithmetic macro-cycle interfaces.

## Finite check

`scripts/verify_ac_acyclic_replenishment_network.py` exhausts small conversion DAGs
and rates and generates random mixed debit/create histories.  It checks the reverse
weight recurrence, path expansion, one-step potential inequality, explicit epoch
bound and condensation-cycle localization.