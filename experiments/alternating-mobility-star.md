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

The normalized alternating digraph has seven vertices. Besides the diagonal
loops, it has the two arcs

```text
0 -> i

i -> 0
```

for every leaf `i=1,...,6`. It is one strongly connected component, but two
nontrivial directed cycles always share the centre.

Exact enumeration gives

```text
perfect matching count                       = 7
maximum mobility                             = 2
one maximum-mobility matching                = (0 1)
mobility hub                                 = {0,1}
hub is a directed feedback set               = true
all nontrivial matching cycles meet the hub  = true
maximum cycles in one matching               = 1
```

The seven matchings are the identity and the six centre--leaf transpositions.
Deleting the hub leaves only diagonal loops on vertices `2,...,6`, so the
nonloop digraph is acyclic.

The checker logic was reproduced and executed locally against this fixture on
25 July 2026, yielding the values above. The regression validates the exact
combinatorial reduction; it does not prove that a hub-routed path system has a
source-admissible low-cost state.