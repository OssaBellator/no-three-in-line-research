# Frontier pass: degenerate rational line charts

## Added

- GC4ay: determinant-zero charts are pair collisions or rationally dependent.
- GC4az: numerator and denominator degrees are bounded by the trajectory difference degrees.
- GC4ba: denominator-exception incidence is at most `pM`.
- GC4bb: complete degenerate-chart router.

## Corrected frontier

A coefficient-degenerate polynomial collinearity chart now returns either an exact pair-collision profile or a bounded-degree rational line-following family with a root-bounded exceptional set. Remaining work is to resolve persistent rational line families and construct the actual finite operation-chart dictionaries.

## Verification

`scripts/verify_gc_degenerate_rational_line_charts.py` checks rational dependence by cross multiplication and denominator root bounds.