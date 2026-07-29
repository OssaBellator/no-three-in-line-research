# Superregular occurrence-slot repair transversal

## Contract

Fix one finite burden-use graph `G=(U,S,E)` over faithful candidate, witness-atom and physical-source slots at one exact conditioned threshold. Every incidence retains candidate, witness, threshold, conditioning, source and lineage fields. Let `C` be the canonical least maximum-deficit burden core from SRR2ei--SRR2em and set

`delta = |C| - |N_G(C)| > 0`.

A repair extension `G+=(U,S+,E+)` contains the old graph and admits an injective burden assignment `P:U -> S+`. Every new slot or compatibility edge retains complete candidate/witness lineage.

## Theorem block SRR2en--SRR2er

### SRR2en — missing-neighbour repair count

For

`R_P(C) = {(u,P(u)) : u in C and P(u) notin N_G(C)}`,

one has `|R_P(C)| >= delta`.

### SRR2eo — genuinely new candidate/witness incidence

Every pair in `R_P(C)` lies in `E+ \ E`. Thus each pair is a newly available candidate/witness slot or a genuinely restored compatibility incidence.

### SRR2ep — canonical repair transversal

The first `delta` pairs in complete conditioned address order form a canonical transversal with distinct burden uses and distinct outside candidate/witness slots.

### SRR2eq — witness/class concentration

If the selected pairs are partitioned into `L` exact candidate, witness-atom, threshold-conditioning or source-creation classes, one class carries at least `ceil(delta/L)` pairs.

### SRR2er — failure and resets

Fewer than `delta` distinct outside compatible slots cannot repair the core. Omitted candidates or witnesses, changed thresholds or conditioning, hidden capacity, splitting, relabelling, reuse or unrecorded source deposits return the first exact reset witness.

## Consequence

Every successful burden repair supplies a deficit-sized transversal of faithful candidate/witness incidences outside the old core neighbourhood. Construct them from the tensor reference, pay them from named capacity, or exclude them geometrically.

This theorem is conditional on the complete conditioned use/slot and repair-extension contracts. It does not prove SRR2, SRR4 or the no-three-in-line conjecture.
