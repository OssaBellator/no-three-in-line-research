# Blocker-cover state-domain diagnostics

This experiment accompanies
[`docs/59-blocker-cover-state-domains.md`](../docs/59-blocker-cover-state-domains.md).
Run

```bash
python scripts/analyze_blocker_cover_state_domains.py \
  certificates/prime-patching-small.json
```

For one complete matching layer, the analyzer enumerates every four-edge
deletion and all 36 width-two degree geometries.  It counts the domains obtained
by imposing:

- internal no-three geometry of the eight patch points;
- local coverage of every retained-pair source blocker;
- avoidance of every retained source anchor on a patch secant;
- all three conditions simultaneously.

## Counts

The total number of states is `36 binom(n,4)` per layer.

| Side | Layer | Total | Internal patch clean | Blocker-cover clean | Anchor clean | Internal + blocker | Internal + anchor | Fully clean |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 0 | 36 | 5 | 3 | 12 | 0 | 1 | 0 |
| 4 | 1 | 36 | 5 | 9 | 0 | 3 | 0 | 0 |
| 5 | 0 | 180 | 32 | 8 | 2 | 1 | 0 | 0 |
| 5 | 1 | 180 | 29 | 2 | 8 | 0 | 0 | 0 |
| 6 | 0 | 540 | 140 | 19 | 9 | 7 | 6 | 0 |
| 6 | 1 | 540 | 135 | 3 | 21 | 0 | 0 | 0 |
| 7 | 0 | 1260 | 448 | 0 | 43 | 0 | 11 | 0 |
| 7 | 1 | 1260 | 433 | 0 | 48 | 0 | 12 | 0 |
| 8 | 0 | 2520 | 979 | 0 | 163 | 0 | 51 | 0 |
| 8 | 1 | 2520 | 1114 | 0 | 95 | 0 | 45 | 0 |
| 9 | 0 | 4536 | 2397 | 0 | 143 | 0 | 51 | 0 |
| 9 | 1 | 4536 | 2110 | 0 | 71 | 0 | 28 | 0 |
| 10 | 0 | 7560 | 3924 | 0 | 258 | 0 | 138 | 0 |
| 10 | 1 | 7560 | 4133 | 0 | 281 | 0 | 142 | 0 |

## Interpretation

The internal width-two geometry is not the limiting resource.  Hundreds or
thousands of internally clean states remain on the larger stored layers, and
many states also avoid retained anchors on patch secants.

The blocker-cover domain is the rigid obstruction.  It vanishes on both layers
from side seven onward, so no state can pay every retained-pair blocker using
only its own four deleted source edges.

The fully external domain is empty in every tested case.  This agrees with the
complete raw width-two extension search, but the domain split identifies the
reason: on the larger cases the failure occurs before anchored-pair cleanliness
is combined with internal geometry.

The next state space must therefore allow blocker endpoints to be deleted by
other blocks, or by an auxiliary protected trade.  Independent unary cleaning of
blocks is not sufficient.