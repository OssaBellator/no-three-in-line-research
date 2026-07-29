# Alternating-core repair-source compatibility Hall cores

## Contract

Fix a finite ordered repair epoch after the deficit-sized transversal and source-conservation steps. Let `R` be the unit set of selected defect-repair incidences and let `T` be the current unit set of live physical/source/certificate repair tokens. Every incidence and token retains its complete repair class and the complete geometric source, issued-source, certificate and defect fields.

Inside each conserved class, join `r in R` to `t in T` exactly when every retained compatibility predicate passes. Numerical class balance from the preceding conservation theorem is assumed: each class contains at least as many live tokens as selected incidences. No omitted field, hidden token, relabelling or multiplicity is allowed.

## Theorem block AC5ff--AC5fj

1. A complete occurrence-faithful source realization exists exactly when every incidence subset satisfies Hall's inequality.
2. If one class fails, choose the canonical positive-deficit subset by maximum deficit, then minimum size, then the complete incidence address. Every proper subset has smaller deficit, and a maximum matching of the core saturates its whole old token neighbourhood.
3. Classwise numerical sufficiency forces at least `delta` live same-class tokens outside that neighbourhood. The product of the core with those outside tokens is a complete missing-compatibility rectangle.
4. Assign each missing pair to its least failed retained predicate. One exact predicate carries at least a `1/q` share of the rectangle, where `q` is the number of retained predicates; one retained incidence carries at least the corresponding `1/q` share of the outside tokens.
5. The minimum number of newly validated source-incidence pairs needed for a complete injection is exactly the Hall deficit `delta`. Thus a deficit-sized repair transversal is source-realizable, or the theorem returns one canonical core, missing rectangle and named failed predicate.

The conclusion resets if a token, incidence, class label, predicate order, retained field or deposit history changes.

## Deterministic audit

Run:

```text
python scripts/verify_ac_repair_source_compatibility_hall_core.py
```

The fixed audit checks:

- systems: `2,600`
- conserved classes: `7,877`
- selected incidences: `23,412`
- live tokens: `31,294`
- old compatible pairs: `54,198`
- Hall subset checks: `87,945`
- complete systems: `698`
- deficient systems: `1,902`
- canonical deficient class cores: `2,916`
- deficit units / exact minimum new pairs: `3,599`
- missing-rectangle pairs: `17,326`
- proper-core checks: `13,598`

## Scope

This is conditional on the complete repair-source compatibility, field-dictionary and unit-token contract. It does not construct the concrete arithmetic or geometric compatibility predicates, prove the endpoint theorem for this track, or prove the no-three-in-line conjecture.
