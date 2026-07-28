# Geometric-cleaning remedy-height source transport

This note records GC2im--GC2iq. It composes a selected integral cause/remedy assignment with an exact transport of its clean-height cost into physical height-credit sources.

## Contract

Let a complete cause/remedy graph have integral cause demand and remedy capacities. Fix one selected integral cause/remedy flow. If remedy `r` is used `u_r` times and has nonnegative integral height cost `h_r`, define its exact height demand by

`d_r^H = h_r u_r`.

Let `P` be a finite dictionary of physical height-credit sources with capacities `b_p` and a complete remedy/source compatibility graph.

## GC2im — exact induced height demand

The selected cause/remedy flow induces total clean-height demand

`sum_r h_r u_r`.

No cost is omitted or reassigned after the remedy flow is fixed.

## GC2in — height-source Hall criterion

All induced height demand is paid if and only if every remedy subset `R_0` satisfies

`sum_{r in R_0} d_r^H <= sum_{p in N(R_0)} b_p`.

The unpaid height credit equals the maximum positive Hall deficiency.

## GC2io — two-stage paid endpoint

If the cause/remedy flow pays every cause and the induced remedy/height-source transport pays every height unit, the cleaning epoch is physically remedied and its exact additive height loss is debited from named sources.

## GC2ip — canonical two-stage failure

Failure of the first transport returns the canonical cause/remedy cut. Failure of the second returns the least deficient remedy/height-source cut. The two failures are not merged into an anonymous shortage.

## GC2iq — reset boundary

Changing the selected remedy flow after height accounting, omitted remedy/source arcs, nonlinear or shared height costs, source reuse without debit, changed remedy identity or untagged credit creation returns reset.

## Finite audit

Run:

`python scripts/verify_gc_remedy_height_source_transport.py`

The deterministic audit checks 6,500 systems. It finds 3,505 fully paid cause/remedy systems, of which 2,066 also pay all induced height demand; 1,439 retain exact height-source cuts.

## Scope

This theorem is conditional on a selected exact cause/remedy flow and a complete height-source graph. It does not prove the concrete remedy geometry, source capacities or height costs, and it does not prove GC5 or the no-three-in-line conjecture.
