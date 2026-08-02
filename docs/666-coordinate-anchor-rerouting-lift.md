# Coordinate anchor-rerouting lift

`docs/660` proves that deleting either two-pair incidence component from the
canonical thirteen-pair source has exact anchor-rerouting radius four. This
chapter lifts one optimal rerouting through the established greedy integer
insertion rule.

## PP3dbi — A canonical four-assignment repair

For the canonical source

```text
P=(9,4,7,3,0,1,12,8,11,10,2,6,5)
Q=(7,12,9,1,4,3,8,0,2,11,5,10,6),
```

delete the two-pair incidence component with source rows `{0,2}`. The surviving
rows are

```text
1,3,4,5,6,7,8,9,10,11,12.
```

Start from the minimum-crossing anchor permutation

```text
(3,6,5,0,1,2,7,4,10,8,12,9,11)
```

on the thirteen rows. On the surviving rows, replace it by

```text
1->3, 3->1, 4->5, 5->6, 6->7, 7->4,
8->10, 9->8, 10->12, 11->9, 12->11.
```

Exactly the assignments of rows `1,3,4,5` change. The result is a valid anchor
bijection on the induced eleven-pair source and attains the proven minimum
rerouting distance four.

## PP3dbj — All eleven-pair compositions embed

Use the established greedy primitive-direction insertion algorithm with the
repaired anchors in increasing surviving-row order. Every ordered composition of
eleven embeds successfully. The complete audit contains

```text
2^10 = 1,024
```

compositions.

In every embedded point set, each collinear triple lies entirely within one
labelled run; no mixed-run triple occurs. The induced source has twenty-two cells,
two in every surviving source row and column resource.

## PP3dbk — Exact finite coordinate bound

Across all 1,024 compositions, the largest absolute coordinate used by the greedy
construction is

```text
132.
```

Thus one of the 144 optimal permutation-level repairs from the selected deletion
case has a complete coordinate realization. The earlier rerouting theorem is not
merely combinatorial in this instance.

## Verification

`scripts/check_prefix_coordinate_rerouting_lift.py` verifies the original
minimum-crossing matching, the four changed assignments, the induced source's
no-three property, all 1,024 compositions, and the coordinate bound.

## Evidence boundary

This is a finite `13 -> 11` lift for one component, one minimum-crossing matching,
and one optimal rerouting. It does not provide a uniform rule choosing among the
144 repairs, a lift for all 208 deletion cases, or a recurrence linking arbitrary
source sizes.
