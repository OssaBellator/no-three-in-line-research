# Threshold all-window separator obstruction

`docs/689` gives the sharp rolling obstruction at window width four. This chapter
uses the separator itself to classify every window width and proves that increasing
rolling memory cannot conceal the forced identity mass.

## PP3dex — Forced-alphabet legality at every width

Let `Phi` be the separator matrix from `docs/683`. Every legal permutation layer
has nonnegative `Phi`-score. The five forced exposed types `P1,...,P5` have score
zero, while the identity layer has score `-2`.

Consider a multiset of `w>=1` layers from

```text
{I,P1,P2,P3,P4,P5}.
```

If it contains `h` identities, its aggregate matrix has score

```text
Phi = -2h.
```

When `h>0`, this score is negative, so the matrix cannot be decomposed into `w`
legal permutation layers, whose total score would be nonnegative. When `h=0`, the
listed `Pi` layers themselves are a legal decomposition. Therefore, for every
window width,

```text
a forced-alphabet endpoint is legal iff its window contains no identity layer.
```

The four-layer classification in `docs/689` is the width-four instance.

## PP3dey — Sharp cyclic formula for arbitrary width

A cyclic schedule of `K` minimum batches has `8K` positions, with `3K` identities
and `5K` exposed legal layers. Remove the identity positions and let
`g_1,...,g_t` be the lengths of the intervening identity-free gaps. Then

```text
sum_i g_i = 5K.
```

A gap of length `g` contains exactly

```text
max(0,g-w+1)
```

legal cyclic windows of width `w`. For fixed total gap length, the sum of these
terms is maximized by concentrating all `5K` legal positions in one gap. Hence

```text
maximum legal w-windows = max(0,5K-w+1),
minimum illegal w-windows = 8K-max(0,5K-w+1).
```

A contiguous identity block attains the formula simultaneously for every `w`.
For fixed `w`, the asymptotic legal density remains `5/8`. If
`w=rho K+O(1)`, the limiting legal density is

```text
max(0,(5-rho)/8).
```

Once `w>5K`, every rolling window is illegal.

## PP3dez — Exact finite audit and optimizer census

`scripts/check_threshold_all_window_widths.py` verifies the separator scores of
all 24 permutation layers and checks all 74,612 forced type multisets of widths
one through sixteen.

It then exhausts every identity-position set for `K=1,2,3` and every window width
from one through `8K`. The maximum agrees with `max(0,5K-w+1)` in every case. For

```text
2 <= w <= 5K,
```

there are exactly `8K` maximizing position sets: the cyclic translates of one
contiguous identity block. At `w=1`, every arrangement has exactly `5K` legal
windows; at `w>5K`, every arrangement has zero.

The isolated audit completes in about seventeen seconds. Wider rolling memory
therefore supplies no concealment mechanism. Any threshold advance must leave the
forced minimum alphabet or use a genuinely unexposed, non-rolling operation.

## Evidence boundary

This is an exact all-width obstruction for schedules whose primitive content is
the minimum equality alphabet. It does not exclude non-minimum hidden mass,
additional primitive types, or a geometric operation whose intermediate layers
are never exposed as endpoint matrices. The all-`n` theorem remains open.

The next theorem identifier is `PP3dfa`.
