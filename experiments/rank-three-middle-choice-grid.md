# Rank-three middle choice-grid diagnostic

This check accompanies
`docs/181-rank-three-middle-paid-choice-grid.md`.

Run:

```bash
python scripts/check_rank_three_middle_choice_grid.py \
  experiments/rank-three-middle-choice-grid-example.json
```

The stored instance has four predecessor choices and four disjoint successor
choices. All sixteen middle states are source-valid, and every state has one
local candidate incidence. The removal credit is one and all residual averages
are zero, so the normalized paid objective is exactly one rather than strictly
below one. The checker therefore returns the weighted-grid/projective-cover
branch.

The sixteen incidences are coloured by four candidates. Each candidate colours
one perfect matching between the predecessor and successor choice sets, verifying
the PP3zh geometry. The candidate lower bound is

```text
16/min(4,4)=4,
```

and is attained exactly.

Changing `removal_credit` to `2` exercises the paid-average-completion branch.
Adding enough source-invalid middle pairs so that
`|P||S|<=omega D_c` exercises the small-outer-core branch.

The diagnostic checks the finite choice-grid, paid-average, and candidate-cover
bookkeeping. It does not prove superregularity of the residual hosts or the
asymptotic residual source/cost bounds required by PP3acq.
