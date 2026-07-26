# Post-trade two-layer assignment diagnostic

Run

```text
python scripts/check_post_trade_two_layer_assignment.py \
  experiments/post-trade-two-layer-assignment-example.json
```

The stored source has two old permutation layers on eight rows and columns.  The
first trade deletes two edges from each old layer and inserts four replacement cells.
Every inserted cell is **cross-origin**: its column was freed from one old layer and
its row was freed from the other.

The post-trade source is nevertheless two-regular.  Alternating its components gives
two current perfect-matching layers.  The four inserted cells split into current
layer blocks of sizes one and three, so their layerwise square demand is

```text
1^2+3^2=10 <= 4^2=16.
```

The exact output is

```text
m 8
old layer sizes [8, 8]
deleted edges 4
inserted edges 4
cross-origin inserted edges 4
post-trade layer sizes [8, 8]
inserted post-trade layer blocks [1, 3]
layerwise square demand 10
global square budget 16
outcome automatic_post_trade_two_layer_assignment
```

This verifies PP3ath--PP3atk in a finite cross-wired model: pre-trade layer ancestry
is irrelevant, while the post-trade source automatically supplies the layer
partition required for sequential complete insertion cancellation.
