# Hamilton parity-constraint incidence growth audit

The checker builds the graph whose vertices are directed pair assignments and
whose labelled edges are compatible owner pairs that forbid exactly one XOR
value.  It records the edge count, maximum assignment degree, and the number of
Hamilton-compatible constraint triangles, split by parity frustration.

| `m` | one-XOR pairs | impossible pairs | maximum degree | compatible triangles | frustrated triangles |
|---:|---:|---:|---:|---:|---:|
| 4 | 8 | 0 | 2 | 0 | 0 |
| 5 | 26 | 0 | 5 | 2 | 2 |
| 6 | 45 | 0 | 6 | 2 | 2 |
| 7 | 75 | 0 | 10 | 6 | 6 |
| 8 | 128 | 4 | 13 | 58 | 58 |
| 9 | 164 | 4 | 15 | 58 | 58 |
| 10 | 221 | 4 | 19 | 74 | 74 |
| 20 | 1,648 | 8 | 46 | 1,534 | 1,406 |
| 30 | 4,453 | 12 | 89 | 4,776 | 4,340 |
| 40 | 9,056 | 24 | 115 | 10,706 | 9,910 |
| 50 | 15,875 | 32 | 143 | 21,992 | 20,556 |
| 60 | 24,404 | 44 | 168 | 36,150 | 33,954 |

Compile and run:

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_parity_constraint_incidence_growth.cpp \
  -o /tmp/check_hamilton_parity_constraint_incidence_growth
/tmp/check_hamilton_parity_constraint_incidence_growth
```

The geometric asymptotic estimates proved in `docs/323` are not inferred from
this table; the table independently checks the sparse incidence regime and the
first frustrated-cycle counts.
