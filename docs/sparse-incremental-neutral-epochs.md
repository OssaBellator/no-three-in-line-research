# Sparse algebraic incremental boundary-neutral epochs

## Status

This note proves SAS5mx--SAS5nb under the exact pair/completion compatibility and boundary-neutral one-use contracts through SAS5mw. It does not construct the concrete boundary-neutral predicate, prove SAS6, or prove the no-three-in-line conjecture.

## Setup

At one sparse repair epoch let `R` be the selected pair/completion incidences, `T` the live boundary-neutral tokens, and `E={(r,t):Compat(r,t)}` the exact dictionary computed from complete sign, profile, move, legality, boundary, source, epoch, occurrence and repair-class addresses. Let `d:R->T` be an injective compatible assignment.

At the next epoch write `R'=R^circ sqcup Delta R` and `T'=T^circ sqcup Delta T`; unchanged records preserve every predicate input, orientation and physical occurrence identity.

## SAS5mx -- unchanged neutral compatibility persists -- PROVED

For every unchanged pair,

\[
\boxed{Compat'(r,t)=Compat(r,t).}
\]

The exact old dictionary is copied on the unchanged product.

## SAS5my -- boundary-only exact audit -- PROVED

Fresh evaluation is required exactly on

\[
\mathcal B=(\Delta R\times T')\sqcup(R^\circ\times\Delta T),
\]

with

\[
\boxed{|\mathcal B|=|\Delta R|\,|T'|+|R^\circ|\,|\Delta T|.}
\]

An exact old dictionary, copied unchanged block and exact boundary audit give the exact next dictionary.

## SAS5mz -- carried neutral-assignment disturbance -- PROVED

Restrict the old assignment to unchanged pair/completion incidences whose assigned neutral tokens remain unchanged. If `a=|Delta R|` and `b` counts unchanged incidences whose assigned token changed or disappeared, the carried matching leaves at most

\[
\boxed{u=a+b}
\]

incidences unmatched.

## SAS5na -- bounded reaugmentation or boundary-neutral Hall core -- PROVED

Exactly one continuation holds:

1. a complete pair/completion assignment exists and is reached in at most `u` augmenting paths;
2. no complete assignment exists, the maximum deficit satisfies `1<=delta<=u`, and the preceding typed boundary-neutral Hall theorem returns its canonical core and missing rectangle;
3. one supposedly unchanged sign, profile, move, legality, boundary, epoch, occurrence or predicate field is false.

The proof is the carried-matching count and the one-edge gain of each augmentation.

## SAS5nb -- recurrent sparse-repair router -- PROVED UNDER THE EPOCH CONTRACT

Across sparse repair epochs, exact dictionaries and compatible neutral assignments require at most `sum_j |B_j|` new compatibility evaluations and `sum_j u_j` augmenting paths. Matching maintenance creates no neutral pair/completion mass and does not change orientation payment; actual debits remain governed by the neutral conservation ledger.

The least failure is a boundary discrepancy, false unchanged declaration, omitted legality field, stale epoch, relabelled move or profile, repeated debit, hidden deposit, or canonical Hall core of deficit at most the current churn.

## Corrected SAS6 frontier

Recurrent boundary-neutral assignment is now charged to changed typed records rather than the full pair-token product. Remaining work is to bound sparse move churn, evaluate the concrete neutral predicate on boundary pairs, and discharge returned Hall cores or lineage failures.

## Finite check

`scripts/verify_sas_incremental_neutral_epochs.py` checks unchanged persistence, exact boundary reconstruction, carried assignment persistence, and the churn bound on new deficit.