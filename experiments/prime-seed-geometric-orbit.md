# Prime-seed geometric orbit diagnostic

Run:

```bash
python scripts/check_prime_seed_geometric_orbit.py \
  experiments/prime-seed-geometric-orbit-example.json
```

For the verified `p=13` certificate, the checker validates all `16`
combinations of the eight square symmetries and layer swap.  Every transformed
state remains a saturated no-three seed and retains relative cycle partition

```text
[4,4,2,2].
```

Layer swap does not change the selected point set, so the geometric orbit has
eight distinct selected sets in this example.

The checker also verifies the explicit warning against arbitrary coordinate
relabeling:

```text
(1,1),(2,2),(3,3)     collinear
(1,1),(2,2),(3,4)     noncollinear
```

where the second triple is obtained by swapping row labels `3` and `4`.
Therefore algebraic row normalization is not a valid Euclidean symmetry of the
seed CSP.
