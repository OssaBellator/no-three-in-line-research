# Hamilton adjacent-transposition embedding

Run:

```bash
python scripts/check_hamilton_adjacent_transposition_embedding.py \
  experiments/hamilton-adjacent-transposition-embedding-audit.json
```

Anchor vertex zero in the directed Hamilton cycle and write the remaining
vertices as a linear order.  Swapping two adjacent entries is exactly one
three-edge successor rotation: choose the predecessor of the pair together
with the two entries.

The audit checks every such embedding through `m=8`:

| `m` | Hamilton cycles | adjacent generators per cycle | checks | comparison coefficient |
|---:|---:|---:|---:|---:|
| 4 | 6 | 2 | 12 | `1/16` |
| 5 | 24 | 3 | 72 | `3/80` |
| 6 | 120 | 4 | 480 | `1/40` |
| 7 | 720 | 5 | 3,600 | `1/56` |
| 8 | 5,040 | 6 | 30,240 | `3/224` |

There are `34,404` exact adjacent-transposition checks in total.  The final
column is

```text
(m-2)/(8 C(m,3)) = 3/[4m(m-1)],
```

the edge-weight ratio used in the Dirichlet-form comparison between the lazy
combined Hamilton chain and the reference adjacent-transposition/hypercube
chain.
