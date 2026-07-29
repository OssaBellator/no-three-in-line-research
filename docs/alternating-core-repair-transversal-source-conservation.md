# Alternating-core repair-transversal source conservation

## Status

This note proves AC5fa--AC5fe under the complete occurrence-faithful repair-source contract. It does not construct the geometric source dictionary and does not prove AC5, AC6 or the no-three-in-line conjecture.

## Setup

Fix the canonical deficit-sized repair transversal returned by AC5ev--AC5ez. Every selected incidence retains its defect address, outside physical/source/certificate slot, repair class and epoch. A **repair-source occurrence** is a unit token with a complete predecessor address and one retained repair class. Initial tokens and named exogenous deposits are the only permitted roots. A transition consumes one predecessor and creates one successor in the same class. Issuing a selected repair incidence consumes one live token exactly once.

## Theorem block

**AC5fa (exact issuance ledger).** If every selected repair incidence names one live compatible repair-source occurrence, then the incidence is an actual one-unit debit rather than merely a newly declared compatibility edge.

**AC5fb (global conservation).** At every prefix,

`live repair tokens + issued transversal incidences = initial tokens + named deposits`.

Consequently cumulative selected repair incidences are at most initial plus deposited repair-source mass.

**AC5fc (classwise conservation).** The same identity holds separately for every complete repair class. Transitions cannot move mass between classes unless the changed class field is recorded as a reset.

**AC5fd (transversal payment).** For a transversal of size `delta`, the class counts sum to `delta`; hence one retained class carries at least `ceil(delta/|C|)` selected incidences. Exact class balances pay these incidences or return the least overloaded repair class.

**AC5fe (first failure).** A nonconserving log returns the first exact source-less issuance, predecessor split, repeated debit, hidden deposit or class/address mismatch. Omitted compatibility, relabelling or unrecorded replenishment is a reset rather than payment.

## Proof

Induct on the event log. A named deposit increases the right side and the live account by one. A valid transition removes one live predecessor and adds one same-class successor. A valid issuance removes one live token and increases the issued account by one. These are the only legal events, so the global and classwise identities are invariant. Each forbidden event is detected at its first prefix. Summing the classwise issued counts gives the concentration claim.

## Remaining interface

The geometric work is now to construct the complete repair-source occurrence dictionary and prove that each selected transversal incidence has a compatible live source token, or to discharge the returned exact failure.