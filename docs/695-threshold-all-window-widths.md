# Threshold obstruction for every rolling-window width

`docs/683` identifies the forced primitive minimum batch: three identity layers
and one copy of each of five legal score-zero layers. `docs/689` proves the sharp
four-window obstruction. This chapter removes the fixed-width restriction and
computes the exact rolling-window optimum for every width.

## PP3der — Identity-free criterion at every width

Let the forced primitive alphabet be

```text
{I,P1,P2,P3,P4,P5},
```

where `I` is the illegal identity permutation and the five `Pi` are legal
score-zero permutations from the primitive equality identity. Use the separating
functional `Phi` from the threshold certificate. Every legal permutation layer
has nonnegative `Phi`-score, while

```text
Phi(I) = -2,
Phi(Pi) = 0.
```

Therefore a multiset of any width `w` drawn from the forced alphabet has score

```text
-2 * (number of identity layers).
```

If it contains an identity layer, its sum cannot equal a sum of legal permutation
layers, because every such legal sum has nonnegative score. If it contains no
identity layer, it is already a sum of the legal `Pi` layers. Hence, for every
window width,

```text
forced-alphabet window is legal
if and only if
it contains no identity layer.
```

This is an all-width separator theorem for the forced minimum alphabet. The audit
checks all 18 legal permutation layers and all 74,612 forced-alphabet multisets of
widths one through sixteen.

## PP3des — Exact cyclic optimum for width `w`

A cyclic schedule of `K` minimum batches has length `8K`, with exactly `3K`
identity positions and `5K` legal positions. Delete the identity positions and
write the lengths of the intervening cyclic legal gaps as

```text
g1,...,g_(3K),
```

so that

```text
sum_i gi = 5K.
```

A legal width-`w` window must lie wholly inside one legal gap. Thus the exact
number of legal cyclic starts is

```text
sum_i max(0, gi-w+1).
```

For fixed total gap length, this convex piecewise-linear expression is maximized
by concentrating all `5K` legal positions into one gap. Consequently the sharp
maximum is

```text
L(K,w) = max(0, 5K-w+1),
```

and the exact minimum number of illegal windows is

```text
8K - max(0, 5K-w+1).
```

A contiguous block of all `3K` identity layers attains the bound simultaneously
for every `w`. Exhaustive identity-position censuses for `K=1,2,3` verify the
formula at every width; they contain 56, 8,008, and 1,307,504 cyclic position sets.

## PP3det — Wider rolling memory cannot conceal the identity mass

For every fixed width `w`, the optimal legal-window density satisfies

```text
L(K,w)/(8K) -> 5/8
```

as `K` tends to infinity. Thus increasing the rolling memory from four to any
other fixed width does not improve the asymptotic legal exposure density.

More generally, for a linearly growing width

```text
w = rho K + O(1),
```

the optimal limiting density is

```text
max(0, (5-rho)/8).
```

It vanishes once the window width exceeds the complete legal mass of one minimum
batch aggregate. Hence no rolling-window mechanism confined to the forced
minimum alphabet can conceal the identity layers. Any successful threshold route
must leave that alphabet or use a genuinely unexposed, non-rolling geometric
operation.

The exact checker is `scripts/check_threshold_all_window_widths.py`.

## Evidence boundary

This is an exact algebraic and cyclic-scheduling obstruction. It does not exclude
larger endpoint alphabets, nonminimum equality batches, or geometric operations
whose intermediate states are never exposed. It does not provide an all-length
coordinate construction, and the all-`n` theorem remains open.
