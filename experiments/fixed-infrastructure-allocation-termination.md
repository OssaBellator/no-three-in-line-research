# Fixed-infrastructure allocation-termination diagnostic

Run

```text
python scripts/check_fixed_infrastructure_allocation_termination.py \
  experiments/fixed-infrastructure-allocation-termination-example.json
```

The stored process starts from the universal fixed pool-label potential

```text
Omega_0=155.
```

Four consecutive allocation attempts fail, but each failure is converted into a
pool-compatible repair with positive designated credit.  The credits are

```text
3, 11, 7, 19,
```

so the chronological potential values are

```text
155, 152, 141, 134, 115.
```

The fifth attempt installs the patch.  No pool coordinate set, row set, numerical
label set, or candidate universe changes between attempts.

The expected output is

```text
initial potential 155
repair credits [3, 11, 7, 19]
potential values [155, 152, 141, 134, 115]
failed attempts 4
trivial failure bound 155
terminal outcome patch_installed
outcome monotone_fixed_infrastructure_allocation_termination
```

This is the finite integer-descent mechanism in PP3avj--PP3avk.  The first decrease
`155 -> 152` matches the geometric fixed-pool diagnostic in
`fixed-pool-label-restart-potential.md`; later values exercise the abstract repeated
attempt theorem.
