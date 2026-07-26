# Critical square-root separated-helper diagnostic

Run

```text
python scripts/check_critical_square_root_helper_host.py \
  experiments/critical-square-root-helper-host-example.json
```

The stored scale is

```text
W=12,
N=W^2=144.
```

The independent branch places every stored positive support outside the first twelve
helpers, so those helpers form a support-free block.

For the rank-two obstruction, partition the 144 helpers into eleven cliques.  Any
independent set has size at most eleven.  The exact support count is 871, compared
with the PP3arr density threshold 78.  The graph has maximum degree 13 and a
67-edge matching, so both target-scale extraction mechanisms are visible.

For the rank-three obstruction, use the complete three-uniform hypergraph.  It has
487,344 edges, compared with threshold 1,107.6.  Fixing one pair leaves 142 disjoint
one-vertex petals.

The exact output is

```text
W 12
N 144
independent chosen helpers 12
independent selected supports 0
rank-two clique parts 11
rank-two support edges 871
rank-two density threshold 78.0
rank-two maximum degree 13
rank-two matching size 67
rank-three support edges 487344
rank-three density threshold 1107.6
rank-three fixed-pair petals 142
outcome critical_square_root_independent_or_target_support
```

This verifies the three exact outcomes of PP3arr--PP3art at the critical square-root
scale.
