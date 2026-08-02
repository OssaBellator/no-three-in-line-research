# Two-level Hall packing

The Hall frontier has two distinct conflicts: candidate motifs may share resources,
and good centres from selected motifs may still be mutually incompatible.  This
chapter composes the two exact graph interfaces.

## PP3dak — Motif packing followed by centre packing

Let `G` be the resource-overlap graph on `M` candidate motifs, with maximum degree
`Delta`.  A greedy packing selects at least

```text
t = ceil(M/(Delta+1))
```

resource-disjoint motifs.  These motifs supply `3t` intrinsically good centres.

Let `H` be the certified conflict graph on those centres.  The maximum retainable
centre set has size

```text
alpha(H) = 3t - tau(H),
```

where `tau(H)` is the minimum vertex-cover number.  Hence the exact two-level Hall
condition is

```text
3*ceil(M/(Delta+1)) - tau(H) >= 28.
```

## PP3dal — Bipartite matching form

If `H` is bipartite, König's theorem gives `tau(H)=nu(H)`.  Under a proved matching
bound `nu(H)<=m`, it is enough to select

```text
q = ceil((28+m)/3)
```

motifs.  Therefore the sharp candidate-pool threshold becomes

```text
(q-1)*(Delta+1)+1.
```

For `Delta=2`, the exact thresholds are:

```text
m=0 or 2: 28 candidates,
m=3 or 5: 31 candidates,
m=6:      34 candidates.
```

## PP3dam — Graph-level sharpness

The motif threshold is sharp by a disjoint union of `q-1` cliques
`K_(Delta+1)`, whose independence number is exactly `q-1`.  On the selected
centres, a matching of size `m` has vertex-cover number `m`, so the retained count
is exactly `3(q-1)-m`.

Thus neither stage can be improved from maximum-degree and matching-number data
alone.

The combined checker is `scripts/check_hall_two_level_packing.py`; the exhaustive
six-vertex graph audit remains in `scripts/check_hall_conflict_graph_packing.py`.

## Evidence boundary

No conditional host has yet produced the required candidate motif family, bounded
resource-overlap degree, bipartite centre-conflict certificate, or the two
source/host-defect degree restrictions simultaneously.
