# Fixed-infrastructure allocation-termination diagnostic

Run

```text
python scripts/check_fixed_infrastructure_allocation_termination.py \
  experiments/fixed-infrastructure-allocation-termination-example.json
```

The stored process starts from the current fixed-infrastructure restart potential

```text
Theta_0=16.
```

Three consecutive allocation attempts fail, but each failure is converted into a
pool-compatible repair with positive designated credit.  The credits are

```text
2, 3, 1,
```

so the chronological potential values are

```text
16, 14, 11, 10.
```

The fourth attempt installs the patch.  No pool coordinate set, row set, numerical
label set, or candidate-cell universe changes between attempts; every newly activated
same-slot entry starts with zero anchor mass.

The expected output is

```text
initial potential 16
repair credits [2, 3, 1]
potential values [16, 14, 11, 10]
failed attempts 3
trivial failure bound 16
terminal outcome patch_installed
outcome monotone_fixed_infrastructure_allocation_termination
```

This is the finite integer-descent mechanism in PP3avj--PP3avk.  The first decrease
`16 -> 14` is the actual geometric activation-safe repair in
`fixed-pool-label-restart-potential.md`; later values exercise the abstract repeated
attempt theorem.
