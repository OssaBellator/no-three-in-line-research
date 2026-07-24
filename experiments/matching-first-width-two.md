# Canonical matching-first width-two experiment

This experiment uses
[`scripts/analyze_matching_first_width_two.py`](../scripts/analyze_matching_first_width_two.py)
and the universal adjacent-pair state PP3bt.

The command is

```bash
python scripts/analyze_matching_first_width_two.py \
  certificates/prime-patching-small.json
```

For each stored source, the script alternates every incidence cycle into two
perfect matching layers, chooses every four-edge subset of either layer, inserts
the canonical adjacent-pair width-two state, and counts exact integer-determinant
certificates.

| Source | Canonical states | Clean states | Minimum total defects | Best blocker count | Best anchor count | Maximum anchor count |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 0 | 3 | 0 | 2 | 3 |
| 5 | 10 | 0 | 4 | 2 | 1 | 5 |
| 6 | 30 | 0 | 1 | 0 | 1 | 6 |
| 7 | 70 | 0 | 6 | 2 | 0 | 6 |
| 8 | 140 | 0 | 6 | 3 | 0 | 8 |
| 9 | 252 | 0 | 8 | 5 | 0 | 10 |
| 10 | 420 | 0 | 5 | 4 | 0 | 8 |

The `best blocker count` and `best anchor count` columns are minima over all
states separately; they need not occur in the same state.  The minimum-total
states have defect splits:

| Source | Blockers | Anchors |
|---:|---:|---:|
| 4 | 0 | 3 |
| 5 | 2 | 2 |
| 6 | 0 | 1 |
| 7 | 4 | 2 |
| 8 | 4 | 2 |
| 9 | 7 | 1 |
| 10 | 5 | 0 |

The side-six state is a one-anchor near miss, while side ten already has states
with no anchor defect.  This supports the deterministic split in PP3bw:
internal triples are absent, anchor defects remain bounded, and nonaxis
retained-pair blockers become the dominant scalable obstruction.

The canonical bank is much smaller than the complete 36-state-per-reservoir
width-two search: it has only `2 binom(m,4)` states.  Its value is structural,
not finite superiority.  Every state comes from the same endpoint-adapted rule
and therefore admits exact hypergeometric spread analysis.