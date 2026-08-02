# Component anchor nesting obstruction

The thirteen-pair saturated source from `docs/642` has incidence-component pair
sizes `2,2,4,5`. This chapter identifies why deleting whole components does not
produce a componentwise nested anchor construction.

## PP3czy — Every two-pair incidence component is internally unpairable

Let a source component contain two rows and two columns, with the `P` and `Q`
edges forming the two perfect matchings of the resulting `K_{2,2}`. No `P` cell
can be paired to a `Q` cell in the same component while using distinct rows and
distinct columns.

### Proof

For either `P` edge, one `Q` edge shares its row and the other shares its column.
These are the only two `Q` edges in the component. ∎

## PP3czz — The canonical source needs at least four cross-component anchors

For the canonical thirteen-pair source, the four incidence components have
internal compatible-anchor matching counts

```text
size 2: 0
size 2: 0
size 4: 2
size 5: 13.
```

Every complete anchor pairing therefore uses at least four cross-component
pairs. This lower bound is sharp, and exactly 104 complete anchor matchings use
four cross-component pairs.

### Proof

Each two-pair component contributes two `P` cells and, by `PP3czy`, neither can
be paired internally, giving the lower bound four. The bitmask assignment audit
in `scripts/check_prefix_component_anchor_obstruction.py` enumerates every legal
row-to-row anchor pairing, counts cross-component pairs, and finds minimum four
with 104 witnesses. ∎

## PP3daa — Whole-component deletion cannot preserve anchors locally

Any nested construction obtained by deleting one of the canonical two-pair
components must reroute anchors in at least one other component. In particular,
there is no componentwise anchor restriction map from the thirteen-pair source
to either induced eleven-pair source.

### Proof

All four `P` cells in the two unpairable components must send anchors outside
their own components. Deleting either component removes two sources and also
removes or invalidates cross-component targets, so the remaining anchor pairing
cannot be obtained by simply restricting independent componentwise matchings. ∎

## Evidence boundary

A uniform saturated family cannot rely on freely adding and deleting arbitrary
four-cycle components while keeping anchors local. It must avoid two-pair
components, or supply an explicit global rerouting rule with bounded cross-
component disturbance.
