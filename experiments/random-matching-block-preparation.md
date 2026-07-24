# Random matching-block preparation diagnostics

This experiment accompanies
[`docs/56-random-matching-block-preparation.md`](../docs/56-random-matching-block-preparation.md).
It constructs the global labelled signature counts used by PP3cl and PP3cm before
choosing the matching-layer equipartition.

Run

```bash
python scripts/analyze_random_matching_block_preparation.py \
  certificates/prime-patching-small.json \
  --block-size 4 --delta 1/72
```

The analyzer uses the complete four-cell support of every source edge in every
reserved width-two interval.  Its `M` counts are deliberately deletion-blind:
source points are counted as possible fixed anchors even when the eventual block
state may delete them.  The reported values are therefore rigorous upper bounds,
not exact expected certificate masses after deletion-aware cleaning.

## Exact local-signature expectations

For `r=4`, the PP3cl value `L_*` on the stored matching layers is:

| Side | Layer 0 | Layer 1 |
|---:|---:|---:|
| 4 | `11` | `8` |
| 5 | `58/5` | `37/5` |
| 6 | `8` | `4` |
| 7 | `186/35` | `158/35` |
| 8 | `71/14` | `13/2` |
| 9 | `137/21` | `33/7` |
| 10 | `137/30` | `151/30` |

These values exceed one because the calculation exposes every possible local
candidate cell before pair-partition feasibility, retained-point deletion, or
clean-domain pruning is used.  PP3cl is an exact expectation for that signature
superset.

## Global deletion-blind profile counts

For the first cases with two labelled blocks, the counts are:

| Side/layer | `M1` | `Mh` | `M2` | `M11` | `Mh1` | `M21` | `M111` |
|---|---:|---:|---:|---:|---:|---:|---:|
| 8/0 | 163 | 70 | 93 | 177 | 57 | 462 | 0 |
| 8/1 | 163 | 72 | 91 | 173 | 30 | 483 | 0 |
| 9/0 | 208 | 77 | 138 | 209 | 33 | 627 | 0 |
| 9/1 | 208 | 82 | 133 | 214 | 39 | 651 | 0 |
| 10/0 | 224 | 89 | 167 | 290 | 48 | 776 | 0 |
| 10/1 | 224 | 91 | 165 | 288 | 45 | 770 | 0 |

`M111=0` here because `K=floor(n/4)=2`; there are no three distinct block
labels.

At `delta=1/72`, the resulting `G_delta` values range from roughly `1.4e5` to
`1.7e5` on sides eight through ten.  PP3cn therefore does not certify these
small examples.  This is expected: the bound counts all controlled signatures
instead of the much smaller set surviving the correlated four-edge deletion and
local clean-domain restriction.

## Interpretation

The experiment separates two tasks.

1. **Partition algebra is closed.**  PP3ck--PP3cn exactly convert global labelled
   signature counts into block-scale expectations, and the powers of `r` cancel.
2. **Geometric compression remains open.**  A useful asymptotic application must
   replace the deletion-blind `M` counts by deletion-aware counts or prove that
   most controlled signatures share a small number of source-edge patterns and
   are removed by local pruning or protected trades.

The most valuable next computation is therefore not a larger raw candidate
sweep.  It is an exact comparison, for each controlled signature class, between:

- the deletion-blind count used here;
- the probability that its source anchors survive the chosen four-edge deletion;
- the probability that its candidate cells survive the clean 36-state domain.

That comparison would quantify the gain available from PP2l inside the random
partition framework.