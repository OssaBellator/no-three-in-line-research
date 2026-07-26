# Bounded marked permutation-layer embedding diagnostic

Run

```text
python scripts/check_bounded_marked_layer_embedding.py \
  experiments/bounded-marked-layer-embedding-example.json
```

The stored permutation layer has 30 tied endpoint indices and eight active
controllers.  The marked set has four indices, one of which is initially a
controller.  Puncturing that marked controller leaves seven active controllers.
After excluding the marked set and three additional forbidden helpers, the exact
controller-disjoint reservoir has size 16.

The chosen cycle is

```text
0,14,8,15,9,16,10,17,18,19.
```

It moves all four marked indices, has no marked-to-marked arc, uses no active
controller, and induces a permutation of all 30 layer indices after the remaining
indices are fixed.

The expected output is

```text
layer size 30
initial active controllers 8
bounded controller punctures 1
active controllers after puncture 7
controller-disjoint reservoir 16
marked indices [0, 8, 9, 10]
chosen helpers [14, 15, 16, 17, 18, 19]
marked-marked arcs 0
permutation image size 30
outcome bounded_marked_controller_disjoint_layer_embedding
```

This verifies PP3arj--PP3arl in a finite model: bounded puncturing leaves a large
helper reservoir, and the separated endpoint cycle preserves the permutation layer,
saturation, and every unpunctured controller.
