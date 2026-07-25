# Projective anchor covers yield resource banks

PP3aam--PP3aap turn a no-chain middle product into a cover by retained source
anchors. Each nonaxis anchor colours a matching between the predecessor and
successor middle sets.

The retained anchors themselves have strong resource structure. View the old
source as a bipartite graph between old rows and old columns, with one graph edge
for each retained source point. Saturation gives maximum degree two. Therefore
any anchor set splits into two row/column-disjoint matchings, one carrying at
least half of the assigned middle-pair incidences.

After this source matching is selected, the assigned blocker triples form a
three-partite hypergraph on anchors, predecessor middles, and successor middles.
A standard star/matching extraction yields either a rich fixed anchor or middle,
or a large family of blocker triples disjoint in all three labels. Thus a
projective middle cover rejoins the established source-star/resource-bank trade
interfaces.

## 1. Resource-disjoint anchor matching

Let `Z` be a set of distinct retained source anchors. Give each `z in Z` the
integer weight

```text
w_z=number of assigned middle pairs witnessed by z.
```

Represent `Z` as an edge set in the bipartite graph

```text
G_Z=(old rows, old columns; Z).
```

### Theorem PP3aaq -- PROVED

The anchor set `Z` is the disjoint union of two matchings

```text
Z=Z_0 union Z_1
```

in old row and column resources. Consequently one of the two matchings satisfies

```text
sum_{z in Z_j} w_z >= (1/2) sum_{z in Z} w_z.
```

#### Proof

The saturated source has exactly two points in every old row and column, so every
subgraph `G_Z` has maximum degree at most two. Each component is a path or an even
cycle because `G_Z` is bipartite. Alternating two edge colours on every component
partitions its edges into two matchings. The heavier colour class carries at least
half the total assigned incidence count. ∎

Thus projective-cover incidence may be concentrated on a resource-disjoint
retained anchor bank without asymptotic loss.

## 2. The anchor-middle blocker hypergraph

Fix the heavier anchor matching `Z_*`. For each `z in Z_*`, retain a set

```text
E_z subseteq P x S
```

of middle pairs assigned to `z`. By PP3aam, `E_z` is a matching between `P` and
`S`.

Form the three-partite, three-uniform hypergraph

```text
T={(z,p,s): z in Z_*, (p,s) in E_z}.
```

Put

```text
E=|T|=sum_{z in Z_*}|E_z|.
```

Every triple records one blocked transition `p->c->s` and one retained source
anchor witnessing it.

## 3. Star or fully disjoint blocker bank

### Theorem PP3aar -- PROVED

For every integer `D>=1`, at least one of the following holds.

1. Some anchor `z` belongs to at least `D` triples of `T`. Its `D` middle pairs
   form a matching between `P` and `S`.
2. Some predecessor middle `p` belongs to at least `D` triples, using `D` distinct
   anchors and `D` distinct successor middles.
3. Some successor middle `s` belongs to at least `D` triples, using `D` distinct
   anchors and `D` distinct predecessor middles.
4. There is a matching of at least

   ```text
   E/(3D)
   ```

   triples whose anchor, predecessor-middle, and successor-middle labels are all
   pairwise distinct.

The anchors in the fourth alternative are also pairwise disjoint in old row and
column resources.

#### Proof

If one of the three vertex classes has a vertex of degree at least `D`, the
corresponding star alternative holds. Otherwise greedily select one hyperedge and
delete every hyperedge sharing one of its three vertices. Fewer than `3D`
hyperedges are deleted per selection, so at least `E/(3D)` pairwise
vertex-disjoint triples are chosen.

For a fixed anchor, `E_z` is a matching, so the middle labels in the anchor-star
alternative are distinct. For a fixed middle, one anchor contributes at most one
incident triple by PP3aam, so the other labels in the middle-star alternatives are
distinct. Resource-disjointness of selected anchors follows from `Z_*`. ∎

## 4. Balanced quantitative extraction

### Corollary PP3aas -- PROVED

Suppose the original projective cover has `E_0` assigned nonaxis middle-pair
incidences. Then it contains one of:

1. a rich anchor, predecessor-middle, or successor-middle star of size at least
   a fixed positive constant times `sqrt(E_0)`;
2. a fully label-disjoint blocker bank of size at least a fixed positive constant
   times `sqrt(E_0)`, whose source anchors are pairwise old-row/column-disjoint.

#### Proof

PP3aaq leaves at least `E_0/2` incidences on `Z_*`. Apply PP3aar with

```text
D=ceil(sqrt(E_0/6)).
```

If a star occurs it has the displayed order. Otherwise the matching size is at
least

```text
(E_0/2)/(3D)=Omega(sqrt(E_0)).
```

Rounding affects only the absolute constant. ∎

In the balanced no-chain core with

```text
|P|,|S|=m^(1/2+o(1)),
```

one has `E_0=m^(1+o(1))` after lower-order collision and axis losses. Hence the
extracted star or matching bank has size

```text
m^(1/2+o(1)).
```

This exceeds the standard resource-bank scale `m^(19/40+o(1))`.

## 5. Revised projective-cover endpoint

### Corollary PP3aat -- PROVED

A large projective transition cover reduces to:

1. a rich retained-anchor matching of middle pairs;
2. a fixed predecessor- or successor-middle star witnessed by many
   resource-disjoint retained anchors;
3. a fully label-disjoint bank of blocked middle transitions with
   resource-disjoint source anchors;
4. paid collateral or source-host failure preventing the corresponding
   source-star/resource-bank trade.

The number of distinct anchors alone is no longer the endpoint. Saturation turns
that anchor population into explicit row/column-disjoint removal-credit banks.

This chapter treats incidence counts. Arbitrary real-valued blocker weights would
require a separate weighted matching statement and are not claimed here.
