# Orbit-phase queue revalidation

## Status

This note proves OP4he--OP4hh under OP4hd. It does not construct phase repairs or replenishment, prove OP5, or prove the no-three-in-line conjecture.

## Setup

Each queued residual/edit to free-source repair has a complete footprint containing endpoint status, quotient, action, owner, unit, valuation, holonomy, carry, boundary, cost and repair-certificate dependencies. A macro edit touches `P`, `H=|P|`; let `eta` be maximum queued-footprint multiplicity.

## OP4he -- support-disjoint phase-job persistence -- PROVED UNDER THE COMPLETE-FOOTPRINT CONTRACT

If `F(e)` is disjoint from `P`, the job remains valid with unchanged debt identity, source reservation and FIFO priority. Any contrary change returns an omitted phase dependency or undeclared write.

## OP4hf -- phase revalidation bound -- PROVED

Only jobs meeting `P` require inspection, and

\[
\boxed{|X(P)|\le H\eta.}
\]

Cumulative inspections are at most `sum_j H_j eta_j`; untouched jobs retain relative order.

## OP4hg -- stable phase debt identity -- PROVED UNDER THE ORIGIN CONTRACT

Touched jobs revalidate, update without new admission, retire when their incidence is no longer unmatched, or return a named rigid phase-repair obstruction. Only newly unmatched incidences create debt identities, so `A_J<=Delta_0+sum_j U_j` remains valid.

## OP4hh -- service or repeated phase-footprint touch -- PROVED UNDER THE SERVICE CONTRACT

For a FIFO head of footprint size `h` and service window `W`, one untouched `W`-step block services the job. If it survives `B` blocks, one quotient/action/unit/valuation/holonomy/carry/owner/boundary primitive is touched in at least

\[
\boxed{\lceil B/h\rceil}
\]

blocks.

## Corrected OP5 frontier

Phase queues now survive unrelated edits, require only support-local revalidation, and turn indefinite delay into a repeated typed phase touch. Remaining work is concrete footprint construction and phase-ledger payment or reset.

## Finite check

`scripts/verify_op_queue_revalidation.py` checks 2,500 generated systems.
