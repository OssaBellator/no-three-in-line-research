# Rational-inverse typed occurrence-slot repair transversal

## Contract

Fix one finite typed owner/charge use graph `G=(U,S,E)` over faithful physical-source and collateral slots. Every use and slot retains owner or perturbation-charge type, target, secant/context, source, collateral, field and lineage addresses. Let `C` be the canonical least maximum-deficit core from RI5fs--RI5fw and set

`delta = |C| - |N_G(C)| > 0`.

A repair extension `G+=(U,S+,E+)` contains the old graph and admits an injective typed assignment `P:U -> S+`. New slots and compatibility incidences retain all arithmetic fields.

## Theorem block RI5fx--RI5gb

### RI5fx — typed missing-neighbour count

For

`R_P(C) = {(u,P(u)) : u in C and P(u) notin N_G(C)}`,

one has `|R_P(C)| >= delta`. The statement is type-blind in its counting but type-faithful in every retained address.

### RI5fy — genuinely new collateral compatibility

Every incidence in `R_P(C)` is in `E+ \ E`; otherwise its assigned slot would already lie in the old neighbourhood of `C`.

### RI5fz — canonical typed repair transversal

The first `delta` incidences in complete typed arithmetic order give distinct core uses and distinct outside slots. Owner and charge labels, source and collateral addresses, and all terminal fields are preserved.

### RI5ga — type/class concentration

Among the selected incidences, either owner or charge type occurs at least `ceil(delta/2)` times. More generally, partition into `L` exact arithmetic repair classes; one class carries at least `ceil(delta/L)` incidences.

### RI5gb — failure and resets

A repair exposing fewer than `delta` distinct outside compatible slots is impossible. Omitted owner/charge fields, changed terminal arithmetic, hidden collateral, splitting, relabelling, reuse or unrecorded deposits return an exact reset witness.

## Consequence

Every successful owner/charge repair must provide a typed transversal of `delta` genuinely new faithful collateral incidences. The remaining arithmetic task is to construct, pay or exclude that transversal.

This theorem is conditional on the complete typed use/slot and repair-extension contracts. It does not prove RI6 or the no-three-in-line conjecture.
