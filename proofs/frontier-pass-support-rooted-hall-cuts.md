# Frontier pass: SRR support-rooted Hall cuts

## Added

- SRR2fu support-key concentration of residual witness roots.
- SRR2fv exact rooted alternating Hall cut with deficit equal to the selected root count.
- SRR2fw numerical conditioned-key witness shortfall or a rooted missing rectangle of at least `m^2` pairs.
- SRR2fx concentration on one named conditioned compatibility predicate and one selected root.

## Executable audit

`python scripts/verify_srr_support_rooted_hall_cuts.py`

The deterministic audit checks 2,500 keyed systems, 50,128 vertices, 45,325 compatibility edges, 8,159 unmatched roots, 4,095 selected support-key roots, 9,661 closure vertices, numerical shortfall mass 5,050, 332 balanced-key cases, 1,294 rooted missing pairs and 821 pairs in the selected failed-predicate classes.

## Remaining

Construct the physical conditioned support/key/predicate dictionaries, prove their numerical bounds, and convert the support-key-predicate burden obstruction into payment, descent, or reset. The global conjecture remains open.