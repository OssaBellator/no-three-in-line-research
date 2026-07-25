# Thresholded fixed-cell fan diagnostic

Run

```text
python scripts/check_thresholded_fixed_cell_fan.py \
  experiments/thresholded-fixed-cell-fan-example.json
```

The stored residual host is the complete `4 x 4` bipartite graph.  The removal
credit is 20 and the reserved slack fraction is `1/2`, so PP3ago sets

```text
theta=(1/2)*20/(2*4)=5/4.
```

All four partner cells incident with the first left resource have multiplicity
2 and are heavy.  Every other partner cell has multiplicity 1 and is light.
Deleting the heavy cells isolates the first left resource, so the light host
has no perfect matching.  The checker returns

```text
heavy_hall_star
```

with maximum heavy resource degree four.

To exercise `paid_light_completion`, lower at least one weight in the first row
to 1.  A light perfect matching then exists, and its total fixed-cell fan cost
is at most

```text
n theta=tau C_a/2=5.
```

The finite diagnostic verifies the deterministic threshold budget and matching
branch.  Superregular inheritance, robust Hall, and candidate-set disjointness
are the asymptotic interfaces recorded in PP3agq--PP3agr.
