# Alternating-core synchronized reserve queue drain

## Status

This note proves AC5gx--AC5ha under the synchronized footprint-costed repair contracts through AC5gw and the six side-track reserve-queue contracts. It does not construct physical replenishment, prove AC6, or prove the no-three-in-line conjecture.

## Setup

Each track `s` in AC, RI, BDA, GC, OP, SRR and SAS has a FIFO queue of validated footprint-local unmatched-incidence/free-token repair jobs. Every job:

- has fixed track type `s`;
- owns one distinct currently unmatched incidence;
- retains its epoch, support, key, predicate, witness and global-footprint signatures;
- lowers synchronized matching deficit by one when executed;
- has a nonnegative cost vector supported only on the typed ledger of `s`.

For track-coordinate `(s,a)`, let `K_{s,a}` be storage capacity and `kappa_{s,a}` the maximum cost of one queued job.

## AC5gx -- typed capacity or oversized queued repair -- PROVED

If a queued job has

\[
c(e)_{s,a}>K_{s,a},
\]

return the least typed coordinate and exact excess `c(e)_{s,a}-K_{s,a}`. Otherwise every job fits in its own track reserve. Splitting one job across incompatible epochs or borrowing across tracks is forbidden.

## AC5gy -- synchronized replenishment-window service -- PROVED UNDER THE WINDOW CONTRACTS

For track `s`, suppose that while one fixed job remains at its FIFO head, every consecutive `W_{s,a}` repair microsteps replenish coordinate `(s,a)` by at least `kappa_{s,a}`, with `K_{s,a}>=kappa_{s,a}`. Put

\[
W_s=\max_a W_{s,a},\qquad W_*=\max_s W_s.
\]

No later job on track `s` spends before the head. Hence that head executes within `W_s` microsteps. If track `s` has `n_s` valid queued jobs, its queue drains within `n_sW_s` service microsteps. A globally serial schedule therefore drains all current queues within

\[
\boxed{\sum_s n_sW_s\le W_*\sum_s n_s.}
\]

Every executed job lowers synchronized deficit by one. If a window contract fails, return the least typed coordinate and least interval with exact shortfall

\[
\boxed{\kappa_{s,a}-\sum r_{t,s,a}>0.}
\]

## AC5gz -- synchronized queue-origin conservation -- PROVED UNDER THE ORIGIN CONTRACT

Let `A_{s,J}` be cumulative first admissions to track `s`, `Delta_0` initial synchronized deficit and `U_j` synchronized support-local disturbance.

Every first admission owns one distinct initial unmatched incidence or an incidence newly unmatched by declared physical disturbance. A previously executed incidence may be admitted again only after a new disturbance, and moving a job between tracks is forbidden. Therefore

\[
\boxed{\sum_s A_{s,J}\le\Delta_0+\sum_{j=1}^J U_j.}
\]

The total active queue size is at most current synchronized deficit. Total typed head-service waiting satisfies

\[
\boxed{\sum_s W_sA_{s,J}
\le W_*\left(\Delta_0+\sum_{j=1}^J U_j\right).}
\]

Repeated reserve checks do not create new repair debt.

## AC5ha -- finite drain or persistent typed shortage router -- PROVED UNDER THE QUEUE AND GENERATION CONTRACTS

One exact continuation holds:

1. every repair assignment is complete;
2. one track-key has a direct numerical token shortage;
3. one queued job exceeds a typed storage capacity;
4. one or more FIFO jobs execute, with exact synchronized-deficit descent equal to the executed count;
5. one typed replenishment window has the displayed persistent shortfall;
6. one queued job is stale in epoch, owner, support, key, predicate, witness, footprint or track type, or its repair certificate fails.

For a frozen physical state, assume every positive synchronized deficit that is not a numerical shortage or rigid repair failure generates at least one validated queued job. Then, under the capacity and replenishment-window contracts, repeated queue service terminates after at most

\[
\boxed{W_*\Delta_0}
\]

repair microsteps: each executed job lowers the nonnegative integer deficit by one. Across changing macro states, cumulative admitted service remains bounded by initial deficit plus declared physical churn.

## Corrected AC6 frontier

Synchronized repair now has bounded cost, bounded overlap and bounded waiting. Remaining work is to construct the seven physical replenishment mechanisms, prove typed capacities and windows, revalidate jobs across macro changes, convert persistent shortages into payment/reset/descent, and combine the finite drain theorem with macro-state recurrence.

## Finite check

`scripts/verify_ac_synchronized_reserve_queue_drain.py` generates 1,500 seven-track queue systems and checks typed capacities, per-track service windows, frozen-state drain bounds, queue-origin conservation and exact persistent-shortage witnesses.