# Rational-inverse typed collision-segment localization

This note refines RI5fd--RI5fh on the complete physical-source/collateral/typed-demand network. It turns each owner/charge path collision into one canonical contiguous shared-capacity segment.

## Contract

Fix the canonical irreducible typed owner/charge core, its canonical split, the canonical cycle-cancelled integral unit paths paying both sides, and one named positive-pressure cut arc. A collision witness is one unit path from each side paired at one occupied capacity slot. Retain owner/charge type, owner, host, context, coherence, arithmetic occurrence, physical-source, collateral and compatibility fields.

## RI5fi--RI5fm

1. The two simple directed unit paths have a unique maximal common contiguous directed segment containing the collision arc.
2. The segment address retains entry, exit, complete edge word, both typed terminal addresses and the ordered side labels.
3. It is either a physical-source prefix followed by distinct outgoing edges, or an internal merge--shared-segment--split with distinct incoming and outgoing edges. Disjoint owner/charge terminal units force the segment to end before the terminal edge.
4. Grouping by complete typed segment signature preserves collision multiplicity. Among `M` witnesses with `Q` signatures, one typed signature occurs at least `ceil(M/Q)` times.
5. An arithmetic separation result excluding that source-prefix or internal collateral segment for the retained typed endpoints excludes the witness. Otherwise its capacity must be paid by the named physical lineage. Suppressed type fields or paths, merged collateral, changed arithmetic state or independent capacity reuse is a reset.

## Consequence

The remaining RI obstruction is one singleton owner/charge shortage or one completely addressed typed path pair sharing a canonical physical-source or collateral segment.

## Scope

This is conditional on the complete fixed typed network and canonical unit-path decomposition. It does not prove RI6 or the no-three-in-line conjecture.
