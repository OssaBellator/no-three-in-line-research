# Sparse algebraic repeated-touch amortization

## Status

This note proves SAS5oi--SAS5ol under the sparse queue-revalidation contracts through SAS5oh. It does not construct sparse ranks, payments, reset tokens, repair maps, or replenishment, prove SAS6, or prove the no-three-in-line conjecture.

## Setup

Fix a validated FIFO head pair/completion-to-free-neutral repair `e`, complete footprint `F(e)`, and service window `W`. Every blocked service window touches a declared row or cell, swap position, arithmetic-profile field, orientation record, legality guard, boundary record, owner occurrence, neutral record, lineage field, or repair slot.

Assign each blocked window occurrence-faithfully to one touched primitive and exactly one class: typed sparse payment, strict decrease of a nonnegative primitive rank, funded reset consumption, or unclassified failure.

## SAS5oi -- exact sparse-interruption decomposition -- PROVED UNDER THE CLASSIFICATION CONTRACT

For blocked count `B`, counts `p_x,d_x,s_x`, and unclassified count `u`,

\[
\boxed{B=\sum_{x\in F(e)}(p_x+d_x+s_x)+u.}
\]

If `u>0`, return the first row/swap/profile/orientation/legality/boundary/lineage touch lacking a valid payment, rank, or reset certificate. Otherwise `P(e)=sum_xp_x` is the exact occurrence-faithful sparse payment count.

## SAS5oj -- sparse rank-reset amortization -- PROVED UNDER THE RANK CONTRACT

Let `r_x^0` be head-entry rank, `R_x` the reset ceiling, and `S_x` the funded reset allowance. Then

\[
\boxed{d_x\le r_x^0+R_xs_x.}
\]

Define

\[
Q(e)=\sum_{x\in F(e)}\bigl(r_x^0+(R_x+1)S_x\bigr).
\]

On the classified branch,

\[
\boxed{P(e)\ge\max\{0,B-Q(e)\}.}
\]

Any rank increase without a funded reset, reset above `R_x`, reused reset token, hidden lineage reset, or cross-ledger orientation payment is an exact sparse contract failure.

## SAS5ok -- bounded sparse service or accumulated payment -- PROVED UNDER THE SERVICE CONTRACT

If the paid-touch budget for the head is at most `Pi(e)`, then `B<=Pi(e)+Q(e)`, so the next untouched service window executes the job within

\[
\boxed{W\bigl(\Pi(e)+Q(e)+1\bigr)}
\]

microsteps. Conversely, survival through `B` blocked windows returns at least `B-Q(e)` units of named row, profile, orientation, legality, boundary, neutral, owner, occurrence, or lineage payment.

## SAS5ol -- queue-wide sparse waiting envelope -- PROVED UNDER THE ORIGIN CONTRACT

For distinct admitted jobs `E_J`, let `A_J=|E_J|`, `P_J=sum_eP(e)`, and `Q_J=sum_eQ(e)`. Total head-service blocks are at most

\[
\boxed{A_J+P_J+Q_J.}
\]

Since `A_J<=Delta_0+sum_jU_j`, if `Q(e)<=Q_*` and service windows are at most `W_*`, total sparse-service microsteps are bounded by

\[
\boxed{W_*\left(P_J+(Q_*+1)\left(\Delta_0+\sum_{j=1}^JU_j\right)\right).}
\]

One continuation holds: neutral assignment completes; a numerical neutral shortage occurs; a repair executes; a named sparse or lineage payment is produced; a rank descends; a funded reset is consumed; or the first unclassified/invalid sparse touch is returned. Revalidation cannot mint payment or structural allowance.

## Corrected SAS6 frontier

Repeated sparse interruption is now amortized. Remaining work is to define row/profile/orientation/legality/lineage ranks, reset tokens, paid-touch ledgers, and a uniform `Q_*`, then prove accumulated payment forces neutral/orientation progress, reset, or finite recurrence descent.

## Finite check

`scripts/verify_sas_repeated_touch_amortization.py` checks 2,500 generated systems.