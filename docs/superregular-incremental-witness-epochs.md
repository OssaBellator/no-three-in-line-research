# Superregular incremental repair-witness epochs

## Status

This note proves SRR2fh--SRR2fl under the exact candidate/witness compatibility and occurrence-faithful witness contracts through SRR2fg. It does not construct the concrete conditioned predicate, prove SRR4, or prove the no-three-in-line conjecture.

## Setup

At one resampling epoch let `R` be the selected candidate incidences, `T` the live witness tokens, and `E={(r,t):Compat(r,t)}` the exact dictionary computed from complete candidate, witness, burden, threshold, conditioned-source, epoch, occurrence and repair-class addresses. Let `d:R->T` be an injective compatible assignment.

At the next epoch write `R'=R^circ sqcup Delta R` and `T'=T^circ sqcup Delta T`; unchanged records preserve every predicate input and physical occurrence identity.

## SRR2fh -- unchanged candidate-witness compatibility persists -- PROVED

For every unchanged pair,

\[
\boxed{Compat'(r,t)=Compat(r,t).}
\]

The old exact dictionary is copied on `R^circ x T^circ`.

## SRR2fi -- boundary-only exact audit -- PROVED

Fresh evaluation is required exactly on

\[
\mathcal B=(\Delta R\times T')\sqcup(R^\circ\times\Delta T),
\]

with

\[
\boxed{|\mathcal B|=|\Delta R|\,|T'|+|R^\circ|\,|\Delta T|.}
\]

An exact old dictionary, copied unchanged block and exact boundary audit give the exact next dictionary.

## SRR2fj -- carried witness-assignment disturbance -- PROVED

Restrict the old assignment to unchanged candidates whose assigned witnesses remain unchanged. If `a=|Delta R|` and `b` counts unchanged candidates whose assigned witness changed or disappeared, the carried matching leaves at most

\[
\boxed{u=a+b}
\]

candidates unmatched.

## SRR2fk -- bounded reaugmentation or conditioned Hall core -- PROVED

Exactly one continuation holds:

1. a complete candidate-witness assignment exists and is reached in at most `u` augmenting paths;
2. no complete assignment exists, the maximum deficit satisfies `1<=delta<=u`, and the preceding conditioned source-compatibility theorem returns its canonical burden core and missing rectangle;
3. one supposedly unchanged threshold, burden, conditioning, epoch, occurrence or predicate field is false.

The proof is the carried-matching count and the one-edge gain of every augmentation.

## SRR2fl -- recurrent witness-epoch router -- PROVED UNDER THE EPOCH CONTRACT

Across resampling epochs, exact dictionaries and compatible witness assignments require at most `sum_j |B_j|` new compatibility evaluations and `sum_j u_j` augmenting paths. Matching maintenance creates no witness mass and does not reduce endpoint burden; actual debits remain governed by witness conservation.

The least failure is a boundary discrepancy, false unchanged declaration, omitted conditioning field, stale epoch, relabelled candidate or witness address, repeated debit, hidden deposit, or canonical Hall core of deficit at most the current churn.

## Corrected SRR frontier

Recurrent candidate-witness assignment is now charged to changed typed records rather than the full compatibility product. Remaining work is to bound bounded-cycle menu churn, evaluate the conditioned predicate on boundary pairs, and discharge returned Hall cores or witness-ledger failures.

## Finite check

`scripts/verify_srr_incremental_witness_epochs.py` checks unchanged persistence, boundary reconstruction, carried matching persistence, and the churn bound on new deficit.