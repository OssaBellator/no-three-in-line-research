# Bounded-denominator restoration-cut decomposition

This note records BDA5es--BDA5ew. It turns every unpaid physical/source/restoration flow into one exact primitive-potential cut identity.

## Contract

Fix a finite ordered integral network with physical primitive-potential capacity, issued source-potential throughput and restoration-demand terminals. Compatibility arcs carry a guard capacity larger than total demand plus all finite capacities. Use split capacity nodes and a fixed deterministic integral maximum-flow rule.

## Theorem block

### BDA5es — residual restoration cut

Residual reachability after maximum flow selects exact physical-potential and issued-source barrier sets together with the restoration classes outside the reachable side.

### BDA5et — arithmetic compatibility closure

No guarded physical-to-source or source-to-restoration arc crosses the finite cut. Thus the returned sets preserve the exact arithmetic source and restoration compatibility relation.

### BDA5eu — exact primitive-potential deficit

For outside restoration set `X` and barrier sets `B_phys,B_src`,

`unpaid(X) = demand(X) - potential(B_phys) - potential(B_src)`.

Hence every failure is the strict arithmetic inequality `demand(X) > potential(B_phys)+potential(B_src)`.

### BDA5ev — restoration-address witness

If unpaid potential is positive, one exact restoration class in `X` carries at least the average outside restoration demand. The cut therefore reduces arithmetic payment to one finite restoration family and its exact blocked physical/source neighbourhood.

### BDA5ew — reset boundary

Changed primitive weights, damping factors, compatibility, restoration addresses, hidden deposits, insufficient guard capacity or incomplete occurrence lineage returns reset or amplification.

## Finite audit

Run `python scripts/verify_bda_restoration_cut_decomposition.py`.

The audit checks 6,000 systems, 42,023 capacity classes, 20,866 restoration classes and 97,198 compatibility arcs. It verifies 38,017 paid and 34,872 unpaid potential units, 4,731 deficient systems, 16,780 outside restoration classes and barrier totals 15,878 physical plus 13,282 issued-source units.

## Scope

This does not prove the concrete BDA gain factors or pay the returned arithmetic cuts. It does not prove BDA6.
