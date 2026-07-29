# Superregular reserve queue drain

## Status

This note proves SRR2gk--SRR2gn under the footprint-costed conditioned-repair contracts through SRR2gj. It does not construct physical resampling replenishment, prove SRR4, or prove the no-three-in-line conjecture.

## Setup

Validated unmatched-candidate/free-witness repairs form a FIFO queue. Every job owns a distinct unmatched candidate incidence, retains its source/endpoint/blocker/cycle/threshold/burden/support/key/predicate/witness/footprint and epoch signatures, lowers witness-assignment deficit by one, and carries a nonnegative typed resampling-cost vector.

For conditioned coordinate `a`, let `K_a` be capacity and `kappa_a=max_e c(e)_a`.

## SRR2gk -- capacity or oversized conditioned repair -- PROVED

If `c(e)_a>K_a`, return the least source, endpoint, blocker, cycle, threshold, burden, occurrence or repair coordinate with exact excess. Otherwise every job fits coordinatewise and no resource is borrowed between conditioned ledgers.

## SRR2gl -- conditioned replenishment-window service -- PROVED UNDER THE WINDOW CONTRACT

While a fixed job remains at the FIFO head, assume every consecutive `W_a` microsteps replenish coordinate `a` by at least `kappa_a`, with `K_a>=kappa_a`. Put `W=max_a W_a`.

No later job spends before the head. Therefore the head executes within `W` microsteps. A queue of `n` jobs drains within

\[
\boxed{nW}
\]

steps and gives witness-deficit descent `n`. A failed window returns the least coordinate and interval with exact shortage `kappa_a-sum r_{t,a}>0`.

## SRR2gm -- conditioned queue-origin conservation -- PROVED UNDER THE ORIGIN CONTRACT

Let `A_J` be cumulative first admissions, `Delta_0` initial witness deficit and `U_j` bounded-cycle disturbance. Every admitted job owns a distinct initial unmatched candidate or one newly unmatched by declared disturbance; requeue after execution requires new disturbance. Hence

\[
\boxed{A_J\le\Delta_0+\sum_{j=1}^J U_j.}
\]

Active queue size is at most current deficit, and cumulative head-service waiting is at most

\[
\boxed{WA_J\le W\left(\Delta_0+\sum_{j=1}^J U_j\right).}
\]

## SRR2gn -- conditioned drain or persistent shortage router -- PROVED UNDER THE QUEUE CONTRACTS

One continuation holds: complete witness assignment; numerical conditioned-key witness shortage; oversized repair; FIFO drain with exact deficit descent; least replenishment-window shortage; or stale source, endpoint, blocker, cycle, threshold, burden, support, key, predicate, witness, footprint or epoch data or a failed repair certificate.

For a frozen conditioned state, complete repair generation and valid capacity/window contracts imply termination within `W Delta_0` repair microsteps.

## Corrected SRR frontier

Conditioned repair now has bounded waiting. Remaining work is to construct cycle/threshold/burden replenishment, prove capacities and windows, revalidate queued jobs after resampling changes, and convert persistent shortages into endpoint-burden payment or reset.

## Finite check

`scripts/verify_srr_reserve_queue_drain.py` checks 2,500 generated conditioned queues, drain bounds, capacity witnesses, replenishment-window failures and origin conservation.