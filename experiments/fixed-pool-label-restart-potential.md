# Fixed pool-label restart-potential diagnostic

Run

```text
python scripts/check_fixed_pool_label_restart_potential.py \
  experiments/fixed-pool-label-restart-potential-example.json
```

The stored saturated no-three source has two permutation layers on seven rows and
columns.  One controller layer contains a fixed pool rectangle with

```text
|X|=|Y|=5.
```

A four-edge tied permutation changes the controller matching inside that rectangle
while preserving the same column set, row set, and fixed numerical labels

```text
A=7,
B=9.
```

Both the initial and final sources remain saturated and no-three.

The fixed candidate-cell universe contains ten cells.  Its excess-shadow potential is
unchanged:

```text
Xi_cell: 14 -> 14.
```

The old controller matching has two active same-slot anchor incidences.  All four new
controller edges have zero anchor mass in the repaired source, and the inserted source
points create no anchor incidence for the one unchanged controller edge.  Hence

```text
Lambda_E: 2 -> 0.
```

The current restart potential therefore satisfies

```text
Theta_initial=14+2=16,
Theta_final  =14+0=14.
```

The fixed candidate-cell identity has equal removal and insertion terms,

```text
cell removal credit 16,
cell insertion cost 16,
```

so the complete decrease comes exactly from deleting old active anchor mass while
activating every new same-slot entry at zero mass.

The expected output is

```text
m 7
pool columns [0, 1, 2, 3, 4]
pool rows [0, 1, 2, 4, 5]
pool size 5
candidate cell universe 10
initial no-three True
final no-three True
new controller edges [(0, 4), (1, 1), (2, 5), (3, 2)]
new-edge anchor activation mass 0
inserted-anchor mass on kept edges 0
active anchor potential [2, 0]
excess cell potential [14, 14]
current restart potential [16, 14]
cell removal and insertion [16, 16]
direct potential change -2
outcome fixed_cells_zero_mass_anchor_activation
```

This verifies PP3aux--PP3ava in an actual geometric source.  Controller pairings may
change, but candidate cells remain fixed and every new anchor entry starts at zero
mass.
