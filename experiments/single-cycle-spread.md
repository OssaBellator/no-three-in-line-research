# Single-cycle spread regression

This experiment accompanies:

- [`docs/165-single-cycle-marked-filler-states.md`](../docs/165-single-cycle-marked-filler-states.md);
- [`scripts/check_single_cycle_spread.py`](../scripts/check_single_cycle_spread.py);
- [`single-cycle-spread-example.json`](single-cycle-spread-example.json).

Run

```bash
python scripts/check_single_cycle_spread.py \
  experiments/single-cycle-spread-example.json
```

For `b=6`, there are exactly

```text
(6-1)! = 120
```

directed single-cycle permutations.

The exact cylinder counts are

```text
one prescribed arc:       24 = (6-1-1)!
two-step path:             6 = (6-2-1)!
two disjoint arcs:         6 = (6-2-1)!
three-step path:           2 = (6-3-1)!
three disjoint arcs:       2 = (6-3-1)!
transposition:             0
directed triangle:         0.
```

Every enumerated state has no fixed point and no transposition. The zero counts
for the transposition and directed triangle verify that a proper directed cycle
cannot occur inside one six-cycle.

The checker logic was independently reproduced and executed against this fixture
on 25 July 2026. The finite regression verifies PP3yx--PP3yz and the exact
cylinder formula. It does not establish the asymptotic source-load or paid-weight
hypotheses of PP3za--PP3zc.
