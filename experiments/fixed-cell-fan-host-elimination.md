# Fixed-cell fan host-elimination diagnostic

Run:

```bash
python scripts/check_fixed_cell_fan_host_elimination.py \
  experiments/fixed-cell-fan-host-elimination-example.json
```

The example contains two heavy-deletion regimes in one complete parent host.
The sparse regime deletes a matching and the checker exhaustively verifies that
the residual remains in the requested superregular parameter class.  The dense
regime deletes six cells at one left resource and is returned as a typed heavy
partner pencil with its accumulated weight.

The allowed outcomes are therefore a uniform residual host or a typed pencil.
An unclassified conditional Hall or endpoint-host result is rejected.
