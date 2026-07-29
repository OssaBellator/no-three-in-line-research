# Frontier pass: GC support-rooted Hall cuts

## Added

- GC2ml support-key concentration of residual donor roots.
- GC2mm exact rooted alternating Hall cut with deficit equal to the selected root count.
- GC2mn numerical donor-key shortfall or a rooted missing rectangle of at least `m^2` pairs.
- GC2mo concentration on one named geometric compatibility predicate and one selected root.

## Executable audit

`python scripts/verify_gc_support_rooted_hall_cuts.py`

The deterministic audit checks 2,500 keyed systems, 50,062 vertices, 44,529 compatibility edges, 8,737 unmatched roots, 4,200 selected support-key roots, 9,602 closure vertices, numerical shortfall mass 5,351, 334 balanced-key cases, 1,255 rooted missing pairs and 827 pairs in the selected failed-predicate classes.

## Remaining

Construct the physical geometric support/key/predicate dictionaries, prove their numerical bounds, and convert the support-key-predicate donor obstruction into payment, descent, or reset. The global conjecture remains open.