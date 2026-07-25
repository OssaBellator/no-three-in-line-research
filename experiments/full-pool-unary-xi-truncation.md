# Full-pool unary Xi truncation diagnostic

This check accompanies
`docs/184-full-pool-unary-xi-truncation.md`.

Run:

```bash
python scripts/check_full_pool_unary_xi_truncation.py \
  experiments/full-pool-unary-xi-truncation-example.json
```

The stored instance has `N=10`, marked centre `0`, and block size `b=4`.
The heavy support is the nine-arc outgoing star at vertex `1`. One heavy arc is
incident with the marked centre and eight are nonincident, so the exact expected
number of selected heavy arcs is

```text
1/9 + 8*2/(9*8) = 1/3.
```

The truncation threshold is three, while

```text
tau*R/(4b)=0.3*160/16=3,
```

so the credit-normalized low-arc bound is `4*3/160=3/40`. With residual
objective `0.7`, the combined first-moment objective exceeds one. The maximum
heavy total degree is nine, all on the outgoing side, and the checker returns a
target heavy-arc star.

Changing `residual_objective` to zero makes the combined objective less than one
and exercises the paid heavy-arc-avoidance branch.

The diagnostic verifies the exact marked-cycle arc probabilities, truncation
budget, degree inequality, and oriented-star extraction. It does not establish
the residual source or binary paid estimates required by PP3adj.
