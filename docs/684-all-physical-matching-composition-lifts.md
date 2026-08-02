# All-physical matching composition lifts

`docs/678` verifies every composition for twenty selected matching
representatives. This chapter removes the representative restriction by auditing
one deterministic optimal route for every physical minimum-crossing matching.

The canonical thirteen-pair source has exactly 104 minimum-crossing anchor
matchings. For each matching, consider both two-pair deletions

```text
{0,2} and {3,5}.
```

## PP3ddk — Uniform radius-four route census

For every one of the

```text
104 * 2 = 208
```

physical matching/deletion cases, the exact minimum surviving-anchor rerouting
distance is four.

Moreover, every case has exactly 144 optimal radius-four routes. Thus the route
count is uniform across all physical labelings, even though the coordinate
embedding rule is not known to be equivariant under the full incidence
automorphism group.

## PP3ddl — Deterministic route succeeds for every composition

In each physical case, select the lexicographically first optimal route. Apply the
established greedy primitive-direction insertion rule to every ordered composition
of eleven.

Every one of the

```text
208 * 2^10 = 212,992
```

route/composition pairs embeds successfully. No audited point set contains a
mixed-run collinear triple.

This gives a deterministic coordinate-safe selector on the complete family of 104
physical minimum-crossing matchings, not merely on orbit representatives.

## PP3ddm — Exact coordinate-bound distributions

For deletion `{0,2}`, the maximum coordinate over all 1,024 compositions for each
selected route has distribution

```text
120:52, 132:52.
```

For deletion `{3,5}`, the distribution is

```text
84:52, 132:52.
```

Thus exactly half of the physical matchings attain each coordinate bound in both
deletion cases.

`scripts/check_prefix_all_physical_compositions.cpp` reconstructs all 104
minimum-crossing matchings, computes all 144 optimal routes in every deletion case,
selects the first, and checks all 212,992 compositions.
`scripts/check_prefix_all_physical_compositions.py` compiles the kernel and verifies
the exact output census.

## Evidence boundary

The deterministic first route is now certified for every physical matching and
every composition. The other 143 optimal routes in each physical case are not all
audited, and no rule links successive reservoirs into an all-size recurrence.
