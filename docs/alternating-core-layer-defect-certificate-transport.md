# Alternating-core layer-defect certificate transport

This note records AC5cd--AC5ch. It replaces a direct geometric proof of every local layer ratio by one finite capacitated certificate problem.

## Contract

Fix one restricted-menu threshold after clearing a common denominator. Let `L` be the finite set of exact conditioned layers and let `d_l` be the nonnegative integral defect demand assigned to layer `l`. The previous weighted shortfall theorem bounds the aggregate menu deficit by `sum_l d_l`.

Let `A` be a finite dictionary of exact defect certificates. Certificate `a` has integral capacity `c_a`, one retained obstruction class, and a complete compatibility relation recording exactly which layer defects it can explain. Certificate use is occurrence-faithful and consumes capacity.

## AC5cd — exact defect-demand network

The layer demands, certificate capacities and complete compatibility relation form the capacitated network

`source -> layers -> certificates -> sink`.

Every integral flow retains the exact layer, certificate and obstruction-class address of every paid defect unit.

## AC5ce — capacitated Hall criterion

All layer defect is paid if and only if every layer subset `X` satisfies

`sum_{l in X} d_l <= sum_{a in N(X)} c_a`.

The unpaid defect is exactly the maximum positive Hall deficiency.

## AC5cf — canonical deficient certificate cut

When full payment fails, the least maximizing layer subset is a canonical exact defect-certificate cut. It retains the unpaid amount, all layer fields and the complete reachable certificate set.

## AC5cg — composition with the obstruction bank

When full payment succeeds, aggregate the used certificate capacity by its retained obstruction class. The resulting class load is bounded by the corresponding class capacity and may be debited directly from AC5az--AC5bd and AC5by--AC5cc. Thus a concrete certificate transport proves the desired layer-ratio payment without forgetting which obstruction paid it.

## AC5ch — reset boundary

Omitted compatibility arcs, fractional units without common-denominator scaling, certificate reuse without debit, changed layer fields, changed obstruction classes or cross-class cancellation are outside the theorem and return reset.

## Finite audit

Run:

`python scripts/verify_ac_layer_defect_certificate_transport.py`

The deterministic audit checks 7,000 finite capacitated systems, 20,969 layers, 20,964 certificates, 36,967 compatibility arcs and 56,716 Hall-subset tests.

## Scope

This theorem does not construct the physical certificate graph or prove its capacities. It reduces the remaining AC5 layer-ratio estimate to a finite exact transport problem and preserves the obstruction class needed by the existing capacity bank. It does not prove AC4, AC5, AC6 or the no-three-in-line conjecture.
