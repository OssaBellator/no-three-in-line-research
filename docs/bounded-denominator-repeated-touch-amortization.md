# Bounded-denominator repeated-touch amortization

## Status

This note proves BDA5il--BDA5io under the restoration queue-revalidation contracts through BDA5ik. It does not construct physical restoration ranks, resets, payments, repairs, or replenishment, prove BDA6, or prove the no-three-in-line conjecture.

## Setup

Fix a validated FIFO head restoration job `e` with complete footprint `F(e)` and service window `W`. Every blocked service window contains a declared touch of a context cell, restoration gate, source, gain/damping field, line record, owner occurrence, arithmetic certificate, occurrence record, or boundary resource in `F(e)`.

Route each blocked window occurrence-faithfully to one touched primitive and exactly one class: typed restoration payment, strict decrease of a nonnegative primitive rank, consumption of a funded reset token, or unclassified failure.

## BDA5il -- exact restoration-interruption decomposition -- PROVED UNDER THE CLASSIFICATION CONTRACT

For blocked-window count `B`, let `p_x,d_x,s_x` be the payment, descent, and reset counts assigned to primitive `x`, and let `u` be the unclassified count. Then

\[
\boxed{B=\sum_{x\in F(e)}(p_x+d_x+s_x)+u.}
\]

If `u>0`, return the first unclassified restoration touch and its missing payment/rank/reset certificate. Otherwise `u=0` and `P(e)=sum_x p_x` is the exact paid-touch count. One physical touch may carry only its declared occurrence capacity.

## BDA5im -- restoration rank-reset amortization -- PROVED UNDER THE RANK CONTRACT

Let `r_x^0` be the initial rank, `R_x` the post-reset ceiling, and `S_x` the funded reset-token allowance while `e` is head. Every descent consumes one rank unit and every reset restores at most `R_x` units, so

\[
\boxed{d_x\le r_x^0+R_xs_x.}
\]

Define

\[
Q(e)=\sum_{x\in F(e)}\bigl(r_x^0+(R_x+1)S_x\bigr).
\]

Then

\[
\boxed{P(e)\ge\max\{0,B-Q(e)\}.}
\]

An unfunded reset, rank increase without reset, reset above `R_x`, or double use of one restoration token is an exact contract failure.

## BDA5in -- bounded restoration service or payment -- PROVED UNDER THE SERVICE CONTRACT

If the available paid-touch budget for the head is at most `Pi(e)`, then `B<=Pi(e)+Q(e)`. Hence the next untouched service window executes the job within

\[
\boxed{W\bigl(\Pi(e)+Q(e)+1\bigr)}
\]

microsteps. Equivalently, survival through `B` blocked windows returns at least `B-Q(e)` units of named gate/source/gain/damping/line/arithmetic restoration payment.

## BDA5io -- queue-wide restoration waiting envelope -- PROVED UNDER THE ORIGIN CONTRACT

Through epoch `J`, let `E_J` be the distinct admitted jobs, `A_J=|E_J|`, `P_J=sum_e P(e)`, and `Q_J=sum_e Q(e)`. Total head-service blocks are at most

\[
\boxed{A_J+P_J+Q_J.}
\]

Because

\[
A_J\le\Delta_0+\sum_{j=1}^JU_j,
\]

if `Q(e)<=Q_*` and service windows are at most `W_*`, total restoration-service microsteps are bounded by

\[
\boxed{W_*\left(P_J+(Q_*+1)\left(\Delta_0+\sum_{j=1}^JU_j\right)\right).}
\]

One exact continuation holds: queue service, numerical potential shortage, typed restoration payment, primitive-rank descent, funded reset, or the first unclassified/over-budget/invalid restoration touch. Revalidation and retry do not create payment or structural allowance.

## Corrected BDA6 frontier

Repeated restoration interruption is now amortized. Remaining work is to define the actual restoration ranks, reset sources, paid-touch ledgers, and uniform `Q_*`, then prove that payment forces rational-gain progress, resource exhaustion, or reset/descent.

## Finite check

`scripts/verify_bda_repeated_touch_amortization.py` checks 2,500 generated restoration systems.