# Bounded-denominator queue revalidation

## Status

This note proves BDA5ih--BDA5ik under BDA5ig. It does not construct physical restoration repairs or replenishment, prove BDA6, or prove the no-three-in-line conjecture.

## Setup

Each queued restoration repair has a complete dependency footprint containing its owner incidence, reserved free potential token, gate/source/gain/damping/line/owner/arithmetic/boundary data, cost and repair certificate. A macro edit touches support `P`, `H=|P|`; let `eta` be the maximum number of active queued footprints containing one primitive.

## BDA5ih -- support-disjoint restoration-job persistence -- PROVED UNDER THE COMPLETE-FOOTPRINT CONTRACT

If a queued footprint is disjoint from `P`, every endpoint, signature, cost and certificate remains unchanged. The job keeps its debt identity and FIFO priority. Any disjoint-support validity change returns an omitted dependency or undeclared write.

## BDA5ii -- restoration revalidation bound -- PROVED

Only jobs whose footprints meet `P` require inspection, and

\[
\boxed{|X(P)|\le H\eta.}
\]

Across epochs, total inspections are at most `sum_j H_j eta_j`; untouched jobs retain relative FIFO order.

## BDA5ij -- stable restoration debt identity -- PROVED UNDER THE ORIGIN CONTRACT

A touched job revalidates, updates under the same owner and priority, retires when its owner is no longer unmatched, or returns a named rigid repair obstruction. Only newly unmatched incidences create new debt identities, so

\[
A_J\le\Delta_0+\sum_j U_j
\]

still holds. Revalidation and retries create no potential debt.

## BDA5ik -- service or repeated restoration-resource touch -- PROVED UNDER THE SERVICE CONTRACT

Let the FIFO head have footprint size `h` and replenishment service window `W`. A `W`-step interval without a footprint touch preserves the job and services it. If the head survives `B` such service blocks, every block touches its footprint, so one gate/source/gain/damping/line/owner/arithmetic/boundary primitive is touched in at least

\[
\boxed{\lceil B/h\rceil}
\]

blocks.

## Corrected BDA6 frontier

Restoration queues now persist under unrelated edits, have support-local revalidation cost, preserve debt identity, and return a quantified repeated-touch certificate under indefinite interruption. Remaining work is to build the concrete footprints and convert repeated restoration-resource touches into payment or reset.

## Finite check

`scripts/verify_bda_queue_revalidation.py` checks 2,500 generated systems.
