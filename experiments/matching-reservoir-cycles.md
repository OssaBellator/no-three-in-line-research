# Matching-reservoir cycle experiments

These checks use
[`scripts/analyze_matching_reservoir_cycles.py`](../scripts/analyze_matching_reservoir_cycles.py)
and the exact factorization in
[`docs/39-matching-reservoir-cycle-factorization.md`](../docs/39-matching-reservoir-cycle-factorization.md).

## Side-four regression

Run:

```bash
python scripts/analyze_matching_reservoir_cycles.py \
  certificates/prime-patching-small.json \
  --n 4 --columns 1,2,3,4 --rows 1,2,3,4
```

The induced reservoir graph consists of two disjoint four-cycles:

```text
columns {1,3} -- rows {2,3}
columns {2,4} -- rows {1,4}
```

Each cycle has two alternating perfect matchings.  The global bank therefore
has

```text
2 * 2 = 4
```

deletion states, every source edge is cycle-optional, and every source edge is
deleted with probability `1/2`.

This is exactly the four-state bank in
[`parabolic-variable-bank-n4.json`](parabolic-variable-bank-n4.json).

## All width-two parabolic reservoirs in the stored corpus

For every translated `L=2,d=1,t=2` coordinate pair supporting a perfect
matching, the component structure is:

| Source `n` | Column offset | Row offset | Component structure | Perfect matchings |
|---:|---:|---:|---|---:|
| 4 | 1 | 1 | two 4-cycles | 4 |
| 5 | 1 | 1 | one 8-vertex path | 1 |
| 5 | 1 | 2 | two 4-vertex paths | 1 |
| 5 | 2 | 1 | one 6-vertex path and one edge | 1 |
| 5 | 2 | 2 | one 6-vertex path and one edge | 1 |
| 6 | 2 | 1 | two 4-vertex paths | 1 |
| 6 | 3 | 1 | two 4-vertex paths | 1 |
| 7 | 4 | 1 | one 4-vertex path and two edges | 1 |
| 8 | 4 | 1 | one 4-vertex path and two edges | 1 |
| 8 | 5 | 2 | one 4-vertex path and two edges | 1 |
| 8 | 5 | 3 | one 6-vertex path and one edge | 1 |

Thus only the side-four coordinate pair has any matching-choice entropy.  Every
other stored parabolic reservoir is path-forced: once the old row and column
sets are chosen, its deletion set is unique.

## Interpretation

The finite data separates two possible sources of a variable-reservoir bank:

1. alternating choices inside degree-two cycle components;
2. variation of the old row/column coordinate sets themselves.

On the stored corpus, the first source is exceptional.  Scaling PP2l cannot rely
on a generic abundance of cycle choices inside one fixed induced graph.  A
prepared asymptotic construction must deliberately install geometry-aligned
cycles or vary the reservoir coordinate patterns and inserted patches together.
