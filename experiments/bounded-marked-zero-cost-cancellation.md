# Bounded marked-set zero-cost cancellation diagnostic

Run

```text
python scripts/check_bounded_marked_zero_cost_cancellation.py \
  experiments/bounded-marked-zero-cost-cancellation-example.json
```

The stored second trade moves four distinguished local cells using the separated
single cycle

```text
d0,h0,d1,h1,d2,h2,d3,h3,h4,h5.
```

No selected arc has two distinguished endpoints.  Hence every nonzero canonical
source or insertion event has ordinary-helper support; the stored independent
helper set leaves the second trade with zero insertion cost.

The first local table has ten atom weights summing to `1000`, original removal
credit `100`, and no nonlocal cost.  The exact output is

```text
marked indices 4
helper indices 6
separated cycle order ['d0', 'h0', 'd1', 'h1', 'd2', 'h2', 'd3', 'h3', 'h4', 'h5']
marked-marked arcs 0
local atom count 10
complete local table weight 1000
first-step change 900
second-step insertion cost 0
second-step change -1000
composite change -100
outcome bounded_marked_zero_cost_cancellation
```

Thus all ten local atoms cancel simultaneously.  The composite change is exactly

```text
first nonlocal cost + second insertion cost - first removal credit = -100.
```
