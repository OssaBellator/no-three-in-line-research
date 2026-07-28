# Orbit-phase unit-edit capacity bank

This note records OP4cl--OP4cp. It pays the unit-field edits that remained separate from the deletion-source account.

## Contract

Let `U` be the finite retained unit-class dictionary. Every nontrivial unit-field change has one exact edit address containing the ordered pair of unit classes and all payment-sensitive residual, source, factor, holonomy and legality fields.

Partition edit addresses into a finite source-class dictionary. An edit of class `a` has nonnegative integral cost `c_e`. Class `a` has an initial balance and exact named deposits. Each edit consumes its cost from exactly one class.

## OP4cl — exact unit-edit partition

Across an epoch, total unit-edit cost is the disjoint sum of the costs assigned to the exact source classes.

## OP4cm — paid epoch or exact overload

If every class cost is at most its initial-plus-deposited balance, every unit edit in the epoch is paid. Otherwise the least overloaded source class is retained with its exact excess.

## OP4cn — cumulative edit bound

Across paid epochs, cumulative unit-edit cost is bounded by cumulative initial balances and named deposits. A cost threshold `tau>0` therefore bounds the number of edits of cost at least `tau`.

## OP4co — composition with dynamic residual edits

The deletion-source capacity bank pays positive residual-deficit variation, while the present bank pays unit-field changes. When both accounts are complete, the entire dynamic signature edit history is paid without suppressing unit sensitivity.

## OP4cp — reset boundary

Unrecorded deposits, changed unit dictionaries, omitted legality fields, zero-cost relabelling of a physically changed unit class, cross-class cancellation or one balance unit paying several edits returns reset.

## Finite audit

Run:

`python scripts/verify_op_unit_edit_capacity_bank.py`

The deterministic audit checks 8,500 epochs, 46,917 edit steps, 33,346 nontrivial unit changes, 83,593 edit-cost units and 16,170 exact source-class checks.

## Scope

The theorem does not prove the physical edit costs, source classes or deposits. It closes the finite accounting interface once those quantities are supplied. OP5 and the no-three-in-line conjecture remain open.
