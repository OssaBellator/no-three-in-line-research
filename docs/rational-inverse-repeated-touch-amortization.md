# Rational-inverse repeated-touch amortization

## Status

This note proves RI5ic--RI5if under the complete-footprint queue-revalidation and service contracts through RI5ib. It does not construct the arithmetic rank, payment, reset, repair, or replenishment mechanisms, prove RI6, or prove the no-three-in-line conjecture.

## Setup

Fix a validated FIFO head repair job `e` with complete footprint `F(e)` and service-window length `W`. Write `h=|F(e)|`. Every service block in which `e` remains pending contains at least one declared touch of `F(e)` by RI5ib.

The occurrence-faithful interruption router assigns each blocked service window to one actual touched primitive `x in F(e)` and exactly one class:

- `pay`: the touch deposits one unit in a named collateral, blocker, owner, arithmetic, charge, or boundary payment ledger;
- `descend`: the touch decreases a declared nonnegative integer rank `r_x` by at least one;
- `reset`: the touch consumes one declared reset token and resets `r_x` to a value at most its ceiling `R_x`;
- `unclassified`: no valid payment, rank descent, or funded reset is declared.

No blocked window may be charged twice.

## RI5ic -- exact interruption decomposition -- PROVED UNDER THE CLASSIFICATION CONTRACT

For `B` blocked service windows let `p_x,d_x,s_x` be the numbers assigned to primitive `x` as payment, descent, and reset, and let `u` be the number of unclassified windows. Then

\[
\boxed{B=\sum_{x\in F(e)}(p_x+d_x+s_x)+u.}
\]

If `u>0`, the first unclassified window, its macro edit, touched primitive, and missing classification are returned as a rigid interruption-certificate failure. Hence on the valid branch `u=0`.

The payment count

\[
P(e)=\sum_x p_x
\]

is occurrence-faithful: one physical touch occurrence can pay only the capacity explicitly assigned to it by the RI resource ledger.

## RI5id -- rank-reset amortization -- PROVED UNDER THE RANK AND RESET CONTRACTS

Let `r_x^0` be the rank when `e` becomes head. Every descent consumes one rank unit. A reset may restore at most `R_x` further rank units. Therefore

\[
\boxed{d_x\le r_x^0+R_xs_x.}
\]

Consequently, on the classified branch,

\[
B\le P(e)+\sum_x r_x^0+\sum_x(R_x+1)s_x.
\]

If primitive `x` has at most `S_x` funded reset tokens while `e` is head, define

\[
Q(e)=\sum_{x\in F(e)}\bigl(r_x^0+(R_x+1)S_x\bigr).
\]

Then

\[
\boxed{P(e)\ge \max\{0,B-Q(e)\}.}
\]

Thus every interruption beyond the certified finite rank-reset allowance produces explicit RI payment.

A rank increase without a reset token, a reset above `R_x`, or reuse of a spent reset token is returned as the first exact contract failure.

## RI5ie -- bounded service or accumulated payment -- PROVED UNDER THE SERVICE CONTRACT

If the available paid-touch budget for this head is at most `Pi(e)`, then

\[
B\le \Pi(e)+Q(e).
\]

The next unblocked service window executes the job, so the head is serviced within at most

\[
\boxed{W\bigl(\Pi(e)+Q(e)+1\bigr)}
\]

repair microsteps.

Equivalently, if the head survives `B` blocked service windows, it has already returned at least `B-Q(e)` units of named RI payment. In the zero-payment branch it executes within `W(Q(e)+1)` microsteps.

## RI5if -- queue-wide amortized waiting envelope -- PROVED UNDER THE ORIGIN AND OCCURRENCE CONTRACTS

Through macro epoch `J`, let `E_J` be the set of distinct jobs first admitted, `A_J=|E_J|`, `P_J=sum_{e in E_J}P(e)`, and `Q_J=sum_{e in E_J}Q(e)`. Every admitted job contributes one successful service block and at most `P(e)+Q(e)` blocked blocks. Hence total FIFO-head service blocks are at most

\[
\boxed{A_J+P_J+Q_J.}
\]

Using queue-origin conservation,

\[
A_J\le \Delta_0+\sum_{j=1}^JU_j.
\]

If every job satisfies `Q(e)<=Q_*` and all service windows have length at most `W_*`, total repair-service microsteps are at most

\[
\boxed{W_*\left(P_J+(Q_*+1)\left(\Delta_0+\sum_{j=1}^JU_j\right)\right).}
\]

One exact continuation holds: the queue drains; a numerical collateral shortage occurs; a repair or reserve certificate fails; a named RI payment is produced; a primitive rank descends; a funded reset is consumed; or the first unclassified/over-budget touch is returned. No retry, signature refresh, or queue revalidation creates payment or structural allowance.

## Corrected RI6 frontier

Repeated queue interruption is now amortized by explicit payment, bounded rank descent, and funded reset consumption. Remaining work is to define the actual RI primitive ranks and reset tokens, prove finite `Q_*`, prove paid-touch capacity, and convert the payment ledger into arithmetic/geometric progress or a finite macro-state descent.

## Finite check

`scripts/verify_ri_repeated_touch_amortization.py` checks exact interruption decomposition, rank-reset bounds, payment lower bounds, bounded service, queue-origin funding, and unclassified-touch routing on 2,500 generated systems.