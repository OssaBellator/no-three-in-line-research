# Geometric-cleaning frontier pass: polynomial charts

**Branch:** `research/geometric-cleaning`

## New theorem block

- **GC4at:** polynomial collinearity degree is at most the sum of the two difference-vector degrees.
- **GC4au:** nondegenerate chart incidence is at most `(p+q)M_p`.
- **GC4av:** exact coefficient-degeneracy profile and actual-degree sharpening.
- **GC4aw:** piecewise-polynomial chart capacities add after least-chart assignment.
- **GC4ax:** complete polynomial-event continuation.

## Executable check

`scripts/verify_gc_polynomial_collinearity_charts.py`

Equivalent local execution verified **32,000** polynomial trajectory charts, including finite-field root counts.

## Updated frontier

Affine and polynomial one-parameter line events have explicit capacities. Remaining work is to construct finite chart dictionaries for actual cleaning operations, bound chart count, degree, fibre multiplicity and top eligible weights, and pay coefficient-degenerate charts, non-polynomial events or returned Hall cores.