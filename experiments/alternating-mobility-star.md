# Alternating mobility star regression

This experiment accompanies
[`docs/147-maximum-mobility-alternating-cycle-bank.md`](../docs/147-maximum-mobility-alternating-cycle-bank.md),
[`scripts/check_alternating_mobility.py`](../scripts/check_alternating_mobility.py),
and
[`alternating-mobility-star-example.json`](alternating-mobility-star-example.json).

Run

```bash
python scripts/check_alternating_mobility.py \
  experiments/alternating-mobility-star-example.json
```

The normalized alternating digraph has seven vertices.  Besides the diagonal
loops, it has the two arcs

```text
0 -> i

i -> 0
```

for every leaf `i=1,...,6`.  It is one strongly connected component, but two
nontrivial directed cycles always share the centre.

The perfect matchings are exactly:

- the identity;
- the six centre--leaf transpositions.

Thus the expected exact output is

```text
perfect matching count                       = 7
maximum mobility                             = 2
one maximum-mobility matching                = (0 1)
mobility hub                                 = {0,1}
hub is a directed feedback set               = true
all nontrivial matching cycles meet the hub  = true
maximum cycles in one matching               = 1
```

Deleting the hub leaves only the diagonal loops on vertices `2,...,6`, so the
nonloop digraph is acyclic.  This is the extremal low-mobility shape behind
PP3up: a large flexible SCC may have only constant simultaneous movement because
all alternating cycles pass through one common resource.

The regression validates the exact combinatorial reduction.  It does not prove
that a hub-routed path system has a source-admissible low-cost state.