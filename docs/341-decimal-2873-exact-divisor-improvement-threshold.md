# Exact divisor-improvement threshold at decimal order 2873

The existing fixed-pivot certificate has directed retained-order margin

`-0.093413 < M_* < -0.093412`

at `N=10^2873`. Under the unchanged repair inequality, a multiplicative improvement `rho` contributes `log rho`, so the exact threshold is

`rho_* = exp(-M_*)`.

## PX1098 — directed threshold interval

Directed 100-digit arithmetic gives

`1.0979139 < rho_* < 1.0979151`.

The enclosing interval has width below `0.0000012`. Thus the missing improvement is approximately `9.7914%`, not merely an unspecified value between nine and ten percent.

## PX1099 — explicit insufficient factor

The factor `1.097913` is insufficient at the lower endpoint under the unchanged inequality. This follows from the upper directed margin plus the upper directed logarithm remaining negative.

## PX1100 — explicit sufficient factor

The factor `1.097916` is sufficient at the lower endpoint. The previously proved positive margin derivative then propagates this fixed-pivot improvement through the complete slab

`10^2873 <= N < 10^2874`.

This is a numerical target, not the missing interval-specific divisor theorem.

## Verification

```bash
python scripts/verify_product_2873_exact_improvement_threshold.py
```
