# Alternating-core collision-segment localization

This note refines AC5eb--AC5ef on the same complete physical/source/certificate/defect network. It turns each cross-side unit-path collision into one canonical contiguous shared-capacity segment.

## Contract

Fix the canonical irreducible defect core, its canonical split `C=A disjoint_union B`, the canonical cycle-cancelled integral unit-path decompositions paying `A` and `B`, and one named positive-pressure cut arc. A collision witness consists of one side-`A` unit path and one side-`B` unit path paired at one occupied capacity slot of that arc. Every physical source, issued source, certificate, compatibility and defect field is retained.

## AC5eg--AC5ek

1. The two simple directed unit paths have a unique maximal common contiguous directed segment containing the named collision arc.
2. The segment is canonical from the ordered path pair and arc. It retains its entry vertex, exit vertex, complete edge word, both terminal defect addresses and the side labels.
3. Exactly one of two shapes occurs: the segment begins at the physical source, giving a shared-source prefix followed by distinct outgoing edges; or it begins internally, in which case the two incoming edges are distinct and the two outgoing edges are distinct, giving a merge--shared-segment--split witness. Distinct terminal units ensure the segment ends before the terminal edge.
4. Grouping collision witnesses by complete segment signature preserves multiplicity. If `M` witnesses realize `Q` signatures, one signature occurs at least `ceil(M/Q)` times.
5. A concrete geometric argument that forbids the retained source-prefix or internal merge--split segment for the two defect classes excludes that witness. Otherwise its shared capacity must be paid from the exact physical lineage. Omitted paths, merged capacities, changed physical state or independent capacity reuse is a reset.

## Consequence

The remaining AC5 obstruction is one singleton defect shortage or one fully addressed pair of defect paths sharing a canonical source prefix or internal physical/source/certificate segment.

## Scope

This theorem is conditional on the complete fixed network and canonical unit-path decomposition. It does not construct the geometric network or prove AC5, AC6 or the no-three-in-line conjecture.
