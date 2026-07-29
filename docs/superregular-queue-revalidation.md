# Superregular queue revalidation

## Status

This note proves SRR2go--SRR2gr under SRR2gn. It does not construct conditioned repairs or replenishment, prove SRR4, or prove the no-three-in-line conjecture.

## Setup

Each queued unmatched-candidate/free-witness repair has a complete footprint containing endpoint status, source, blocker, cycle, threshold, burden, conditioning, occurrence, cost and repair-certificate dependencies. A macro edit touches `P`, `H=|P|`; let `eta` be maximum queued-footprint multiplicity.

## SRR2go -- support-disjoint conditioned-job persistence -- PROVED UNDER THE COMPLETE-FOOTPRINT CONTRACT

If `F(e)` is disjoint from `P`, the queued job remains valid with unchanged debt identity, witness reservation and FIFO priority. Any contrary change returns an omitted conditioned dependency or hidden write.

## SRR2gp -- conditioned revalidation bound -- PROVED

Only jobs meeting `P` require inspection, with

\[
\boxed{|X(P)|\le H\eta.}
\]

Cumulative inspections are at most `sum_j H_j eta_j`; untouched jobs retain relative order.

## SRR2gq -- stable conditioned debt identity -- PROVED UNDER THE ORIGIN CONTRACT

Touched jobs revalidate, update without new admission, retire when their candidate is no longer unmatched, or return a named rigid conditioned-repair obstruction. Only newly unmatched candidates create debt identities, preserving `A_J<=Delta_0+sum_j U_j`.

## SRR2gr -- service or repeated conditioned-footprint touch -- PROVED UNDER THE SERVICE CONTRACT

For a FIFO head of footprint size `h` and service window `W`, one untouched `W`-step block services the job. If it survives `B` service blocks, one source/endpoint/blocker/cycle/threshold/burden/conditioning primitive is touched in at least

\[
\boxed{\lceil B/h\rceil}
\]

blocks.

## Corrected SRR frontier

Conditioned queues now survive unrelated edits, have support-local revalidation cost, and convert indefinite delay into a repeated typed conditioned touch. Remaining work is concrete footprint construction and endpoint-burden payment or reset.

## Finite check

`scripts/verify_srr_queue_revalidation.py` checks 2,500 generated systems.
