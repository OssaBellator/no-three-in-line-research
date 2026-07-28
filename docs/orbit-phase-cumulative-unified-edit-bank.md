# Orbit-phase cumulative unified edit bank

This note records OP4cv--OP4cz. It extends the one-epoch unified deletion/unit-edit transport through repeated edit epochs with named shared-source deposits.

## Contract

Deletion-charge classes and unit-edit-cost classes form one finite demand set. Exact edit-source classes have current balances and one complete combined compatibility graph. Initial balances and every source deposit are named. A successful epoch uses one integral flow and debits shared source capacity once.

## Theorem block OP4cv--OP4cz

### OP4cv — current combined edit payment

All deletion and unit-edit demands are paid exactly iff the current combined Hall inequalities hold.

### OP4cw — single shared debit

The integral flow debits each edit source by actual use, preventing deletion and unit costs from spending the same source unit.

### OP4cx — cumulative edit account

Across successful epochs, cumulative unified edit debit is bounded by initial source balance plus named deposits.

### OP4cy — first unpaid mixed edit cut

The first failed epoch returns the canonical maximum-deficit subset of deletion/unit demand classes and its exact source neighbourhood.

### OP4cz — reset boundary

Changed unit fields, deletion addresses, source classes, compatibility or unrecorded deposits return reset.

## Proof

Apply integral max flow to the current combined graph and induct on epochs using the exact source-side debit vector.

## Finite audit

Run `python scripts/verify_op_cumulative_unified_edit_bank.py`.

## Scope

The theorem does not prove the physical edit graph, costs or deposits and does not prove OP5 or the no-three-in-line conjecture.
