# Orbit-phase residual/edit cut decomposition

This note records OP4dp--OP4dt. It localizes every unpaid cumulative mixed epoch to one exact residual-or-edit source cut.

## Contract

Fix a finite ordered integral bipartite network from current source balances to terminal demands labelled zero-drift residual or deletion/unit edit. Guarded compatibility arcs exceed total demand plus all finite capacity. Use split source-capacity nodes and a fixed deterministic integral maximum-flow rule.

## Theorem block

### OP4dp — residual mixed cut

Residual reachability after maximum flow returns the exact source barrier set and the outside residual/edit demand set.

### OP4dq — unit-sensitive compatibility closure

No guarded source-to-demand arc crosses the finite cut. Hence every outside demand retains its full unit class, residual signature and edit-source compatibility.

### OP4dr — exact unpaid identity

For outside demand set `X` and source barrier `B`,

`U = demand(X) - cap(B)`.

Thus the first unpaid epoch is exactly one source-capacity inequality rather than a sum of independently computed residual and edit deficits.

### OP4ds — residual-or-edit localization

Partition `X` by demand type. One of residual demand or edit demand carries at least half of `demand(X)`; the least class of a maximizing type is a canonical physical target.

### OP4dt — reset boundary

Changed unit fields, signatures, edit costs, source compatibility, hidden deposits, insufficient guard capacity or omitted legality data returns reset.

## Finite audit

Run `python scripts/verify_op_residual_edit_cut_decomposition.py`.

The audit checks 5,200 systems, 18,214 source classes, 18,231 terminal classes and 42,241 compatibility arcs. It verifies 42,237 paid and 21,647 unpaid units over 3,362 deficient systems. Outside demand totals are 22,431 residual and 22,332 edit units, with 25,503 source barrier units.

## Scope

This theorem does not prove the concrete residual/edit graph or its source capacities. It does not prove OP5.
