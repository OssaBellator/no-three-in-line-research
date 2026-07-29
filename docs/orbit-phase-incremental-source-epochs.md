# Orbit-phase incremental repair-source epochs

## Status

This note proves OP4fx--OP4gb under the exact typed residual/edit source-compatibility and occurrence-faithful source contracts through OP4fw. It does not construct the unit-sensitive predicate, prove OP5, or prove the no-three-in-line conjecture.

## Setup

At one quotient-repair epoch let `R` be the selected residual/edit incidences, `T` the live source tokens, and `E={(r,t):Compat(r,t)}` the exact dictionary computed from complete residual/edit, unit, valuation, holonomy, quotient, owner, epoch, occurrence and repair-class addresses. Let `d:R->T` be an injective compatible assignment.

At the next epoch write `R'=R^circ sqcup Delta R` and `T'=T^circ sqcup Delta T`; unchanged records preserve every predicate input, physical identity and occurrence address.

## OP4fx -- unchanged unit-sensitive compatibility persists -- PROVED

For every unchanged pair,

\[
\boxed{Compat'(r,t)=Compat(r,t).}
\]

The exact old dictionary is copied on the unchanged product.

## OP4fy -- boundary-only exact audit -- PROVED

Fresh evaluation is required exactly on

\[
\mathcal B=(\Delta R\times T')\sqcup(R^\circ\times\Delta T),
\]

and

\[
\boxed{|\mathcal B|=|\Delta R|\,|T'|+|R^\circ|\,|\Delta T|.}
\]

The copied unchanged block plus an exact boundary audit gives the exact next dictionary.

## OP4fz -- carried source-assignment disturbance -- PROVED

Restrict the old assignment to unchanged incidences whose assigned tokens remain unchanged. If `a=|Delta R|` and `b` counts unchanged incidences whose assigned token changed or disappeared, the carried matching leaves at most

\[
\boxed{u=a+b}
\]

incidences unmatched.

## OP4ga -- bounded reaugmentation or unit-sensitive Hall core -- PROVED

Exactly one continuation holds:

1. a complete typed source assignment exists and is reached in at most `u` augmenting paths;
2. no complete assignment exists, the maximum deficit satisfies `1<=delta<=u`, and the preceding unit-sensitive Hall theorem returns its canonical residual/edit core and missing rectangle;
3. one supposedly unchanged quotient, unit, valuation, holonomy, epoch, occurrence or predicate field is false.

The proof is the carried-matching count and one-edge gain of each augmentation.

## OP4gb -- recurrent quotient-repair router -- PROVED UNDER THE EPOCH CONTRACT

Across quotient-repair epochs, exact dictionaries and assignments require at most `sum_j |B_j|` new compatibility evaluations and `sum_j u_j` augmenting paths. Matching maintenance creates no source mass, residual payment or edit credit; actual debits remain controlled by the typed source ledger.

The first failure is a boundary discrepancy, false unchanged declaration, omitted unit or holonomy field, stale epoch, relabelled quotient address, repeated debit, hidden deposit, or canonical Hall core of deficit at most the current churn.

## Corrected OP5 frontier

Recurrent typed source assignment is now charged to changed quotient records rather than the full compatibility product. Remaining work is to bound actual OP churn, evaluate the unit-sensitive predicate on boundary pairs, and discharge returned Hall cores or source-ledger failures.

## Finite check

`scripts/verify_op_incremental_source_epochs.py` checks unchanged persistence, exact boundary reconstruction, carried assignment persistence, and the churn bound on new deficit.