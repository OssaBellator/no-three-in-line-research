# Geometric-cleaning repeated-touch amortization

## Status

This note proves GC2nj--GC2nm under the queue-revalidation contracts through GC2ni. It does not construct geometric ranks, payments, reset tokens, repair maps, or replenishment, prove GC5, or prove the no-three-in-line conjecture.

## Setup

Fix a validated FIFO head unmatched-remedy/free-donor repair `e`, complete footprint `F(e)`, and service window `W`. Every blocked service window touches a declared moved cell, protected event, chart record, donor occurrence, remedy slot, height certificate, occurrence field, or boundary primitive.

Assign each blocked window occurrence-faithfully to one touched primitive and exactly one class: geometric payment, strict decrease of a nonnegative primitive rank, consumption of a funded reset token, or unclassified failure.

## GC2nj -- exact geometric-interruption decomposition -- PROVED UNDER THE CLASSIFICATION CONTRACT

For blocked count `B`, payment/descent/reset counts `p_x,d_x,s_x`, and unclassified count `u`,

\[
\boxed{B=\sum_{x\in F(e)}(p_x+d_x+s_x)+u.}
\]

If `u>0`, return the first unclassified chart/protected-event/donor/remedy/height/boundary touch and its missing certificate. Otherwise `P(e)=sum_x p_x` is the exact occurrence-faithful geometric payment count.

## GC2nk -- geometric rank-reset amortization -- PROVED UNDER THE RANK CONTRACT

Let `r_x^0` be the head-entry rank, `R_x` the post-reset ceiling, and `S_x` the funded reset allowance. Since each descent consumes one rank unit and each reset restores at most `R_x`,

\[
\boxed{d_x\le r_x^0+R_xs_x.}
\]

With

\[
Q(e)=\sum_{x\in F(e)}\bigl(r_x^0+(R_x+1)S_x\bigr),
\]

one has

\[
\boxed{P(e)\ge\max\{0,B-Q(e)\}.}
\]

A hidden rank increase, unfunded reset, reset above its ceiling, or reused reset token is an exact geometric contract failure.

## GC2nl -- bounded cleaning service or geometric payment -- PROVED UNDER THE SERVICE CONTRACT

If paid touches available to the head are bounded by `Pi(e)`, then `B<=Pi(e)+Q(e)`, and the next untouched service window executes the repair within

\[
\boxed{W\bigl(\Pi(e)+Q(e)+1\bigr)}
\]

microsteps. Conversely, surviving `B` blocked windows returns at least `B-Q(e)` units of named protected-height, chart, donor, remedy, occurrence, or boundary payment.

## GC2nm -- queue-wide cleaning waiting envelope -- PROVED UNDER THE ORIGIN CONTRACT

For distinct admitted jobs `E_J`, put `A_J=|E_J|`, `P_J=sum_eP(e)`, and `Q_J=sum_eQ(e)`. Total cleaning head-service blocks are at most

\[
\boxed{A_J+P_J+Q_J.}
\]

Using `A_J<=Delta_0+sum_jU_j`, if `Q(e)<=Q_*` and service windows are at most `W_*`, total service microsteps are at most

\[
\boxed{W_*\left(P_J+(Q_*+1)\left(\Delta_0+\sum_{j=1}^JU_j\right)\right).}
\]

Thus one continuation holds: donor assignment completes; a numerical donor shortage occurs; a repair executes; a named geometric payment is produced; a primitive rank descends; a funded reset is consumed; or the first unclassified/invalid geometric touch is returned.

## Corrected GC5 frontier

Repeated cleaning interruption is now amortized. Remaining work is to construct the chart/protected-event ranks and resets, prove uniform `Q_*`, and convert geometric paid touches into protected-height payment, reset, or monotone cleaning descent.

## Finite check

`scripts/verify_gc_repeated_touch_amortization.py` checks 2,500 generated systems.