# Geometric-cleaning physical remedy-height cut localization

This note records GC2jq--GC2ju. It decomposes every deficient physical/remedy/height/cause flow into exact finite geometric barriers.

## Contract

Fix a finite ordered integral network with physical-source, remedy-capacity and height-capacity layers followed by cause-demand terminals. Guarded compatibility arcs exceed total demand plus all finite capacities. Use split capacity nodes and a fixed deterministic integral maximum-flow rule.

## Theorem block

### GC2jq — residual mixed-cut extraction

Residual reachability returns exact physical-source, remedy and height barrier sets and the outside cause-demand set.

### GC2jr — remedy-height compatibility closure

No guarded physical/remedy, remedy/height or height/cause edge crosses the finite cut. Every returned item therefore retains its exact cause, remedy and height-source address.

### GC2js — exact unpaid cause identity

For outside cause set `X` and barriers `B_phys,B_rem,B_ht`,

`U = demand(X) - cap(B_phys) - cap(B_rem) - cap(B_ht)`.

Thus a cleaning failure is precisely a strict inequality between one complete cause set and its three retained capacity barriers.

### GC2jt — cause-address concentration

If `U>0`, one exact cause class in `X` carries at least `demand(X)/|X|`. This localizes the missing physical estimate to one cause class and its closed remedy-height predecessor region.

### GC2ju — reset boundary

Changed height costs, cause/remedy compatibility, omitted donors or sources, hidden deposits, insufficient guard capacity or untagged feedback returns reset.

## Finite audit

Run `python scripts/verify_gc_physical_remedy_height_cuts.py`.

The audit checks 5,000 systems, 52,462 capacity classes, 17,471 cause classes and 121,379 compatibility arcs. It verifies 26,808 paid and 34,375 unpaid units, 4,291 deficient systems, 15,294 outside causes and barrier totals 8,331 physical, 7,825 remedy and 6,493 height units.

## Scope

This theorem does not establish concrete clean-height costs or physical capacities. It does not prove GC5.
