# Geometric-cleaning support-local donor churn

## Status

This note proves GC2mh--GC2mk under the key-local donor and incremental contracts through GC2mg. It does not construct the geometric dependency dictionary, prove GC5, or prove the no-three-in-line conjecture.

## Setup

Let `X` be the primitive cleaning-resource set: moved cells, protected triples or lines, polynomial/rational chart records, donor occurrences, remedy slots, height-band certificates and boundary records. One cleaning operation has support `S subseteq X`, with `1<=|S|<=H`.

Each changed/new remedy incidence, changed/new next donor token, and changed/deleted old donor token declares a dependency set meeting `S`. A changed record whose declared dependency misses the support is returned as a nonlocal geometric-change witness.

## GC2mh -- exact cleaning-support witness -- PROVED UNDER THE DEPENDENCY CONTRACT

Every changed record has a least touched primitive cause. Missing dependencies, a hidden chart or height change, an undeclared moved cell, or a global donor relabelling are first exact failures.

## GC2mi -- primitive geometric churn bounds -- PROVED

Let `alpha_R`, `alpha_+`, and `alpha_-` be the maximum numbers of changed remedy incidences, changed/new next donor tokens, and changed/deleted old donor tokens depending on one touched primitive. Then

\[
\boxed{|\Delta R|\le H\alpha_R,\qquad |\Delta T|\le H\alpha_+,\qquad |T\setminus T^\circ|\le H\alpha_-.}
\]

This follows by counting every changed record at one or more support primitives and bounding the sum over at most `H` primitives.

## GC2mj -- support-local donor audit -- PROVED

With key-fibre bounds `L_T,L_R` from GC2mf, the fresh geometric compatibility work is at most

\[
\boxed{H(\alpha_RL_T+\alpha_+L_R)}.
\]

The carried donor matching leaves at most

\[
\boxed{u\le H(\alpha_R+\alpha_-)}
\]

remedy incidences unmatched. At most this many augmenting paths restore a complete donor assignment, or the geometric Hall deficit is at most this quantity. Matching maintenance creates no donor mass and changes no protected-height accounting.

## GC2mk -- support-anchored donor obstruction -- PROVED

After maximal reaugmentation, every unmatched incidence is initially support-disturbed: it is changed/new, or its old assigned donor changed or disappeared. Assign its least support cause.

If the residual deficit is `delta>0`, one moved cell, protected event, chart, donor occurrence, remedy slot or boundary record anchors at least

\[
\boxed{\lceil\delta/H\rceil}
\]

unmatched roots. Each root has a closed alternating search with no free donor and is an explicit support-local geometric obstruction.

## Corrected GC5 frontier

Cleaning churn is now bounded by physical support and primitive dependency incidence. Remaining work is to construct the actual dependency sets, prove support, incidence and key-fibre bounds for concrete cleaning operations, evaluate the small boundary, and pay the support-anchored donor/remedy obstruction.

## Finite check

`scripts/verify_gc_support_local_donor_churn.py` checks support incidence bounds, key-local audit bounds, carried donor disturbance, residual-root concentration and nonlocal-change detection.