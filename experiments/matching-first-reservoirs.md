# Matching-first reservoir decomposition

This experiment validates the universal construction in
[`docs/48-matching-density-and-matching-first.md`](../docs/48-matching-density-and-matching-first.md).

The command is

```bash
python scripts/analyze_matching_first_reservoirs.py \
  certificates/prime-patching-small.json --widths 2,3
```

Every stored saturated certificate decomposes into two perfect matching layers
by alternating the edges of each row-column incidence cycle.

## Cycle structure

| Side `m` | Incidence-cycle edge lengths |
|---:|---|
| 2 | `4` |
| 3 | `6` |
| 4 | `4+4` |
| 5 | `10` |
| 6 | `12` |
| 7 | `4+10` |
| 8 | `8+8` |
| 9 | `18` |
| 10 | `20` |

The decomposition is valid whether the source graph is one Hamiltonian cycle or
several smaller cycles.

## Width-two matching-first bank

For `t=2`, choose one of the two perfect matching layers and then four of its
edges.  The exact output is:

| Source `m` | Layer-labelled reservoirs `2 binom(m,4)` | Source-edge deletion marginal | Old-coordinate marginal | Rank-two coordinate marginal |
|---:|---:|---:|---:|---:|
| 4 | 2 | `1/2` | `1` | `1` |
| 5 | 10 | `2/5` | `4/5` | `3/5` |
| 6 | 30 | `1/3` | `2/3` | `2/5` |
| 7 | 70 | `2/7` | `4/7` | `2/7` |
| 8 | 140 | `1/4` | `1/2` | `3/14` |
| 9 | 252 | `2/9` | `4/9` | `1/6` |
| 10 | 420 | `1/5` | `2/5` | `2/15` |

These values agree with PP3bs:

```text
source-edge deletion       t/m
coordinate inclusion       2t/m
rank-r coordinate inclusion (2t)_r/(m)_r
```

## Width-three samples

| Source `m` | Layer-labelled reservoirs `2 binom(m,6)` | Source-edge deletion marginal | Old-coordinate marginal | Rank-two coordinate marginal |
|---:|---:|---:|---:|---:|
| 6 | 2 | `1/2` | `1` | `1` |
| 7 | 14 | `3/7` | `6/7` | `5/7` |
| 8 | 56 | `3/8` | `3/4` | `15/28` |
| 9 | 168 | `1/3` | `2/3` | `5/12` |
| 10 | 420 | `3/10` | `3/5` | `1/3` |

## Interpretation

Matching availability is not the asymptotic bottleneck: every saturated source
has an exponentially large matching-first bank with exact all-rank deletion
spread.  The independent parabolic-template route fails for the opposite
reason.  Its old-column and old-row sets are too weakly correlated with the
`2m` source edges, and PP3bq bounds its admissible density by
`4mt/(H_A H_B)`.

The next experiment should attach internally clean endpoint-adapted movement and
refill states to these matching-first reservoirs, rather than search independent
old-coordinate templates and condition on the rare event that they happen to
contain a perfect matching.