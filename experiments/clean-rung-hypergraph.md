# Clean-rung hypergraph packing experiment

This experiment uses
[`scripts/analyze_clean_rung_hypergraph.py`](../scripts/analyze_clean_rung_hypergraph.py)
and the packing endpoint in
[`docs/53-clean-rung-hypergraph-packing.md`](../docs/53-clean-rung-hypergraph-packing.md).

The command is

```bash
python scripts/analyze_clean_rung_hypergraph.py \
  certificates/prime-patching-small.json
```

For each perfect matching layer, the vertices are its source edges and the
hyperedges are the locally clean four-edge canonical rung states.

| Side | Layer | Clean states | Maximum vertex degree | Matching number | Transversal number | Common clean-state vertices |
|---:|---:|---:|---:|---:|---:|---|
| 4 | 0 | 1 | 1 | 1 | 1 | 4 |
| 4 | 1 | 1 | 1 | 1 | 1 | 4 |
| 5 | 0 | 2 | 2 | 1 | 1 | 3 |
| 5 | 1 | 3 | 3 | 1 | 1 | 2 |
| 6 | 0 | 3 | 3 | 1 | 1 | 1 |
| 6 | 1 | 7 | 7 | 1 | 1 | 1 |
| 7 | 0 | 3 | 3 | 1 | 1 | 1 |
| 7 | 1 | 4 | 4 | 1 | 1 | 1 |
| 8 | 0 | 3 | 3 | 1 | 1 | 2 |
| 8 | 1 | 2 | 2 | 1 | 1 | 2 |
| 9 | 0 | 3 | 3 | 1 | 1 | 1 |
| 9 | 1 | 3 | 3 | 1 | 1 | 3 |
| 10 | 0 | 8 | 6 | 1 | 2 | 0 |
| 10 | 1 | 7 | 6 | 1 | 2 | 0 |

`Common clean-state vertices` is the number of source edges lying in every clean
state.  Up to side nine, at least one edge is common to all clean states, so a
single source edge hits the complete clean domain.  At side ten the common
intersection disappears, but two edges still hit every clean state.

The matching number is one in all fourteen nontrivial layer instances.  Thus no
stored perfect matching layer contains two edge-disjoint locally clean canonical
rungs, even when it contains seven or eight clean states.

This concentration explains why raw state count is the wrong asymptotic metric.
The useful quantity is the degree ratio `h/Delta`, or equivalently whether the
clean-state hypergraph has a large disjoint matching.  A prepared source must
make the clean domain diffuse, or protect the one- or two-edge transversal core
that currently pins every state.