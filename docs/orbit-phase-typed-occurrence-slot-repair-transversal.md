# Orbit-phase typed occurrence-slot repair transversal

## Contract

Fix one finite typed residual/edit use graph `G=(U,S,E)` over faithful unit-sensitive physical-source slots. Every use and slot retains residual or edit type, unit class, valuation, holonomy, source and lineage addresses. Let `C` be the canonical least maximum-deficit core from OP4ey--OP4fc and set

`delta = |C| - |N_G(C)| > 0`.

A repair extension `G+=(U,S+,E+)` contains the old graph and admits an injective typed assignment `P:U -> S+`. New source slots and compatibility incidences retain all unit-sensitive fields.

## Theorem block OP4fd--OP4fh

### OP4fd — typed missing-neighbour count

For

`R_P(C) = {(u,P(u)) : u in C and P(u) notin N_G(C)}`,

one has `|R_P(C)| >= delta`.

### OP4fe — genuinely new source compatibility

Every pair in `R_P(C)` lies in `E+ \ E`; otherwise its slot would already belong to the old neighbourhood of the core.

### OP4ff — canonical typed repair transversal

The first `delta` pairs in complete unit-sensitive address order form a canonical transversal of distinct residual/edit uses and distinct outside source slots.

### OP4fg — type/class concentration

Residual or edit type occupies at least `ceil(delta/2)` selected pairs. More generally, among `L` exact unit, valuation, holonomy or source-creation classes, one class carries at least `ceil(delta/L)` pairs.

### OP4fh — failure and resets

A repair with fewer than `delta` distinct outside compatible source slots is impossible. Omitted unit/valuation/holonomy fields, hidden factor or source creation, splitting, reuse, relabelling or unrecorded deposits return the first exact reset witness.

## Consequence

Every complete residual/edit repair must construct a deficit-sized transversal of genuinely new unit-sensitive source incidences. The remaining task is to pay, construct or exclude that transversal.

This theorem is conditional on the complete typed source/use and repair-extension contracts. It does not prove OP5 or the no-three-in-line conjecture.
