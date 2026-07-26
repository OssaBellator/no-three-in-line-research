# Automatic layerwise coordinate-reservoir diagnostic

Run

```text
python scripts/check_automatic_layerwise_coordinate_reservoir.py \
  experiments/automatic-layerwise-coordinate-reservoir-example.json
```

The stored model uses

```text
m=10^20,
R=10^19,
W=3,000,000,000.
```

The target marked set is split between two permutation layers with sizes
`1.8*10^9` and `1.2*10^9`.  With helper constant two, the layer demands are

```text
6.48*10^18,
2.88*10^18.
```

Even after globally reserving `10^18` and `2*10^18` coordinates, the two layers
retain approximately `9.9*10^19` and `9.8*10^19` available indices.  The total
unscaled square demand is

```text
4.68*10^18 <= (3*10^9)^2=9*10^18.
```

The exact output is

```text
m 100000000000000000000
R 10000000000000000000
R to m ratio 0.1
W 3000000000
layer marked sizes [1800000000, 1200000000]
globally reserved [1000000000000000000, 2000000000000000000]
layer helper demands [6480000000000000000, 2880000000000000000]
layer available coordinates [98999999998200000000, 97999999998800000000]
total layer square demand 4680000000000000000
global square budget 9000000000000000000
outcome automatic_layerwise_coordinate_reservoir
```

This verifies PP3ata--PP3atd in a finite scale model: layerwise quadratic helper
demand remains below the global square budget and far below the ambient layer size.
