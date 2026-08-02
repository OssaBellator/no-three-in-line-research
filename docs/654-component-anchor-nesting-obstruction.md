# Component anchor nesting obstruction

The canonical thirteen-pair saturated source has an incidence decomposition, but
its smallest components do not support independent anchor pairings. This chapter
records the exact obstruction.

## PP3czy — Two-pair components are internally unpairable

Let

```text
P=(9,4,7,3,0,1,12,8,11,10,2,6,5)
Q=(7,12,9,1,4,3,8,0,2,11,5,10,6).
```

The row-column incidence graph has component pair-sizes

```text
2,2,4,5.
```

For either two-pair component, no bijection from its `P` cells to its `Q` cells
has both distinct endpoint rows and distinct endpoint columns. For either `P`
cell, one candidate `Q` cell shares its row and the other shares its column.

## PP3czz — Exact internal matching counts

The numbers of valid anchor matchings confined to the four incidence components
are, in increasing component-size order,

```text
0,0,2,13.
```

Thus neither two-pair component can be anchored internally, while the larger
components have finite internal freedom.

## PP3daa — Sharp cross-component requirement

Every complete anchor pairing of all thirteen `P` cells to all thirteen `Q` cells
uses at least four cross-component pairs. The lower bound is sharp: exactly 104
complete anchor matchings use four cross-component pairs.

Therefore deleting either two-pair component cannot preserve an existing anchor
system by componentwise restriction. Any nested construction must globally reroute
at least four assignments or avoid such components.

The exact audit is `scripts/check_prefix_component_anchor_obstruction.py`.

## Evidence boundary

This is a finite combinatorial obstruction at the anchor-permutation layer. It
does not rule out global rerouting or a different infinite source family.
