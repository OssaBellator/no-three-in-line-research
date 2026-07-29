# Rational-inverse queue revalidation

## Status

This note proves RI5hy--RI5ib under the reserve-queue contracts through RI5hx. It does not construct the arithmetic repair maps or replenishment process, prove RI6, or prove the no-three-in-line conjecture.

## Setup

A queued RI repair job `e` owns one unmatched incidence and one reserved free collateral token. Its complete dependency footprint `F(e)` contains every physical coordinate capable of changing its endpoint status, support, key, predicate, witness, cost, repair map, or matching-preservation certificate. A macro edit touches a physical support `P` with `H=|P|`.

Let

\[
\eta=\max_x |\{e:x\in F(e)\}|.
\]

Queue debt identities and FIFO priorities are stable across revalidation; updating a job does not create a new admission.

## RI5hy -- support-disjoint queue persistence -- PROVED UNDER THE COMPLETE-FOOTPRINT CONTRACT

If `F(e) cap P` is empty, then every dependency of `e`, including its owner incidence, reserved token, unmatched/free status, typed cost and repair certificate, is unchanged. Hence `e` remains valid with the same debt identity and FIFO priority.

A job whose validity changes despite disjoint support returns the least omitted dependency or undeclared shared-state write.

## RI5hz -- touched-job inspection bound -- PROVED

Only jobs in

\[
X(P)=\{e:F(e)\cap P\ne\varnothing\}
\]

require revalidation. By the union bound,

\[
\boxed{|X(P)|\le H\eta.}
\]

Across macro epochs `1,...,J`, with edit sizes `H_j` and active multiplicities `eta_j`, total job inspections are at most

\[
\boxed{\sum_{j=1}^J H_j\eta_j.}
\]

Untouched jobs retain their relative FIFO order.

## RI5ia -- stable debt identity under revalidation -- PROVED UNDER THE ORIGIN CONTRACT

Each touched job has one exact continuation:

1. it revalidates unchanged;
2. it receives updated signatures but keeps the same owner, debt identity and FIFO priority;
3. its owner is no longer unmatched, so the job retires and releases debt;
4. its owner remains unmatched but no valid repair exists, yielding a named rigid repair obstruction.

Only incidences newly unmatched by declared support-local disturbance may create new debt identities. Therefore revalidation does not alter the admission bound

\[
A_J\le \Delta_0+\sum_{j=1}^J U_j.
\]

Repeated retries and signature refreshes do not create collateral debt.

## RI5ib -- head service or repeated-footprint instability -- PROVED UNDER THE SERVICE CONTRACT

Fix a FIFO head job `e`, put `h=|F(e)|`, and let `W` be its replenishment service-window bound from RI5hv. If one consecutive block of `W` repair microsteps contains no edit touching `F(e)`, then the job remains valid throughout that block and executes by its end.

If the same head survives `B` consecutive service blocks without execution, every block contains a touch of `F(e)`. Hence one primitive `x in F(e)` is touched in at least

\[
\boxed{\left\lceil\frac{B}{h}\right\rceil}
\]

of those blocks.

Thus indefinite delay returns a quantified repeated arithmetic-resource touch rather than an unstructured stale-job event.

## Corrected RI6 frontier

RI queue service is now stable under bounded macro edits: unaffected jobs persist, revalidation work is support-local, debt identities cannot duplicate, and repeated interruption concentrates on one declared footprint primitive. Remaining work is to build the concrete footprints and convert repeated-touch certificates into arithmetic/geometric payment, reset or recurrence descent.

## Finite check

`scripts/verify_ri_queue_revalidation.py` checks disjoint-support persistence, the `H eta` inspection bound, stable debt identities, cumulative inspection accounting, and the service-or-repeated-touch dichotomy on 2,500 generated systems.
