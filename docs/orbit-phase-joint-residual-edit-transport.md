# Orbit-phase joint residual/edit transport

This note records OP4df--OP4dj. It combines zero-drift residual payment with deletion and unit-edit costs so the same physical source capacity cannot be counted once by the residual bank and again by the edit bank.

## Contract

Fix finite residual-demand classes `R`, edit-cost classes `E` and physical source classes `S`. Retain complete compatibility relations from both demand types to the same source side, exact integral residual demands, exact integral deletion/unit-edit costs and exact integral source capacities. Every paid unit debits one compatible source unit.

## Theorem block

### OP4df — one combined demand family

Take the disjoint union of residual and edit classes, preserving the residual signature, unit field, deletion address and edit-source address of every unit.

### OP4dg — simultaneous Hall criterion

All residual and edit demand is paid exactly when every subset of the combined demand family satisfies its capacitated Hall inequality against the shared source capacities. Equivalently, the combined maximum flow equals total demand.

### OP4dh — separate feasibility is insufficient

Residual demand and edit demand may each be feasible against the full source vector while their union is infeasible. Therefore the two banks cannot be checked independently when they share physical sources.

### OP4di — canonical mixed cut

Failure returns a canonical maximizing deficit set containing exact residual and edit classes together with its source neighborhood and unpaid mass.

### OP4dj — reset boundary

Omitted unit fields, changed residual signatures, changed deletion addresses, hidden source deposits, payment across a noncompatible edge or source-less creation returns reset or amplification.

## Finite audit

Run:

`python scripts/verify_op_joint_residual_edit_transport.py`

The deterministic audit checks 6,000 systems, 21,102 residual classes, 20,922 edit classes, 20,875 source classes, 75,802 compatibility arcs, 104,118 total demand units, 58,554 paid units, 45,564 unpaid units, 1,348,304 exact Hall-subset checks and 503 systems where both separate banks are feasible but the combined bank is deficient.

## Scope

This theorem does not construct the concrete residual/edit compatibility graph or prove its physical capacities, costs and deposits. It does not prove OP5 or the no-three-in-line conjecture.