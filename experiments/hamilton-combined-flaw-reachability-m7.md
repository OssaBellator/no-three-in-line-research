# Hamilton combined-flaw reachability through `m=7`

Compile and run:

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_combined_flaw_reachability_m7.cpp \
  -o /tmp/check_hamilton_combined_flaw_reachability_m7
/tmp/check_hamilton_combined_flaw_reachability_m7
```

The dedicated checker independently reconstructs every signed Hamilton state at
`m=7`, every selected grid line, every two-owner or three-owner bad triple, and
every legal combined flaw-targeted move. It then builds both forward and reverse
CSR graphs and performs exact breadth-first searches.

The `m=7` totals are:

```text
signed Hamilton states                 92,160
defective states                       92,124
valid states                               36
two-owner bad-triple occurrences      344,064
three-owner bad-triple occurrences  2,219,520
directed flaw-targeted edges         4,427,088
maximum distance to validity                 4
maximum strict-descent horizon               4
```

Distance to the valid set:

| distance | states |
|---:|---:|
| 0 | 36 |
| 1 | 1,576 |
| 2 | 31,112 |
| 3 | 58,712 |
| 4 | 724 |

Among the `6,676` nonvalid one-step local minima, the shortest distance to any
strictly lower total triple count is:

| descent horizon | local minima |
|---:|---:|
| 2 | 5,936 |
| 3 | 692 |
| 4 | 48 |

All other `85,448` nonvalid states have an immediately decreasing targeted move.
The combined ledger for `m=4,5,6,7` is stored in
`hamilton-combined-flaw-reachability-m7-results.json`.

This is a finite bounded-look-ahead result. It does not prove a uniform
asymptotic horizon or the asymptotic seed theorem.
