# Superregular collision-segment localization

This note refines SRR2dt--SRR2dx on the complete physical-source/atom/burden network at one fixed conditioned threshold. It turns each paired burden-path collision into one canonical contiguous shared-capacity segment.

## Contract

Fix the canonical irreducible burden core, its canonical split, the canonical cycle-cancelled integral unit paths paying both sides, and one named positive-pressure cut arc. A collision witness is one unit burden path from each side paired at one occupied capacity slot. Retain candidate, threshold, conditioning, witness-atom, physical-source, compatibility and burden fields.

## SRR2dy--SRR2ec

1. The two simple directed unit paths have a unique maximal common contiguous directed segment containing the collision arc.
2. Entry, exit, complete edge word, both burden terminals and side labels form its canonical candidate/witness address.
3. The segment either begins at a physical source and later splits, or begins internally with distinct incoming edges and ends with distinct outgoing edges, giving a merge--shared-segment--split witness. Distinct burden terminals force the split before the terminal edge.
4. Grouping by complete segment signature preserves multiplicity. If `M` witnesses realize `Q` signatures, one signature occurs at least `ceil(M/Q)` times.
5. A geometric incidence, conditioning or witness-separation estimate excluding the retained segment excludes the witness. Otherwise its shared capacity must be paid by the named physical or atom lineage. Omitted witnesses or paths, merged atom capacity, changed conditioning or independent capacity reuse is a reset.

## Consequence

The remaining SRR obstruction is one singleton burden shortage or one fully addressed candidate/burden path pair sharing a canonical physical-source or witness-atom segment.

## Scope

This is conditional on the complete fixed conditioned network and canonical unit-path decomposition. It does not prove SRR2, SRR4 or the no-three-in-line conjecture.
