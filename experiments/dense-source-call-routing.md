# Dense-source call-routing diagnostic

Run:

```bash
python scripts/check_dense_source_call_routing.py \
  experiments/dense-source-call-routing-example.json
```

The stored instance exercises both paired-switch and fixed-centre filler calls and all
three permitted raw complete-support outcomes:

```text
independent_cycle
dense_current_support
dense_source_support
```

They route respectively to a source-valid joint state, a named current conversion, and
a directly paid canonical source structure.  Raw conditional Hall, alternating-host,
and role-host outcomes are rejected.

The diagnostic checks the finite call-matrix bookkeeping used by
`docs/277-paired-secant-source-host-leaf-elimination.md`; it does not replace the
asymptotic helper and source-mass theorems.
