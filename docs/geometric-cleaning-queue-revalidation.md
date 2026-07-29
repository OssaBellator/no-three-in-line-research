# Geometric-cleaning queue revalidation

## Status

This note proves GC2nf--GC2ni under GC2ne. It does not construct geometric repair maps or replenishment, prove GC5, or prove the no-three-in-line conjecture.

## Setup

Every queued unmatched-remedy/free-donor repair has a complete footprint containing endpoint status, chart, height, protected-event, donor, remedy, occurrence, boundary, cost and repair-certificate dependencies. A macro edit touches `P`, `H=|P|`; let `eta` be the largest number of queued footprints through one primitive.

## GC2nf -- support-disjoint cleaning-job persistence -- PROVED UNDER THE COMPLETE-FOOTPRINT CONTRACT

If `F(e)` is disjoint from `P`, the repair job remains valid with the same debt identity and FIFO priority. Any changed validity returns an omitted geometric dependency or hidden write.

## GC2ng -- cleaning revalidation bound -- PROVED

Only `X(P)={e:F(e) cap P != empty}` requires inspection, and

\[
\boxed{|X(P)|\le H\eta.}
\]

Cumulative inspections are at most `sum_j H_j eta_j`; untouched jobs retain relative order.

## GC2nh -- stable donor-repair debt identity -- PROVED UNDER THE ORIGIN CONTRACT

Touched jobs revalidate, update without new admission, retire when their remedy is no longer unmatched, or return a rigid geometric repair obstruction. Only newly unmatched remedies create debt identities, so `A_J<=Delta_0+sum_j U_j` remains valid.

## GC2ni -- service or repeated geometric-footprint touch -- PROVED UNDER THE SERVICE CONTRACT

For a FIFO head of footprint size `h` and service window `W`, one `W`-step interval with no footprint touch services the job. If it survives `B` service blocks, one moved cell, protected event, chart, donor, remedy, height or boundary primitive is touched in at least

\[
\boxed{\lceil B/h\rceil}
\]

blocks.

## Corrected GC5 frontier

Cleaning queues now persist across unrelated edits and repeated delay localizes to one declared geometric primitive. Remaining work is concrete footprint construction and conversion of repeated touches into protected-height payment or reset.

## Finite check

`scripts/verify_gc_queue_revalidation.py` checks 2,500 generated systems.
