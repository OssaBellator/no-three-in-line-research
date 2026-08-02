# All-physical prefix unit routes

`docs/678` verifies all compositions for twenty selected matching representatives.
This chapter removes the remaining physical-labelling gap for the all-unit
composition.

## PP3ddk — Deterministic route on all 104 matchings

The canonical thirteen-pair source has exactly 104 minimum-crossing anchor
matchings. For each matching and each two-pair deletion

```text
{0,2} and {3,5},
```

compute the exact radius-four rerouting set and select its lexicographically first
optimal route.

Every one of the resulting

```text
104 * 2 = 208
```

physical matching/deletion cases has rerouting distance exactly four.

## PP3ddl — All 208 all-unit lifts pass

Apply the established greedy primitive-direction insertion rule with one inserted
point on each of the eleven surviving anchors. Every deterministic route embeds
without a mixed-run collinear triple.

Thus the result is not inferred from incidence automorphisms or orbit
representatives: every physical matching is checked in its original coordinate
labelling.

The exact maximum-coordinate histograms are

```text
deletion {0,2}:
40:8, 50:20, 52:16, 58:4, 66:4, 84:52;

deletion {3,5}:
44:44, 47:8, 48:52.
```

## PP3ddm — Exact remaining prefix gap

The deterministic selector is now coordinate-certified for all 104 physical
matchings at the all-unit composition. The remaining finite gap is precisely the
extension from one unit on every route to all `2^10=1,024` ordered compositions
for every physical matching.

The existing representative audit covers those compositions on twenty selected
matchings. No coordinate-equivariance theorem currently transfers that result to
the other 84 physical matchings, and no all-size recurrence is proved.

## Verification

`scripts/check_prefix_all_physical_unit_routes.py` reconstructs all 104
minimum-crossing matchings, computes the lexicographically first optimal
radius-four route for both deletions, and performs all 208 coordinate insertions
and final collinearity audits.

## Evidence boundary

This is a complete finite coordinate result for one composition and one
deterministic route per physical matching. It is not arbitrary-composition
coverage, a uniform all-size selector, or a recurrence.
