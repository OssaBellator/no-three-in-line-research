# Alternating-core synchronized queue revalidation

## Status

This note proves AC5hb--AC5he under AC5ha and the six side-track queue-revalidation contracts. It does not construct the physical footprints or repeated-touch payments, prove AC6, or prove the no-three-in-line conjecture.

## Setup

Every queued job has fixed track type `s`, one unmatched owner incidence, one reserved free token, a stable debt identity and FIFO priority, and a complete global physical footprint `F(e)`. The footprint contains all track-local and shared-state coordinates capable of changing endpoint status, signatures, typed cost, repair validity, matching preservation, or another track dictionary.

A macro edit touches global support `P_j`, with `H_j=|P_j|`. Define

\[
\beta_j=\max_x |\{e\text{ active before epoch }j:x\in F(e)\}|,
\]

where a shared physical primitive is counted once, not once per track label.

## AC5hb -- synchronized support-disjoint persistence -- PROVED UNDER THE COMPLETE-GLOBAL-FOOTPRINT CONTRACT

If `F(e) cap P_j` is empty, the queued job remains valid with the same track, owner, reserved token, unmatched/free status, signatures, typed cost, repair certificate, debt identity and FIFO priority. Every other track dictionary is unchanged on the job's dependencies.

Any validity change outside the declared footprint returns the least hidden shared-state or track-local dependency.

## AC5hc -- global revalidation bound -- PROVED

Only

\[
X_j=\{e:F(e)\cap P_j\ne\varnothing\}
\]

requires inspection. The global union bound gives

\[
\boxed{|X_j|\le H_j\beta_j.}
\]

Hence cumulative synchronized revalidation work through epoch `J` is at most

\[
\boxed{\sum_{j=1}^J H_j\beta_j.}
\]

This includes cross-track invalidation caused by shared-state edits. Untouched jobs preserve their relative order inside each typed FIFO queue.

## AC5hd -- typed stable debt identity -- PROVED UNDER THE ORIGIN CONTRACT

A touched job either revalidates unchanged, updates signatures under the same debt identity and FIFO priority, retires because its owner is no longer unmatched, or returns a typed rigid-repair obstruction. Jobs cannot move between tracks.

Only incidences newly unmatched by declared synchronized disturbance create new debt identities. Therefore

\[
\boxed{\sum_s A_{s,J}\le \Delta_0+\sum_{j=1}^J U_j}
\]

continues to hold after arbitrary revalidation. Repeated polling, signature refresh and failed reserve checks create no debt.

## AC5he -- service or repeated global-footprint instability -- PROVED UNDER THE SERVICE CONTRACTS

Fix a selected FIFO head `e` on track `s`, let `h=|F(e)|`, and let `W_s` be its typed replenishment service-window bound. If one consecutive `W_s`-microstep block contains no macro edit touching `F(e)`, the job remains valid and executes by the end of the block.

If the same head survives `B` consecutive service blocks without execution, every block contains a touch of `F(e)`. Consequently one declared global physical primitive `x in F(e)` is touched in at least

\[
\boxed{\left\lceil\frac{B}{h}\right\rceil}
\]

blocks.

Thus one exact continuation holds: all assignments complete; a numerical track-key shortage; bounded support-local revalidation followed by service; retirement of stale debt; a typed rigid repair failure; or a quantified repeated-touch certificate on one track-local or shared-state primitive.

For a frozen physical state, `P_j` is empty and AC5ha's `W_* Delta_0` drain bound is recovered. Across changing states, all revalidation work is bounded by global support churn and all new debt by matching disturbance.

## Corrected AC6 frontier

Synchronized queues now have bounded overlap, cost, waiting and macro-edit revalidation. Remaining work is to construct complete global footprints, prove numerical `beta_j` bounds, and convert repeated-touch certificates into payment, reset or finite macro-state descent.

## Finite check

`scripts/verify_ac_synchronized_queue_revalidation.py` checks global shared-state multiplicity, the `H beta` bound, fixed track/debt identities, service-or-repeated-touch certificates, and synchronized admission accounting on 1,500 generated seven-track systems.
