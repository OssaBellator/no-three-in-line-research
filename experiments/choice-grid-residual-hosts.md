# Choice-grid residual-host diagnostic

Run:

```bash
python scripts/check_choice_grid_residual_hosts.py \
  experiments/choice-grid-residual-hosts-example.json
```

The finite example uses a complete balanced host of order eight and three
compatible two-cell local states.  The checker deletes the four used endpoint
resources, then exhaustively verifies the requested minimum-degree and
large-subset density conditions in every residual graph.  All residuals belong
to one common superregular parameter class, so the example rejects a separate
residual-host-failure output.

This diagnostic checks a finite instance only.  The theorem uses the uniform
bounded-vertex slicing argument and the existing superregular spread theorem.
