# Sparse algebraic reserve queue drain

## Status

This note proves SAS5oa--SAS5od under the footprint-costed sparse-repair contracts through SAS5nz. It does not construct sparse replenishment, prove SAS6, or prove the no-three-in-line conjecture.

## Setup

Validated unmatched pair/completion-incidence to free-neutral repairs form a FIFO queue. Every job owns a distinct unmatched incidence, retains its move/profile/orientation/legality/boundary/lineage/support/key/predicate/witness/footprint and epoch signatures, lowers neutral-assignment deficit by one, and carries a nonnegative typed sparse-cost vector.

For sparse coordinate `a`, let `K_a` be capacity and `kappa_a=max_e c(e)_a`.

## SAS5oa -- capacity or oversized sparse repair -- PROVED

If `c(e)_a>K_a`, return the least row/cell, swap, profile, orientation, legality, boundary, owner, occurrence, neutral or lineage coordinate with exact excess. Otherwise every queued job fits coordinatewise and no cost migrates between sparse ledgers.

## SAS5ob -- sparse replenishment-window FIFO service -- PROVED UNDER THE WINDOW CONTRACT

While a fixed job remains at the head, assume every consecutive `W_a` microsteps replenish coordinate `a` by at least `kappa_a`, with `K_a>=kappa_a`. Put `W=max_a W_a`.

No later job spends first. Hence the head executes within `W` microsteps. A queue of `n` jobs drains within

\[
\boxed{nW}
\]

steps and gives neutral-deficit descent `n`. Failure returns the least coordinate and least interval with exact shortfall `kappa_a-sum r_{t,a}>0`.

## SAS5oc -- sparse queue-origin conservation -- PROVED UNDER THE ORIGIN CONTRACT

Let `A_J` be cumulative first admissions, `Delta_0` initial neutral deficit and `U_j` sparse-move disturbance. Every admitted job owns a distinct initial unmatched pair/completion incidence or one newly unmatched by declared disturbance; requeue after execution requires new disturbance. Therefore

\[
\boxed{A_J\le\Delta_0+\sum_{j=1}^J U_j.}
\]

Active queue size is at most current deficit and cumulative head-service waiting is at most

\[
\boxed{WA_J\le W\left(\Delta_0+\sum_{j=1}^J U_j\right).}
\]

## SAS5od -- sparse drain or persistent shortage router -- PROVED UNDER THE QUEUE CONTRACTS

One continuation holds: complete neutral assignment; numerical neutral-key shortage; oversized repair; FIFO drain with exact deficit descent; least replenishment-window shortage; or stale move, profile, orientation, legality, boundary, lineage, support, key, predicate, witness, footprint or epoch data or a failed repair certificate.

For a frozen sparse state, complete repair generation and valid capacity/window contracts imply termination within `W Delta_0` repair microsteps.

## Corrected SAS6 frontier

Sparse repair now has bounded waiting. Remaining work is to construct move/orientation/lineage replenishment, prove capacities and windows, revalidate queued jobs across sparse changes, and turn persistent shortages into neutral, orientation or lineage payment.

## Finite check

`scripts/verify_sas_reserve_queue_drain.py` checks 2,500 generated sparse queues, drain bounds, capacity witnesses, replenishment-window failures and origin conservation.