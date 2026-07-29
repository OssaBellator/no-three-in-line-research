# Geometric-cleaning incremental donor epochs

## Status

This note proves GC2ly--GC2mc under the exact donor/remedy/height compatibility and occurrence-faithful source contracts through GC2lx. It does not construct the geometric compatibility predicate, prove GC5, or prove the no-three-in-line conjecture.

## Setup

At one cleaning epoch let `R` be the selected remedy incidences, `T` the live donor-source tokens, and `E={(r,t):Compat(r,t)}` the exact dictionary computed from complete donor, remedy, height, geometric source, certificate, defect, epoch, occurrence and repair-class addresses. Let `d:R->T` be an injective compatible assignment.

At the next epoch write `R'=R^circ sqcup Delta R` and `T'=T^circ sqcup Delta T`, where unchanged records preserve every compatibility input and physical identity.

## GC2ly -- unchanged donor compatibility persists -- PROVED

For every unchanged incidence-token pair,

\[
\boxed{Compat'(r,t)=Compat(r,t).}
\]

Hence the old exact dictionary is copied on `R^circ x T^circ`.

## GC2lz -- boundary-only exact audit -- PROVED

Fresh evaluation is required exactly on

\[
\mathcal B=(\Delta R\times T')\sqcup(R^\circ\times\Delta T),
\]

with

\[
\boxed{|\mathcal B|=|\Delta R|\,|T'|+|R^\circ|\,|\Delta T|.}
\]

The copied unchanged block plus an exact boundary audit gives the exact next dictionary.

## GC2ma -- carried donor assignment disturbance -- PROVED

Restrict `d` to unchanged incidences whose assigned donors remain unchanged. If `a=|Delta R|` and `b` is the number of unchanged incidences whose old donor left the unchanged token set, then the carried matching leaves at most

\[
\boxed{u=a+b}
\]

incidences unmatched.

## GC2mb -- bounded reaugmentation or geometric Hall core -- PROVED

Exactly one continuation holds:

1. at most `u` augmenting paths restore a complete donor assignment;
2. no complete assignment exists, its deficit satisfies `1<=delta<=u`, and the preceding geometric source-compatibility theorem returns its canonical donor/remedy Hall core and missing rectangle;
3. one supposedly unchanged donor, remedy, height, source, epoch, occurrence or predicate field is false.

The proof is the carried-matching count: each augmentation adds one matched incidence, while the carried matching is at most `u` short of saturation.

## GC2mc -- recurrent cleaning-epoch router -- PROVED UNDER THE EPOCH CONTRACT

Across cleaning epochs, exact dictionaries and compatible donor assignments require at most `sum_j |B_j|` new compatibility evaluations and `sum_j u_j` augmenting paths. Matching maintenance creates no donor mass and does not alter height accounting; actual debits remain governed by the existing source-conservation ledger.

The least failure is a boundary discrepancy, false unchanged declaration, omitted geometric field, stale epoch, relabelled address, repeated donor debit, hidden deposit, or canonical Hall core of deficit at most the current churn.

## Corrected GC5 frontier

Recurrent donor assignment is now charged to changed geometric records rather than the full remedy-token product. Remaining work is to bound cleaning-menu churn, evaluate the geometric predicate on boundary pairs, and pay returned Hall cores or donor-ledger failures.

## Finite check

`scripts/verify_gc_incremental_donor_epochs.py` checks unchanged persistence, exact boundary reconstruction, carried matching persistence, and the churn bound on new deficit.