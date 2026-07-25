# Target-cycle horizon diagnostic

Run

```text
python scripts/check_target_cycle_horizon.py \
  experiments/target-cycle-horizon-example.json
```

The stored parameters are

```text
R=10^12,
W=sqrt(R)=10^6,
xi=0.2,
alpha=0.02,
q=100.
```

The exact calculation gives:

```text
generations to threshold       203
generation/target ratio        0.000203
threshold defect             20000
actual defect                20098
overshoot                       98
defect/target ratio             0.020098
binary/R ratio                  0.000403909506
conservative star lower bound 3731714.598...
star/target ratio               3.731714...
outcome target_scale_alternating_cycle_boundary
```

The chosen `alpha` is below both `sqrt(xi/8)` and `xi/4`. The first threshold
crossing occurs after far fewer than `W` generations, its binary domain loss is
well below `xi R/4`, and a failed final unary margin would produce a source star
more than three times the target width.
