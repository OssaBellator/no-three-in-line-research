# Sparse typed occurrence-slot repair transversal

## Contract

Fix one finite typed pair/completion use graph `G=(U,S,E)` over faithful boundary-neutral physical-source and move slots. Every incidence retains pair or completion type, sign, boundary profile, legality, source, move and lineage fields. Let `C` be the canonical least maximum-deficit core from SAS5ly--SAS5mc and set

`delta = |C| - |N_G(C)| > 0`.

A repair extension `G+=(U,S+,E+)` contains the old graph and admits an injective typed neutral assignment `P:U -> S+`. New slots and compatibility incidences retain all boundary-neutral fields.

## Theorem block SAS5md--SAS5mh

### SAS5md — typed missing-neighbour count

For

`R_P(C) = {(u,P(u)) : u in C and P(u) notin N_G(C)}`,

one has `|R_P(C)| >= delta`.

### SAS5me — genuinely new neutral compatibility

Every incidence in `R_P(C)` lies in `E+ \ E`; otherwise its assigned source/move slot would already lie in the old core neighbourhood.

### SAS5mf — canonical typed repair transversal

The first `delta` incidences in complete boundary-neutral address order give distinct pair/completion uses and distinct outside neutral slots.

### SAS5mg — type/class concentration

Pair or completion type occupies at least `ceil(delta/2)` selected incidences. More generally, among `L` exact sign, profile, legality, source or move-creation classes, one class carries at least `ceil(delta/L)` pairs.

### SAS5mh — failure and resets

A repair exposing fewer than `delta` distinct outside compatible neutral slots is impossible. Omitted sign/profile/legality fields, hidden capacity, splitting, reuse, relabelling or unrecorded physical deposits return the first exact reset witness.

## Consequence

Every complete neutral execution repair must exhibit a deficit-sized transversal of genuinely new boundary-neutral source/move incidences. Construct, pay or exclude that transversal.

This theorem is conditional on the complete typed neutral use/slot and repair-extension contracts. It does not prove SAS6 or the no-three-in-line conjecture.
