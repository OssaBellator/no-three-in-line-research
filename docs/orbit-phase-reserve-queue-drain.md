# Orbit-phase reserve queue drain

## Status

This note proves OP4ha--OP4hd under the footprint-costed phase-repair contracts through OP4gz. It does not construct quotient-phase replenishment, prove OP5, or prove the no-three-in-line conjecture.

## Setup

Validated unmatched residual/edit-incidence to free-source repairs are stored in FIFO order. Every job owns a distinct unmatched incidence, retains its quotient/support/key/predicate/witness/footprint and epoch signatures, lowers source-assignment deficit by one, and carries a nonnegative typed phase-cost vector.

For phase coordinate `a`, let `K_a` be capacity and `kappa_a=max_e c(e)_a`.

## OP4ha -- capacity or oversized phase repair -- PROVED

If one job has `c(e)_a>K_a`, return the least source, residual, edit, unit, valuation, holonomy, carry, owner, occurrence or boundary coordinate with exact excess. Otherwise every job fits coordinatewise and no phase resource is borrowed from another ledger.

## OP4hb -- phase replenishment-window FIFO service -- PROVED UNDER THE WINDOW CONTRACT

While a fixed job remains at the head, assume every consecutive `W_a` repair microsteps replenish coordinate `a` by at least `kappa_a`, with `K_a>=kappa_a`. Put `W=max_a W_a`.

No later job spends first. Hence each coordinate reaches the head cost within its window, the head executes within `W` steps, and `n` queued jobs drain within

\[
\boxed{nW}
\]

steps with source-deficit descent `n`. Failure returns the least coordinate and least window with exact shortfall `kappa_a-sum r_{t,a}>0`.

## OP4hc -- phase queue-origin conservation -- PROVED UNDER THE ORIGIN CONTRACT

Let `A_J` be cumulative first admissions, `Delta_0` initial source deficit and `U_j` support-local phase disturbance. Every job owns a distinct initial unmatched residual/edit incidence or one newly unmatched by declared disturbance; requeue after execution requires fresh disturbance. Thus

\[
\boxed{A_J\le\Delta_0+\sum_{j=1}^J U_j.}
\]

Active queue size is at most current deficit, and cumulative head-service waiting is at most

\[
\boxed{WA_J\le W\left(\Delta_0+\sum_{j=1}^J U_j\right).}
\]

## OP4hd -- phase drain or persistent shortage router -- PROVED UNDER THE QUEUE CONTRACTS

One continuation holds: complete source assignment; numerical quotient-key source shortage; oversized repair; FIFO drain with exact deficit descent; least replenishment-window shortage; or stale quotient, unit, valuation, holonomy, carry, support, key, predicate, witness, footprint or epoch data or a failed repair certificate.

For a frozen physical state, complete repair generation and valid capacity/window contracts imply termination within `W Delta_0` repair microsteps.

## Corrected OP5 frontier

Phase repair now has bounded waiting as well as bounded cost. Remaining work is to construct physical quotient/action replenishment, prove capacities and windows, revalidate jobs across phase changes, and turn persistent typed shortages into phase-ledger payment or reset.

## Finite check

`scripts/verify_op_reserve_queue_drain.py` checks 2,500 generated phase queues, capacity witnesses, replenishment-window failures, drain bounds and origin conservation.