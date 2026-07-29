# Frontier pass: SAS support-rooted Hall cuts

## Added

- SAS5nk support-key concentration of residual neutral roots.
- SAS5nl exact rooted alternating Hall cut with deficit equal to the selected root count.
- SAS5nm numerical neutral-key shortfall or a rooted missing rectangle of at least `m^2` pairs.
- SAS5nn concentration on one named boundary-neutral compatibility predicate and one selected root.

## Executable audit

`python scripts/verify_sas_support_rooted_hall_cuts.py`

The deterministic audit checks 2,500 keyed systems, 49,928 vertices, 44,793 compatibility edges, 8,428 unmatched roots, 4,147 selected support-key roots, 9,851 closure vertices, numerical shortfall mass 5,172, 335 balanced-key cases, 1,209 rooted missing pairs and 782 pairs in the selected failed-predicate classes.

## Remaining

Construct the physical sparse support/key/predicate dictionaries, prove their numerical bounds, and convert the support-key-predicate neutral obstruction into payment, descent, reset, or a lineage witness. The global conjecture remains open.