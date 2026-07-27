# Exact `m=8` combined-flaw reachability audit

The compressed checker scores all signed Hamilton states by precomputed two-owner
and three-owner interaction tables. It stores only the defect count and the two
owner-mask sets needed to reconstruct targeted predecessors.

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_combined_flaw_reachability_m8.cpp \
  -o /tmp/check_hamilton_combined_flaw_reachability_m8
/tmp/check_hamilton_combined_flaw_reachability_m8
```

Exact result:

| quantity | value |
|---|---:|
| signed Hamilton states | 1,290,240 |
| valid states | 28 |
| unreachable states | 0 |
| maximum distance to validity | 5 |

Distance distribution:

```text
0:      28
1:   1,560
2:  57,408
3: 736,212
4: 493,728
5:   1,304
```

Because every nonvalid state reaches a valid state in at most five targeted
moves, every nonvalid state reaches a strictly lower value of `Psi=B_3/4` in at
most five moves. This is an upper bound on the strict-descent horizon; the audit
does not assert that five is the minimum possible uniform horizon.
