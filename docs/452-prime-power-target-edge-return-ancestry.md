# Returned target edges have exact redeletion, ancestry and contraction transitions

This chapter records CMR2956--CMR2967. CMR2944--CMR2955 install the forced
mixed-certificate escape bank and identify one precise restoration operation.
The present chapter installs the returned-target-edge operation of
CMR720--CMR726.

The executable checker is:

```text
scripts/check_prime_power_target_edge_return_ancestry.py
```

## CMR2956 — literal returned-edge restoration

Fix a factor context after a target edge `e` has been deleted. The deletion
context therefore omits `e` from its allowed edge set. Store one exact perfect
matching

\[
M_0\in\operatorname{PM}(H_0-e).
\]

A later return context has the same labelled row and column domains, contains
`e`, and may both restore old deleted edges and delete other old edges.

The checker seals both masks and records

```text
restored_edges
simultaneously_deleted_edges
```

Thus the return of `e` is a literal restoration transition rather than an
anonymous temporal event.

## CMR2957 — stored avoidance validation

The stored matching must be a generated feasible matching of the deletion
context and must avoid `e`. The later endpoint supplies one exact matching of the
return context.

The operation labels bind the fixed owner, target edge, deletion-context digest
and later-context digest.

## CMR2958 — surviving stored matching gives exact redeletion

If every edge of `M_0` remains allowed in the return context, then `M_0` is a
later perfect matching avoiding `e`.

The checker constructs the literal redeletion child by removing `e` from the
later allowed edge set and proves

\[
\operatorname{PM}(H_1-e)
=
\{M\in\operatorname{PM}(H_1):e\notin M\}.
\]

It also verifies that `M_0` belongs to this generated child. The typed response
is

```text
stored-avoidance-survives-exact-redeletion
```

This is the exact CMR720 branch.

## CMR2959 — blocked stored matching exposes deletion ancestry

If `M_0` does not survive, the checker generates

\[
M_0\setminus E(H_1)
\]

and chooses its least edge as the canonical deletion-ancestry witness.

The complete missing subset is sealed in the transition record. This is the
literal CMR721 witness and makes no claim that one missing edge explains every
possible avoiding matching.

## CMR2960 — blocked but nonessential return

The stored avoidance matching may be blocked even though the returned edge is
still nonessential. In that case the checker generates all later matchings
avoiding `e`, constructs the literal redeletion child and proves exact family
equality.

The typed response is

```text
blocked-stored-avoidance-nonessential-return
```

It carries both the old stored-edge deletion witness and the exact alternate
redeletion context.

## CMR2961 — essential return has a mandatory stored-edge witness

If `e` is essential in the later context, no later avoiding matching exists.
Consequently the stored matching cannot survive and its canonical missing edge
is mandatory.

The typed response begins

```text
essential-return-deletion-ancestry-and-contraction
```

This is the exact CMR722 implication.

## CMR2962 — exact essential target contraction

For an essential returned edge `e=(r,c)`, remove row `r`, column `c`, and all
incident factor edges. The generated residual context has feasible family
exactly

\[
\{M\setminus\{e\}:M\in\operatorname{PM}(H_1)\}.
\]

Adjoining `e` is the inverse map. The checker verifies both directions and
strict factor-side descent.

This is the executable CMR725 factorisation.

## CMR2963 — rank-two target transfer

Supply a current matching-compatible target triple `T` containing `e`. After
contraction the residual prescription is

\[
T\setminus\{e\},
\]

which has exactly two edges in the three-edge regression witness and always has
rank at most two.

The complete residual target prescription is sealed in the contraction record.
It enters the existing low-rank deletion, essential-transfer or certificate
banks without recreating a rank-three target anonymously.

## CMR2964 — linear stored-witness stock

For essential returns at one fixed owner, target edge and stored matching, every
episode receives the least missing edge of `M_0`.

If `|M_0|=m` and the recurrence threshold is `mu>=2`, then either one stored edge
occurs as witness at least `mu` times or

\[
K\le(\mu-1)m.
\]

The checker verifies both finite-history and recurrent-witness branches. This is
the exact CMR723 linear stock, smaller than the complete host-edge universe.

## CMR2965 — absence runs and reintroduction

For one recurrent stored witness edge, a boolean presence timeline generates its
maximal absence runs and absent-to-present transitions.

The checker proves the exact identity

\[
\rho(f)\le 1+I(f).
\]

The regression timeline has three absence runs and two reintroductions. This is
the CMR724 route into the existing reintroduction and entering-edge ledgers.

## CMR2966 — finite regression and corruption rejection

The checker records:

```text
4 canonical return scenarios
1 stored-survival exact-redeletion scenario
1 blocked nonessential alternate-redeletion scenario
2 essential-return contraction scenarios
10 exhaustive two-by-two returned-edge transitions
4 two-by-two stored-survival cases
6 two-by-two blocked-stored cases
6 two-by-two essential-return cases
2 essential-return history scenarios
1 finite and 1 recurrent history branch
3 maximal absence runs and 2 reintroductions
8 rejected malformed or corrupted cases
```

The contract digest is:

```text
04a533666c90c2f13bcb18731e10e0bca4d6357a806f8be44ee47af6f90e2382
```

The finite census is regression evidence. CMR2956--CMR2965 are exact matching,
context, recurrence and contraction statements.

## CMR2967 — T02 consequence and honesty boundary

The construction transition bank now contains genuine ancestry for:

```text
returned target-edge restoration
stored-avoidance exact redeletion
stored-edge deletion ancestry
blocked nonessential alternate redeletion
essential returned-edge contraction
rank-two target transfer
linear recurrence stock
absence-run/reintroduction routing
```

Therefore:

```text
returned_target_edge_ancestry_proved = 1
returned_target_edge_restoration_exact = 1
essential_target_contraction_exact = 1
```

The permanent boundary remains:

```text
all_restoration_operations_proved = 0
all_returned_edge_operations_proved = 0
all_construction_ancestry_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

Owner changes, general closure-envelope transitions, non-target restorations,
target-bank handoffs and scheduler transitions remain uninstalled. The separate
finite stocks, redeletions and strict contractions have not yet been assembled
into one exhaustive global termination theorem. No all-`n` theorem or downstream
population, chamber or final implication is claimed.
