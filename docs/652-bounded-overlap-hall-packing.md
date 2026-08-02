# Bounded-overlap Hall packing

This chapter consolidates the three concurrent Hall packing reductions into one
canonical two-stage interface. Candidate motifs may overlap in resources, and the
good centres retained after motif packing may still have cross-copy conflicts.

## PP3czs — Two-stage conflict-graph reduction

Let `G` be the resource-overlap graph on `M` candidate four-centre motifs, with
maximum degree `Delta`. Then `G` contains an independent set of at least

```text
q = ceil(M/(Delta+1))
```

resource-disjoint motifs. These motifs supply `3q` intrinsically good centres.
Let `H` be the graph on those centres, joining two centres exactly when a
certified cross-copy conflict prevents their simultaneous use. The maximum
retainable Hall pool is

```text
alpha(H) = 3q - tau(H),
```

where `tau(H)` is the minimum vertex-cover number. Hence the 28-resource
interface holds exactly when

```text
3*ceil(M/(Delta+1)) - tau(H) >= 28.
```

The first packing bound follows by greedy closed-neighbourhood deletion; the
second identity is the complement relation between independent sets and vertex
covers.

## PP3czt — Matching and edge certificates

If `H` is bipartite, König's theorem gives `tau(H)=nu(H)`, where `nu(H)` is its
maximum matching number. The exact condition becomes

```text
3*ceil(M/(Delta+1)) - nu(H) >= 28.
```

For an arbitrary certified conflict graph with `E` edges, `tau(H)<=E`, so

```text
3*ceil(M/(Delta+1)) - E >= 28
```

is always sufficient. A matching of `e` independent corruption edges recovers
the earlier `3q-e` law exactly.

## PP3czu — Sharp candidate threshold under a matching bound

Assume `H` is bipartite with `nu(H)<=m`. The least selected motif count certified
by the interface is

```text
q = ceil((28+m)/3),
```

and the sharp candidate-pool threshold under only the motif-overlap degree bound
is

```text
M = (q-1)*(Delta+1) + 1.
```

The motif threshold is sharp by a disjoint union of `q-1` cliques
`K_(Delta+1)`. The matching loss is sharp when `H` is a matching of size `m`.
For `Delta=2`, the candidate thresholds are 28 for `m=0` or `m=2`, and 31 for
`m=3`.

## Verification

- `scripts/check_hall_overlap_packing.py` checks the sharp motif-overlap threshold.
- `scripts/check_hall_conflict_graph_packing.py` verifies `alpha+tau=n` on all
  labelled six-vertex graphs and `tau=nu` on every bipartite member.
- `scripts/check_hall_cross_copy_conflict_packing.py` checks the degree-only
  centre-conflict specialisation and clique sharpness models.

## Evidence boundary

This is an exact combinatorial pipeline. The conditional host must still generate
candidate motifs with a proved overlap bound, certify every cross-copy failure in
`H`, and retain the separate source and host-defect degree-two restrictions on
the selected centres.
