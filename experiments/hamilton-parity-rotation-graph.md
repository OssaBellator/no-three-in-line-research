# Parity-satisfiable Hamilton rotation graph

Run:

```bash
python scripts/check_hamilton_parity_rotation_graph.py \
  experiments/hamilton-parity-rotation-graph-audit.json
```

For every Hamilton pair cycle through `m=7`, the checker reconstructs the exact
two-owner signed parity CSP from orbit geometry. It then applies every
three-source successor rotation and compares the two constraint graphs.

Every changed parity constraint touches one of the three rotated sources. The
maximum observed numbers of changed constraints are:

```text
m=4: 1
m=5: 5
m=6: 7
m=7: 9
```

The general deterministic upper bound is `3m-6`.

The parity-satisfiable cycle subgraphs are:

| `m` | cycles | satisfiable | inconsistent | induced components | minimum satisfiable neighbours | maximum distance to satisfiable |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 6 | 0 | 1 | 4 | 0 |
| 5 | 24 | 22 | 2 | 1 | 9 | 1 |
| 6 | 120 | 112 | 8 | 1 | 16 | 1 |
| 7 | 720 | 664 | 56 | 1 | 26 | 1 |

Directed rotation transitions at `m=7` split as

```text
satisfiable -> satisfiable     21,616
satisfiable -> inconsistent     1,624
inconsistent -> satisfiable     1,624
inconsistent -> inconsistent      336
```

Thus parity cleanliness is not preserved by every successor rotation, but the
induced satisfiable graph remains connected in the complete audited range.

This is a finite structural diagnostic. It does not prove that the satisfiable
induced graph is connected or even nonempty for all large `m`.
