# Bounded-denominator repair-transversal potential conservation

## Status

This note proves BDA5gl--BDA5gp under the complete occurrence-faithful primitive-potential repair-source contract. It does not construct the rational-gain compatibility graph and does not prove BDA6 or the no-three-in-line conjecture.

## Setup

Fix the canonical restoration repair transversal from BDA5gg--BDA5gk. Every selected incidence retains its restoration address, outside primitive-potential slot, source vertex, gain, damping factor and repair class. A unit primitive-potential token is rooted only in initial stock or a named exogenous deposit. A valid transition consumes one predecessor and creates one same-class successor. Issuing a repair incidence consumes one live token exactly once.

## Theorem block

**BDA5gl (exact potential issuance).** Every selected repair incidence backed by a live compatible primitive-potential occurrence is one actual unit debit.

**BDA5gm (global conservation).** At every event prefix,

`live primitive-potential tokens + issued repair incidences = initial tokens + named deposits`.

**BDA5gn (classwise conservation).** The identity holds separately for every complete source/gain/damping class; changing a retained arithmetic field is a reset.

**BDA5go (transversal payment).** A transversal of deficit `delta` has class counts summing to `delta`, so one class carries at least `ceil(delta/|C|)` incidences. Current class balances pay the transversal or return the least overloaded arithmetic class.

**BDA5gp (first failure).** The first violation is an exact source-less issuance, predecessor split, repeated debit, hidden deposit or arithmetic-class mismatch. Unrecorded replenishment and relabelling reset the account.

## Proof

Induction on the ordered event log gives the global and classwise identities. Deposits add one token to both source and live accounts; valid transitions preserve live mass and class; valid issuance exchanges one live token for one issued incidence. No other event preserves the identities. Summing classwise issuance proves the concentration statement.

## Remaining interface

The arithmetic work is to construct the complete primitive-potential occurrence dictionary and verify a live compatible source for every selected restoration incidence, or discharge the returned exact failure.