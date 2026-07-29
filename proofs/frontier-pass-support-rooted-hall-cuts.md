# Frontier pass: OP support-rooted Hall cuts

## Added

- OP4gk support-key concentration of residual phase roots.
- OP4gl exact rooted alternating Hall cut with deficit equal to the selected root count.
- OP4gm numerical quotient-key source shortfall or a rooted missing rectangle of at least `m^2` pairs.
- OP4gn concentration on one named unit-sensitive compatibility predicate and one selected root.

## Executable audit

`python scripts/verify_op_support_rooted_hall_cuts.py`

The deterministic audit checks 2,500 keyed systems, 49,879 vertices, 44,919 compatibility edges, 8,283 unmatched roots, 4,122 selected support-key roots, 9,964 closure vertices, numerical shortfall mass 5,090, 315 balanced-key cases, 1,148 rooted missing pairs and 755 pairs in the selected failed-predicate classes.

## Remaining

Construct the physical phase support/key/predicate dictionaries, prove their numerical bounds, and convert the support-key-predicate residual/edit obstruction into payment, descent, or reset. The global conjecture remains open.