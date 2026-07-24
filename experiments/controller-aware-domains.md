# Controller-aware domain diagnostics

This experiment accompanies
[`docs/84-controller-aware-safe-macro-domains.md`](../docs/84-controller-aware-safe-macro-domains.md)
and
[`scripts/analyze_controller_aware_domains.py`](../scripts/analyze_controller_aware_domains.py).

Run

```bash
python scripts/analyze_controller_aware_domains.py \
  certificates/prime-patching-small.json \
  --labels 12 --gamma 1/3
```

The active pool is one complete perfect-matching layer.  Candidate values are
tested against the **full** saturated source, including unselected edges of the
active pool.  A movement or refill cell is controller-safe only when every
blocker pair through it contains the controller edge.  The same-slot source
anchor condition is then removed before building the label graph.

## Exact controller-aware label graphs

With twelve movement labels, twelve refill labels, and density threshold
`gamma=1/3`, the graph statistics are:

| Side | Layer | Graph edges | Maximum label matching | Maximum domain size |
|---:|---:|---:|---:|---:|
| 4 | 0 | 118 | 10 | 4 |
| 4 | 1 | 119 | 10 | 4 |
| 5 | 0 | 110 | 11 | 5 |
| 5 | 1 | 111 | 11 | 5 |
| 6 | 0 | 97 | 10 | 6 |
| 6 | 1 | 96 | 10 | 6 |
| 7 | 0 | 30 | 7 | 5 |
| 7 | 1 | 28 | 7 | 5 |
| 8 | 0 | 25 | 5 | 6 |
| 8 | 1 | 23 | 5 | 6 |
| 9 | 0 | 17 | 5 | 6 |
| 9 | 1 | 17 | 5 | 6 |
| 10 | 0 | 4 | 3 | 5 |
| 10 | 1 | 2 | 2 | 4 |

The fixed-core refined graph previously had a full twelve-label matching on both
layers at sides eight through ten for the looser thresholds.  That phenomenon
does not survive the controller-aware correction: unselected active-pool edges
supply many additional blocker pairs.

## Cell-entry shadow

For each layer there are `24n` typed candidate entries: twelve movement labels
and twelve refill labels for every one of the `n` controller edges.  The total
controller-safe and bad counts are:

| Side | Safe entries | Bad entries | Total entries |
|---:|---:|---:|---:|
| 4 | 85 | 11 | 96 |
| 5 | 89 | 31 | 120 |
| 6 | 93 | 51 | 144 |
| 7 | 70 | 98 | 168 |
| 8 | 70 | 122 | 192 |
| 9 | 68 | 148 | 216 |
| 10 | 68 | 172 | 240 |

The counts are the same for the two deterministic matching layers because the
candidate cells depend on the controller coordinates while blocker safety is
tested against the full source.

## Blocker structure

The chosen noncontroller blocker witnesses already show the star-or-matching
structure predicted asymptotically.

| Side | Distinct blocker pairs | Maximum endpoint entry-degree | Exact blocker-graph matching number |
|---:|---:|---:|---:|
| 4 | 9 | 7 | 3 |
| 5 | 20 | 14 | 4 |
| 6 | 32 | 19 | 5 |
| 7 | 54 | 30 | 7 |
| 8 | 70 | 33 | 7 |
| 9 | 105 | 40 | 9 |
| 10 | 119 | 45 | 10 |

The blocker graph reaches a perfect matching on the twenty source points at
side ten, while individual endpoints also support dozens of bad entries.  The
finite examples therefore exhibit both ingredients of PP3hu--PP3hy: large
endpoint stars and large endpoint-disjoint blocker families.

## Interpretation

These data rule out treating controller-aware density as a minor perturbation
of the fixed-core label graph on the stored seeds.  The remaining asymptotic
theorem must genuinely use one of:

1. special structure of the large prime-size seeds;
2. complementary-degree allocation across many macro graphs;
3. alternating-star neutralisation;
4. the resource-matching endpoint trade and its paid collateral endpoint.

The experiment is a finite diagnostic, not an asymptotic obstruction.  The
slab-optimal pools have size `m^0.95`, far larger than the stored sides.
