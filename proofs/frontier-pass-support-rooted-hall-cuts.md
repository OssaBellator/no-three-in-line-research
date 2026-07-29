# Frontier pass: RI support-rooted Hall cuts

## Added

- RI5he support-key concentration of unmatched collateral roots.
- RI5hf exact rooted alternating closure with `N(A)=B` and deficit equal to the selected root count.
- RI5hg numerical key shortfall or a rooted missing rectangle of at least `m^2` pairs.
- RI5hh concentration on one named failed retained predicate and one selected root.

## Executable audit

`python scripts/verify_ri_support_rooted_hall_cuts.py`

The deterministic audit checks 2,500 keyed systems, 50,283 vertices, 45,911 compatibility edges, 8,198 unmatched roots, 4,072 selected support-key roots, 9,702 alternating-closure vertices, numerical shortfall mass 5,059, 330 balanced-key rectangle cases, 1,222 rooted missing pairs and 802 pairs in the selected failed-predicate classes.

## Remaining

Construct the physical arithmetic support/key/predicate dictionaries, prove their numerical bounds, and convert the returned support-key-predicate obstruction into collateral payment, monotone descent, or reset. The global conjecture remains open.