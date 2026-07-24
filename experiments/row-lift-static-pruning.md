# Static row-lift pruning experiments

These computations test the static endpoints PP3p and PP3r from
[`docs/32-row-lift-pruning-barriers.md`](../docs/32-row-lift-pruning-barriers.md).
They use exact integer determinants and rational event weights.

## 1. Fully deleted side-three reservoir

Run

```bash
python scripts/analyze_row_lift_static_pruning.py \
  certificates/prime-patching-small.json \
  --n 3 --rows 1,2,3
```

For the stored side-three certificate, all old points are deleted. The canonical
family therefore has only movement collisions, refill collisions, and internal
inserted-point triples.

Among all 24 layer orders, the best order under the static conditioned-mass
criterion is

```text
red-move, blue-move, refill-a, refill-b
```

with the following stage data:

| Stage | Layer | Geometric residual events | PP3p vertex load | PP3r conditioned mass |
|---:|---|---:|---:|---:|
| 1 | red-move | 2 | `1/3` | `1/3` |
| 2 | blue-move | 13 | `2` | `9` |
| 3 | refill-a | 16 | `13/6` | `23/6` |
| 4 | refill-b | 21 | `5/2` | `15` |

Thus

- the best static PP3p maximum vertex load is `5/2`, versus threshold `1/24`;
- the best static PP3r maximum conditioned mass is `15`, versus threshold `1`.

The prefix-aware PP3l analyzer gives the smaller best maximum load `13/6`, so
the gap `5/2 - 13/6 = 1/3` measures residual events that cannot be activated
together in one legal prefix. Static overcounting is visible but is not the main
obstruction in this instance.

## 2. Fully deleted side-two reservoir

For

```bash
python scripts/analyze_row_lift_static_pruning.py \
  certificates/prime-patching-small.json \
  --n 2 --rows 1,2
```

the best static values are:

| Quantity | Value |
|---|---:|
| PP3p maximum vertex load | `3/2` |
| PP3r maximum conditioned mass | `9/2` |

Even with no retained core, the full width-two bank is blocked by internal
geometry. This agrees with the exhaustive clean-state search.

## 3. Interpretation

The static tests are deliberately conservative, but the failures above are by
large constant factors. More importantly, Proposition PP3o proves that the
unpruned refill support contains `Omega(t^4 log t)` compatible nonaxis triples,
so the global PP3j support-count route fails asymptotically as well.

A scalable row-lift construction must therefore change the state space, not
merely select reservoir rows. The next computational target is to impose sparse
algebraic position sets on each permutation layer and measure:

1. the terminal vertex loads of PP3p;
2. the collision-conditioned terminal masses of PP3r;
3. the prefix-aware loads of PP3l only for candidates passing one of the static
   screens.