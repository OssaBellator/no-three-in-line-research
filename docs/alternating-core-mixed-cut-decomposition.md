# Alternating-core residual mixed-cut decomposition

This note records AC5dh--AC5dl. It converts every unpaid cut in the physical/source/certificate/defect network into an exact finite barrier identity.

## Contract

Fix a finite ordered integral network with physical-source, issued-source and certificate capacity layers followed by defect-demand terminals. Compatibility arcs carry a guard capacity larger than total terminal demand plus all finite capacities. Capacity nodes are split into input/output copies. Use a fixed deterministic integral maximum-flow rule.

## Theorem block

### AC5dh — residual mixed-cut extraction

After maximum flow, let `R` be the vertices reachable from the source in the residual network. The split capacity edges crossing `R` define exact physical, issued-source and certificate barrier sets, while the defect terminals outside `R` define the unpaid defect side.

### AC5di — compatibility closure

No guarded compatibility arc crosses this finite cut. Hence every reachable upstream output has all compatible downstream inputs reachable, and every retained address is a genuine physical/source/certificate/defect address.

### AC5dj — exact unpaid identity

Let `X` be the defect terminals outside `R`, and let `B_phys`, `B_src`, `B_cert` be the three split-edge barrier sets. If `U` is total unpaid defect demand, then

`U = demand(X) - cap(B_phys) - cap(B_src) - cap(B_cert)`.

In particular, deficiency is exactly the strict physical inequality `demand(X) > cap(B_phys)+cap(B_src)+cap(B_cert)`.

### AC5dk — defect-address concentration

When `U>0`, `X` is nonempty and one exact defect class in `X` has demand at least `demand(X)/|X|`. Together with the three barrier lists, this gives a finite physical target for a local incidence or obstruction-class estimate.

### AC5dl — reset boundary

Changed compatibility, omitted capacity nodes, changed defect weights, a guard capacity too small to forbid compatibility cuts, hidden deposits or non-occurrence-faithful relabelling returns reset rather than payment.

## Finite audit

Run `python scripts/verify_ac_mixed_cut_decomposition.py`.

The deterministic audit checks 5,000 systems, 52,720 capacity classes, 17,561 defect classes and 122,397 compatibility arcs. It verifies 27,005 paid units, 34,372 unpaid units, 4,273 deficient systems, 15,304 outside defect classes and exact barrier totals 8,448, 7,717 and 6,746 at the physical, issued-source and certificate layers.

## Scope

This theorem does not prove the concrete AC5 physical incidence inequalities or AC5/AC6. It only exposes the exact cut those estimates must pay.
