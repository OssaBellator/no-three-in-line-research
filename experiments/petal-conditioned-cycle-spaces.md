# Arc/path petal conditioned-cycle diagnostic

Run:

```bash
python scripts/check_petal_conditioned_cycle_spaces.py \
  experiments/petal-conditioned-cycle-spaces-example.json
```

For a seven-vertex filler block, the checker enumerates every directed Hamilton cycle
with a fixed root representation.  It verifies:

- `(b-2)!` cycles containing one prescribed arc;
- `(b-3)!` cycles containing one prescribed two-arc path;
- the exact falling-factorial cylinder count for additional compatible forest arcs;
- the exhaustive endpoint set `paid_completion` or
  `typed_weighted_concentration`; and
- rejection of `host_failure` as a petal endpoint.

The enumeration checks the finite combinatorial identities used by
PP3bbo--PP3bbt.  It does not replace the asymptotic source and potential estimates.
