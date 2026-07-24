# Matching-block clean-domain diagnostics

This experiment uses
[`scripts/analyze_matching_block_states.py`](../scripts/analyze_matching_block_states.py)
and the multistate block construction in
[`docs/51-matching-block-multistate-rungs.md`](../docs/51-matching-block-multistate-rungs.md).

The command is

```bash
python scripts/analyze_matching_block_states.py \
  certificates/prime-patching-small.json
```

Each perfect matching layer is treated as one block.  Every four-edge subset is
a state; the script first checks cleanliness against the retained points of that
same layer, then counts defects against the complete two-layer source.

| Side | Layer 0 locally clean / total | Layer 1 locally clean / total | Minimum global defects L0 | Minimum global defects L1 |
|---:|---:|---:|---:|---:|
| 4 | `1/1` | `1/1` | 4 | 3 |
| 5 | `2/5` | `3/5` | 4 | 6 |
| 6 | `3/15` | `7/15` | 1 | 3 |
| 7 | `3/35` | `4/35` | 6 | 7 |
| 8 | `3/70` | `2/70` | 6 | 7 |
| 9 | `3/126` | `3/126` | 8 | 11 |
| 10 | `8/210` | `7/210` | 5 | 7 |

Every stored matching layer has a nonempty locally clean domain, but no state is
globally clean.  The clean fraction falls from a positive constant at sides
four through six to only a few states among `Theta(m^4)` candidates at sides
eight and nine.

This finite concentration is not a theorem about large prepared blocks.  It
shows why PP3bz is formulated with explicit unary pruning rather than claiming
that every matching block keeps positive state density.  A scalable source
construction must control the secant shadow inside each block, or attach local
trades that turn many currently bad states into clean equal-margin states.