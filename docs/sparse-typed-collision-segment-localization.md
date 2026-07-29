# Sparse typed collision-segment localization

This note refines SAS5lj--SAS5ln on the complete neutral-source/move/pair-completion network. It turns each typed path collision into one canonical contiguous boundary-neutral capacity segment.

## Contract

Fix the canonical irreducible typed pair/completion core, its canonical split, the canonical cycle-cancelled integral unit paths paying both sides, and one named positive-pressure cut arc. A collision witness is one unit path from each side paired at one occupied capacity slot. Retain pair/completion type, sign, boundary profile, neutral-source, move, compatibility and legality fields.

## SAS5lo--SAS5ls

1. The two simple directed unit paths have a unique maximal common contiguous directed segment containing the collision arc.
2. Its canonical address retains entry, exit, complete edge word, both typed terminal addresses and ordered side labels.
3. The segment is either a neutral-source prefix followed by distinct outgoing edges, or an internal merge--shared-segment--split with distinct incoming and outgoing edges. Disjoint pair/completion terminal units force the split before the terminal edge.
4. Grouping by complete typed segment signature preserves multiplicity. Among `M` witnesses with `Q` signatures, one signature occurs at least `ceil(M/Q)` times.
5. A sign, boundary-neutrality, move-legality or shareability argument excluding the retained segment excludes the witness. Otherwise its capacity must be paid from the named neutral-source lineage. Omitted legality fields or paths, merged moves, changed boundary state or independent neutral-capacity reuse is a reset.

## Consequence

The remaining SAS obstruction is one singleton pair/completion shortage or one fully addressed typed path pair sharing a canonical neutral-source or move segment.

## Scope

This is conditional on the complete fixed boundary-neutral network and canonical unit-path decomposition. It does not prove SAS6 or the no-three-in-line conjecture.
