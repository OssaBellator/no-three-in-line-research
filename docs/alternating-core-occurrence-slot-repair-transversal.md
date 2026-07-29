# Alternating-core occurrence-slot repair transversal

## Contract

Fix a finite occurrence-faithful unit assignment graph `G=(U,S,E)` for one localized AC5 defect system. Every use and slot retains its complete physical-source, issued-source, certificate, layer, obstruction and defect address. Let `C` be the canonical least maximum-deficit Hall core from AC5eq--AC5eu, let

`delta = |C| - |N_G(C)| > 0`,

and order all use/slot incidences by their complete retained addresses.

A **repair extension** is a graph `G+=(U,S+,E+)` with `S subseteq S+` and `E subseteq E+`, together with an injective assignment `P:U -> S+` satisfying `(u,P(u)) in E+` for every use. New slots, new compatibility edges, changed physical fields and all deposits must remain explicitly addressed.

## Theorem block AC5ev--AC5ez

### AC5ev — missing-neighbour repair count

For every complete repair assignment `P`, define

`R_P(C) = {(u,P(u)) : u in C and P(u) notin N_G(C)}`.

Then `|R_P(C)| >= delta`.

Indeed, at most `|N_G(C)|` uses of `C` can be assigned inside the old neighbourhood, while `P` assigns all `|C|` core uses to distinct slots.

### AC5ew — genuine new compatibility

Every incidence in `R_P(C)` lies in `E+ \ E`. If `u in C` and `P(u) notin N_G(C)`, the old graph contained no edge from any core use to that slot, in particular no edge `(u,P(u))`.

### AC5ex — canonical repair transversal

Sort `R_P(C)` by the complete pair address and retain its first `delta` incidences. They form a canonical repair transversal with `delta` distinct core uses and `delta` distinct outside slots. Thus any complete repair supplies at least `delta` separately usable physical slot occurrences or compatibility restorations.

### AC5ey — class concentration

If every selected repair incidence has one exact physical creation or compatibility-restoration class from a finite dictionary of size `L`, one class carries at least `ceil(delta/L)` transversal incidences. The class label retains the source, certificate, layer and defect fields.

### AC5ez — failure and reset alternatives

A proposed repair is impossible if it exposes fewer than `delta` distinct outside slots compatible with the core. Hidden slots, omitted compatibility, occurrence splitting, slot reuse, relabelling, changed physical fields or unrecorded deposits do not count as repair; they return the first exact reset witness.

## Consequence

The abstract Hall deficit is converted into a finite physical target: construct `delta` distinct addressed repair slots/incidences for the returned core, pay them through named deposits, or prove that no complete repair extension exists.

This theorem is conditional on the complete fixed occurrence-slot graph and repair-extension contracts. It does not prove AC5, AC6 or the no-three-in-line conjecture.
