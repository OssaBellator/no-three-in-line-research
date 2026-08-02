# All-physical prefix composition lifts

`docs/678` audits one deterministic optimal route for twenty selected matching
representatives. This chapter removes the orbit-representative restriction and
checks the same selector on every physical minimum-crossing matching.

## PP3ddk — Uniform radius and route count on all physical cases

The canonical thirteen-pair source has 104 minimum-crossing anchor matchings. For
each matching, delete each of the two two-pair components

```text
{0,2} and {3,5}.
```

Across all

```text
104 * 2 = 208
```

physical matching/deletion cases, the exact minimum rerouting distance is four.
Moreover, every case has exactly 144 optimal radius-four routes.

Thus the combinatorial radius and optimal-route count are uniform on the full
physical family, not merely on selected orbit representatives.

## PP3ddl — Deterministic selector passes every composition

In each of the 208 cases, choose the lexicographically first optimal route. Apply
the established greedy primitive-direction insertion rule to all

```text
2^10 = 1,024
```

ordered compositions of eleven.

Every embedding succeeds with no mixed-run collinear triple. The exact audit size
is

```text
208 * 1,024 = 212,992
```

route/composition pairs.

This gives a deterministic coordinate-safe route selector for all 104 physical
minimum-crossing matchings and both deletion types.

## PP3ddm — Exact coordinate-bound distributions

For deletion `{0,2}`, the maximum coordinate over all compositions has distribution

```text
120:52, 132:52.
```

For deletion `{3,5}`, the distribution is

```text
84:52, 132:52.
```

The selector therefore has global audited maximum coordinate 132. Exactly half of
the physical matchings attain the smaller bound in each deletion case.

## Verification

`scripts/check_prefix_all_physical_compositions.cpp` reconstructs all 104
minimum-crossing matchings, computes the exact optimal rerouting family after both
deletions, verifies radius four and 144 optimal routes in every case, selects the
lexicographically first route, and checks all 212,992 compositions.

## Evidence boundary

The finite physical family is now complete for this deterministic selector. The
result still concerns the fixed thirteen-pair source: it does not lift every
optimal route, prove coordinate equivariance across source sizes, or produce an
all-size recurrence between reservoirs.
