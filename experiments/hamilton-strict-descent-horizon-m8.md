# Exact `m=8` strict-descent horizon

An incremental reverse breadth-first search processes the 46 defect levels in
increasing order.  Immediately before level `d` is activated as a new target
set, the stored distance of a state with `B_3=d` is its exact directed distance
to a state with smaller defect.

The full signed Hamilton state space has 1,290,240 states.  The strict-descent
distance distribution over the 1,290,212 nonvalid states is:

| distance to smaller `B_3` | states |
|---:|---:|
| 1 | 1,232,660 |
| 2 | 53,444 |
| 3 | 3,616 |
| 4 | 448 |
| 5 | 44 |

The 44 five-step states all lie at `B_3=4`, the smallest positive defect level.
At that level the distribution is `1:4, 2:32, 3:88, 4:204, 5:44`.  Every state
with at least 40 bad triples has an immediate decreasing move.

Compile and run:

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_strict_descent_horizon_m8.cpp \
  -o /tmp/check_hamilton_strict_descent_horizon_m8
/tmp/check_hamilton_strict_descent_horizon_m8
```
