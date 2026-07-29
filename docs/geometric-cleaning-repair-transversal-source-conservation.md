# Geometric-cleaning repair-transversal source conservation

## Status

This note proves GC2lj--GC2ln under the complete occurrence-faithful cleaning repair-source contract. It does not construct the donor/remedy/height repair graph and does not prove GC5 or the no-three-in-line conjecture.

## Setup

Fix the canonical cause repair transversal from GC2le--GC2li. Every selected incidence retains its cause, donor, remedy, height, physical-source and epoch fields. A unit cleaning-source token is rooted only in initial stock or a named exogenous deposit. A valid transition consumes one predecessor and creates one same-class successor. Issuing a selected repair incidence consumes one live token exactly once.

## Theorem block

**GC2lj (exact cleaning issuance).** Every selected cause-to-slot repair incidence backed by a live compatible cleaning occurrence is one actual unit debit.

**GC2lk (global conservation).** At every event prefix,

`live cleaning-source tokens + issued repair incidences = initial tokens + named deposits`.

**GC2ll (classwise conservation).** The identity holds separately for every complete donor/remedy/height/source class; changed geometry or untagged feedback is a reset.

**GC2lm (transversal payment).** For deficit `delta`, the retained class counts sum to `delta`, so one class carries at least `ceil(delta/|C|)` incidences. Exact balances pay the transversal or return the least overloaded cleaning-source class.

**GC2ln (first failure).** The first violation is an exact source-less issuance, predecessor split, repeated debit, hidden deposit or geometric-class mismatch. Relabelling, omitted donor data and unrecorded feedback reset.

## Proof

Induct through the event log. Deposits add one source and one live unit. Valid transitions preserve total live mass and complete cleaning class. Valid issuance converts one live unit into one issued incidence. These operations preserve both identities; every forbidden operation breaks one at its first prefix. Summing classwise issued counts proves concentration.

## Remaining interface

The geometric work is to construct the complete donor/remedy/height occurrence dictionary and verify a live compatible source token for every selected repair incidence, or discharge the returned exact failure.