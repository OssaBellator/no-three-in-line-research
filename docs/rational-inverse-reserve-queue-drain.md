# Rational-inverse reserve queue drain

## Status

This note proves RI5hu--RI5hx under the footprint-costed repair contracts through RI5ht. It does not construct the arithmetic replenishment mechanism, prove RI6, or prove the no-three-in-line conjecture.

## Setup

A validated RI repair job is one footprint-local unmatched-incidence/free-collateral repair whose execution lowers collateral deficit by one and has a nonnegative typed cost vector `c(e)`. Jobs are stored in FIFO order. Each queued job owns one distinct unmatched repair incidence and retains its epoch, support, key, predicate, witness and footprint signatures.

For each typed RI resource coordinate `a`, let `K_a` be storage capacity and let

\[
\kappa_a=\max_e c(e)_a.
\]

The reserve is replenished between repair microsteps. A head job executes as soon as its whole cost vector is available.

## RI5hu -- capacity or oversized repair -- PROVED

If some queued job has `c(e)_a>K_a`, return the least such coordinate and the exact excess

\[
\boxed{c(e)_a-K_a>0.}
\]

Otherwise every job fits in the reserve coordinatewise. No splitting across epochs or borrowing from another RI resource coordinate is permitted.

## RI5hv -- replenishment-window head service -- PROVED UNDER THE WINDOW CONTRACT

Assume that, while one fixed job remains at the head, every consecutive `W_a` repair microsteps replenish coordinate `a` by at least `\kappa_a`, and `K_a\ge\kappa_a`. Put

\[
W=\max_a W_a.
\]

No later job spends reserve before the head. Hence within at most `W_a` steps coordinate `a` reaches at least `\kappa_a`, with capacity truncation harmless because `K_a\ge\kappa_a`. Therefore the head job is feasible and executes within at most `W` microsteps.

A FIFO queue of `n` valid jobs consequently drains within

\[
\boxed{nW}
\]

repair microsteps and lowers collateral deficit by exactly `n` in total.

If the window contract fails, return the least coordinate `a` and least interval of length `W_a` with exact replenishment shortfall

\[
\boxed{\kappa_a-\sum r_{t,a}>0.}
\]

## RI5hw -- queue-origin conservation -- PROVED UNDER THE ORIGIN CONTRACT

Let `A_J` be the number of distinct jobs first admitted through macro epoch `J`, `Delta_0` the initial collateral deficit, and `U_j` the support-local matching disturbance at epoch `j`.

Every first job owns a distinct initial unmatched incidence or an incidence newly unmatched by a declared disturbance. A previously executed incidence may be queued again only after a new disturbance. Therefore

\[
\boxed{A_J\le \Delta_0+\sum_{j=1}^J U_j.}
\]

The active queue size is at most the current deficit. Combining with RI5hv, total head-service waiting over all admitted jobs is at most

\[
\boxed{WA_J\le W\left(\Delta_0+\sum_{j=1}^J U_j\right).}
\]

Repeated retries do not create new jobs or new collateral debt.

## RI5hx -- reserve-queue drain or persistent shortage router -- PROVED UNDER THE QUEUE CONTRACTS

One exact continuation holds:

1. the collateral assignment is complete;
2. one collateral key has a direct numerical token shortage;
3. one repair job exceeds a typed storage capacity;
4. the FIFO queue drains, with one unit of collateral-deficit descent per executed job;
5. one typed replenishment window has the displayed exact shortfall;
6. one queued job has a stale epoch, owner, support, key, predicate, witness or footprint signature, or its repair certificate fails.

For a frozen physical state, if every positive deficit produces a valid queued job and the capacity and replenishment-window contracts hold, repair terminates after at most `W Delta_0` microsteps. Across changing states, all admitted service is funded by initial deficit and declared physical churn.

## Corrected RI6 frontier

RI now has bounded waiting as well as bounded repair cost. Remaining work is to construct the physical replenishment process, prove numerical capacities and window lengths, revalidate queued jobs across macro changes, and turn persistent typed shortages into arithmetic or geometric payment.

## Finite check

`scripts/verify_ri_reserve_queue_drain.py` checks FIFO service, capacity witnesses, replenishment-window failures, queue-origin conservation and the `nW` drain bound on 2,500 generated systems.