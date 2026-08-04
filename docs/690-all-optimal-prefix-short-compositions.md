# All-optimal prefix short compositions

`docs/684` certifies one deterministic optimal route for every physical matching
and all 1,024 ordered compositions of eleven. This chapter moves in the orthogonal
direction: it certifies every optimal route for the complete family of
compositions with at most three runs.

## PP3dec — Complete optimal-route family

The canonical thirteen-pair source has 104 minimum-crossing matchings. For each
matching and each deletion `{0,2}` or `{3,5}`, the exact rerouting distance is four
and the number of optimal routes is exactly 144.

Thus the complete physical optimal-route family contains

```text
104 * 2 * 144 = 29,952
```

matching/deletion/route cases.

## PP3ded — Every one-, two-, and three-run composition embeds

The number of ordered compositions of eleven with at most three parts is

```text
C(10,0)+C(10,1)+C(10,2) = 1+10+45 = 56.
```

Apply the established greedy primitive-direction insertion rule to every one of
the 29,952 optimal route cases and all 56 short compositions.

Every embedding succeeds. The exact audit size is

```text
29,952 * 56 = 1,677,312
```

route/composition pairs, with no mixed-run collinear triple.

This proves that the finite coordinate lift is not an artefact of the
lexicographically first route: every radius-four optimal rerouting survives the
entire one-, two-, and three-run composition family.

## PP3dee — Uniform coordinate bounds

Across all matchings, all 144 optimal routes, and all 56 audited compositions, the
maximum coordinate is

```text
delete {0,2}: 120,
delete {3,5}: 154.
```

The bound is uniform over all 104 physical matchings in each deletion class.

`scripts/check_prefix_all_optimal_short_compositions.py` derives a temporary exact
C++ kernel from the canonical all-physical composition checker and verifies the
full output census.

## Evidence boundary

This is complete for all optimal routes but only for compositions with at most
three runs. The remaining 968 compositions per route are not audited, and no rule
links the thirteen-pair source to larger reservoirs or yields an all-size
recurrence.
