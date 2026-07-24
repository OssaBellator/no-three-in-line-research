# Matching-block local-load experiment

This experiment uses
[`scripts/analyze_matching_block_loads.py`](../scripts/analyze_matching_block_loads.py)
and the first-moment criterion PP3ca.

The command is

```bash
python scripts/analyze_matching_block_loads.py \
  certificates/prime-patching-small.json
```

For each complete perfect matching layer, the analyzer unions the exact feasible
blocker, same-edge anchor, and ordinary two-edge anchor signatures over all
canonical four-edge states.

| Side | Layer | `B` | `A_1` | `A_2` | PP3ca upper bound | Exact average local triples | Clean states |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 0 | 0 | 0 | 0 | `0` | `0` | 1 |
| 4 | 1 | 0 | 0 | 0 | `0` | `0` | 1 |
| 5 | 0 | 0 | 1 | 4 | `16/5` | `1` | 2 |
| 5 | 1 | 0 | 0 | 2 | `6/5` | `2/5` | 3 |
| 6 | 0 | 4 | 1 | 6 | `86/15` | `4/3` | 3 |
| 6 | 1 | 2 | 0 | 4 | `44/15` | `4/5` | 7 |
| 7 | 0 | 7 | 0 | 12 | `52/7` | `13/7` | 3 |
| 7 | 1 | 5 | 1 | 10 | `44/7` | `58/35` | 4 |
| 8 | 0 | 9 | 1 | 11 | `103/14` | `163/70` | 3 |
| 8 | 1 | 13 | 1 | 18 | `76/7` | `167/70` | 2 |
| 9 | 0 | 18 | 0 | 26 | `37/3` | `74/21` | 3 |
| 9 | 1 | 13 | 1 | 20 | `86/9` | `45/14` | 3 |
| 10 | 0 | 13 | 3 | 25 | `146/15` | `281/105` | 8 |
| 10 | 1 | 11 | 3 | 25 | `134/15` | `79/30` | 7 |

PP3ca certifies both side-four layers directly.  From side five onward its union
bound is above one, even when the exact average is below one and several clean
states exist.  This demonstrates two distinct gaps:

1. the signature-probability bounds can be much larger than the exact state
   probabilities because rank conditions and retained-point requirements are
   ignored;
2. first moment is sufficient but not necessary, so an exact multistate solver
   can succeed after the coarse load endpoint fails.

The failure trichotomy PP3cb is nevertheless informative.  On the larger stored
layers, blocker signatures grow linearly and ordinary anchor signatures
quadratically, exactly the two scales that an asymptotic prepared block must
suppress.