# Fixed-centre source degree-saving diagnostic

This check accompanies
`docs/190-fixed-centre-residual-source-degree-saving.md`.

Run:

```bash
python scripts/check_fixed_centre_source_degree_saving.py \
  experiments/fixed-centre-source-degree-saving-example.json
```

The stored instance has seven endpoint indices, captive centre `0`, block size
six, fourteen retained anchors, and a six-arc outgoing unary star at the centre.

The finite enumeration returns:

```text
anchored-pair degree through c: 117
rank-four triple degree:         16
rank-five triple degree:         76
rank-six triple degree:          18
```

The corresponding one-power-saving comparison scales are

```text
|anchors| D_m N + N^2: 1029
N^2:                       49
N^3:                      343
N^4:                     2401.
```

The diagnostic is intentionally finite and the theorem constants are
asymptotic, so the script uses a conservative absolute comparison constant.
It directly enumerates compatible cell pairs and three-arc partial
permutations, rejects proper directed cycles, and checks collinearity by an
integer determinant.

The unary table consists of

```text
0->1, 0->2, ..., 0->6.
```

Thus the marked unary degree is six, exceeding the displayed
credit-normalized diagnostic threshold, and the checker returns

```text
marked_centre_unary_star
```

with outgoing star size six. Deleting these six arcs exercises the
`residual_source_light` branch. Moving the same number of arcs to a vertex
different from the centre exercises the global unary-resource-star branch.

The normalized high-support load printed for this tiny instance is not expected
to be small: the theorem is asymptotic and uses a growing pool. The diagnostic
checks the exact enumeration, the one-power-saving degree scales, and the unary
handoff, not the asymptotic exponent limit.
