# Inverse-layer extension diagnostic

Run:

```bash
python scripts/check_inverse_layer_extension.py \
  experiments/inverse-layer-extension-example.json
```

The checker first verifies that every scaled inverse layer

```text
x -> a/x  (mod p)
```

is a permutation and has no exact integer collinear triple.  It then solves
the complete second-layer line-capacity CSP using:

- secant-cell pruning;
- minimum-remaining-value branching;
- exact maximal-line capacities; and
- a perfect-matching Hall test at every search node.

The stored instance verifies:

```text
p=5:  extendable multipliers 1,2,3,4
p=7:  extendable multipliers 2,3,4,5
p=11: extendable multipliers 3,5,6,8
p=13,17,19,23,29,31: no multiplier extends
```

It also checks a `p=17` near-state whose two layers are individually
no-three and whose union has exactly one bad triple.  Complete fixed-layer
search proves that neither layer can be held fixed, so any repair must move
both permutations.

These are exact finite computations.  The diagnostic explicitly reports
that the asymptotic seed theorem is not proved.
