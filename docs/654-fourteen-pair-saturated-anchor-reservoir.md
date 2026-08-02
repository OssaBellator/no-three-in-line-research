# Fourteen-pair saturated anchor reservoir

`docs/648` proves that the canonical thirteen-pair source has no fourteen-pair
extension inside a complete bounded local neighbourhood. A global search outside
that neighbourhood finds a new saturated source at size fourteen. This chapter
certifies the source, its anchors, and every unary-run composition.

## PP3czy — Explicit saturated source on `14 x 14`

Let

```text
P = (8,6,2,3,10,13,5,12,1,0,4,9,11,7),
Q = (7,3,8,0,11,1,2,10,9,13,5,12,4,6).
```

The union of the two permutation graphs

```text
(r,P[r]) and (r,Q[r]),  0 <= r < 14,
```

contains twenty-eight distinct cells, has degree two in every row and every
column, and contains no collinear triple. This is a genuinely global witness:
`docs/648` exhausts the insertion-plus-one-transposition neighbourhood of the
canonical thirteen-pair source and finds no source there.

## PP3czz — Fourteen disjoint anchors and all compositions

Pair the `P`-cell in row `r` with the `Q`-cell in row

```text
r+5 mod 14.
```

Equivalently, the pairing permutation is

```text
(5,6,7,8,9,10,11,12,13,0,1,2,3,4).
```

These fourteen pairs partition all twenty-eight source cells, and each pair has
distinct row and column resources. Apply the established greedy primitive-
direction insertion rule to every ordered composition of fourteen. All

```text
2^13 = 8,192
```

compositions embed successfully. Every collinear triple in the resulting point
set lies within one labelled run; there are no mixed-run triples. Across the
complete audit, the maximum absolute coordinate is `100`.

## PP3daa — Single-cycle incidence and non-nesting

For this source, the incidence permutation

```text
sigma = Q^{-1} o P
```

is one cycle of length fourteen. Hence the two-regular row-column incidence graph
has one component and offers no proper component deletion that preserves a
smaller saturated source. The witness advances the finite source frontier from
thirteen to fourteen pairs, but it does not provide a nested extension rule or an
infinite family.

## Comparison with the thirteen-pair source

The previous thirteen-pair source has component sizes `2,2,4,5`. Every two-pair
component is internally anchor-unpairable: for either `P` edge, one `Q` edge
shares its row and the other shares its column. A complete anchor pairing for that
source therefore requires at least four cross-component pairs; exactly 104
pairings attain the minimum. This explains why component deletion there requires
global rerouting, while the new fourteen-pair witness avoids the four-cycle issue
by using a single incidence cycle.

The comparison is checked by
`scripts/check_prefix_component_anchor_obstruction.py` and is supplementary to
the three canonical fourteen-pair theorems above.

## Verification

- `scripts/check_prefix_saturated_anchor_reservoir_14.cpp` checks the source,
  anchors, all 8,192 compositions, the coordinate bound, and the incidence cycle.
- `scripts/check_prefix_saturated_anchor_reservoir_14.py` compiles the exact C++
  audit and validates its certificate line.
- `scripts/check_prefix_component_anchor_obstruction.py` checks the older
  component-routing obstruction.

## Remaining prefix obligation

A uniform construction for arbitrary pair count, or a recurrence linking these
finite saturated sources while preserving anchor compatibility, remains open.
