# Threshold identity-window density

`docs/683` proves that every minimum hidden-mass equality batch has the same
primitive aggregate: three identity layers and five legal score-zero layer types
per eight primitive layers. This chapter determines the best possible rolling
four-window exposure density for any number of repeated minimum batches.

## PP3ddz — Exact four-layer type classification

Let `I` be the identity permutation and let `P1,...,P5` be the five legal
score-zero primitive types forced by the minimum equality aggregate. Consider any
four-layer multiset drawn from these six types.

There are

```text
C(9,4) = 126
```

such multisets. Exact comparison with the complete catalogue of 4,475 legal
four-layer matrices gives

```text
contains I: 56 multisets, 0 legal,
contains no I: 70 multisets, 70 legal.
```

Therefore a rolling four-layer endpoint built from the forced primitive alphabet
is legal exactly when its window contains no identity layer. The ordering and
multiplicities of the five legal types do not otherwise matter.

## PP3dea — Sharp density for `K` minimum batches

A cyclic schedule containing `K` minimum batches has

```text
8K total primitive positions,
3K identity positions,
5K legal-type positions.
```

A length-four cyclic window is illegal exactly when its start lies in the
three-step backward neighbourhood of the identity-position set. For any nonempty
set of `3K` positions on a cycle of length `8K`, the interval-neighbourhood
inequality gives at least

```text
3K+3
```

contaminated starts. Hence the number of legal four-windows is at most

```text
8K-(3K+3) = 5K-3.
```

This bound is sharp: place all `3K` identity layers in one contiguous block. The
remaining block of `5K` legal types has exactly `5K-3` length-four windows fully
inside it, and every such window is legal by `PP3ddz`.

Thus the exact optimum is

```text
maximum legal windows = 5K-3,
minimum illegal windows = 3K+3.
```

In particular, increasing rolling memory by repeating minimum batches cannot
remove a positive density of illegal exposure. The optimal asymptotic legal-window
density is

```text
lim_{K->infinity} (5K-3)/(8K) = 5/8.
```

## PP3deb — Exhaustive small-multiple census

`scripts/check_threshold_identity_window_density.py` reconstructs all 18 legal
permutation layers and all 4,475 legal four-layer matrices, verifies the complete
126-type classification, and exhausts all identity-position sets for `K=1,2,3`.

The maxima and numbers of maximizing position sets are

```text
K=1: maximum 2,  maximizers 8,
K=2: maximum 7,  maximizers 16,
K=3: maximum 12, maximizers 24.
```

The full legal-window histograms are

```text
K=1: 0:32, 1:16, 2:8,
K=2: 0:1456, 1:2160, 2:2016, 3:1360, 4:680,
     5:240, 6:80, 7:16,
K=3: 0:74336, 1:185472, 2:269760, 3:280192, 4:224808,
     5:145344, 6:76832, 7:33600, 8:12432, 9:3648,
     10:864, 11:192, 12:24.
```

Each maximum agrees with `5K-3`; the maximizing sets are the cyclic translates of
a contiguous identity block in these audited cases.

## Evidence boundary

This is a sharp obstruction for rolling four-layer schedules that retain the
minimum-equality primitive aggregate. It does not exclude larger endpoint windows,
a non-rolling hidden operation, a non-minimum hidden mass, or a construction that
leaves the six-type primitive alphabet.
