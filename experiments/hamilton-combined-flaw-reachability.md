# Combined Hamilton flaw-repair reachability

Run:

```bash
python scripts/check_hamilton_combined_flaw_reachability.py \
  experiments/hamilton-combined-flaw-reachability-audit.json
```

The diagnostic combines two exact flaw-targeted moves inside the signed Hamilton
family:

1. for a bad triple with two orbit owners, flip the orientation bit of either
   owner;
2. for a bad triple with three orbit owners, apply the three-edge successor
   rotation and choose arbitrary fresh signs on the changed sources.

A quarter-turn orbit is a four-vertex square, so a line contains at most two
points from one owner.  Every bad triple therefore has exactly two or three
owners, and the combined rule always has a legal flaw-targeted move.

The exhaustive reachability results are:

| `m` | states | minimum triples | minimum states | directed targeted edges | maximum distance to minimum |
|---:|---:|---:|---:|---:|---:|
| 4 | 96 | 0 | 16 | 864 | 2 |
| 5 | 768 | 0 | 16 | 15,632 | 3 |
| 6 | 7,680 | 4 | 84 | 252,896 | 3 |

Every state reaches the global minimum triple count in the directed
flaw-targeted graph.  At `m=4,5`, the global minimum is zero and hence every
state reaches a valid seed.  At `m=6`, no signed Hamilton state is valid, but all
states reach one of the 84 four-triple minima.

The one-step local minima from the drift audit remain present, but they are not
closed traps:

| `m` | nonminimal one-step local minima | distance two | distance three |
|---:|---:|---:|---:|
| 4 | 36 | 36 | 0 |
| 5 | 140 | 96 | 44 |
| 6 | 764 | 736 | 28 |

The owner-pattern census checks

```text
m=4: 64 two-owner and 416 three-owner bad-triple occurrences
m=5: 2,304 two-owner and 7,552 three-owner occurrences
m=6: 24,576 two-owner and 126,464 three-owner occurrences.
```

The result is finite evidence for a bounded-look-ahead or witness-sequence
analysis.  It does not prove an asymptotic descent or termination theorem.
