# Orbit-phase unified edit transport

This note records OP4cq--OP4cu. It combines deletion-capacity charges and unit-field edit costs into one shared physical source account.

## Contract

Let `D_del` be the finite exact deletion-charge classes and `D_unit` the finite exact unit-edit classes. Let `S` be the finite edit-source dictionary with integral current capacities. Retain the complete compatibility graph from both demand types to `S`; source capacity is shared and may be debited only once.

## Theorem block

### OP4cq — combined edit-demand graph

The disjoint union `D_del union D_unit` with the shared source side is one integral transport problem. Residual signature, unit class, edit address and demand type remain retained fields.

### OP4cr — simultaneous Hall criterion

All deletion and unit-edit costs are paid exactly if and only if every subset `X` of the combined demand graph satisfies

`d(X) <= cap(N(X))`.

### OP4cs — shared-capacity protection

Separate success of the deletion bank and unit-edit bank does not certify joint payment. A combined flow is required to prevent the same source unit from paying both costs.

### OP4ct — canonical mixed edit cut

Maximum unpaid edit cost equals the maximum combined Hall deficit. The least maximizing subset returns the exact mix of deletion and unit-edit classes and its source neighborhood.

### OP4cu — reset boundary

An omitted unit field, residual class, edit event, compatibility arc, source capacity or deposit, or an edit whose cost changes inside the system, returns reset.

## Proof

Integral max-flow/min-cut on the combined bipartite graph proves the criterion and canonical cut. Shared source arcs appear once, proving OP4cs.

## Finite audit

Run `python scripts/verify_op_unified_edit_transport.py`.

The deterministic audit checks 5,500 systems, 33,070 combined edit-demand classes, 58,415 compatibility arcs, 65,676 edit-cost units, 37,454 paid units, 28,222 deficient units, 1,498,624 Hall-subset checks, and 2,155 systems where independent bank calculations would double-spend edit-source capacity.

## Scope

This theorem does not construct the physical edit-source classes, costs, capacities or deposits. It gives the required unified accounting once those data are proved. OP5 and the no-three-in-line conjecture are not proved.