# Bounded-denominator reserve queue drain

## Status

This note proves BDA5id--BDA5ig under the footprint-costed restoration contracts through BDA5ic. It does not construct physical restoration replenishment, prove BDA6, or prove the no-three-in-line conjecture.

## Setup

Validated footprint-local restoration repairs are stored in a FIFO queue. Each job owns a distinct unmatched repair incidence, retains its epoch/support/key/predicate/witness signatures, lowers potential-assignment deficit by one when executed, and has a nonnegative typed cost vector `c(e)`.

For restoration coordinate `a`, let `K_a` be capacity and `kappa_a=max_e c(e)_a`.

## BDA5id -- capacity or oversized restoration job -- PROVED

If `c(e)_a>K_a`, return the least coordinate with exact excess `c(e)_a-K_a`. Otherwise every queued repair fits coordinatewise. Costs cannot be split across unrelated gate, source, gain, damping, line, owner, arithmetic or boundary ledgers.

## BDA5ie -- replenishment-window FIFO service -- PROVED UNDER THE WINDOW CONTRACT

While one job remains at the head, suppose every consecutive `W_a` microsteps replenish coordinate `a` by at least `kappa_a`, with `K_a>=kappa_a`. Put `W=max_a W_a`.

No later job spends before the head. Capacity truncation cannot prevent the reserve reaching `kappa_a`. Thus the head executes within `W` steps. A queue of `n` jobs drains within

\[
\boxed{nW}
\]

steps and lowers restoration deficit by `n`.

A failed window returns the least coordinate and interval with exact shortfall

\[
\boxed{\kappa_a-\sum r_{t,a}>0.}
\]

## BDA5if -- restoration queue-origin conservation -- PROVED UNDER THE ORIGIN CONTRACT

Let `A_J` be cumulative first admissions, `Delta_0` initial restoration deficit, and `U_j` support-local disturbance. Every admission owns a distinct initial unmatched incidence or one newly unmatched by a declared disturbance; requeue after execution requires new disturbance. Therefore

\[
\boxed{A_J\le\Delta_0+\sum_{j=1}^J U_j.}
\]

The active queue size is at most current deficit, and total head-service waiting is at most

\[
\boxed{WA_J\le W\left(\Delta_0+\sum_{j=1}^J U_j\right).}
\]

## BDA5ig -- restoration drain or persistent shortage router -- PROVED UNDER THE QUEUE CONTRACTS

One continuation holds: complete potential assignment; direct restoration-key shortage; oversized repair cost; FIFO drain with one deficit unit per job; least replenishment-window shortage; or stale epoch/support/key/predicate/witness/footprint data or a failed repair certificate.

For a frozen physical state, complete repair generation and valid capacity/window contracts imply termination within `W Delta_0` repair microsteps.

## Corrected BDA6 frontier

The restoration ledger now controls both expenditure and waiting. Remaining work is to construct physical replenishment, prove numerical capacities/windows, revalidate queued repairs across macro edits, and convert persistent shortages into rational-gain payment or reset.

## Finite check

`scripts/verify_bda_reserve_queue_drain.py` checks 2,500 generated FIFO restoration queues, drain bounds, capacity witnesses, window failures and origin conservation.