# Rank-three outer path-petal diagnostic

This check accompanies
`docs/182-rank-three-outer-disjoint-path-petal-bank.md`.

Run:

```bash
python scripts/check_rank_three_outer_path_petals.py \
  experiments/rank-three-outer-path-petals-example.json
```

The stored instance has ten endpoint indices, captive centre `0`, and one
exceptional middle index. Every other source-valid predecessor path has weight
four, above the heavy threshold three. Hence the heavy outer-role family has

```text
8*8=64
```

paths.

All weights lie in the dyadic interval `[4,8)`. The checker greedily selects four
paths whose index pairs are disjoint. Their noncentral typed resource sets

```text
{L_r,L_p,R_p}
```

are therefore pairwise disjoint, while every path shares only the centre resource
`R_0`. The stored target bank size four is attained exactly.

Adding at least six source-invalid predecessor pairs exercises the outer-transition
source-core branch. Adding three low-cost predecessors at one nonexceptional
middle index correctly violates the bounded-choice hypothesis.

The diagnostic verifies finite support, dyadic, and typed-resource extraction. It
does not establish the residual source/paid first moments required by PP3acy.
