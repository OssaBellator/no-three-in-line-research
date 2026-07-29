# Sparse algebraic queue revalidation

## Status

This note proves SAS5oe--SAS5oh under SAS5od. It does not construct sparse repairs or replenishment, prove SAS6, or prove the no-three-in-line conjecture.

## Setup

Each queued unmatched pair/completion to free-neutral repair has a complete footprint containing endpoint status, row/cell, swap, profile, orientation, legality, boundary, owner, occurrence, neutral, lineage, cost and repair-certificate dependencies. A macro edit touches `P`, `H=|P|`; let `eta` be maximum queued-footprint multiplicity.

## SAS5oe -- support-disjoint sparse-job persistence -- PROVED UNDER THE COMPLETE-FOOTPRINT CONTRACT

If `F(e)` is disjoint from `P`, the queued job remains valid with unchanged debt identity, neutral-token reservation and FIFO priority. Any contrary change returns an omitted sparse/lineage dependency or hidden write.

## SAS5of -- sparse revalidation bound -- PROVED

Only jobs meeting `P` require inspection, with

\[
\boxed{|X(P)|\le H\eta.}
\]

Cumulative inspections are at most `sum_j H_j eta_j`; untouched jobs retain relative order.

## SAS5og -- stable sparse debt identity -- PROVED UNDER THE ORIGIN CONTRACT

Touched jobs revalidate, update without new admission, retire when their pair/completion incidence is no longer unmatched, or return a named rigid sparse-repair obstruction. Only newly unmatched incidences create debt identities, preserving `A_J<=Delta_0+sum_j U_j`.

## SAS5oh -- service or repeated sparse-footprint touch -- PROVED UNDER THE SERVICE CONTRACT

For a FIFO head of footprint size `h` and service window `W`, one untouched `W`-step block services the job. If it survives `B` service blocks, one row/cell/swap/profile/orientation/legality/boundary/owner/neutral/lineage primitive is touched in at least

\[
\boxed{\lceil B/h\rceil}
\]

blocks.

## Corrected SAS6 frontier

Sparse queues now survive unrelated edits, have support-local revalidation cost, and convert indefinite delay into a repeated typed sparse or lineage touch. Remaining work is concrete footprint construction and neutral/orientation/lineage payment or reset.

## Finite check

`scripts/verify_sas_queue_revalidation.py` checks 2,500 generated systems.
