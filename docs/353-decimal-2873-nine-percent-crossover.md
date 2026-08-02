# Decimal-2873 nine-percent crossover

This chapter localizes where a uniform nine-percent divisor-cap improvement becomes sufficient for the unchanged fixed-pivot retained-order inequality. It does not prove such an improvement.

## PX1143 — uniform derivative bracket

Throughout the decimal-2873 slab, the fixed-pivot logarithmic margin derivative with respect to `log N` satisfies

`0.051 < M'(log N) < 0.054`.

The lower bound retains the exact negative correction term at its worst left-endpoint value. The upper bound drops that negative term.

## PX1144 — nine percent remains insufficient initially

At

`N = 10^(2873.0585)`,

the directed upper bound for the retained-order margin after a factor-`1.09` divisor improvement is below

`-0.0000025`.

Because the margin is increasing, the unchanged inequality with only a nine-percent improvement is insufficient throughout

`10^2873 <= N <= 10^(2873.0585)`.

## PX1145 — nine percent is sufficient after a short transition

At

`N = 10^(2873.0616)`,

the directed lower bound after a factor-`1.09` improvement exceeds

`0.0000095`.

The positive derivative then makes the same nine-percent improvement sufficient for every larger order in the decimal-2873 slab.

Therefore the unresolved crossover for the unchanged inequality lies inside the narrow exponent interval

`2873.0585 < log_10 N < 2873.0616`,

of width `0.0031` decimal exponent. Only the first approximately `6.16%` of the logarithmic slab can require an improvement larger than nine percent; the exact lower endpoint still requires approximately `9.7914%`.

## Verification

```bash
python scripts/verify_product_2873_nine_percent_crossover.py
```
