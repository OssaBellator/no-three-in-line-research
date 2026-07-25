# Rank-four binary Xi support diagnostic

This example checks PP3acc--PP3ach from
`docs/179-fixed-centre-rank-four-binary-xi-support-localization.md`.

Run:

```bash
python scripts/check_rank_four_binary_xi_support.py \
  experiments/rank-four-binary-xi-support-example.json
```

Here `N=8`, `b=4`, and one centre arc is fixed, so every supported remote arc
has exact probability

```text
kappa=(b-3)/((N-2)(N-3))=1/30.
```

The support has twelve arcs, hence expected selected support `12/30=2/5`.
This exceeds the residual slack `3/10`, so the support-avoidance criterion is not
certified by the finite first moment. Every typed tail/head degree is two, below
the supplied star threshold three. The greedy maximal matching has five arcs,
which exceeds the guaranteed lower bound `12/(2*3)=2`, so the checker returns the
remote partner-matching branch.

Deleting any four support arcs gives expectation at most `8/30=4/15<3/10` and
exercises the support-avoidance branch. Replacing the support by five arcs with a
common tail exercises the partner-resource-star branch.

This diagnostic verifies exact support normalization and finite graph
bookkeeping. It does not prove the residual source/paid estimates required by
PP3acd.
