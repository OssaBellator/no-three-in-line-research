# Frontier pass: labeled RI conflicts

## Added

- RI5bz: exact center-plus-label partition of a heavy conflict neighborhood.
- RI5ca: one center or least conflict label retains at least a `1/(K+1)` fraction.
- RI5cb: finite sublabel refinements preserve an explicit `1/R` fraction.
- RI5cc: complete labeled conflict router.

## Corrected frontier

A failed requested RI subbank now returns a quantitatively heavy physical conflict label or sublabel, rather than an unlabeled neighborhood. Remaining work is class-specific overlap/owner/blocker payment, repeated-coset correlations, blocker repair and replenishable recurrence.

## Verification

`scripts/verify_ri_conflict_label_concentration.py` checks the partition and concentration bounds on exhaustive small and deterministic larger neighborhoods.