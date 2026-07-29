# Bounded-denominator incremental repair-potential epochs

## Status

This note proves BDA5ha--BDA5he under the exact repair-potential compatibility and one-use potential contracts through BDA5gz. It does not construct the rational-gain compatibility predicate, prove BDA6, or prove the no-three-in-line conjecture.

## Setup

At one restoration epoch let `R` be the selected repair incidences, `T` the live potential-source tokens, and `E={(r,t):Compat(r,t)}` the exact dictionary computed from complete source, gain, damping, arithmetic, owner, epoch, occurrence and restoration-gate addresses. Let `d:R->T` be an injective compatible assignment.

At the next epoch write `R'=R^circ sqcup Delta R` and `T'=T^circ sqcup Delta T`, where the unchanged records preserve every predicate input and physical identity.

## BDA5ha -- unchanged potential compatibility persists -- PROVED

For `r in R^circ` and `t in T^circ`,

\[
\boxed{Compat'(r,t)=Compat(r,t).}
\]

The old dictionary is therefore copied on the unchanged product.

### Proof

The deterministic predicate and every retained source/gain/damping input are unchanged. QED.

## BDA5hb -- boundary-only exact audit -- PROVED

Fresh evaluation is required exactly on

\[
\mathcal B=(\Delta R\times T')\sqcup(R^\circ\times\Delta T),
\]

and

\[
\boxed{|\mathcal B|=|\Delta R|\,|T'|+|R^\circ|\,|\Delta T|.}
\]

An exact old dictionary, copied unchanged block and exact boundary audit give an exact next dictionary.

### Proof

The next pair product is the disjoint union of the unchanged block and the displayed boundary. QED.

## BDA5hc -- carried potential assignment disturbance -- PROVED

Restrict `d` to unchanged incidences whose assigned potential tokens remain unchanged. With

\[
a=|\Delta R|,
\qquad
b=|\{r\in R^\circ:d(r)\notin T^\circ\}|,
\]

the carried matching leaves at most

\[
\boxed{u=a+b}
\]

incidences unmatched.

### Proof

Restriction preserves injectivity and BDA5ha preserves each retained edge. Count new incidences and old assignments whose tokens changed. QED.

## BDA5hd -- bounded reaugmentation or potential Hall core -- PROVED

Exactly one continuation holds:

1. a complete potential assignment exists and is reached in at most `u` augmenting paths;
2. no complete assignment exists, the maximum deficit satisfies `1<=delta<=u`, and the preceding arithmetic source-compatibility Hall theorem returns its canonical core and missing rectangle;
3. one supposedly unchanged source, gain, damping, gate, epoch, occurrence or arithmetic field is false.

### Proof

The carried matching is at most `u` edges short of saturation. Every successful augmentation adds one edge; if saturation is impossible, the carried matching bounds the maximum deficit by `u`. QED.

## BDA5he -- recurrent restoration-epoch router -- PROVED UNDER THE EPOCH CONTRACT

Across restoration epochs, exact dictionaries and assignments require at most `sum_j |B_j|` new compatibility evaluations and `sum_j u_j` augmenting paths. Carrying or augmenting a proposed assignment creates no gain or potential mass; actual debits remain governed by the existing one-use conservation ledger.

The least failure is a boundary edge discrepancy, false unchanged declaration, stale gate or epoch, relabelled arithmetic address, repeated debit, hidden deposit, or canonical Hall core of deficit at most the current churn.

## Corrected BDA6 frontier

Recurrent repair-potential assignment is charged to changed typed records rather than the complete source-incidence product. Remaining work is to prove bounded restoration-gate churn, evaluate rational-gain compatibility on the boundary, and discharge returned arithmetic Hall cores.

## Finite check

`scripts/verify_bda_incremental_potential_epochs.py` checks exact boundary reconstruction, carried matching persistence, and the churn bound on new maximum-matching deficit.