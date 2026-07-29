# Orbit-phase support-local source churn

## Status

This note proves OP4gg--OP4gj under the key-local typed-source and incremental contracts through OP4gf. It does not construct the unit-sensitive dependency dictionary, prove OP5, or prove the no-three-in-line conjecture.

## Setup

Let `X` be the primitive quotient-repair resource set: changed quotient coordinates, residual/edit slots, action records, owner occurrences, unit or valuation fields, holonomy records, carry fields and boundary contexts. One quotient-phase edit has support `S subseteq X`, with `1<=|S|<=H`.

Every changed/new residual or edit incidence, changed/new next source token, and changed/deleted old source token carries a dependency set meeting `S`. A changed record whose dependency misses `S` is a nonlocal phase-change witness.

## OP4gg -- exact quotient-support witness -- PROVED UNDER THE DEPENDENCY CONTRACT

Every changed record has a least touched primitive cause. Missing dependencies, a hidden quotient coordinate, an undeclared unit/valuation/holonomy change, or a global source relabelling are first exact failures.

## OP4gh -- primitive phase-churn bounds -- PROVED

Let `alpha_R`, `alpha_+`, and `alpha_-` be the maximum numbers of changed residual/edit incidences, changed/new next source tokens, and changed/deleted old source tokens depending on one touched primitive. Then

\[
\boxed{|\Delta R|\le H\alpha_R,\qquad |\Delta T|\le H\alpha_+,\qquad |T\setminus T^\circ|\le H\alpha_-.}
\]

Every changed record meets the support and is therefore counted at least once in the sum of primitive incidences.

## OP4gi -- support-local unit-sensitive audit -- PROVED

With quotient key-fibre bounds `L_T,L_R` from OP4gd, one phase edit requires at most

\[
\boxed{H(\alpha_RL_T+\alpha_+L_R)}
\]

fresh compatibility evaluations. Its carried source matching leaves at most

\[
\boxed{u\le H(\alpha_R+\alpha_-)}
\]

incidences unmatched. At most this many augmenting paths restore a complete typed source assignment, or the residual/edit Hall deficit is at most this quantity. Carrying or augmenting creates no source mass, residual payment, or edit credit.

## OP4gj -- support-anchored phase obstruction -- PROVED

After maximal reaugmentation, every unmatched incidence is initially support-disturbed: it is changed/new, or its old source token changed or disappeared. Assign its least support cause.

If the residual deficit is `delta>0`, one quotient coordinate, action slot, owner occurrence, unit/valuation/holonomy field, carry field or boundary context anchors at least

\[
\boxed{\lceil\delta/H\rceil}
\]

unmatched roots. Each root has a closed alternating search with no free typed source token and is an explicit support-local phase obstruction.

## Corrected OP5 frontier

OP recurrence maintenance is now bounded by the physical edit support and primitive dependency incidence. Remaining work is to construct the actual dependency sets, prove support, incidence and quotient-key fibre bounds, evaluate the small boundary, and pay the support-anchored residual/edit obstruction.

## Finite check

`scripts/verify_op_support_local_source_churn.py` checks support incidence bounds, key-local audit bounds, carried source disturbance, residual-root concentration and nonlocal-change detection.