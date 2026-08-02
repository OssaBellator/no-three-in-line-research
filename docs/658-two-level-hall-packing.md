# Degree-sequence Hall packing

`docs/652` gives a two-stage packing interface from a maximum motif-overlap degree
and a centre-conflict vertex-cover or matching bound. This chapter replaces the
coarse maximum-degree motif estimate by the full degree sequence.

## PP3dak — Caro–Wei motif packing

Let the candidate-motif resource-overlap graph have vertex degrees
`d_1,...,d_M`. It contains a resource-disjoint motif set of size at least

```text
q = ceil(sum_i 1/(d_i+1)).
```

### Proof

Choose a uniformly random ordering of the motifs and retain a motif when it
precedes all its neighbours. Motif `i` is retained with probability
`1/(d_i+1)`. The expected retained count is the displayed sum, so some ordering
attains at least its ceiling. ∎

## PP3dal — Average-degree corollary and sharpness

If the overlap graph has average degree `d_bar`, then

```text
q >= ceil(M/(d_bar+1)).
```

This follows from convexity of `x -> 1/(x+1)`. The degree-sequence and average-
degree bounds are sharp for disjoint unions of equal cliques, where every clique
contributes exactly one selected motif.

The degree-sequence form can be much stronger than a maximum-degree bound. For
the degree sequence consisting of nine zeros and ten nines, it certifies ten
motifs, while the maximum-degree-only estimate certifies only two.

## PP3dam — Two-stage centre-conflict certificate

After selecting `q` resource-disjoint motifs, there are `3q` intrinsically good
centres. If their certified cross-copy conflict graph is bipartite with maximum
matching number at most `m`, at least

```text
3q-m
```

centres remain. Thus the 28-resource Hall interface follows whenever

```text
3*ceil(sum_i 1/(d_i+1)) - m >= 28.
```

The required selected motif counts are ten for `m=0` or `m=2`, eleven for
`m=3` or `m=5`, and twelve for `m=6`.

## Verification

`scripts/check_hall_degree_sequence_packing.py` exhausts all 32,768 labelled
six-vertex graphs, checks the Caro–Wei and average-degree bounds against exact
independence numbers, checks clique equality cases, and verifies the two-stage
matching thresholds.

## Evidence boundary

The conditional host must still derive the motif degree sequence and a certified
centre-conflict matching bound from coordinates, while preserving the separate
source and host-defect degree-two restrictions.
