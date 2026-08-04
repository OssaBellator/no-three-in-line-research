# Threshold obstruction for all rolling window widths

`docs/689` proves the exact four-window obstruction for the forced primitive
minimum-batch alphabet. This chapter extends the separator and cyclic scheduling
bound to every rolling window width.

## PP3deu — Identity-free is the exact all-width legality criterion

Let the forced primitive alphabet be

```text
{I,P1,P2,P3,P4,P5},
```

where `I` is the identity layer and the five `Pi` are the legal score-zero layers
from the minimum hidden-mixture decomposition. The separating functional `Phi`
has `Phi(I)=-2` and `Phi(Pi)=0`, while every sum of legal permutation layers has
nonnegative score.

Consequently a forced-alphabet multiset of any positive width can be a legal-layer
sum only if it contains no identity layer. Conversely, an identity-free multiset
already consists of legal layers. Thus

```text
forced rolling window is legal iff its identity count is zero.
```

The checker verifies all 74,612 forced-alphabet multisets of widths one through
sixteen; the score argument proves the criterion for every width.

## PP3dev — Exact cyclic optimum at width `w`

A cycle of `K` minimum batches has length `8K`, with `3K` identity positions and
`5K` nonidentity positions. If the cyclic nonidentity gap lengths are
`g_1,...,g_(3K)`, then `sum_i g_i=5K`, and the number of legal width-`w` windows is

```text
sum_i max(0,g_i-w+1).
```

Concentrating all `5K` nonidentity positions in one gap maximizes this convex
quantity, giving the sharp formula

```text
L(K,w)=max(0,5K-w+1).
```

The exact minimum number of illegal windows is

```text
8K-max(0,5K-w+1).
```

A contiguous identity block attains the formula simultaneously for every width.
Exhaustive censuses for `K=1,2,3` verify all widths over 56, 8,008, and 1,307,504
identity-position sets. The checker also verifies the contiguous extremizer for
`K=1,...,64`.

## PP3dew — Wider rolling memory cannot conceal identity mass

For every fixed width `w`, the optimal legal-window density tends to `5/8`. For
linearly growing width `w=rho*K`, the limiting upper density is

```text
max(0,(5-rho)/8).
```

It decreases with `rho` and vanishes once `rho>=5`. Wider rolling windows therefore
make concealment no easier within the forced minimum alphabet. Progress requires
leaving that alphabet or using a genuinely unexposed, non-rolling geometric
operation.

The exact audit is `scripts/check_threshold_all_window_widths.py`.

## Evidence boundary

This is an algebraic and scheduling obstruction. It does not construct a hidden
geometric operation, prove a coordinate recurrence, or close the all-`n` theorem.
The next theorem identifier is `PP3dex`.
