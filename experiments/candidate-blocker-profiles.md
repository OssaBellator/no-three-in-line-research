# Candidate blocker-cover diagnostics

This experiment accompanies
[`docs/58-candidate-blocker-cover-barrier.md`](../docs/58-candidate-blocker-cover-barrier.md).
Run

```bash
python scripts/analyze_candidate_blocker_profiles.py \
  certificates/prime-patching-small.json --block-size 4
```

For every labelled candidate cell, the analyzer removes the automatic controller
axis blocker and records:

- the number of additional source blocker pairs;
- how many additional pairs have zero, one, or two endpoints in the selected
  matching layer;
- the exact PP3cs probability that the full `4K`-edge deletion union covers all
  additional blockers;
- the expected numbers of blocker-safe and unsafe selected candidate cells.

## Additional blocker histograms

The number of labelled candidate entries with each additional-blocker count is
the same for the two matching layers; only the endpoint-layer profile changes.
For `r=4`:

| Side | Candidate entries | Additional-blocker histogram |
|---:|---:|---|
| 4 | 16 | `0:7, 1:7, 2:2` |
| 5 | 20 | `0:5, 1:12, 2:2, 3:1` |
| 6 | 24 | `0:7, 1:8, 2:9` |
| 7 | 28 | `0:2, 1:12, 2:14` |
| 8 | 64 | `0:5, 1:26, 2:26, 3:7` |
| 9 | 72 | `0:4, 1:25, 2:25, 3:11, 4:7` |
| 10 | 80 | `0:4, 1:25, 2:34, 3:17` |

Thus the axis-clean support is already a small minority in the stored examples.
At sides seven through ten it consists of only two to five labelled entries.

## Undeletable blocker pairs

A candidate is impossible for the selected layer if one additional blocker pair
has both endpoints in the other matching layer.  The counts are:

| Side | Layer 0 | Layer 1 |
|---:|---:|---:|
| 4 | 4 | 2 |
| 5 | 3 | 8 |
| 6 | 3 | 9 |
| 7 | 7 | 12 |
| 8 | 24 | 22 |
| 9 | 31 | 36 |
| 10 | 31 | 35 |

This layer dependence is invisible in the raw additional-blocker histogram and
shows why matching-layer choice remains a useful state variable.

## Exact safe/unsafe expectations

Each complete product state selects exactly `8K` patch cells.  The exact PP3cs
cover probabilities give:

| Side/layer | Expected safe | Expected unsafe | Total selected |
|---|---:|---:|---:|
| 4/0 | `6` | `2` | `8` |
| 4/1 | `7` | `1` | `8` |
| 5/0 | `6` | `2` | `8` |
| 5/1 | `43/10` | `37/10` | `8` |
| 6/0 | `31/6` | `17/6` | `8` |
| 6/1 | `19/5` | `21/5` | `8` |
| 7/0 | `23/7` | `33/7` | `8` |
| 7/1 | `15/7` | `41/7` | `8` |
| 8/0 | `10` | `6` | `16` |
| 8/1 | `21/2` | `11/2` | `16` |
| 9/0 | `143/18` | `145/18` | `16` |
| 9/1 | `125/18` | `163/18` | `16` |
| 10/0 | `1301/180` | `1579/180` | `16` |
| 10/1 | `203/30` | `277/30` | `16` |

These are expectations under the unconditioned random equipartition and full
36-state product measure.  They are not lower bounds for every deterministic
state.  They show that the product measure is centered far from retained-pair
cleanliness even in small cases.

## Consequence

Random partitioning successfully normalizes block membership, but it does not
correlate selected cells with deletion covers of their blocker matchings.  At the
prime-gap scale, the deletion fraction tends to zero, so every candidate with an
additional blocker has cover probability `o(1)`.

A viable constant-width architecture must therefore prune or correlate the
support before applying PP3ci or PP3bl.  Useful next objects are:

1. an axis-clean candidate support graph with equal-margin state realizations;
2. a blocker-demand graph whose endpoint neighborhoods can be clustered inside
   matching blocks;
3. protected trades targeted at the undeletable other-layer blocker pairs.