# Superregular geometric atom-cut extraction

This note records SRR2cz--SRR2dd. It converts every deficient physical-source/atom/burden flow into an exact geometric witness cut.

## Contract

Fix a finite ordered integral network with physical-source capacity, witness-atom throughput and burden-demand terminals. Guarded compatibility arcs exceed total demand plus all finite capacities. Use split capacity nodes and a fixed deterministic integral maximum-flow rule.

## Theorem block

### SRR2cz — residual atom cut

Residual reachability after maximum flow returns physical-source and witness-atom barrier sets and the outside burden-demand set.

### SRR2da — complete witness closure

No guarded physical-to-atom or atom-to-burden edge crosses the finite cut. The returned cut therefore preserves the complete witness-atom dictionary and every burden address.

### SRR2db — exact burden deficit

For outside burden set `X` and barriers `B_phys,B_atom`,

`U = burden(X) - cap(B_phys) - cap(B_atom)`.

Positive unpaid burden is exactly a strict geometric source/atom cut inequality.

### SRR2dc — heavy burden address

If `U>0`, one exact burden class in `X` carries at least the average outside burden. If burden classes are grouped by their retained witness atom, one atom group carries at least the average group burden and becomes the geometric target.

### SRR2dd — reset boundary

Omitted conflicts, changed witness atoms, changed threshold, hidden deposits, insufficient guard capacity or incomplete physical-source lineage returns reset.

## Finite audit

Run `python scripts/verify_srr_geometric_atom_cut_extraction.py`.

The audit checks 5,500 systems, 38,467 capacity classes, 19,272 burden classes and 89,280 compatibility arcs. It verifies 34,644 paid and 32,759 unpaid burden units, 4,377 deficient systems, 15,570 outside burden classes and barrier totals 14,290 physical plus 12,592 atom units.

## Scope

This theorem does not construct the geometric tensor reference or prove the required atom-capacity estimates. It does not prove SRR2 or SRR4.
