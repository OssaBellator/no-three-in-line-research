# Adaptive cascade budget diagnostic

Run

```text
python scripts/check_adaptive_cascade_budget.py \
  experiments/adaptive-cascade-budget-example.json
```

The stored instance uses

```text
R=10^12,
W_R=sqrt(R)=10^6,
d=100,
xi=0.2.
```

The explicit adaptive choice

```text
q=floor(sqrt(W_R/d))
```

gives `q=100`.  The exact diagnostic is:

```text
planned depth                         100
chosen marked subbank size           100
cumulative inserted-size bound     10000
cumulative/target ratio              0.01
binary domain bound              99990000
binary/R ratio                   0.00009999
guaranteed final-star lower bound 10000000
star/target ratio                     10
single-step self-recapture fraction 9.8e-11
joint trace scale                  0.0001
outcome  sub_square_root_target_star_preserved
```

The cumulative final-size bound is only one per cent of the target width, so its
square is a negligible fraction of `R`.  If final unary shadow still destroys a
margin, the pigeonhole star lower bound is ten times the target width.

The `joint_trace_scale` is the finite analogue of

```text
d q^3/Q_a=o(1),
```

with ambient marked-layer size `Q_a=R` in the stored example.  It verifies that
the same adaptive choice is compatible with simultaneous self-recapture
thinning across all planned generations.

The checker reports `finite_budget_or_host_failure` if the finite parameters do
not keep cumulative size below `sqrt(R)`, binary loss below the reserved margin,
the guaranteed star above target width, and the joint trace scale below one.