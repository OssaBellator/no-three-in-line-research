# Second-host raw-leaf elimination diagnostic

This diagnostic exercises the finite bookkeeping behind
`docs/270-second-host-explicit-leaf-elimination.md`.

Run:

```bash
python scripts/check_second_host_leaf_elimination.py \
  experiments/second-host-leaf-elimination-example.json
```

The stored example contains all three raw outcomes:

1. an independent zero-current-cost cycle;
2. dense current support;
3. dense source support.

For every block the checker verifies:

- `1<=r<=W`;
- at least `r^2` helpers;
- maximum role-domain loss at most `kappa r`;
- support rank at most three;
- buffered set size `ceil((kappa+1)r)`;
- at least `r` allowed buffered helpers per role;
- the sum-of-squares helper inequality; and
- rejection of any raw explicit-host-failure outcome.

The script is a finite regression check.  It does not prove the asymptotic
conversion theorems reached after dense current or source support.
