# Sparse neutral-move cut localization

This note records SAS5kp--SAS5kt. It extracts an exact sign-pair-or-completion obstruction from every deficient physical-source/move cut.

## Contract

Fix a finite ordered integral network with physical neutral-source capacity, neutral-move throughput and terminal demands labelled sign-pair execution or zero-boundary completion. Guarded compatibility arcs exceed total demand plus all finite capacities. Use split capacity nodes and a fixed deterministic integral maximum-flow rule.

## Theorem block

### SAS5kp — residual neutral-move cut

Residual reachability after maximum flow returns physical-source and neutral-move barrier sets and the complete outside mixed-demand set.

### SAS5kq — boundary-neutral compatibility closure

No guarded physical-to-move or move-to-demand edge crosses the finite cut. Every returned move remains genuinely boundary-neutral and every pair/task address is retained.

### SAS5kr — exact mixed deficit

For outside demand set `X` and barriers `B_phys,B_move`,

`U = demand(X) - cap(B_phys) - cap(B_move)`.

Thus zero-boundary completion fails exactly at one complete physical neutral-source cut.

### SAS5ks — pair-or-task localization

Partition `X` into sign-pair and completion-task demands. One type carries at least half of `demand(X)`; the least class in a maximizing type is the canonical endpoint for the remaining Hall or output estimate.

### SAS5kt — reset boundary

Changed boundary coordinates, nonneutral moves, omitted pair/task compatibility, hidden deposits, insufficient guard capacity or incomplete source lineage returns reset.

## Finite audit

Run `python scripts/verify_sas_neutral_move_cut_localization.py`.

The audit checks 5,200 systems, 36,371 capacity classes, 18,287 mixed-demand classes and 84,847 compatibility arcs. It verifies 33,152 paid and 31,137 unpaid units over 4,177 deficient systems. Outside totals are 27,420 sign-pair and 27,555 completion units; physical and move barrier totals are 13,994 and 11,581.

## Scope

This theorem does not prove physical pair-graph Hall inequalities, core shareability or the actual neutral-move capacities. It does not prove SAS6.
