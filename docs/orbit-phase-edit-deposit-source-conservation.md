# Orbit-phase edit-deposit source conservation

This note records OP4da--OP4de. It traces named deposits in the cumulative unified deletion/unit-edit bank back to occurrence-faithful physical source mass.

## Contract

Let `P` be exact physical edit-source occurrences and `E` exact unified edit-source classes. Initial physical mass and explicitly named exogenous physical deposits are the only new mass. A legal physical transition is one-for-one and output mass is at most input mass. Issuing `x` units into edit class `e` consumes exactly `x` units from one compatible physical source occurrence. Deletion charges and unit-edit costs consume edit balance.

## Theorem block

### OP4da — physical edit-source conservation

Legal source transitions preserve or decrease live physical mass plus terminally consumed mass.

### OP4db — edit deposits are transfers

Every named edit-source deposit transfers equal mass from one retained physical occurrence to one exact edit class. It is not free replenishment.

### OP4dc — joint cumulative law

At every point,

`live physical mass + live edit balance + terminal paid/expired mass <= initial physical mass + exogenous deposits`.

Therefore cumulative deletion and unit-edit payment cannot exceed the physical account.

### OP4dd — first amplification witness

Splitting, mass increase, source-less edit issuance, missing predecessor lineage or an unrecorded physical deposit is returned at the first violated joint-mass inequality.

### OP4de — reset boundary

Changed valuation, unit, holonomy, action, blocker or compatibility fields, relabelled source classes and nonadditive edit semantics return reset rather than conservation.

## Proof

Transitions are nonamplifying, issuance moves mass from the physical account to the edit account, and payment moves edit mass to terminal consumption. Summing the stepwise identities proves OP4dc.

## Finite audit

Run `python scripts/verify_op_edit_deposit_source_conservation.py`.

## Scope

This does not construct physical edit sources or their exogenous deposits. It does not prove OP5 or the no-three-in-line conjecture.