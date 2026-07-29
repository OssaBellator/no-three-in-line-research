# RI frontier pass: heavy conflict neighborhoods

**Branch:** `research/rational-inverse-expansion`

## New theorem block

- **RI5bv:** maximal independent closed neighborhoods cover the component inventory.
- **RI5bw:** failure of a `q`-component subbank concentrates at least `W/(q-1)` paid weight on one closed conflict neighborhood.
- **RI5bx:** the heavy neighborhood splits into an individually heavy component or a heavy cloud of small conflicts.
- **RI5by:** complete requested-bank versus heavy-neighborhood versus local-readiness router.

## Executable check

`scripts/verify_ri_conflict_neighborhood_concentration.py`

Equivalent local execution verified **11,235** maximal-independent-set neighborhood inequalities.

## Updated frontier

The extraction gap is now local. Remaining RI work is to pay or ticket one heavy conflict neighborhood by its least overlap, cross-constraint, owner, occurrence or exterior-field labels; close repeated-coset correlations and blocker repair; and control replenishable-source recurrence.