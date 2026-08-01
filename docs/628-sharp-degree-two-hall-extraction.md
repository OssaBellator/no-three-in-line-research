# Sharp degree-two Hall reserve extraction

`docs/622` obtains a six-resource completion core once three restricted forbidden
families are partial matchings. This chapter gives the sharp pool size forcing
such a core when each family has bipartite maximum degree two.

## Theorem PP3cwy — collision degree six

On one resource side, join two vertices when they share a neighbour in one of the
three forbidden families. A maximum-degree-two bipartite family contributes a
collision graph of maximum degree two. The union collision graph therefore has
maximum degree at most six.

Any independent set in this union restricts every forbidden family to a partial
matching.

## Theorem PP3cwz — thirty-six residual resources suffice

Every graph of maximum degree six on thirty-six vertices has an independent set
of size at least

```text
ceil(36/7)=6.
```

Applying this independently on both resource sides extracts six residual
resources per side on which all three forbidden families are partial matchings.
The six-resource completion theorem from `docs/622` then survives one additional
blocked cell.

Thus thirty-six residual resources, or thirty-eight resources before the local
pair consumes two, suffice.

## Theorem PP3cxa — sharpness at thirty-five

The threshold thirty-six is sharp under only the degree-two hypotheses. The
complete graph `K7` decomposes into three Hamilton cycles. Each cycle is the
collision graph of a bipartite forbidden family of maximum degree two.

Five disjoint copies of this construction give thirty-five resources whose union
collision graph has independence number five. Therefore no six-resource reserve
is forced at thirty-five.

The remaining source obligation is to prove the required degree-two restrictions
inside the actual asymptotic conditional host.
