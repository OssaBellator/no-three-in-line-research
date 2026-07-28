# Exact blocker frontier and proof-completion schedule

The fixed obligation DAG identifies what is open, but the next useful question is which proof
modules are actionable now and how unresolved dependencies propagate to the final implication.

## Theorem CMR2326 — PROVED AS AN INTERFACE

For every obligation `o`, the checker reconstructs the exact transitive dependency set

\[
D^*(o)=D(o)\cup\bigcup_{d\in D(o)}D^*(d).
\]

The dependency order is inherited from the fixed nineteen-node DAG; no supplied edge is
trusted.

## Theorem CMR2327 — PROVED

The open blocker set of `o` is

\[
\boxed{B(o)=\{d\in D^*(o)\cup\{o\}:d\text{ is not closed}\}.}
\]

Every blocker list is reconstructed exactly. In particular, the blocker set of
`GLOBAL_QUOTIENT_IMPLIES_ALL_N` contains every still-unclosed prerequisite of the final root.

## Theorem CMR2328 — PROVED

The current actionable frontier is the set of open obligations whose immediate dependencies
are all closed. This agrees with the frontier definition in CMR2310--CMR2317, but now each
frontier record also publishes its required typed artifact kinds and downstream impact.

## Theorem CMR2329 — PROVED

For an open obligation, define its earliest parallel completion wave recursively by

\[
\tau(o)=1+\max\{\tau(d):d\in D(o)\text{ open}\},
\]

with the maximum of the empty set equal to zero. Closed obligations have wave zero.

The root wave is the minimum number of dependency stages required if every open proof can be
completed as soon as all prerequisites close.

## Theorem CMR2330 — PROVED

For every open obligation, the checker publishes a canonical longest open dependency chain and
the complete set of unclosed downstream obligations that it blocks.

The downstream count is an exact impact measure over the fixed DAG, not a subjective research
priority score.

## Theorem CMR2331 — PROVED

The schedule publishes exact root blocker count, root critical-chain length, minimum parallel
completion waves, frontier size and all schedule/frontier digests.

## Theorem CMR2332 — HONEST PLANNING BOUNDARY

The schedule assumes a declared artifact becomes available in one wave after its dependencies.
It predicts dependency depth only; it does not estimate proof difficulty, time or truth.

## Corollary CMR2333 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_obligation_blocker_schedule.py` computes the exact blocker sets,
actionable frontier, dependency waves, longest open chains and downstream impacts.

The checker was syntax-compiled in the publication environment.
