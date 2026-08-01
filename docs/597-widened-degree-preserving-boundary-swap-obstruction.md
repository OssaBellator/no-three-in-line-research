# Widened degree-preserving boundary swap obstruction

`docs/585` found four sharp six-block repairs obtained by deleting three old
points.  `docs/591` showed that the three deleted row/column incidences cannot be
refilled directly.  This chapter enlarges the corrector by one further deleted
point and tests every resulting four-point degree-preserving swap.

### Theorem PP3ctj -- PROVED / FOUR-POINT SWAP ENUMERATION

For each of the four sharp repairs, delete one additional surviving point.  Match
the resulting multiset of four deficient columns to the multiset of four
deficient rows in every possible way.  Across the four repairs this produces
exactly `2112` distinct degree-preserving swap attempts.

#### Proof

The checker reconstructs the eight radius-32 five-block survivors, the four sharp
three-deletion extensions, and then enumerates every fourth deletion and every
multiset bijection between the induced row and column deficits.  Duplicate cells
and non-size-preserving insertions are discarded before the geometric test. ∎

### Theorem PP3ctk -- PROVED / WIDENED LOCAL SWAP OBSTRUCTION

None of the `2112` four-point swaps is no-three-in-line.

#### Proof

For every candidate, the checker restores the original point count and every
affected row and column degree, then exhaustively tests all point triples.
Every candidate has a collinear triple. ∎

### Theorem PP3ctl -- PROVED / MINIMUM STRUCTURAL ENLARGEMENT REQUIREMENT

A corrector based on the explicit side-four blocks must either alter at least two
further incidences beyond the sharp three deletions, insert points outside the
deleted degree support, or change the block geometry.

#### Proof

The three-deletion repair is sharp by `docs/585`.  Direct three-point refill fails
by `docs/591`, and every one-extra-incidence four-point swap fails by `PP3ctk`.
The listed alternatives exhaust the ways to leave this finite correction class. ∎

Run:

```bash
python scripts/check_boundary_widened_swap_obstruction.py
```

This is a finite coordinate obstruction, not an all-offset impossibility theorem.
