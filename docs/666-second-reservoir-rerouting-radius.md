# Second-reservoir rerouting radius

`docs/660` supplies a second explicit fourteen-pair saturated source with incidence
component sizes `2,2,2,2,3,3`. This chapter determines the exact anchor-crossing
and deletion-repair structure of that reservoir.

Let

```text
P=(8,3,4,11,13,6,1,12,7,0,10,5,2,9),
Q=(4,11,8,3,7,12,13,0,1,6,2,9,10,5).
```

## PP3dbi — Exact component anchor counts

The six incidence components, ordered by their first row, are

```text
(0,2), (1,3), (4,6,8), (5,7,9), (10,12), (11,13).
```

Their internal valid-anchor matching counts are

```text
0, 0, 1, 1, 0, 0.
```

Thus all four two-pair components are internally unpairable, while each
three-pair component has a unique internal anchor matching.

## PP3dbj — Sharp eight-crossing anchor theorem

Every complete anchor matching uses at least eight cross-component assignments.
The bound is sharp: exactly 4,752 complete anchor matchings use eight crossings.

The four internally unpairable two-pair components force this larger crossing
budget. In particular, any component deletion or nesting rule must coordinate
anchors globally rather than restricting a componentwise system.

## PP3dbk — Complete two-component deletion audit

For each of the 4,752 minimum-crossing anchor matchings and each of the four
 two-pair components, delete that component and optimally repair the anchor
permutation on the twelve surviving rows. This gives 19,008 exact deletion cases.

The minimum Hamming-distance distribution is

```text
2:15744, 3:3072, 4:192.
```

The distribution is identical for each two-pair component:

```text
2:3936, 3:768, 4:48.
```

Therefore every minimum-crossing anchor system repairs after any two-pair
component deletion within assignment radius four. The lower bound two is attained
in 15,744 cases because the two surviving assignments that point into the deleted
component can often be rerouted without disturbing any additional assignment.

The exhaustive audit is
`scripts/check_prefix_second_reservoir_rerouting.py`.

## Evidence boundary

This is a finite exact theorem at the anchor-permutation layer. It does not lift
the repaired assignments into the integer insertion geometry, prove mixed-run
legality after rerouting, or produce an all-size recurrence.
