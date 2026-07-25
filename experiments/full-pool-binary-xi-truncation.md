# Full-pool binary Xi truncation diagnostic

This check accompanies
`docs/185-full-pool-binary-xi-truncation.md`.

Run:

```bash
python scripts/check_full_pool_binary_xi_truncation.py \
  experiments/full-pool-binary-xi-truncation-example.json
```

The stored instance has `N=8`, block size five, and every rank-three directed
path at the heavy threshold three. There are

```text
8*7*6=336
```

heavy rank-three patterns. Exactly 126 contain the marked centre and 210 do not,
so the marked-cycle expectation is

```text
126/(7*6) + 210*2/(7*6*5)
=
3+2
=
5.
```

This agrees with the fact that every five-cycle contains exactly five adjacent
two-arc paths. The maximum rank-three support degree is 126 at every vertex, so
the checker returns the rank-three fixed-centre core.

The rank-four table is below threshold. Changing `default_rank3_weight` from
three to one removes every heavy binary pattern; with residual objective zero,
the truncated paid criterion is then satisfied. Setting rank three below
threshold and rank four at threshold exercises the rank-four fixed-centre core.

The diagnostic verifies finite pattern enumeration, exact marked probabilities,
low-cost capacity, and support-degree concentration. It does not carry out the
subsequent fixed-centre conversions.
