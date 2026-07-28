# Orbit-phase typed collision-segment localization

This note refines OP4ej--OP4en on the complete shared-source residual/edit network. It turns each typed path collision into one canonical contiguous unit-sensitive capacity segment.

## Contract

Fix the canonical irreducible typed residual/edit core, its canonical split, the canonical cycle-cancelled integral unit paths paying both sides, and one named positive-pressure cut arc. A collision witness is one unit path from each side paired at one occupied capacity slot. Retain residual/edit type, unit class, valuation, holonomy, source, compatibility and quotient-state fields.

## OP4eo--OP4es

1. The two simple directed unit paths have a unique maximal common contiguous directed segment containing the collision arc.
2. Its canonical address retains entry, exit, complete edge word, both typed terminal addresses and ordered side labels.
3. The segment is either a physical-source prefix followed by distinct outgoing edges, or an internal merge--shared-segment--split with distinct incoming and outgoing edges. Disjoint residual/edit terminal units force the split before the terminal edge.
4. Grouping by complete typed segment signature preserves multiplicity. Among `M` witnesses with `Q` signatures, one signature occurs at least `ceil(M/Q)` times.
5. A valuation, holonomy, unit-class or legality separation excluding the retained segment excludes the witness. Otherwise its shared capacity must be paid from the named source lineage. Suppressed unit fields or paths, merged sources, changed quotient state or independent capacity reuse is a reset.

## Consequence

The remaining OP obstruction is one singleton residual/edit shortage or one fully addressed typed path pair sharing a canonical source segment.

## Scope

This is conditional on the complete fixed unit-sensitive network and canonical unit-path decomposition. It does not prove OP5 or the no-three-in-line conjecture.
