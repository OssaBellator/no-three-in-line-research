# Alternating-core synchronized repeated-touch amortization

## Status

This note proves AC5hf--AC5hi under the synchronized queue-revalidation contracts through AC5he and the six side-track repeated-touch contracts. It does not construct physical ranks, payments, reset tokens, repair maps, or replenishment, prove AC6, or prove the no-three-in-line conjecture.

## Setup

Each active FIFO head repair `e` has fixed track type `s(e)`, complete global footprint `F(e)`, service-window bound `W_e`, one unmatched owner incidence, and one reserved free token. Every blocked service window contains at least one macro edit touching `F(e)`.

The synchronized occurrence router assigns each blocked head-window to one actual touched global primitive and exactly one class:

- typed payment in the ledger of `s(e)`;
- strict decrease of a declared nonnegative integer primitive rank;
- consumption of a funded reset token, resetting the rank to at most its ceiling;
- unclassified failure.

One head-window is counted once. A physical edit occurrence that interrupts several heads must carry the corresponding declared multi-use capacity; cross-track payment and hidden duplication are forbidden.

## AC5hf -- exact synchronized interruption decomposition -- PROVED UNDER THE CLASSIFICATION CONTRACTS

For each head `e`, let `B_e` be its blocked-window count, `p_{e,x},d_{e,x},s_{e,x}` its classified counts, and `u_e` its unclassified count. Then

\[
\boxed{B_e=\sum_{x\in F(e)}(p_{e,x}+d_{e,x}+s_{e,x})+u_e.}
\]

Summing over distinct admitted jobs through epoch `J`,

\[
\boxed{B_J=P_J+D_J+S_J+U_J^{\rm bad}.}
\]

Here `P_J=sum_s P_{s,J}` is a disjoint sum of typed payments. If `U_J^{bad}>0`, return the first unclassified track, job, service block, edit occurrence, and touched primitive. A payment occurrence exceeding its declared physical capacity is also returned exactly.

## AC5hg -- trackwise rank-reset amortization -- PROVED UNDER THE RANK CONTRACTS

For job `e` and primitive `x`, let `r_{e,x}^0` be head-entry rank, `R_{e,x}` the reset ceiling, and `S_{e,x}` the funded reset allowance. Then

\[
\boxed{d_{e,x}\le r_{e,x}^0+R_{e,x}s_{e,x}.}
\]

Define the structural allowance

\[
Q(e)=\sum_{x\in F(e)}\bigl(r_{e,x}^0+(R_{e,x}+1)S_{e,x}\bigr).
\]

On the classified branch,

\[
\boxed{P(e)\ge\max\{0,B_e-Q(e)\}.}
\]

Therefore, with `Q_J=sum_eQ(e)`,

\[
\boxed{P_J\ge\max\{0,B_J-Q_J\}.}
\]

No reset token, rank unit, or paid-touch unit may move between tracks or between unrelated resource coordinates.

## AC5hh -- synchronized amortized service envelope -- PROVED UNDER THE ORIGIN CONTRACT

Let `E_{s,J}` be the distinct jobs first admitted to track `s`, `A_{s,J}=|E_{s,J}|`, `P_{s,J}=sum_{e in E_{s,J}}P(e)`, and `Q_{s,J}=sum_{e in E_{s,J}}Q(e)`. Each job contributes one successful service block and at most `P(e)+Q(e)` blocked blocks. Thus track `s` uses at most

\[
\boxed{A_{s,J}+P_{s,J}+Q_{s,J}}
\]

head-service blocks. Hence total repair-service microsteps are at most

\[
\boxed{\sum_s W_s\bigl(A_{s,J}+P_{s,J}+Q_{s,J}\bigr),}
\]

where `W_s` bounds service windows on track `s`.

Queue-origin conservation gives

\[
\sum_sA_{s,J}\le\Delta_0+\sum_{j=1}^JU_j.
\]

If `Q(e)<=Q_*` and `W_s<=W_*`, then

\[
\boxed{T_J\le W_*\left(P_J+(Q_*+1)\left(\Delta_0+\sum_{j=1}^JU_j\right)\right).}
\]

Repeated polling, revalidation, reserve checks, and track-local signature refresh do not create jobs, payment, rank, or reset allowance.

## AC5hi -- finite recurrence or typed payment router -- PROVED UNDER THE MACRO CONTRACT

Consider a macro interval in which initial deficit, total support-local disturbance, total issued structural allowance, and total paid-touch capacity are finite. Then AC5hh bounds all queue-head service microsteps on that interval. Consequently queue delay cannot recur infinitely without one of the following:

1. synchronized assignments complete;
2. one track-key has a numerical token shortage;
3. footprint-local repairs execute and lower synchronized deficit;
4. a typed paid-touch ledger grows by the displayed occurrence-faithful amount;
5. a declared primitive rank strictly decreases;
6. a funded reset token is consumed;
7. support-local disturbance or reset issuance exceeds its declared finite budget;
8. an unclassified touch, over-capacity payment, illegal rank increase, unfunded reset, stale certificate, or cross-track transfer is returned.

In particular, on a finite recurrent macro-state set with uniformly bounded structural allowance and paid-touch capacity, infinite queue delay is impossible unless the recurrence produces an explicit resource payment or a named contract violation.

## Corrected AC6 frontier

Synchronized repair now has bounded overlap, cost, waiting, revalidation, and repeated-touch amortization. Remaining work is to construct the seven physical primitive ranks, reset sources, and paid-touch ledgers; prove uniform `Q_*` and physical occurrence capacities; and show every accumulated payment or exhausted budget forces reset, replenishment, or strict finite macro-state descent.

## Finite check

`scripts/verify_ac_synchronized_repeated_touch_amortization.py` checks seven-track exact decompositions, rank-reset allowances, typed payment lower bounds, origin-funded admissions, and the synchronized waiting envelope on 1,500 generated systems.