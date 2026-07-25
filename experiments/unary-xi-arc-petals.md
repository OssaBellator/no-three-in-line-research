# Unary Xi arc-petal diagnostic

This check accompanies
`docs/183-fixed-axis-unary-xi-arc-petal-bank.md`.

Run:

```bash
python scripts/check_unary_xi_arc_petals.py \
  experiments/unary-xi-arc-petals-example.json
```

The stored instance has nine admissible incoming arcs into centre `0`. Every arc
has weight four, above the heavy threshold three. All arcs therefore lie in the
dyadic interval `[4,8)` and share only the centre resource `R:0`; their variable
resources `L:1` through `L:9` are distinct.

The checker extracts the requested four-arc bank. Its total local unary weight is
sixteen. With removal credit three and zero residual objective, the dyadic paid
upper bound is `8/3`, so the paid criterion is not certified. The failed paid
branch forces the lower bound

```text
(1/2)*3*4=6,
```

which the selected bank exceeds. The checker returns the global rank-two unary
threshold branch.

Changing `removal_credit` to `10` gives paid upper objective `8/10<1` and
exercises the paid arc-petal branch. Setting `residual_objective` to at least one
exercises the residual-concentration branch.

The diagnostic verifies finite dyadic and typed-resource bookkeeping. It does
not establish the residual source or centre-core averages required by PP3ade.
