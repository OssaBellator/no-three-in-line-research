# Rational-inverse owner-charge cut-address extraction

This note records RI5ej--RI5en. It extracts an exact owner/charge address from every deficient physical-source/collateral cut.

## Contract

Fix a finite ordered integral network with physical-source capacity, collateral throughput and terminal demands labelled either symmetric-owner cost or perturbation charge. Guarded compatibility arcs exceed total demand plus all finite capacities. Use split capacity nodes and a fixed deterministic integral maximum-flow rule.

## Theorem block

### RI5ej — residual physical-collateral cut

Residual reachability after maximum flow returns physical-source and collateral barrier sets and the complete outside demand set.

### RI5ek — compatibility closure

No guarded physical-to-collateral or collateral-to-demand edge crosses the finite cut. The cut therefore retains exact owner, charge, collateral and physical-source addresses.

### RI5el — exact unpaid identity

For outside demand set `X` and barriers `B_phys,B_col`,

`U = demand(X) - cap(B_phys) - cap(B_col)`.

The mixed cut is deficient exactly when the outside owner-plus-charge demand strictly exceeds those two retained capacity totals.

### RI5em — owner-or-charge localization

Partition `X` into symmetric-owner and perturbation-charge demand. One type carries at least half of `demand(X)`; choosing the least class in a maximizing type gives a canonical arithmetic address for the remaining RI6 estimate.

### RI5en — reset boundary

Changed owners, retained fields, charges, collateral compatibility, hidden deposits, insufficient guard capacity or omitted physical lineage returns reset.

## Finite audit

Run `python scripts/verify_ri_owner_charge_cut_addresses.py`.

The audit checks 5,000 systems, 35,037 capacity classes, 17,517 demand classes and 81,548 compatibility arcs. It verifies 31,691 paid and 29,216 unpaid units over 3,974 deficient systems. Outside demand totals are 25,928 owner units and 26,113 charge units; physical and collateral barrier totals are 13,285 and 11,031.

## Scope

This theorem does not construct the concrete arithmetic compatibility graph or prove its cut inequalities. It does not prove RI6.
