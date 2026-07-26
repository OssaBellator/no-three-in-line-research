# Robust target-cycle absorption diagnostic

Run

```text
python scripts/check_target_cycle_robust_absorption.py \
  experiments/target-cycle-robust-absorption-example.json
```

The stored parameters are

```text
R=10^12,
W=10^6,
xi=0.2,
alpha=0.02,
q=100.
```

At the first target-cycle crossing, the conservative length upper bound is

```text
L=20,099.
```

The complete binary final-shadow allowance is therefore

```text
L(L-1)=403,949,702
         =0.000403949702 R,
```

far below the reserved quarter-margin `xi R/4=5*10^10`.  The conservative
source-star lower bound is

```text
3 xi R/(8L)=3,731,528.93...
```

or more than `3.73W`.

Two unary-loss cases are checked:

```text
direct case:
  unary loss       190,000,000,000
  total loss       190,403,949,702
  outcome          current_cycle_direct_absorption

star case:
  unary loss       210,000,000,000
  total loss       210,403,949,702
  outcome          super_target_final_source_star
```

No chord, feedback-hub, or alternate matching-state data enter either decision.
The checker reports `initial_base_certificate_or_scale_failure` only when the
binary budget or the target-star constant does not meet the theorem's robust
range.
