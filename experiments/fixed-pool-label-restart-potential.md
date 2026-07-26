# Fixed pool-label universal restart-potential diagnostic

Run

```text
python scripts/check_fixed_pool_label_restart_potential.py \
  experiments/fixed-pool-label-restart-potential-example.json
```

The stored saturated no-three source has two permutation layers on seven rows and
columns.  One controller layer contains a fixed pool rectangle with

```text
|X|=|Y|=5
```

and five movement and five refill labels.  A four-edge tied permutation changes the
controller pairing inside the pool while preserving the same column and row sets.
Both the initial and final sources remain saturated and no-three.

The fixed movement/refill candidate-cell universe has size 50.  Its excess-cell
potential changes from 59 to 55.  The complete latent same-slot anchor potential,
which counts every pair in `X x Y` rather than only the active controller matching,
changes from 96 to 97.  The actual active-matching anchor mass is much smaller:

```text
20 before the repair,
17 after the repair.
```

The exact pair and linear incidence terms are

```text
cell removal credit       67
cell insertion cost       63
anchor removal credit      0
anchor insertion cost      1
```

so the universal identity gives

```text
(63+1)-(67+0)=-3.
```

The direct potential values agree:

```text
Omega_initial=59+96=155,
Omega_final  =55+97=152.
```

The expected output is

```text
m 7
pool columns [0, 1, 2, 3, 4]
pool rows [0, 1, 2, 4, 5]
pool size 5
candidate cell universe 50
initial no-three True
final no-three True
actual anchor mass [20, 17]
latent anchor potential [96, 97]
excess cell potential [59, 55]
combined universal potential [155, 152]
cell removal and insertion [67, 63]
anchor removal and insertion [0, 1]
identity change -3
direct potential change -3
outcome fixed_pool_label_universal_restart_potential
```

This verifies PP3aux--PP3ava on an actual geometric source: controller pairings may
change, but the fixed coordinate-label universe and its exact dynamic potential do
not restart.
