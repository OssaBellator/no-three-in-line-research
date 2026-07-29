# Rational-inverse joint owner and perturbation-charge transport

This note records RI5dk--RI5do. It prevents the symmetric owner bank and the compatibility-deletion charge bank from independently spending the same collateral capacity.

## Contract

Let `D_sym` be the finite set of exact symmetric owner-demand classes and `D_edit` the finite set of exact owner-local perturbation-charge classes. Let `S` be the finite collateral-source dictionary with integral capacities. Retain the complete compatibility graph from both demand types to `S`.

## Theorem block

### RI5dk — combined demand graph

The disjoint union `D_sym union D_edit` with shared source capacities is one integral transportation problem. Demand type, owner, terminal address and perturbation address remain part of every left vertex.

### RI5dl — exact shared-capacity Hall criterion

All symmetric and perturbation charges are paid simultaneously if and only if every subset `X` of the combined demand graph satisfies

`d(X) <= cap(N(X))`.

### RI5dm — no-double-spend principle

Separate feasibility of the two banks does not imply joint feasibility. Only one combined flow certifies that a collateral unit is debited at most once.

### RI5dn — canonical mixed failure cut

Maximum unpaid mass equals the maximum combined Hall deficit. The least maximizing subset returns an exact mixture of symmetric and perturbation-charge classes together with its shared source neighborhood.

### RI5do — reset boundary

Changed owner, coherence, secant, root, terminal address, demand type, compatibility arc, source capacity or deposit is outside the fixed joint system and returns reset.

## Proof

Apply integral max-flow/min-cut to the disjoint combined left side and the shared source side. The capacity arcs occur only once, which proves the no-double-spend claim. The min cut gives RI5dn.

## Finite audit

Run `python scripts/verify_ri_joint_owner_charge_transport.py`.

The deterministic audit checks 5,000 systems, 29,836 combined demand classes, 51,655 compatibility arcs, 59,402 demand units, 33,347 paid units, 26,055 deficient units, 1,321,004 exact Hall-subset checks, and 1,981 systems where separate bank calculations would overclaim shared capacity.

## Scope

This theorem does not construct the arithmetic compatibility graph, source capacities or deposits. It supplies the required final cross-bank comparison once those physical data are proved. RI6 and the no-three-in-line conjecture are not proved.