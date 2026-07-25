# Recapture-free resource-bank diagnostic

This check accompanies
`docs/194-recapture-free-resource-bank-endpoint.md`.

Run:

```bash
python scripts/check_recapture_free_resource_bank.py \
  experiments/recapture-free-resource-bank-example.json
```

The stored instance has `q=100`, zero designated recapture support, source
local mass `0.001`, maximum foreign unary degree one, maximum foreign binary
degree ten, and high-support source objective `0.01`.

Its local support mass is

```text
0.001 + 1/100 + 10/(100*99)
= 0.0120101...
< 1/24.
```

The checker therefore returns `zero_insertion_paid_completion`.

Setting at least ten unary degrees to ten exercises the foreign unary linear
core.  Setting at least ten binary degrees to one thousand exercises the
foreign binary linear core.  Raising the source high-support objective above
one while keeping both degree families diffuse exercises source/host failure.

The diagnostic checks the finite support thresholds after designated
recapture has been removed.  It does not establish source regularity or the
ambient random-thinning theorem.
