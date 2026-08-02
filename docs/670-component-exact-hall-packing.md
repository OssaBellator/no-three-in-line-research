# Component-exact Hall packing

The local resource-load certificate in `docs/664` applies Caro--Wei to the entire
motif overlap graph. This chapter records the exact decomposition available when
coordinate resource lists split that graph into bounded components.

## PP3dbu — Componentwise Caro--Wei certificate

Let `G` be the graph whose vertices are candidate motifs and whose edges join
motifs sharing at least one certified resource. Write its connected components as
`C_1,...,C_t` and let `d(v)` be the degree of `v` in `G`.

Then the number of pairwise resource-disjoint motifs is at least

```text
q_component = sum_i ceil(sum_{v in C_i} 1/(d(v)+1)).
```

This dominates the global rounded certificate

```text
ceil(sum_v 1/(d(v)+1)),
```

because rounding is performed separately after the exact component split.

The domination can be strict. Two disjoint three-vertex paths, represented by
resource sets

```text
{0}, {0,1}, {1}    and    {2}, {2,3}, {3},
```

have global Caro--Wei certificate three but componentwise certificate four.

## PP3dbv — Exact bounded-component packing

Independence number is additive across connected components:

```text
alpha(G) = sum_i alpha(G[C_i]).
```

Therefore, if every coordinate-derived overlap component has size at most a fixed
constant `B`, the exact motif packing number is computable by a finite local audit
on at most `B` motifs per component. No global maximum-degree or average-degree
loss is then necessary.

This is a host-auditable interface: the required input is only the finite resource
list of each motif. The overlap graph, its components, and each local independence
number follow exactly from those lists.

## PP3dbw — Two-stage Hall condition

After certifying `q` resource-disjoint motifs, retain the separate selected-centre
conflict graph from the earlier Hall interface. If its matching or vertex-cover
loss is at most `m`, the 28-resource condition follows whenever

```text
3q - m >= 28.
```

Thus a coordinate host with bounded overlap components may use exact local motif
packing first and the centre-conflict certificate second.

## Verification

`scripts/check_hall_component_resource_packing.py` exhausts all 54,263 multisets
of at most six nonempty resource types on four labelled resources. It verifies

```text
global Caro--Wei <= component Caro--Wei <= exact independence number,
```

finds exactly three strict component-rounding improvements, and finds the
component certificate exact in 50,387 cases.

## Evidence boundary

The theorem does not construct an asymptotic coordinate host. Promotion still
requires actual motif resource lists with uniformly bounded overlap components,
a selected-centre conflict bound, and both restricted degree-two conditions.
