# Geometric-cleaning reserve queue drain

## Status

This note proves GC2nb--GC2ne under the footprint-costed cleaning contracts through GC2na. It does not construct geometric replenishment, prove GC5, or prove the no-three-in-line conjecture.

## Setup

Validated unmatched-remedy/free-donor repairs form a FIFO queue. Every job owns a distinct unmatched remedy incidence, retains its chart/height/support/predicate/witness/footprint signatures, lowers donor-assignment deficit by one, and carries a nonnegative typed geometric cost vector.

For geometric coordinate `a`, let `K_a` be capacity and `kappa_a=max_e c(e)_a`.

## GC2nb -- capacity or oversized cleaning repair -- PROVED

If `c(e)_a>K_a`, return the least chart, height, donor, remedy, protected-event, occurrence or boundary coordinate with exact excess. Otherwise every queued repair fits coordinatewise and no geometric credit is borrowed across ledger types.

## GC2nc -- geometric replenishment-window service -- PROVED UNDER THE WINDOW CONTRACT

While a job remains at the FIFO head, suppose every consecutive `W_a` microsteps replenish coordinate `a` by at least `kappa_a`, with `K_a>=kappa_a`. For `W=max_a W_a`, the head becomes feasible within at most `W` steps because no later repair spends first and capacity truncation cannot prevent reserve reaching `kappa_a`.

Thus `n` queued repairs drain within

\[
\boxed{nW}
\]

steps and give total donor-deficit descent `n`. A failed window returns the least coordinate and interval with shortage `kappa_a-sum r_{t,a}>0`.

## GC2nd -- cleaning queue-origin conservation -- PROVED UNDER THE ORIGIN CONTRACT

Let `A_J` be cumulative first admissions, `Delta_0` initial donor deficit and `U_j` support-local cleaning disturbance. Distinct job owners are initial unmatched remedies or remedies newly unmatched by declared disturbance; requeue after execution requires fresh disturbance. Hence

\[
\boxed{A_J\le\Delta_0+\sum_{j=1}^J U_j.}
\]

Active queue size is at most current deficit and total head-service waiting is at most

\[
\boxed{WA_J\le W\left(\Delta_0+\sum_{j=1}^J U_j\right).}
\]

## GC2ne -- cleaning drain or persistent geometric shortage -- PROVED UNDER THE QUEUE CONTRACTS

One continuation holds: complete donor assignment; numerical chart/height-key donor shortage; oversized repair; FIFO drain with exact deficit descent; least replenishment-window shortage; or stale chart, protected-event, epoch, support, key, predicate, witness or footprint data or a failed repair certificate.

In a frozen physical state, complete repair generation and valid capacity/window contracts imply termination within `W Delta_0` repair microsteps.

## Corrected GC5 frontier

Cleaning now has bounded repair waiting. Remaining work is to construct chart/protected-event replenishment, prove concrete capacities and windows, revalidate jobs across geometric changes, and convert persistent shortages into protected-height payment or reset.

## Finite check

`scripts/verify_gc_reserve_queue_drain.py` checks 2,500 generated queues, drain bounds, capacity and replenishment witnesses, and queue-origin conservation.