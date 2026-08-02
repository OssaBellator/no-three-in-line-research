# Coordinate anchor-rerouting lift

`docs/660` proves that deleting either two-pair incidence component from the
canonical thirteen-pair source has exact anchor-rerouting radius four. This
chapter lifts the complete optimal rerouting families for one canonical
minimum-crossing anchor matching through the established greedy integer insertion
rule.

## PP3dbi — Canonical matching and both component deletions

For

```text
P=(9,4,7,3,0,1,12,8,11,10,2,6,5)
Q=(7,12,9,1,4,3,8,0,2,11,5,10,6),
```

the lexicographically first anchor matching with the minimum four cross-component
assignments is

```text
(3,6,5,0,1,2,7,4,10,8,12,9,11).
```

Consider each two-pair incidence component in turn:

```text
{0,2} and {3,5}.
```

After either deletion, the exact minimum rerouting distance is four and there are
exactly 144 optimal anchor bijections on the eleven surviving rows.

## PP3dbj — All 288 optimal reroutings embed

For each of the two deletion cases and each of its 144 optimal reroutings, use the
established greedy primitive-direction insertion algorithm in increasing
surviving-row order. Every ordered composition of eleven embeds successfully.

Thus the exhaustive audit covers

```text
2 * 144 * 2^10 = 294,912
```

rerouting/composition pairs. In every embedded point set, every collinear triple
lies entirely within one labelled run; no mixed-run triple occurs.

This is stronger than a single coordinate witness: every optimal radius-four
repair for both component deletions is geometrically viable for the selected
minimum-crossing matching.

## PP3dbk — Exact coordinate-bound distributions

For deletion `{0,2}`, the maximum-coordinate distribution across the 144
reroutings is

```text
87:6, 89:1, 96:1, 98:3, 100:4, 102:11,
111:1, 115:2, 120:99, 132:15, 144:1.
```

For deletion `{3,5}`, it is

```text
84:7, 98:2, 99:13, 104:2, 108:2, 117:2,
132:71, 142:12, 144:12, 152:2, 154:16, 156:3.
```

The best audited coordinate bounds are therefore 87 and 84 respectively, while
the worst are 144 and 156.

## Verification

- `scripts/check_prefix_coordinate_rerouting_lift.py` checks one canonical lift
  and its 1,024 compositions.
- `scripts/check_prefix_rerouting_geometry.cpp` reconstructs the 104
  minimum-crossing matchings, chooses the canonical first matching, enumerates all
  144 optimal reroutings for each two-pair deletion, and checks all 294,912
  rerouting/composition pairs.

## Evidence boundary

This is a complete coordinate lift for both two-pair deletions of one canonical
minimum-crossing matching. It does not prove that all 104 minimum-crossing
matchings admit the same lift, provide a uniform selection rule for arbitrary
sources, or produce an all-size recurrence.
