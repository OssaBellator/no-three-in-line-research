# Fourteen-pair saturated anchor reservoir

The local obstruction in `docs/648` applies only to the canonical thirteen-pair
source.  A deterministic global low-defect search reaches a different legal source
at size fourteen.

## PP3daq — Explicit global source

Let

```text
P=(8,3,4,11,13,6,1,12,7,0,10,5,2,9)
Q=(4,11,8,3,7,12,13,0,1,6,2,9,10,5).
```

The union of the two permutation graphs on `14 x 14` has twenty-eight distinct
cells, degree two in every row and column, and no collinear triple.

A deterministic search starts from a score-one pair, expands only valid states of
score at most four, and reaches this source at transposition depth fourteen after
scoring 884,907 distinct valid states.

## PP3dar — Fourteen anchors and all compositions

Pair the `P` cell in row `r` with the `Q` cell in row

```text
(1,0,3,2,5,4,7,6,9,8,11,10,13,12)[r].
```

These fourteen pairs partition all twenty-eight source cells and have distinct row
and column endpoints.  The established greedy primitive-direction insertion audit
passes all

```text
2^13 = 8,192
```

ordered compositions of fourteen.  Every mixed-run collinear triple is excluded,
and the maximum absolute coordinate over the full audit is 80.

## PP3das — Incidence components and finite nesting

The source incidence permutation has component sizes

```text
2,2,2,2,3,3.
```

Deleting any two-cycle component leaves an induced twelve-pair saturated source,
providing four such deletions.  Deleting either three-cycle component leaves an
induced eleven-pair saturated source.

The displayed anchor pairing is not component-respecting, and no componentwise
restriction supplies a nested anchor construction.  The source therefore gives
finite incidence nesting but not an anchor-compatible recurrence.

Exact checkers:

- `scripts/check_prefix_14_low_defect_search.cpp`
- `scripts/check_prefix_saturated_anchor_reservoir_14_components.cpp`
- `scripts/check_prefix_fourteen_pair_reservoir.py`

## Evidence boundary

Explicit saturated anchor reservoirs now exist at eleven, twelve, thirteen, and
fourteen pairs.  No uniform all-size construction or infinite family is proved.
