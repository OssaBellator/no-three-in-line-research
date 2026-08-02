# Fourteen-pair saturated anchor reservoir

`docs/648` proves that the canonical thirteen-pair source has no fourteen-pair
extension inside a complete bounded local neighbourhood. A global search outside
that neighbourhood finds a new saturated source at size fourteen. This chapter
certifies the source, its anchors, and every unary-run composition.

## PP3dat — Explicit saturated source on `14 x 14`

Let

```text
P = (8,6,2,3,10,13,5,12,1,0,4,9,11,7),
Q = (7,3,8,0,11,1,2,10,9,13,5,12,4,6).
```

The union of the two permutation graphs `(r,P[r])` and `(r,Q[r])` contains
twenty-eight distinct cells, has degree two in every row and column, and contains
no collinear triple.

This is a genuinely global witness: it lies outside the insertion-plus-one-
transposition neighbourhood exhausted in `docs/648`.

## PP3dau — Fourteen disjoint anchors and all compositions

Pair the `P`-cell in row `r` with the `Q`-cell in row `r+5 mod 14`. The pairing
permutation is

```text
(5,6,7,8,9,10,11,12,13,0,1,2,3,4).
```

These fourteen pairs partition all twenty-eight source cells and each pair has
distinct row and column resources.

The established greedy primitive-direction insertion rule succeeds for all

```text
2^13 = 8,192
```

ordered compositions of fourteen. Every collinear triple in an embedded point
set lies within one labelled run; there are zero mixed-run triples. The maximum
absolute coordinate over the complete audit is `100`.

## PP3dav — Single-cycle incidence and non-nesting

For this source, the incidence permutation `Q^{-1} o P` is one cycle of length
fourteen. Thus the two-regular row-column incidence graph has one component and
offers no proper component deletion that preserves a smaller saturated source.

The witness resolves the finite fourteen-pair existence question left open in the
canonical handoff, but it does not provide a nested extension rule or an infinite
family.

## Verification

- `scripts/check_prefix_saturated_anchor_reservoir_14.cpp` checks the source,
  anchor partition, all 8,192 compositions, coordinate bound, and incidence cycle.
- `scripts/check_prefix_saturated_anchor_reservoir_14.py` compiles the C++ audit
  and validates its exact certificate line.

## Remaining prefix obligation

A uniform construction for arbitrary pair count, or a recurrence linking the
finite eleven-, twelve-, thirteen-, and fourteen-pair sources while preserving
anchor compatibility, remains open.
