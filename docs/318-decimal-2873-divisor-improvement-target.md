# Exact divisor-improvement target at decimal order 2873

PX966--PX969 prove that the current universal Euler-product divisor family misses
decimal order `2873` by a small amount. PX994--PX996 show that the classical
Nicolas--Robin subexponential estimate is not competitive in this range. This
chapter quantifies the remaining interval-specific arithmetic target.

Use the fixed exponent

\[
\alpha_* = \frac{\log 2}{\log 13033},
\]

which globally maximizes the universal-family retained-order margin at
`N=10^2873`. The exact Euler product is evaluated with directed 100-digit
arithmetic.

## 1. Exact lower-endpoint deficit

### Theorem PX1016 -- PROVED FINITE/ARITHMETIC

At `N=10^2873`, the divisor-controlled retained-order margin for the fixed-pivot
certificate satisfies

\[
-0.093413
< M_* <
-0.093412.
\]

More precisely, the directed interval is centered at approximately

`-0.0934127587875807661`.

Thus the current certificate fails by less than one tenth of a natural-log unit.
All four auxiliary repair margins are already positive at this order; only the
ambient-divisor loss blocks the reduction.

## 2. Nine percent versus ten percent

Suppose an interval-specific theorem improves the ambient divisor cap by a
multiplicative factor `rho>1`, so that the logarithmic retained-order margin
gains `log rho`.

### Theorem PX1017 -- PROVED FINITE/ARITHMETIC

A nine-percent improvement is insufficient:

\[
M_*+\log(1.09)<-0.0072.
\]

A ten-percent improvement is sufficient:

\[
M_*+\log(1.10)>0.0018.
\]

Therefore the exact multiplicative improvement threshold lies strictly between
`1.09` and `1.10`.

This is a modest target compared with replacing the entire divisor theorem. An
interval-specific reduction of the ambient divisor bound by ten percent would
close the lower endpoint of the missing decimal slab.

## 3. Persistence through the slab

### Corollary PX1018 -- PROVED REDUCTION

For the fixed exponent `alpha_*`, the retained-order margin derivative throughout
the slab beginning at `10^2873` has the explicit lower bound

\[
M_*'(\log N)>0.051.
\]

Consequently a uniform ten-percent improvement to this fixed-pivot divisor cap
through the interval

\[
10^{2873}\le N<10^{2874}
\]

would make the retained-order inequality hold everywhere in that slab. Orders at
or above `10^2874` are already covered by PX964--PX965.

Thus one exact finite-range bridge target is:

> prove a divisor estimate, or reduce the effective divisor loss in the repair
> inequality, by a uniform factor of `1.10` on the decimal-2873 slab.

A factor `1.09` cannot suffice at the lower endpoint under the unchanged
inequality.

This does not itself provide the required interval-specific estimate and does
not prove an all-side theorem.

## 4. Verification

```bash
python scripts/verify_product_2873_divisor_improvement_target.py
```

The verifier reconstructs the optimal pivot product, encloses the exact margin,
checks the nine- and ten-percent comparisons with directed rounding, and proves
the positive derivative bound.
